# -*- coding: utf-8 -*-
# Апрель 2018

import ui
import os
from utils.parser import Parser
from utils.lexer import *

@ui.Timer("Time")
def main(name=''):
    # установка ui (логгера)
    ui.setup(verbose=True)

    choices = ["Directory", "File"]
    choices = ui.ask_choice("What to convert", choices)
    if (choices == "File"):
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

            #print(code)
            #print(tConstruction(code))

            pasfile = str(name).replace('.pon', '.pas')

            file = open(pasfile, 'w+')
            for line in code:
                ui.info(line)
                file.write(line + '\n')

            # Вывод информации
            ui.info_section("Status")
            ui.info("Converted to Pascal: ", ui.green, "ok")
            ui.info("File saved: ", ui.green, "ok")
    else:
        name = ui.ask_string("Folder", default="./examples/")

        confirm = ui.ask_yes_no("Confirm?", default=True)
        if (confirm):
            ui.info_count(1, 6, "Read list of files")

            files = os.listdir(name)

            for f in files:
                if f.endswith('.pon'):
                    file = open(name + f)

                    ui.info_count(2, 6, "Get source code on PON file")

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

                    pasfile = str(f).replace('.pon', '.pas')

                    file = open(name + pasfile, 'w+')
                    for line in code:
                        ui.info(line)
                        file.write(line + '\n')

                    ui.info(f + " converted to Pascal: ", ui.green, "ok")

            # Вывод информации
            ui.info_section("Status")
            ui.info("Converted to Pascal: ", ui.green, "ok")
            ui.info("Files saved on folder: ", ui.green, "ok")

if __name__ == "__main__":
    # start main code
    main()
