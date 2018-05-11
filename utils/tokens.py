
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

    # названия переменных
    (r'(i|j)', "VAR"),

    # значения переменных
    (r'\=[0-9]+', "SET_INT"),
    (r'\=(true|false)', "SET_BOOLEAN"),

    # данные
    (r'(\d+)', "INTEGER"),

    # синтаксис
    (r'\;', "END_LINE"),

    (r'var', "INIT_VAR"),
    (r'const', "CONSTANTA"),

    # базовые операции
    (r'\:\=', "OP_EQ"),
    (r'\+', "OP_SUM"),
    (r'\-', "OP_SUB"),

    (r'(\w+)', "WORD")

]

# после токенизации
post = [
    (r'(\w+)+(\(|\))', "FUNCTION")
]
