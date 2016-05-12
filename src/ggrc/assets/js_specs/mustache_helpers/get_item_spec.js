/*!
  Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
  Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
  Created By: peter@reciprocitylabs.com
  Maintained By: peter@reciprocitylabs.com
*/

describe('can.mustache.helper.get_item', function () {
  'use strict';

  var helper;
  var fakeOptions;  // a fake "options" argument

  beforeAll(function () {
    helper = can.Mustache._helpers.get_item.fn;
  });

  beforeEach(function () {
    fakeOptions = {};
  });

  it('raises an error on missing arguments', function () {
    var obj = {foo: 'foo123', bar: 'bar123'};
    expect(function () {
      helper(obj, fakeOptions);
    }).toThrow(new Error('Invalid number of arguments (1), expected 2.'));
  });

  it('raises an error on too many arguments', function () {
    var obj = {foo: 'foo123', bar: 'bar123'};
    expect(function () {
      helper(obj, 'foo', 'bar', fakeOptions);
    }).toThrow(new Error('Invalid number of arguments (3), expected 2.'));
  });

  it('raises an error if given a non-object', function () {
    expect(function () {
      helper(1234, 'foo', fakeOptions);
    }).toThrow(new Error('First argument must be an object.'));
  });

  it('returns the value of the correct model attribute', function () {
    var obj = {foo: 'foo123', bar: 'bar456'};
    var result = helper(obj, 'bar', fakeOptions);
    expect(result).toEqual('bar456');
  });

  // The helper sometimes receives arguments wrapped in functions that return
  // the actual argument values, and thus must work with them, too.
  it('returns the value of the correct model attribute if given ' +
    'function arguments',
    function () {
      var obj = function () {
        return {foo: 'foo123', bar: 'bar456'};
      };
      var key = function () {
        return 'bar';
      };

      var result = helper(obj, key, fakeOptions);

      expect(result).toEqual('bar456');
    }
  );
});
