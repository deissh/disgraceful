# -*- coding: utf-8 -*-

import ui

"""
Преобразует синтаксис PON в синтаксис Pascal.ABC
"""
class toPas:
    def __init__(self, cfg=[]):
        self.cfg = cfg

    @ui.Timer("Converting to Pascal style")
    def start(self, context):
        ui.info_section("Converted to Pascal")

        # запуск преобразоателей кода
        context = self.toFor(context) # Преобразование цикла for
        context = self.toBegin(context) # Преобразование { и } в begin и end
        context = self.toComments(context) # Преобразование коментариев

        # Вывод в консоль результата
        for line in context:
            ui.info_1(line)

        return context

    def toFor(self, context):
        # TODO: add parser
        return context

    """
    Используеться для преобразования фигурных скобок в begin\end
    @param context: Принимает преобразованый исходный код PON в виде списка
    """
    def toBegin(self, context):
        for i, line in enumerate(context):
            for j, string in enumerate(line):
                if context[i][j] == '{': context[i][j] = 'begin'
                if context[i][j] == '}': context[i][j] = 'end'

        return context

    """
    Используеться для преобразования коментариев написаных на PON в коментарии Pascal
    @param context: Принимает преобразованый исходный код PON в виде списка
    """
    def toComments(self, context):
        for i, line in enumerate(context):
            for j, string in enumerate(line):
                if context[i][j] == '/*': context[i][j] = '{'
                if context[i][j] == '*/': context[i][j] = '}'

        return context
