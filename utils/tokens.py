
main = [

    # главные функции и конструкции
    (r'program', "INIT_NAME"),
    (r'\{', "BEGIN"),
    (r'\}', "END"),
    (r'uses', "IMPORT"),

    (r'for', "FOR"),

    (r'(\(|\))', "MODIFICATOR"),

    # коментари и докстринг
    (r'\//', "COMMENT_LINE"),
    (r'/\*', "COMMENT_MULTI_START"),
    (r'\*/', "COMMENT_MULTI_END"),

    # значения переменных
    (r'\=[0-9]+', "SET_INT"),
    (r'\=(true|false)', "SET_BOOLEAN"),

    # данные
    (r'(\d+)', "INTEGER"),

    # синтаксис
    (r'\;', "END_LINE"),

    (r'const', "CONSTANTA"),

    # базовые операции
    (r'\:\=', "OP_EQ"),
    (r'\+', "OP_SUM"),
    (r'\-', "OP_SUB"),

    (r'(\w+)', "WORD"),
    (r'\.', "END_MAIN_PROGRAMM"),
    (r'.+', "SIM")

]

# после токенизации
constr = [
    (r'(boolean|integer).(\w+)(.*:=.*(\w+)|.*;)', "INIT_VAR_CONSTR"),


    (r'(.+)', "LINE")
]
