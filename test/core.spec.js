const should = require('chai').should();
const mocha = require('mocha');
const cases = require('./compile.test');
const core = require('../src/core');


describe('core', () => {
    it('can compile to pas', () => {
        cases.map(([pas, pon]) => {
            let res = core.compile(pon, "pon");
            res.chould.equal(pas)
        });
    });
});
