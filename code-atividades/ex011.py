# Cada time é comparado com os demais, mas o índice evita repetir A x B e B x A.
times = ('Flamengo', 'Fluminense', 'Botafogo', 'Vasco', 'America - RJ')
for indice, time1 in enumerate(times):
    for time2 in times[indice + 1:]:
        if time1 != time2:
            print(time1, 'x', time2)
