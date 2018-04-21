# -*- coding: utf-8 -*-

import ui
import os
import json
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from utils.code import toPas

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
            ui.info_1(conv)
            text.append(conv)
        return text

        d.detokenize(self.token)
