import qrcode

qr = qrcode.QRCode(version=1, box_size=1, border=0)
login = 'login'
password = 'password'
text = f'{login.ljust(12)}\n{password.ljust(12)}'
key = 'BB - BigBrains'
qr.add_data(''.join([chr(ord(key[i % len(key)]) ^ ord(j)) for i, j in enumerate(text)]))
img = qr.make_image()
img.save('qr.png')
