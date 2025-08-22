Bu Python scripti, kendi QR kodunuzu oluşturmanıza ve ortasına logo eklemenize olanak sağlar.  
QR kod renklerini, arka plan rengini ve linki kolayca değiştirebilirsiniz.

## Gereksinimler

Python 3 yüklü olmalı. Kullanılacak kütüphaneler:

- `qrcode`
- `pillow` (PIL)

## Kurulum

### 1️⃣ Kütüphaneleri yükleyin

Windows veya Linux terminal/cmd’de:

pip install qrcode[pil] pillow

## Kullanım

1. `main.py` dosyasını açın ve `data = "LINK"` kısmına, QR kod okutulduğunda yönlendirilmesini istediğiniz linki yapıştırın.  

2. QR kod renklerini değiştirmek için qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB") kısmından istediğiniz renk'in kodunu veyahut adını yazıp kullanabilirsiniz.

3. logo.png eklemek qr kodda istediğiniz logoyu eklemek için kullandığınız logoyu png formatına dönüştrüp logo.png olarak dosyaya eklemek.
