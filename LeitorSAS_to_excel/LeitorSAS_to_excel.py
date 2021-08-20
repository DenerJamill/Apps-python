def leitorsas(arqentrada):
    r"""
     A função leitorsas lê um arquivo de programação sas(extensão '.sas') e gera um arquivo excel(extensão '.xlsx')
     informando as tabelas usadas e seus dependentes.
    :param arqentrada: Nome do arquivo de entrada entre aspas(simples ou duplas) sem a extensão. Ex: 'teste',
    r'I:\Aplicativos\teste'
    :return: Um arquivo xlsx gerado com as informações de criação e dependencia vinda a partir do arquivo de entrada.
    """
    from xlsxwriter import Workbook
    textfile = arqentrada
    # Tratamento de enconde de leitura para poder lê-los sem problemas.
    f = open(textfile, 'r+')
    row_list = []  # Lista de linhas
    # noinspection PyTypeChecker
    for row in f:
        row_list.append(row)
    # Criação do arquivo e escrita do cabeçalho.
    workbook = Workbook(arqentrada + '.xlsx')
    worksheet = workbook.add_worksheet('Planilha1')
    worksheet.write(0, 0, 'Tabela')
    worksheet.write(0, 1, 'Tabela Dependente')
    lista = []
    lista_linha = []
    lin = 1
    # tab = ''
    flag = 0
    # Escrita dos elementos do arquivo
    for row in row_list:
        if 'CREATE TABLE' in row or 'DATA' in row:
            if 'DATA' in row and 'SORT' not in row:
                tabela = row.split()
                for i in tabela:
                    if '.' in i:
                        tab = i
            elif 'CREATE TABLE' in row:
                tabela = row.split()
                for i in tabela:
                    if '.' in i:
                        tab = i
            flag = 1
        elif 'FROM' in row and flag == 1:
            tabela = row.split()
            worksheet.write(lin, 1, tab)
            for i in tabela:
                if '.' in i:
                    lista_linha.append(tab)
                    worksheet.write(lin, 0, i)
                    lista_linha.append(i)
                    lin += 1
                    lista.append(lista_linha.copy())
                    lista_linha.clear()
        elif 'SET' in row and flag == 1:
            tabela = row.split()
            worksheet.write(lin, 1, tab)
            lista_linha.append(tab)
            escrito = 1
            for i in tabela:
                if '.' in i and escrito == 1:
                    escrito = 0
                    lista_linha.append(tab)
                    worksheet.write(lin, 0, i)
                    lin += 1
                    lista_linha.append(i)
                    lista.append(lista_linha.copy())
                    lista_linha.clear()
        elif 'JOIN' in row and flag == 1:
            tabela = row.split()
            worksheet.write(lin, 1, tab)
            escrito = 1
            for i in tabela:
                if '.' in i and escrito == 1:
                    escrito = 0
                    lista_linha.append(tab)
                    worksheet.write(lin, 0, i)
                    lin += 1
                    lista_linha.append(i)
                    lista.append(lista_linha.copy())
                    lista_linha.clear()
    # Verificação e escrita do caso 2 "Se tabela 2 é dependente de tabela 1 e tabela 1 é dependente da tabela 3, então
    # a tabela 2 é dependente da tabela 3
    worksheet.write(lin, 0, 'Enquadrados no caso 2')
    lin += 1
    for linha in lista:
        for j in range(len(lista)):
            if linha[0] == lista[j][1]:
                worksheet.write(lin, 1, lista[j][0])
                worksheet.write(lin, 0, linha[1])
                lin += 1
    workbook.close()
