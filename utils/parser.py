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
            ui.info_1(line)

        return tokens

    def toFor(self, tokens):
        # TODO: add parser
        return tokens

    """
    Используеться для преобразования фигурных скобок в begin\end
    @param tokens: Принимает преобразованый исходный код PON в виде списка
    """
    def toBegin(self, tokens):
        for line in tokens:
            for word in line:
                if word[1] == "BEGIN":
                    word[0] = "begin"
                elif word[1] == "END":
                    word[0] = "end"
        return tokens

    """
    Используеться для преобразования коментариев написаных на PON в коментарии Pascal
    @param tokens: Принимает преобразованый исходный код PON в виде списка
    """
    def toComments(self, tokens):
        for line in tokens:
            for word in line:
                if word[1] == "COMMENT_MULTI_START":
                    word[0] = "{"
                elif word[1] == "COMMENT_MULTI_END":
                    word[0] = "}"

        return tokens
