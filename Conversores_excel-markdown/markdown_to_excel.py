def markdown_to_excel(arqentrada, arqsaida='convertido', divisor='|'):
    """
     Converte um arquivo markdown(txt) em um arquivo excel(xls)
    :param arqentrada: Nome do arquivo de entrada entre aspas(simples ou duplas) sem a extensão. Ex: 'conversão'
    :param arqsaida: Nome do arquivo de saída entre áspas(simples ou duplas) sem a extensão. Ex: 'conversao'
    Por padrão o arquivo de saida é definido como 'convertido'
    :param divisor: Caracter separador do arquivo entre áspas(simples ou duplas). Ex: ','
    Por padrão o divisor é definido como '|'
    :return: Um arquivo xls convertido a partir do arquivo de entrada.
    """
    import xlwt
    textfile = arqentrada + '.txt'

    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    style = xlwt.XFStyle()
    f = open(textfile, 'r+')
    row_list = []
    for row in f:
        row_list.append(row.split(divisor))
    column_list = zip(*row_list)
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    i = 0
    for column in column_list:
        for item in range(len(column)):
            value = column[item].strip()
            if is_number(value):
                worksheet.write(item, i, int(value), style=style)
            else:
                worksheet.write(item, i, value)
        i += 1
    workbook.save(arqsaida + '.xls')


markdown_to_excel('conversão')
