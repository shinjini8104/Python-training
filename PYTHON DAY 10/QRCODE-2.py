import qrcode

a=qrcode.QRCode()
def get_info():
    file=open("cat.txt","r")
    x=file.read()
    return x
text_msg=get_info()
a.add_data(text_msg)
a.make(fit=True)
ab=a.make_image(fill_color="black", back_color="white")
ab.save("cat.png")
print("saved successfully")



