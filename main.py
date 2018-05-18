# -*- coding: utf-8 -*-
# Апрель 2018

import ui
import os
from utils.parser import Parser
from utils.lexer import *


def main(name=''):
    # установка ui (логгера)
    ui.setup(verbose=True)

    choices = ["Directory", "File"]
    if (ui.ask_choice("What to convert", choices) == "File"):

        name = ui.ask_string("File name", default="./examples/hello-world.pon")

        confirm = ui.ask_yes_no("Confirm?", default=True)
        if (confirm):
            ui.info_count(1, 6, "Read file")

            file = open(name)

            ui.info_count(2, 6, "Get source code on PON")

            # иницилизация класса для работы с кодом на PON и PAS
            ui.info_count(3, 6, "Init main class to convert Pascal")

            cont = tokenize(file.read())
            file.close()

            ui.info_2(cont)

            ui.info_count(4, 6, "Convert PON code to Pascal")

            pas = Parser()
            code = pas.start(cont)

            for line in code:
                ui.info(line[0], ui.green, line[1])

            ui.info_count(5, 6, "Save new file")

            code = detokenize(code)

            file = open("./examples/hello-world.pas", 'w+')
            for line in code:
                ui.info(line)
                file.write(line + '\n')

            # Вывод информации
            ui.info_section("Status")
            ui.info("Converted to Pascal: ", ui.green, "Normal")
            ui.info("File saved: ", ui.green, "Normal")
    else:
        ui.fatal("Please select file")
if __name__ == "__main__":
    # start main code
    main()
