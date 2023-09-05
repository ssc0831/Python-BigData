import xlrd
import xlwt

workbook = xlrd.open_workbook('C:/Users/admin/Desktop/Python, BigData/source/Excel/singer.xls')
outWorkbook = xlwt.Workbook()
idx = 4  # 평균 키의 인덱스

wsheetList = workbook.sheets()
outSheet = outWorkbook.add_sheet("singer")
worksheet = wsheetList[0]
for col in range(worksheet.ncols):
    outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList:
    for row in range(1, worksheet.nrows):
        height = worksheet.cell_value(row, idx)
        if int(height) >= 165:
            totalRow += 1
            for col in range(worksheet.ncols):
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

# 인원이 6명 이상인 경우에만 저장
if totalRow >= 6:
    outWorkbook.save('C:/Users/admin/Desktop/Python, BigData/source/outSinger3.xls')
    print("Save. OK~")
else:
    print("Save. OK~")
