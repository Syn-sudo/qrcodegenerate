import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

# QR kodu oluşturmak istediğiniz linki buraya giriniz
data = "LİNK"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=12,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# QR kodun renklerini ayarlayın: fill_color -> kareler, back_color -> arka plan
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

logo = Image.open("logo.png")
qr_w, qr_h = qr_img.size

target = int(min(qr_w, qr_h) * 0.22)
logo.thumbnail((target, target), Image.LANCZOS)

lx = (qr_w - logo.width) // 2
ly = (qr_h - logo.height) // 2
qr_img.paste(logo, (lx, ly), mask=logo if logo.mode in ("RGBA","LA") else None)

qr_img.save("qr_logo.png")
print("QR kod oluşturuldu")

##ことわざ 殺人
##-Syn  