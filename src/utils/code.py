# -*- coding: utf-8 -*-

import ui

"""
Преобразует синтаксис PON в синтаксис Pascal.ABC
"""
class toPas:
    def __init__(self, cfg=[]):
        self.cfg = cfg

    def start(self, context):
        context = self.toFor(context)
        context = self.toBegin(context)
        return context

    @ui.Timer("Convert for to while")
    def toFor(self, context):
        return context

    @ui.Timer("Convert to begin/end")
    def toBegin(self, context):
        for i, line in enumerate(context):
            for j, string in enumerate(line):
                if context[i][j] == '{': context[i][j] = 'begin'
                if context[i][j] == '}': context[i][j] = 'end'
        ui.info_1(context)

        return context
