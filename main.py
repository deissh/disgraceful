# -*- coding: utf-8 -*-
# Апрель 2018

import ui
import os
from utils.lexer import pon2pas

def main(name=''):
    # установка ui (логгера)
    ui.setup(verbose=True)

    choices = ["Directory", "File"]
    if (ui.ask_choice("What to convert", choices) == "File"):

        name = ui.ask_string("File name", default="./examples/hello-world.pon")

        confirm = ui.ask_yes_no("Confirm?", default=False)
        if (confirm):
            ui.info_count(1, 6, "Read file")
            file = open(name)
            ui.info_count(2, 6, "Get source code on PON")

            # иницилизация класса для работы с кодом на PON и PAS
            ui.info_count(3, 6, "Init main class to convert Pascal")
            cont = pon2pas(file.readlines())
            ui.info_count(4, 6, "Convert PON code to Pascal")
            pas = cont.main()
            ui.info_count(5, 6, "Save new file")

            # Вывод информации
            ui.info_section("Status")
            ui.info("Converted to Pascal: ", ui.green, "Normal")
            ui.info("File saved: ", ui.green, "Normal")
    else:
        ui.fatal("Please select file")
if __name__ == "__main__":
    # start main code
    main()
