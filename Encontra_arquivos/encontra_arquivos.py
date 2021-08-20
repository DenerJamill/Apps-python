def encontra_arquivos(diretorio='padrao', tipo='.egp', arq_saida='Arquivos encontrados'):
    r"""
    Encontra arquivos do tipo especificado no diretório também especificado.
    :param diretorio: Diretório a ser lido. Por padrão o diretório definido é I:\. Ex: C:\, C:\pasta, D:\...
    :param tipo: Tipo de arquivos a ser procurado nos diretórios especificados. Por padrão é definido como .egp.
    Ex: .egp, .xlsx, .txt...
    :param arq_saida: Nome do arquivo excel a ser gerado.
    :return: Planilha excel com os arquivos especificados presentes nos diretórios e subdiretórios pesquisados.
    """
    from pathlib import Path
    from datetime import datetime
    import win32security
    import xlsxwriter

    cabecalho = ['id', 'Caminho do arquivo', 'data de criação',
                 'data de modificação', 'data do ultimo acesso', 'Proprietário']
    linha = []
    lista = []
    # Verificação se o diretório é o padrão (I:\) ou se é um outro diretório.
    if diretorio == 'padrao':
        path = Path(r'C:\ '.strip())
    else:
        path = Path(diretorio)
    cont = 0
    # Leitura dos arquivos do tipo especificado
    for filename in path.rglob('*' + tipo):
        cont += 1
        # Coleta as informações armazenadas no sistema de arquivos windows.
        info = filename.stat()
        # Conversão do nome do arquivo para str.
        arq = str(filename)
        # Coletando informações de proprietário armazenados no windows
        sd = win32security.GetFileSecurity(arq, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        nome, dominio, tip = win32security.LookupAccountSid(None, owner_sid)
        lista.append(cont)  # Contador de aplicações encontradas(id)
        lista.append(str(filename))  # Caminho completo do arquivo encontrado
        lista.append(str(datetime.fromtimestamp(info.st_ctime)))  # Data de criação do arquivo
        lista.append(str(datetime.fromtimestamp(info.st_mtime)))  # Data de modificação do arquivo
        lista.append(str(datetime.fromtimestamp(info.st_atime)))  # Data do ultimo uso do arquivo
        lista.append(str(dominio + r'\ '.strip() + nome))
        linha.append(lista.copy())
        lista.clear()
    # Criação e escrita da planilha
    workbook = xlsxwriter.Workbook(arq_saida + '.xlsx')
    worksheet = workbook.add_worksheet('Planilha1')
    for k in range(len(cabecalho)):
        worksheet.write(0, k, cabecalho[k])
    for i in range(len(linha)):
        for j in range(len(linha[i])):
            worksheet.write(i+1, j, linha[i][j])
        print(f'Linha {linha[i][2]} escrita')
    workbook.close()
    print(f'Temos ao todo {cont} arquivos do tipo "{tipo}"')


if __name__ == '__main__':
    encontra_arquivos()
