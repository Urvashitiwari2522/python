import qrcode as qr
img = qr.make("https://github.com/urvashitiwari2522")
img.save("Github_Qr.png")
print("QR code generator!")