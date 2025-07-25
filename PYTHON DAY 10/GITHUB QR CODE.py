import qrcode
url="https://github.com/shinjini8104"

a = qrcode.QRCode()

a.add_data(url)
a.make(fit=True)
ab=a.make_image(fill_color="black", back_color="white")
ab.save("github.png")
print("saved successfully")