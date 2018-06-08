#!/usr/bin/env node

const commander = require('commander');
const package = require('../package.json');
const yopt = require('./core');
const fs = require('fs');

commander
    .version(package.version, '-v, --version')
    .command('compile <path>')
    .option('-d, --dir', 'compile dirictory')
    .action(function(path, cmd) {
        if (cmd.dir) {
            return process.exit(1);
        } else {
            fs.readFile(path, 'utf8', function(err, content) {
                if (err) {
                    console.error(err);
                    return process.exit(1);
                }

                console.log(yopt.compile(content, "pon"));
            });
        }
    });

commander
    .command('decompile <path>')
    .option('-d, --dir', 'decompile dirictory')
    .action(function(path, cmd) {
        if (cmd.dir) {
            return process.exit(1);
        } else {
            fs.readFile(path, 'utf8', function(err, content) {
                if (err) {
                    console.error(err);
                    return process.exit(1);
                }

                console.log(yopt.compile(content, "pas"));
            });
        }
    });
commander.parse(process.argv);
