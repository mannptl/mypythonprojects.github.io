import qrcode
import image

qrcode = qrcode.QRCode()

data = "www.instagram.com/compify.works"

qrcode.add_data(data)
qrcode.make(fit = True)

img = qrcode.make_image(fill="Black" , back_color="white")

img.save("Compify Works - Instagram.png")