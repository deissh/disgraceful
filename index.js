'use strict';
const inquirer = require('inquirer');

let questions = [];

questions.file = [
    {
        type: 'input',
        name: 'file',
        message: 'Имя файла:',
        default: function() {
            return 'example.pon';
        }
    },
    {
        type: 'list',
        name: 'charset',
        message: 'Выберите кодировку:',
        choices: [
            'UTF-8',
            'Другая'
        ]
    },
    {
        type: 'input',
        name: 'save',
        message: 'Сохранить как:',
        default: function() {
            return 'example.pas';
        }
    }
];


inquirer.prompt(questions.file).then(answ => {
    console.log(answ);
});
