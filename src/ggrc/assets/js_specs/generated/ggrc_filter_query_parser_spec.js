/*!
  Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
  Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
  Created By: miha@reciprocitylabs.com
  Maintained By: miha@reciprocitylabs.com
  */

describe('GGRC.query_parser', function() {


  var values = {
    'a': 'b',
    'hello': 'world',
    'n': '22',
    '5words': 'These are just 5 words',
    'bacon ipsum': 'Bacon ipsum dolor amet meatloaf pork loin fatback ball'+
      'tip chicken frankfurter swine bresaola beef ribs ribeye shankle sho'+
      'rt ribs drumstick leberkas sirloin. Turducken hamburger drumstick g'+
      'round round ham biltong. Alcatra turkey brisket pancetta jowl bilto'+
      'ng meatball, shank pork chop. Flank fatback capicola chuck chicken '+
      'jerky venison meatball beef drumstick.'
  }

  var parser_structure = {
    parse: jasmine.any(Function),
    toSource: jasmine.any(Function),
    SyntaxError: jasmine.any(Function)
  };


  it("should exist", function() {
    expect(GGRC.query_parser).toEqual(parser_structure);
  });


  describe("parse", function() {

    it("parses an empty query", function(){

      var empty_result = {
        expression: {},
        keys: [],
        evaluate: jasmine.any(Function),
        order_by : { keys : [ ], order : '', compare : null }
      }

      expect(GGRC.query_parser.parse("")).toEqual(empty_result);
      expect(GGRC.query_parser.parse(" ")).toEqual(empty_result);
      expect(GGRC.query_parser.parse(" \t ")).toEqual(empty_result);
      expect(GGRC.query_parser.parse("\t")).toEqual(empty_result);
    });


    it("parses simple single word queries", function(){

      var single_word_queries = [
        'a',
        'word',
        '--this--is',
        'i_hope-this7531',
        '7531902468'
      ];

      can.each(single_word_queries, function(query_str){
        expect(GGRC.query_parser.parse(query_str)).toEqual({
          expression: {
            left: query_str,
            op: 'boolean',
            evaluate: jasmine.any(Function)
          },
          order_by : { keys : [ ], order : '', compare : null },
          keys: [query_str],
          evaluate: jasmine.any(Function)
        });
      });

    });


    it("parses quoted single word queries", function(){

      var single_word_queries = [
        '""',
        '" "',
        '" word "',
        '"wo   rd"',
        '" wo rd  "',
        '"wo \\\"  rd"',
        '"\\\"wo\\\"   rd"',
        '"wo \\\"\\\"  rd\\\""'
      ];

      can.each(single_word_queries, function(query_str){
        var unqouted = query_str.slice(1,-1).replace(/\\"/g,'"');
        expect(GGRC.query_parser.parse(query_str)).toEqual({
          expression: {
            left: unqouted,
            op: 'boolean',
            evaluate: jasmine.any(Function)
          },
          order_by : { keys : [ ], order : '', compare : null },
          keys: [unqouted],
          evaluate: jasmine.any(Function)
        });
      });

    });


    it("parses \'=\' queries", function(){

      var simple_queries = [
        'a=b',
        'hello=world',
        ' with = spaces',
        'but= not_all_spaces  '
      ];

      can.each(simple_queries, function(query_str){
        var query = query_str.split('=');
        expect(GGRC.query_parser.parse(query_str)).toEqual({
          expression: {
            left: query[0].trim(),
            op: { name: '=', evaluate: jasmine.any(Function) },
            right: query[1].trim(),
            evaluate: jasmine.any(Function)
          },
          order_by : { keys : [ ], order : '', compare : null },
          keys: [query[0].trim()],
          evaluate: jasmine.any(Function)
        });
      });
    });

    it('parses \'~\' queries', function(){

      expect(GGRC.query_parser.parse('5words ~ just')).toEqual({
          expression: {
            left: '5words',
            op: { name: '~', evaluate: jasmine.any(Function) },
            right: 'just',
            evaluate: jasmine.any(Function)
          },
          order_by : { keys : [ ], order : '', compare : null },
          keys: ['5words'],
          evaluate: jasmine.any(Function)
        })

    });

    it('works with order by statement', function(){

      expect(GGRC.query_parser.parse('5words ~ just order by some,"name with spaces" desc')).toEqual({
          expression: {
            left: '5words',
            op: { name: '~', evaluate: jasmine.any(Function) },
            right: 'just',
            evaluate: jasmine.any(Function)
          },
          order_by : {
            keys : ['some', 'name with spaces' ],
            order : 'desc',
            compare : jasmine.any(Function)
          },
          keys: ['5words'],
          evaluate: jasmine.any(Function)
        })

    });

    describe("evaluate", function(){

      it("returns true on an empty query", function(){
        expect(GGRC.query_parser.parse("").evaluate()).toEqual(true);
        expect(GGRC.query_parser.parse(" ").evaluate()).toEqual(true);
        expect(GGRC.query_parser.parse("\t").evaluate()).toEqual(true);
        expect(GGRC.query_parser.parse("  \t  ").evaluate()).toEqual(true);
        expect(GGRC.query_parser.parse("    \t").evaluate()).toEqual(true);
      });

      it("works on simple queries", function(){

        expect(GGRC.query_parser.parse('a=b')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('n = 22')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('5words = "These are just 5 words"')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('5words = "is a phraze"')
            .evaluate(values)).toEqual(false);
        expect(GGRC.query_parser.parse('n != "this is a phraze"')
            .evaluate(values)).toEqual(true);
      });

      it("works on more comlpex queries", function(){

        expect(GGRC.query_parser.parse('a=b')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('(n = 22 or n = 5)')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('(n = 22 and  n = 5) and ("bacon ipsum" !~ bacon)')
            .evaluate(values)).toEqual(false);
        expect(GGRC.query_parser.parse('("bacon ipsum" ~ bacon) and ("bacon ipsum" !~ bacon)')
            .evaluate(values)).toEqual(false);
        expect(GGRC.query_parser.parse('(n = 22 or n = 5) and ("bacon ipsum" ~ bacon)')
            .evaluate(values)).toEqual(true);
        expect(GGRC.query_parser.parse('n != "something that does not exist"')
            .evaluate(values)).toEqual(true);
      });

    });

  });

});

