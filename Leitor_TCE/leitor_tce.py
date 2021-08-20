from bs4 import BeautifulSoup
import urllib.request
from unidecode import unidecode


def read_est_org_tce(link):
    soup = BeautifulSoup(urllib.request.urlopen(link), 'html.parser')
    body = soup('div', {"class": "item-page"})
    # print(body)
    linha = str(body[0])
    # Ajustes específicos para facilitar leitura
    linha = linha.replace('\r', '')
    linha = linha.replace('<br/>', '')
    linha = linha.replace('<p>', '')
    linha = linha.replace('</p>', '')
    linha = linha.replace('<b>', '')
    linha = linha.replace('</b>', '')
    linha = linha.replace('<span id="form:lista:0:cv2">', '')
    linha = linha.replace('<span id="form:lista:1:cv2">', '')
    linha = linha.replace('<span id="form:lista:2:cv2">', '')
    linha = linha.replace('<span id="form:lista:3:cv2">', '')
    linha = linha.replace('<span id="form:lista:4:cv2">', '')
    linha = linha.replace('<span id="form:lista:5:cv2">', '')
    linha = linha.replace('<span id="form:lista:6:cv2">', '')
    linha = linha.replace('<span id="form:lista:7:cv2">', '')
    linha = linha.replace('<span id="form:lista:8:cv2">', '')
    linha = linha.replace('<span id="form:lista:9:cv2">', '')
    linha = linha.replace('<span id="form:lista:10:cv2">', '')
    linha = linha.replace('</span>', '')
    linha = linha.replace('<span>', '')
    linha = linha.replace('<pre>', '')
    linha = linha.replace('</pre>', '')
    linha = linha.replace('\xa0', '')  # Nova linha
    linha = linha.replace('Servidor', '')
    linha = linha.split('\n')
    # print(linha)  # Linha de testes
    lista = []
    flag = 0
    # Criação da lista de nomes
    for i in range(len(linha)):
        if '<' in linha[i] or '>' in linha[i] or '\t' in linha[i] or '\xa0' in linha[i] \
                and 'TELEFONE' not in linha[i].upper():
            pass
        else:
            if linha[i] != '':
                # Ajuste de nomes que apresentam "Conselheiro(a)" no nome de modo a retirar o título.
                if 'Conselheiro' in linha[i] or 'Conselheira' in linha[i]:  # linha adicionada
                    linha[i] = linha[i].replace('Conselheiro ', '')  # linha adicionada
                    linha[i] = linha[i].replace('Conselheira', '')
                lista.append(unidecode(linha[i]))
            # Ajustes para retirar algumas palvras como "rua", "telefone" e "contatos" na lista de nomes
            if ('TELEFONE' in linha[i].upper() or 'RUA' in linha[i].upper() or 'CONTATOS' in linha[i].upper()) \
                    and flag < 1:
                tel = len(lista)-1
                flag += 1
                # print(f'Telefone está do indice {tel}')
    # print(lista)
    tam = len(lista)
    # retirada das linhas após os ajustes anteriores
    for i in range(tam-tel):
        lista.pop()
    print(lista)
    print(len(lista))
    return lista


if __name__ == '__main__':
    x = read_est_org_tce('https://www.tce.ce.gov.br/institucional/estrutura-organizacional/30-rh/institucional/'
                         'estrutura-organizacional/62-gabinete-do-auditor-itacir-todero')
    print(x)
