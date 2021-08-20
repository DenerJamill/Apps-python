def separador_excel(arqent, col=1, sheini=1, entrada='padrao'):
    r"""
    Separa arquivos excel(xls e xlsx) pela coluna especificada.
    :param arqent: Arquivo de entrada(sem a extensão)
    :param col: Coluna de analise para a separação
    :param sheini: Planilha de inicio de leitura.
    :param entrada: Esse parametro é usado para caso queira fazer separação de elemenos especificos presentes na coluna
    de analise
    :return: Planilhas separadas pela coluna indicada.
    """
    import xlrd
    import xlsxwriter
    from os import mkdir
    from time import time
    iniciotot = time()
    iniciord = time()

    # Remove Caracteres, tem seu uso no criador de arquivos pois o Windows não aceita alguns caracteres especiais.
    def chr_remove(old, to_remove):
        new_string = old
        for z in to_remove:
            new_string = new_string.replace(z, '-')
        return new_string

    # Faz leitura do arquivo e retorna uma lista onde cada elemento da lista representa uma linha da planilha
    def xlread(arq_xls, ini=sheini):
        #  abre o arquivo para leitura
        xls = xlrd.open_workbook(arq_xls)
        # pega a primeira linha do arquivo
        plan = xls.sheets()
        leitura = []
        for b in range(ini-1, len(plan)):
            plan = xls.sheets()[b]
            for i in range(plan.nrows):
                # ler cada valor da linha
                leitura.append(plan.row_values(i))
                # yield plan.row_values(i)
        return leitura

    arquivo = xlread(arqent + '.xlsx', ini=sheini)
    arquivo = list(arquivo)
    planilha = xlrd.open_workbook(arqent + '.xlsx')
    nome_planilha = planilha.sheet_names()
    nome_planilha = nome_planilha[0]
    lista = []
    # Criação da lista de componentes a serem divididos.
    c = 0
    if entrada == 'padrao':
        for line in arquivo:
            if c == 0:
                c += 1
                pass
            elif line[col - 1] not in lista:
                lista.append(line[col - 1])
    else:
        for line in arquivo:
            linha = line[col-1]
            linha = linha.upper()
            if c == 0:
                c += 1
                pass
            elif line[col-1] not in lista and linha in entrada:
                lista.append(line[col-1])
    finalrd = time()
    tempo_leitura = finalrd - iniciord
    print(f'Tempo de leitura de {tempo_leitura:.2f} Segundos')
    print(lista)
    elementos_lista = len(lista)
    print(f'A lista possui {elementos_lista} elementos.')
    # Determinação de tamanho do cabeçalho como maior numero de caracteres.
    maior = []
    for y in range(len(arquivo[0])):
        tam = len(str(arquivo[0][y])) + 3
        if tam > 150:
            tam = 150
        maior.append(tam)
    # Criando pasta com as separações
    try:
        mkdir(arqent)
    except FileExistsError:
        pass
    # Criação dos arquivos com base na lista de componentes.
    cont = 0
    nome_arquivo = arqent.split('\\')
    nome_arquivo = nome_arquivo[-1]
    for a in lista:
        iniciowt = time()
        texto = str(a)
        novo = chr_remove(texto, r'\/:*?"<>|')
        workbook = xlsxwriter.Workbook(arqent + '\\' + nome_arquivo + '_' + novo + '.xlsx')
        worksheet = workbook.add_worksheet(nome_planilha)
        x = 1
        y = 0
        cont += 1
        cabecalho = []
        item = 0
        for line in arquivo:
            if y == 0:
                for item in range(len(line)):
                    value = line[item]
                    valued = {'header': value}
                    cabecalho.append(valued)
                y += 1
            if id(str(a)) == id(str(line[col - 1])):
                for item in range(len(line)):
                    if 'dt_' in arquivo[0][item] or '_data' in arquivo[0][item] or 'data_' in arquivo[0][item]:
                        value = line[item]
                        str_value = str(value)
                        data = workbook.add_format({'num_format': 'dd/mm/yyyy'})
                        worksheet.write(x, item, value, data)
                        if maior[item] < len(str_value) < 150:
                            maior[item] = len(str_value)
                        worksheet.set_column(item, item, maior[item])
                    elif 'vl_' in arquivo[0][item] or 'valor_' in arquivo[0][item]:
                        value = line[item]
                        str_value = str(value)
                        valor = workbook.add_format({'num_format': 'R$ #,##0.00'})
                        worksheet.write(x, item, value, valor)
                        if maior[item] < len(str_value) < 150:
                            maior[item] = len(str_value)
                        worksheet.set_column(item, item, maior[item])
                    else:
                        value = line[item]
                        str_value = str(value)
                        if maior[item] < len(str_value) < 150:
                            maior[item] = len(str_value)
                        worksheet.write(x, item, value)
                        worksheet.set_column(item, item, maior[item])
                x += 1
        worksheet.add_table(0, 0, x-1, item, {'columns': cabecalho})
        workbook.close()
        cabecalho.clear()
        print(f'{cont}/{elementos_lista}. Planilha "{a}" criada!')
        finalwt = time()
        print(f'Tempo de escrita de {finalwt - iniciowt:.2f} segundos')
        tempo_previsto = int(((finalwt - iniciowt) * (elementos_lista - cont))/60)
        print(f'Tempo previsto de conculsão de aproximadamente {tempo_previsto} minutos.')
    print('FINALIZADO!')
    finaltot = time()
    print(f'Tempo de execução de {(finaltot - iniciotot)/60:.2f} minutos.')

