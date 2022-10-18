campeonato = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians'
              ,'Bragantino','Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional'
              ,'São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
print('-='*30)
print(f'Lista de times do Brasileirão: {campeonato}')
print('-='*30)
print(f'Os 5 primeiros colocados são {campeonato[0:4]}')
print('-='*30)
print(f'Os 4 últimos colocados são {campeonato[-4:]}')
print('-='*30)
print(f'Em ordem alfabética, os times participantes em 2021 são: {sorted(campeonato)}')
print('-='*30)
print(f'O Chapecoense terminou o campeonato na {campeonato.index("Chapecoense")+1}ª posição')
