import pandas as pd
import xlsxwriter
from difflib import SequenceMatcher


def xlread(arq_xls):
    #  abre o arquivo para leitura
    xls = pd.read_excel(arq_xls)
    # Pega os valores de cada linha(excluindo a linha de cabeçalho)
    xls = xls.values
    leitura = []
    linha = []
    for i in range(len(xls)):
        # guarda apenas os valores da coluna de nomes
        if len(xls[i]) == 2:
            linha.append(xls[i][0])
            linha.append(xls[i][1])
        else:
            linha.append(xls[i][0])
        leitura.append(linha.copy())
        linha.clear()
    return leitura


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


arquivo1 = 'Funcionários_TCE'
arquivo2 = 'Funcionários_TCE1'
leitura1 = xlread(arquivo1 + '.xlsx')
print(leitura1)
print(len(leitura1))
leitura2 = xlread(arquivo2 + '.xlsx')
print(leitura2)
print(len(leitura2))
print(leitura1[0][0])
nomes_faltosos = []
for j in range(len(leitura1)):
    nome = str(leitura1[j][0])
    flag_achou = 0
    for k in range(len(leitura2)):
        if nome.upper().strip() in str(leitura2[k][0]).upper().strip():
            flag_achou = 1
            break
    if flag_achou == 0:
        nomes_faltosos.append(leitura1[j])

for j in range(len(leitura2)):
    nome = str(leitura2[j][0])
    flag_achou = 0
    for k in range(len(leitura1)):
        if nome.upper().strip() in str(leitura1[k][0]).upper().strip():
            flag_achou = 1
            break
    if flag_achou == 0:
        nomes_faltosos.append(leitura2[j])

print(nomes_faltosos)
print(len(nomes_faltosos))
nome_arquivo = 'Nomes_Faltosos'
nome_planilha = 'Nomes_Faltosos'
workbook = xlsxwriter.Workbook(nome_arquivo + ' - teste.xlsx')
worksheet = workbook.add_worksheet(nome_planilha)
lista = []
flag = 0
linha = 0
for m in range(len(nomes_faltosos)):
    if m == 0:
        worksheet.write(linha, 0, 'Nome')
        worksheet.write(linha, 1, 'Similaridade')
        worksheet.write(linha, 2, 'Setor')
        worksheet.write(linha, 3, 'Caso')
        linha += 1
    if len(nomes_faltosos[m]) == 2 and flag == 0:
        for n in range(len(nomes_faltosos)-m):
            if n == 0:
                pass
            else:
                nome1 = str(nomes_faltosos[m][0])
                nome2 = str(nomes_faltosos[-n][0])
                similaridade = similar(nome1.upper(), nome2)
                if similaridade > 0.8:
                    worksheet.write(linha, 0, nomes_faltosos[m][0])
                    worksheet.write(linha, 1, nomes_faltosos[-n][0])
                    worksheet.write(linha, 3, 'Caso 3')
                    linha += 1
                    flag = 0
                    lista.append(nomes_faltosos[-n][0])
                    break
                else:
                    flag = 1
    if len(nomes_faltosos[m]) == 2 and flag != 0:
        worksheet.write(linha, 0, nomes_faltosos[m][0])
        worksheet.write(linha, 2, nomes_faltosos[m][1])
        worksheet.write(linha, 3, 'Caso 1')
        linha += 1
    elif len(nomes_faltosos[m]) != 2 and nomes_faltosos[m][0] not in lista:
        worksheet.write(linha, 0, nomes_faltosos[m][0])
        worksheet.write(linha, 3, 'Caso 2')
        linha += 1
    flag = 0
worksheet.set_column(0, 1, 50)
workbook.close()
