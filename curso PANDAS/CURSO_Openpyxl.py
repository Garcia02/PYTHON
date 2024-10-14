import openpyxl as ex

# Carregar o arquivo Excel existente
arquivo = 'arquivoTeste.xlsx'

workbook = ex.load_workbook(arquivo)

sheet = workbook.active

sheet['A1'].font = ex.styles.Font(bold = True)