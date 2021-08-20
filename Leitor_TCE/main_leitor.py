from leitor_tceV2 import read_est_org_tce
import xlsxwriter
from lista_link import lista_link_tce

nome_arquivo = 'Funcionários_TCE'  # nome do arquivo excel
nome_planilha = 'Funcionários_TCE'  # nome da planilha(aquela aba no arquivo)

# leitura da lista de links de modo a entrar em cada link e fazer a verificação dos nomes e trazer para um aquivo excel
geral = lista_link_tce()
print(geral)
print(len(geral))
print('*' * 150)
lista_setor = []
for link in geral:
    divisor = link.split('/')
    lista_setor.append(divisor[-1])
print(lista_setor)
print(len(lista_setor))
# pagina = ['44-gabinete-da-presidencia', '45-procuradoria-juridica']
tabela = []
lista = ['Nome', 'Setor']
tabela.append(lista.copy())
lista.clear()
for i in range(len(geral)):
    print(f'Link analisado {geral[i]}')
    leitura = read_est_org_tce(geral[i])
    setor = lista_setor[i].replace('/', '')
    print(f'Início de leitura de {setor}')
    lista_linha = []
    for nome in leitura:
        lista_linha.append(nome)
        lista_linha.append(setor)
        tabela.append(lista_linha.copy())
        lista_linha.clear()
    leitura.clear()
    print(f'Fim da leitura de {setor}')
    print('*' * 150)

# for item in setor:
#     ulr = geral
#     leitura = read_est_org_tce(ulr)
#     setor = item.replace('/', '')
#     lista_linha = []
#     for nome in leitura:
#         lista_linha.append(nome)
#         lista_linha.append(setor)
#         tabela.append(lista_linha.copy())
#         lista_linha.clear()
#     leitura.clear()
#     print(f'Fim da leitura de {setor}')
print(tabela)
print(len(tabela))
workbook = xlsxwriter.Workbook(nome_arquivo + '.xlsx')
worksheet = workbook.add_worksheet(nome_planilha)
for i in range(len(tabela)):
    worksheet.write(i, 0, tabela[i][0])
    worksheet.write(i, 1, tabela[i][1])
workbook.close()
