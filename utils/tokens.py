
main = [
    (r'(\w+)', "WORD"),

    (r'program', "INIT_NAME"),
    (r'\{', "BEGIN"),
    (r'\}', "END"),


    (r'\=[0-9]+', "INT_TO"),

    (r'\;', "END_LINE"),

    (r'var', "VAR"),
    (r'const', "CONSTANTA")

]
