import qrcode
a = qrcode.QRCode()
text_mg=("hello world")
a.add_data(text_mg)
a.make(fit=True)
ab=a.make_image(fill_color="black", back_color="white")
ab.save("abh.png")
print("saved successfully")