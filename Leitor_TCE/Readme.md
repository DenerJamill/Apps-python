# Leitor_TCE
Realiza a leitura dos nomes de cada setor da página de estrutura organizacional do TCE e compara com os nomes encontrados em planilhas baixadas do portal da transparência do TCE.

A ordem de execução dos aplicativos é:
- main_leitor.py: Essa aplicação cria uma planilha com os nomes encontrados no site do TCE
- junta_planilha.py: Pega as informações nas planilhas baixadas do portal da transparência e converte para apenas uma planilha com todas as informações das outras.
- compara_planilhas.py: Faz a comparação entre as planilhas obtidas nos processos anteriores.
