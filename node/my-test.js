var chai = require('chai');
var sinon = require('sinon');
var expect = chai.expect;
var my = require('./my');

describe('My', function() {
    it ('returnsTrue() should return true', function() {
        var value = my.returnsTrue();
	expect(value).to.be.true;
    });
});

