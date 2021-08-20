
def excel_to_markdown_txt(arqentrada, lcab=2, planilha=1, arqsaida=''):
    r"""
    Transforma arquivos excel em markdown e coloca essa conversão em um txt.
    :param arqentrada: Nome do arquivo a ser transformado entre áspas (duplas ou simples) ''. Ex: arq='test'
    :param lcab: Linha onde se encontra o cabeçalho. Por padrão é definida como a segunda linha do arquivo.
    :param arqsaida: Nome do arquivo de saida. Por padrão o arquivo de saida será criado com o mesmo nome
    e na mesma pasta do arquivo de entrada, com a extensão '.txt'
    Ex: arqentrada = teste.xlsx -> arqsaida = teste.txt
    :return: Um arquivo txt com a conversão do arquivo xlsx para markdown.
    """
    import xlrd
    # Checa se o arquivo existe.
    try:
        book = xlrd.open_workbook(arqentrada + '.xlsx')
    except FileNotFoundError:
        return print(f'Não existe arquivo "{arqentrada + ".txt"}" nesta pasta.')
    # Criação do arquivo de texto
    if len(arqsaida) > 0:
        arquivo = open(arqsaida + '.txt', 'w')
    else:
        arquivo = open(arqentrada + '.txt', 'w')
    # Escreve o cabeçalho da tabela
    sh = book.sheet_by_index(planilha-1)
    for i in range(lcab-1, lcab + 1):
        arquivo.write('| ')
        for j in range(0, sh.ncols):
            if i == lcab-1:
                arquivo.write(str(sh.cell_value(rowx=i, colx=j)).replace('.0', '') + ' | ')
            else:
                arquivo.write('---' + ' | ')
        arquivo.write('\n')
    # Escreve a tabela
    for i in range(lcab, sh.nrows):
        arquivo.write('| ')
        for j in range(0, sh.ncols):
            arquivo.write(str(sh.cell_value(rowx=i, colx=j)).replace('.0', '') + ' | ')
        arquivo.write('\n')
    arquivo.close()
    print('PROGRAMA FINALIZADO!')
