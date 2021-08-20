# para ter acesso as bibliotecas primeiramente instale-as através do terminal, segue comando de instalação:
# pip install pdfminer3k
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen


def ler_pdf(arquivopdf):
    # PDFResourceManager Usado para armazenar recursos compartilhados
    # como fontes e imagens
    recursos = PDFResourceManager()
    buffer = StringIO()
    layout_params = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layout_params)
    process_pdf(recursos, dispositivo, arquivopdf)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo


# Abrindo arquivo PDF online
pdf_lido = 'http://imagens.seplag.ce.gov.br/PDF/20210719/do20210719p01.pdf'
arquivoPDF = urlopen(pdf_lido)
stringSaida = ler_pdf(arquivoPDF)
# print(stringSaida)
arquivoPDF.close()
leitura = stringSaida.split('*** *** ***')
# print(leitura)
print(len(leitura))
lista = []
flag_acerto = 0
for i in range(len(leitura)):
    if 'Licitação' in leitura[i] or 'LICITAÇÃO' in leitura[i]:
        if flag_acerto == 0:
            texto = leitura[i].split('AVISO DE')
            lista.append('AVISO DE' + texto[-1])
        # elif i < len(leitura) - 1:
        else:
            lista.append(leitura[i])
        flag_acerto += 1
        # else:
        #     texto = leitura[i].split('*** *** ***')
        #     lista.append(texto[0])
print(len(lista))
print(f'Foram encontrados {flag_acerto} casos.')
arquivo = open('saida.txt', 'w', encoding='UTF-8')
arquivo.write('Dados retirados do pdf encontrado em: ' + pdf_lido + '\n')
arquivo.write('-' * 150)
arquivo.write('\n')
for i in lista:
    # print(i)
    # print('-' * 150)
    arquivo.write(i)
    arquivo.write('-' * 120)
arquivo.close()
# print(stringSaida)
