from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = wb = Workbook()                # Create the work book
ws = wb.active


img = Image("image.png")              # Load the image file
ws.add_image(img, "C3")             # Put the image into the C3 cell


wb.save("sample_image.xlsx")
wb.close()                           # Close the work book



#### Error handling
# ImportError: You must install Pillow to fetch image objects
# --> pip install Pillow