palavras = ('aprender','programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'Na palavra {p.upper()} temos', end=' ')
    for i in p:
        if i.lower() in 'AaEeIiOoUu':
            print(i, end=' ')
    print()
