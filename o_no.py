from openpyxl import load_workbook
from xlrd import open_workbook

wb = open_workbook('o_no.xls')
ws = wb.sheet_by_index(0)
a = ws.cell(1, 0).value
b = ws.cell(2, 0).value
a_bool = bool(a)
b_bool = bool(b)
print(a, type(a), a_bool)
print(b, type(b), b_bool)

wb = load_workbook('o_no.xlsx', data_only=True)
ws = wb.active
a = ws["A2"].value
b = ws["A3"].value
a_bool = bool(a)
b_bool = bool(b)
print(a, type(a), a_bool)
print(b, type(b), b_bool)
