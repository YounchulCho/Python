from openpyxl import Workbook


wb = Workbook()             # Create the work book
ws = wb.active              # Get the ativated sheet
ws.title = "RPASheet"       # Change the sheet's name
wb.save("sample.xlsx")      # Save the file with name
wb.close()                  # Close the work book
