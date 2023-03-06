import qrcode

link = input("Link: ")

qr = qrcode.QRCode(version=1)
qr.add_data(link)
qr.make()

img = qr.make_image()
img.save("testQR.png")