# -*- coding: utf-8 -*-

import ui

"""
Преобразует синтаксис PON в синтаксис Pascal.ABC
"""
class Parser:
    def __init__(self, cfg=[]):
        self.cfg = cfg

    @ui.Timer("Converting to Pascal style")
    def start(self, tokens):
        ui.info_section("Converted to Pascal")

        # запуск преобразоателей кода
        tokens = self.toFor(tokens) # Преобразование цикла for
        tokens = self.toBegin(tokens) # Преобразование { и } в begin и end
        tokens = self.toComments(tokens) # Преобразование коментариев

        # Вывод в консоль результата
        for line in tokens:
            if line != []:
                pass
                #ui.info_1(line[0][0], ui.red, line[0][1])

        return tokens

    def toFor(self, tokens):
        # TODO: add parser
        return tokens

    """
    Используеться для преобразования фигурных скобок в begin\end
    @param tokens: Принимает преобразованый исходный код PON в виде списка
    """
    def toBegin(self, tokens):
        temp = []
        for line in tokens:
            for word in line:
                if word[1] == "BEGIN":
                    word[0] = "begin"
                elif word[1] == "END":
                    word[0] = "end"
                temp.append(word)
        return temp

    """
    Используеться для преобразования коментариев написаных на PON в коментарии Pascal
    @param tokens: Принимает преобразованый исходный код PON в виде списка
    """
    def toComments(self, tokens):
        return tokens
