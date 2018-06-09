const chai = require('chai');
const mocha = require('mocha');
const cases = require('./compile.test');
const core = require('../src/core');

describe('core', () => {
    it('can compile to js', () => cases.map(([js, ys]) => chai.assert.equal(yopt.compile(ys, "ys"), js)));
    it('can decompile from js', () => cases.map(([js, ys]) => chai.assert.equal(yopt.compile(js, "js"), ys)));
});
