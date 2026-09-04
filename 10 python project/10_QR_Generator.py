# import qrcode
# import shutil
# import os
# url = input("Enter the URL you want to convert to QRcode: ")
# filename = input("Enter the filename you want to save it as: ")

# if not(filename.endswith(".png")):
#     filename = filename + '.png'

# img = qrcode.make(url)
# img.save(filename)
# if not os.path.exists("QR"):
#     os.mkdir("QR")
# if filename.endswith('.png'):
#     shutil.move(filename, os.path.join("QR", filename))


import qrcode
import shutil
import os

url = input("Enter the URL you want to convert to QRcode: ")
filename = input("Enter the filename you want to save it as: ")

if not(filename.endswith(".png")):
    filename = filename + '.png'

qr = qrcode.QRCode(
    version=10,      # This sets the QR code size/version
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,     # This controls the size of each small square in the QR code.
    border=4,       # This sets the thickness of the empty border around the QR code. 
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save(filename)

if not os.path.exists("QR"):
    os.mkdir("QR")
if filename.endswith('.png'):
    shutil.move(filename, os.path.join("QR", filename))