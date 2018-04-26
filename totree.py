import ui
from utils.lexer import totree

s = [['program', 'Hello-World', ';'], [], ['uses', 'crd', ';'], [], ['var', 'i', ':', 'integer', ';'], [], ['/*'], ['Многострочный', 'коментарий'], ['*/'], ['//', 'обычный', 'коментарий'], [';'], ['{'], ['for', '(', 'i', ':', '=10', ')', 'do', '{'], ['WriteLn', '(', 'i', ')', ';'], ['}', ';'], ['}', '.']]

y = []

for i in s:
    for j in i:
        y.append(j)

ui.info_2(totree.main(y))
