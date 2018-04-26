# -*- coding: utf-8 -*-
# TODO: покрыть тестами

import ui
import os
import json
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
#from utils.code import toPas

"""
Клас для получения токенов из кода и сопостовление с уже имеющимися конструкциями на Pascal
При иницилизации получает:
@param code: Строка которая содержит исходный код на PONe
"""
class pon2pas:
    def __init__(self, code):
        self.code = code
        self.token = []

    def main(self):
        # проебразуем pon код в список
        token = self.tokenize()
        ui.info(token)
        # транслируем PON код в Pascal
        pas = toPas().start(token)
        # получение текста из списка
        text = self.detokenize(pas)
        return pas

    def tokenize(self):
        token = []
        ui.info_section("Tokenized code")
        # построчно преобразуем(для сохранения структуры кода)
        for line in self.code:
            conv = TreebankWordTokenizer().tokenize(line)
            # вывод работы
            ui.info_1(conv)

            token.append(conv)
        return token

    def detokenize(self, tokens):
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

        d.detokenize(self.token)

"""
Преобразует вывод лексера в JSON дерево с привязкой потомков
@param code: список команд после работы лексера

Для вывода результата используеться main который и иницилизирует работу данного класса
"""
class totree:
    def main(code):
        # TODO: добавить выход из класса
        return totree.conv2tree(code)

    def conv2line(code):
        ui.info_section("Prepering to JSON tree")
        #лист для хранение всего кода в строку
        s = []

        # запуск фор по всем строкам
        for line in code:
            # по всем словам в строке
            for r in line:
                # добавляем в временную преременную
                s.append(r)

        # вывод результата в консоль
        ui.info_1(s)
        return s

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
            elif code[i] == "{" or code[i] == "}":
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
    s = [['program', 'Hello-World', ';'], [], ['uses', 'crd', ';'], [], ['var', 'i', ':', 'integer', ';'], [], ['/*'], ['Многострочный', 'коментарий'], ['*/'], ['//', 'обычный', 'коментарий'], [';'], ['{'], ['for', '(', 'i', ':', '=10', ')', 'do', '{'], ['WriteLn', '(', 'i', ')', ';'], ['}', ';'], ['}', '.']]

    y = []

    for i in s:
        for j in i:
            y.append(j)
    temp = totree.main(y)
    for line in temp[1]:
        print(line)
