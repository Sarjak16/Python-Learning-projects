import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=3)

features.add_data('http://www.youtube.com')
features.make(fit=True)
generate_image= features.make_image(fill_color="black", back_color="white")
generate_image = qrcode.make("HELLO_WORLD")
generate_image.save(image.png)

