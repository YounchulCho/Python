from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")       # sample.xlsx file load
ws = wb.active

# Delete the row line
ws.delete_rows(3)                   # Delete the data at 3rd line of row
ws.delete_rows(6, 3)                # Delete three lines from 6th line of row


# Delete the column line
ws.delete_cols(2)                   # Delete the data at 2nd line of column
ws.delete_cols(1, 2)                # Delete two lines from 1st line of column


wb.save("sample_delete_lines.xlsx")
wb.close()                              # Close the work book