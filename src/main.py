# -*- coding: utf-8 -*-
# Author: Deissh
# Апрель 2018

import ui
import os
from utils.lexer import pon2pas

# установка ui (логгера)
ui.setup(verbose=True)

name = ui.ask_string("Enter file", default="./examples/hello-world.pon")

confirm = ui.ask_yes_no("Продолжить?", default=False)
if (confirm):
    ui.info_2("Start read file")
    file = open(name)

    ui.info_2("Start get context")
    # иницилизация класса для работы с кодом на PON и PAS
    cont = pon2pas(file.readlines())
    pas = cont.main()
