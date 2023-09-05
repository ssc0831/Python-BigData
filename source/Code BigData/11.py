import xlrd
import xlwt

workbook = xlrd.open_workbook('C:/Users/admin/Desktop/Python, BigData/source/Excel/singer.xls')
outWorkbook = xlwt.Workbook()

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    outSheet = outWorkbook.add_sheet(worksheet.name)
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            outSheet.write(row, col, worksheet.cell_value(row, col))

outWorkbook.save('C:/Users/admin/Desktop/Python, BigData/source/Excel/outSinger1.xls')
print("Save. OK~")
