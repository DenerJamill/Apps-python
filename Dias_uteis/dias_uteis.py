# Verificação se o ano informado é um ano bissexto
def bissexto(anob):
    bissext = False
    if anob % 4 == 0:
        if anob % 100 == 0:
            if anob % 400 == 0:
                bissext = True
        else:
            bissext = True
    return bissext


# Verifica qual dia do ano será a páscoa
def feriado_pascoa(anop):
    dia_pascoa = []
    c = anop // 100
    n = anop - 19 * (anop // 19)
    k = (c - 17) // 25
    i = c - (c // 4) - ((c - k) // 3) + (19 * n) + 15
    i = i - 30 * (i // 30)
    i = i - ((i // 28) * (1 - (i // 28) * (29 // (i + 1)) * ((21 - n) // 11)))
    j = anop + (anop // 4) + i + 2 - c + (c // 4)
    j = j - 7 * (j // 7)
    l1 = i - j
    m = 3 + ((l1 + 40) // 44)
    d = l1 + 28 - 31 * (m // 4)
    dia_pascoa.append(d)
    dia_pascoa.append(m)
    dia_pascoa.append('Feriado de Páscoa')
    return dia_pascoa


# Verifica quais dias serão carnaval
def feriado_carnaval(anoc):
    dia_car = []
    pasc = feriado_pascoa(anoc)
    carnaval = 47 - pasc[0]
    if pascoa[1] == 4:
        if carnaval > 30:
            carnaval = carnaval - 31
            if bissexto(anoc):
                dia_carnaval = 29 - carnaval
            else:
                dia_carnaval = 28 - carnaval
            mes_carnaval = 2
        else:
            dia_carnaval = 31 - carnaval
            mes_carnaval = 3
    else:
        if bissexto(anoc):
            dia_carnaval = 29 - carnaval
        else:
            dia_carnaval = 28 - carnaval
        mes_carnaval = 2
    dia_car.append(dia_carnaval)
    dia_car.append(mes_carnaval)
    dia_car.append('Feriado de Carnaval')
    return dia_car


# Verifica qual dia será a sexta feira da paixão(Corpus Christi
def feriado_paixao(anop):
    dia_pai = []
    pas = feriado_pascoa(anop)
    dia_paixao = pas[0] - 2
    mes_paixao = pas[1]
    if dia_paixao < 1:
        mes_paixao -= 1
        dia_paixao = 31 - abs(dia_paixao)
    dia_pai.append(dia_paixao)
    dia_pai.append(mes_paixao)
    dia_pai.append('Feriado de Sexta feira da Paixão')
    return dia_pai


anos_visualizacao = 1  # quantos anos serão verificados
ano = 2021  # Qual o primeiro ano a ser verificado
mes = 1  # A partir de que mês será verificado
dia = 1  # A partir de que dia será verificado
lista_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
"""A variavel "cont" se refera a qual dia da semana será o primeiro dia da verificação, no caso em questão
o dia 01/01/2021 foi uma sexta logo o dia da semana é o quarto elemento do lista_semana, caso altere as variáveis
ano, mes ou dia, verifique qual dia é o dia da semana e mude de acordo"""
cont = 4
semana = lista_semana[cont]
# cont = 4
dias_ano = []

# Criação e escrita do arquivo txt
with open('teste.txt', 'w', encoding='UTF-8') as arquivo:
    for c_ano in range(anos_visualizacao):
        # Lista de feriados não móveis
        lista = [[1, 1, 'Confraternização Universal'], [19, 3, 'Dia de São José'], [25, 3, 'Data Magna do Ceará'],
                 [21, 4, 'Tiradentes'], [1, 5, 'Dia do trabalho'], [15, 8, 'Dia de Nossa Senhora da Assunção'],
                 [7, 9, 'Independência do Brasil'], [12, 10, 'Feriado de Nossa Senhora Aparecida'], [2, 11, 'Finados'],
                 [15, 11, 'Proclamação da República'], [25, 12, 'Natal']]
        # Verificação dos feriados móveis
        pascoa = feriado_pascoa(ano)
        f_carnaval = feriado_carnaval(ano)
        if f_carnaval[0] < 2:
            if bissexto(ano):
                f_carnaval2 = [29, 2, f_carnaval[2]]
            else:
                f_carnaval2 = [28, 2, f_carnaval[2]]
        else:
            f_carnaval2 = [f_carnaval[0] - 1, f_carnaval[1], f_carnaval[2]]
        if bissexto(ano):
            if f_carnaval[0] > 28:
                cinzas = [1, 3, 'Feriado de quarta feira de cinzas']
            else:
                cinzas = [f_carnaval[0] + 1, f_carnaval[1], 'Feriado de quarta feira de cinzas']
            dias = 366
        else:
            if f_carnaval[0] > 27:
                cinzas = [1, f_carnaval[1] + 1, 'Feriado de quarta feira de cinzas']
            else:
                cinzas = [f_carnaval[0] + 1, f_carnaval[1], 'Feriado de quarta feira de cinzas']
            dias = 365
        f_paixao = feriado_paixao(ano)
        if pascoa[0] < 2:
            f_corpus_christi = [31, 5, 'Feriado de Corpus Christi']
        else:
            f_corpus_christi = [pascoa[0] - 1, pascoa[1]+2, 'Feriado de Corpus Christi']
        # Acescentando os feriados móveis a lista de feriados
        lista.append(f_carnaval2)
        lista.append(f_carnaval)
        lista.append(cinzas)
        lista.append(f_paixao)
        lista.append(f_corpus_christi)
        print(lista)
        cont2 = 0
        print(f'ano {ano} dias {dias}')
        # Verificação de dias uteis
        while cont2 < dias:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if dia > 31:
                    dia = 1
                    mes += 1
            elif mes == 2:
                if bissexto(ano):
                    if dia > 29:
                        dia = 1
                        mes += 1
                else:
                    if dia > 28:
                        dia = 1
                        mes += 1
            else:
                if dia > 30:
                    dia = 1
                    mes += 1
            if mes > 12:
                mes = 1
            if cont > 6:
                cont = 0
            semana = lista_semana[cont]
            if cont in range(0, 5):
                util = 'Dia útil'
                if pascoa[0] == dia and pascoa[1] == mes:
                    util = 'Feriado de Páscoa'
                for feriado in lista:
                    if feriado[0] == dia and feriado[1] == mes:
                        util = feriado[2]
                        break
            else:
                util = 'FDS'
            arquivo.write(f'{semana}, dia {dia}, mês {mes}, ano {ano} é {util}.\n')
            dias_ano.append([semana, dia, mes, ano, util])
            dia += 1
            cont += 1
            cont2 += 1
        ano += 1
# verificação de dias uteis em um determinado periodo de tempo
# contador_dias_util = 0
# for x in dias_ano:
#     if (x[4] == 'Dia útil' or x[4] == 'Feriado de Carnaval' or x[4] == 'Feriado de quarta feira de cinzas') \
#             and 2 <= x[2] <= 4:
#         if x[2] == 4 and x[1] <= 18:
#             contador_dias_util += 1
#         elif x[2] == 3 and x[1] >= 8:
#             contador_dias_util += 1
#         else:
#             pass
# print(contador_dias_util)
