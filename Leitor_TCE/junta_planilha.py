import xlrd
import xlsxwriter


def xlread(arq_xls, sheini=1):
    leitura = []
    for k in arq_xls:
        #  abre o arquivo para leitura
        xls = xlrd.open_workbook(k + '.xls')
        # pega a primeira linha do arquivo
        plan = xls.sheets()
        for b in range(sheini - 1, len(plan)):
            plan = xls.sheets()[b]
            for i in range(plan.nrows):
                # retira o cabeçalho
                if i < 2 or 'Nome' in plan.row_values(i):
                    pass
                # ler o valor das linhas restantes
                else:
                    leitura.append(plan.row_values(i))
                # yield plan.row_values(i)
        leitura.pop()
        print(f'Fim da leitura de {k}')
        print('*' * 180)
    return leitura


if __name__ == '__main__':
    lista = ['informacoesFuncionais', 'informacoesFuncionais (5)', 'informacoesFuncionais (4)',
             'informacoesFuncionais (3)', 'informacoesFuncionais (2)', 'informacoesFuncionais (1)']
    juntado = xlread(lista)
    for item in juntado:
        print(item)
    print(len(juntado))
    nome_arquivo = 'Funcionários_TCE1'
    nome_planilha = 'Funcionários_TCE'
    workbook = xlsxwriter.Workbook(nome_arquivo + '.xlsx')
    worksheet = workbook.add_worksheet(nome_planilha)
    for i in range(len(juntado)):
        if i == 0:
            worksheet.write(i, 0, 'Nome')
        worksheet.write(i+1, 0, juntado[i][0])
    workbook.close()
