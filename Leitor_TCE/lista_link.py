from bs4 import BeautifulSoup
import urllib.request


# Retorna os links de cada setor da estrutura organizacional de modo que não precise deigitar-los 1 a 1.
def lista_link_tce():
    link = 'https://www.tce.ce.gov.br/institucional/estrutura-organizacional'

    soup = BeautifulSoup(urllib.request.urlopen(link), 'html.parser')
    body = soup('div', {"class": "item-page"})[0].find_all('li')
    separador = str(body)
    separador = separador.split('"')
    nova_lista1 = []
    nova_lista2 = []
    for k in range(len(separador)):
        if 'estrutura-organizacional' in separador[k]:
            nova_lista1.append(separador[k])
        # if '>' in teste[k] or '<' in teste[k]:
        #     pass
        # else:
        #     nova_lista1.append(teste[k])
    # print(nova_lista1)
    # print(len(nova_lista1))
    nova_lista2 = []
    for i in nova_lista1:
        if 'http://' in i:
            link = i
        else:
            link = 'http://www.tce.ce.gov.br' + i
        nova_lista2.append(link)
    # print(nova_lista2)
    # teste dos strong
    body = soup('div', {"class": "item-page"})[0].find_all('strong')
    separador = str(body)
    separador = separador.split('"')
    nova_lista1 = []
    for k in range(len(separador)):
        if 'estrutura-organizacional' in separador[k]:
            nova_lista1.append(separador[k])
    # print(nova_lista1)
    # print(len(nova_lista1))
    for i in nova_lista1:
        if 'http://' in i:
            link = i
        else:
            link = 'http://www.tce.ce.gov.br' + i
        nova_lista2.append(link)
    return nova_lista2
# for i in body:
#     novo_link = str(i).replace('<li><a href="', '')
#     nova_lista2.append(novo_link)
# print(nova_lista2)
# print(len(nova_lista2))
