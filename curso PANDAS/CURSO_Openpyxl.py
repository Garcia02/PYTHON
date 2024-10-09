import openpyxl as ex

# Carregar o arquivo Excel existente
arquivo = 'arquivoTeste.xlsx'

workbook = ex.load_workbook(arquivo)

sheet = workbook.active

sheet.merge_cells("D3:F3")

workbook.save(arquivo)

