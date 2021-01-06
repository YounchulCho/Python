from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")       # sample.xlsx file load
ws = wb.active


# Insert the new Row
ws.insert_rows(4)       # Insert the new line at 2nd row
ws.insert_rows(8, 5)    # Insert five lines from 8th row

# Insert the new Column
ws.insert_cols(1)           # Insert the new line at 2nd column
ws.insert_cols(3, 3)        # Insert two lines from 2nd coumn


wb.save("sample_insert_lines.xlsx")
wb.close()                              # Close the work book