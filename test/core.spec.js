const
  chai = require('chai'),
  cases = require('./compile.cases'),
  pon = require('../src/core');


describe('core', () => {
  it('can compile to pas', () => cases.map(([pas, pon]) => chai.assert.equal(pon.compile(pon, "pon"), pon)));
  it('can decompile from pas', () => cases.map(([js, ys]) => chai.assert.equal(pon.compile(pas, "pas"), pas)));
});
