import xlrd
import csv

workbook = xlrd.open_workbook('C:/Users/admin/Desktop/Python, BigData/source/Excel/singer.xls')

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    with open("C:/Users/admin/Desktop/Python, BigData/source/Excel/singer_" + worksheet.name + ".csv", "w", newline='') as outFp:
        csvWriter = csv.writer(outFp)
        for row in range(worksheet.nrows) :
                row_list = worksheet.row_values(row)
                csvWriter.writerow(row_list)

print("Save. OK~")
