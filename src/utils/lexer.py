# -*- coding: utf-8 -*-

import ui
import os
import json
from nltk.tokenize import TreebankWordTokenizer
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

    @ui.Timer("Getting context")
    def main(self):
        # проебразуем pon код в список
        token = self.tokenize()
        # транслируем PON код в Pascal
        pas = toPas().start(token)

        return pas

    def tokenize(self):
        token = []
        # построчно преобразуем(для сохранения структуры кода)
        for line in self.code:
            token.append(TreebankWordTokenizer().tokenize(line))
        return token
