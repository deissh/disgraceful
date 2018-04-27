# -*- coding: utf-8 -*-
# TODO: покрыть тестами

import ui
import re
import os
import json
import tokens
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

def tokenize(code):
    token = []

    ui.info_section("Tokenized code")
    # построчно преобразуем(для сохранения структуры кода)
    for line in code:
        temp = []
        conv = TreebankWordTokenizer().tokenize(line)

        for word in conv:
            for token_ex in tokens.main:
                pattern, tag = token_ex
                regex = re.compile(pattern)
                match = regex.match(word)
                if match:
                    text = match.group(0)
                    if tag:
                        temp = [
                            text,
                            tag
                        ]

        token.append(temp)

    return token

"""
Преобразует токены в текст
@param tokens: Список токенов которые нужно преобразовать
"""

def detokenize(tokens):
    text = []

    ui.info_section("Detokenized code")
    # построчно преобразуем(для сохранения структуры кода)
    for line in tokens:
        conv = TreebankWordDetokenizer().detokenize(line)
        # вывод работы
        ui.info(conv)
        # добавляем строку
        text.append(conv)

    return text

"""
Получает дерево кода из токенизированного PONа
# WARNING: Рекурсия (может не выйти)
@param code: Принимает токенизированный код для преобразования в JSON дерево
@param tree: Используеться для промежуточного хранения дерева между итерациями
"""
def conv2tree(code, tree=[]):
    temp = [] # обнуление времено переменной перед началом работы

    # главный курсор
    for i in range(0, len(code)-1):
        template = {
            'line': '',
            'sub': []
        }

        if (code[i] == ";"):# end of line
            temp.append(code[i])# добавление в конец точки с зяпятой

            template['line'] = temp

            tree.append(template) # добавление все йстроки (до точки с зяпятой в дерево)
            temp = [] # обнуление для следущей итерации
        elif (code[i] == "{" or code[i] == "}"):
            # если это не конец строки то добавляем в временную переменую для последующей работы
            tree.append(code[i])
        else:
            temp.append(code[i])

        # второй курсор для поиска закрывающих скобок
        # запуск рекурсии по всему коду между ({ и })
        if (code[i] == "{"):
            for j in range(len(code)-i, -1, -1):
                if (code[j] == "}"):
                    template['sub'].append(code[i+1:j-1])
                    tree.append(template)
                    # запуск рекурсии
                    code, tree = self.conv2tree(code[i+1:j-1], tree)

    return code[i+1:j-1], tree


#
# DEV
#
if __name__ == '__main__':
    s = [['program', 'Hello-World', ';'], ['uses', 'crd', ';'], ['var', 'i', ':', 'integer', ';'], ['/*'], ['Многострочный', 'коментарий'], ['*/'], ['//', 'обычный', 'коментарий'], [';'], ['{'], ['for', '(', 'i', ':', '=10', ')', 'do', '{'], ['WriteLn', '(', 'i', ')', ';'], ['}', ';'], ['}', '.']]

    y = []

    for i in s:
        for j in i:
            y.append(j)
    temp = tokenize(y)
    for line in temp:
        print(line)
