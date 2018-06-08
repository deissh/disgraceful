#!/usr/bin/env node
/*!
 * YoptaScript v0.3.4 (https://yopta.space)
 * Copyright (c) 2016-2017 Yopta.Space project and Contributors
 * Licensed under the MIT license
 */

const
  yopt = require('./core'),
  fs = require('fs');

let
  filepath = process.argv[2];

if (!filepath) {
    console.log('Missing filename argument.');
    return process.exit();
}

fs.readFile(filepath, 'utf8', function (err, content) {
    if (err) {
        console.error(err);
        return process.exit(1);
    }

    console.log(yopt.compile(content, "pon"));
});
