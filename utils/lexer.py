# -*- coding: utf-8 -*-
# TODO: покрыть тестами

import ui
import re
import os
import json
from utils import tokens
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer


@ui.Timer("Tokenizing constructions")
def tConstruction(code):
    token = []

    temp = []
    status = False  # для проверки найдены ли совпадения по данному слову
    
    for token_ex in tokens.constr:
        pattern, tag = token_ex
        regex = re.compile(pattern)

        match = regex.match(code)

        if (match and status == False):
            line = match.group(0)
            if tag != "LINE":
                status = True
                temp.append([
                    text,
                    tag
                ])
            else:
                status = True
                temp.append([
                    line,
                    tag
                ])
    print(token)
    token.append(temp)

    return token


@ui.Timer("Tokenizing code")
def tokenize(code):
    token = []

    ui.info_section("Tokenized code")
    # построчно преобразуем(для сохранения структуры кода)
    code = TreebankWordTokenizer().tokenize(code)

    for word in code:
        temp = []
        status = False  # для проверки найдены ли совпадения по данному слову

        for token_ex in tokens.main:
            pattern, tag = token_ex
            regex = re.compile(pattern)

            match = regex.match(word)

            if (match and status == False):
                text = match.group(0)
                print(match.group())
                if tag:
                    status = True
                    temp.append([
                        text,
                        tag
                    ])

        token.append(temp)

    return token


"""
Преобразует токены в текст
@param tokens: Список токенов которые нужно преобразовать
"""


@ui.Timer("Detokenizing code")
def detokenize(tokens):
    text = []
    code = []
    temp = []

    for word in tokens:
        if word[1] in ['END_LINE', 'BEGIN', 'END_MAIN_PROGRAMM']:
            temp.append(word[0])
            code.append(temp)
            temp = []
        else:
            temp.append(word[0])
    # TODO: заглушка для ошибки, изменить логику!
    code.append(temp)

    # построчно преобразуем(для сохранения структуры кода)
    for line in code:
        conv = TreebankWordDetokenizer().detokenize(line)
        # вывод работы
        ui.info(conv)
        # добавляем строку
        text.append(conv)

    return text


#
# DEV
#
if __name__ == '__main__':
    s = [['program', 'Hello-World', ';'], ['uses', 'crd', ';'], ['var', 'i', ':', 'boolean', ';'], ['i', ':=', '10', '+', '5'],
         [';'], ['{'], ['for', '(', 'i', ':', '=10', ')', 'do', '{'], ['WriteLn', '(', 'i', ')', ';'], ['}', ';'], ['}', '.']]

    temp = tokenize(s)

    for line in temp:
        for word in line:
            ui.info(word[0], ui.green, word[1])
