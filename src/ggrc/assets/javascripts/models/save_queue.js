/*!
    Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
    Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
    Created By: anze@reciprocitylabs.com
    Maintained By: anze@reciprocitylabs.com
*/

(function (can, $) {
  /*  GGRC.SaveQueue
   *
   *  SaveQueue is used by CMS.Models.Cacheable to prevent firing
   *  multiple requests to the server at once. It makes sure the requests
   *  are grouped together (inside _queue) and then resolved in batches.
   *
   *  It will also try to group POST request and use the custom collection post
   *  API and then redistribute responses in order to trace in latency for
   *  throughput. This is done by a "thread" (of timeouts) per object type (per
   *  bucket) that enqueues as a regular request but then greedily dispatches
   *  requests that arrived while it was in the queue.
   *
   *  enqueue(obj: CMS.Models.Cacheable, save_args) -> null
   */
  can.Construct('GGRC.SaveQueue', {

    DELAY: 100, // Number of ms to wait before the first batch is fired
    BATCH: GGRC.config.MAX_INSTANCES || 3, // Maximum number of POST/PUT requests at any given time
    BATCH_SIZE: 100,
    _queue: [],
    _buckets: {},
    _timeout: null,

    _enqueue_bucket: function (bucket) {
      var that = this;
      return function () {
        var objs = bucket.objs.splice(0, that.BATCH_SIZE);
        var body = _.map(objs, function (obj) {
          var list = {};
          list[bucket.type] = obj.serialize();
          return list;
        });
        var dfd = $.ajax({
          type: 'POST',
          url: '/api/' + bucket.plural,
          data: body
        }).promise();
        dfd.always(function (data, type) {
          var cb;
          var single;
          var obj;
          var i = 0;

          if (type === 'error') {
            data = data.responseJSON;
            if (_.isUndefined(data)) {
              return;
            }
          }
          cb = function (single) {
            return function () {
              this.created(single[1][bucket.type]);
              return $.when(
                can.Model.Cacheable.resolve_deferred_bindings(this));
            };
          };
          for (; i < objs.length; i++) {
            single = data[i];
            obj = objs[i];
            if (single[0] >= 200 && single[0] < 300) {
              obj._save(cb(single));
            } else {
              obj._dfd.reject(obj, single);
            }
          }
        }).always(function () {
          if (bucket.objs.length) {
            that._step(that._enqueue_bucket(bucket));
          } else {
            bucket.in_flight = false;
          }
        });

        return dfd;
      };
    },

    _step: function (elem) {
      this._queue.push(elem);
      if (_.isNumber(this._timeout)) {
        clearTimeout(this._timeout);
      }
      this._timeout = setTimeout(function () {
        new GGRC.SaveQueue(this._queue.splice(0, this._queue.length));
      }.bind(this), this.DELAY);
    },

    enqueue: function (obj, args) {
      var type;
      var bucket;
      var plural;
      var elem = function () {
        return obj._save.apply(obj, args);
      };
      if (obj.isNew()) {
        type = obj.constructor.table_singular;
        bucket = this._buckets[type];
        if (_.isUndefined(bucket)) {
          plural = obj.constructor.table_plural;
          bucket = {
            objs: [],
            type: type,
            plural: plural,
            in_flight: false // is there a "thread" running for this bucket
          };
          this._buckets[type] = bucket;
        }
        bucket.objs.push(obj);
        if (bucket.in_flight) {
          return;
        }
        elem = this._enqueue_bucket(bucket);
        bucket.in_flight = true;
      }
      this._step(elem);
    }
  }, {
    init: function (queue) {
      this._queue = queue;
      this._resolve();
    },
    _resolve: function () {
      var objs;
      if (!this._queue.length) {
        // Finished
        return;
      }
      objs = this._queue.splice(0, this.constructor.BATCH);
      $.when.apply($, objs.map(function (fn) {
        return fn.apply(this);
      }.bind(this.constructor))).always(this._resolve.bind(this)); // Move on to the next one
    }
  });
})(window.can, window.can.$);
