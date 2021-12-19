import qrcode


def gen_qr(login, password):
    if len(login) > 12 or len(password) > 12:
        raise ValueError('Login or password too long')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    text = f'{login.ljust(12)}\n{password.ljust(12)}'
    key = 'BB - BigBrains'
    qr.add_data(''.join([chr(ord(key[i % len(key)]) ^ ord(j)) for i, j in enumerate(text)]))
    print(text)
    print(''.join([chr(ord(key[i % len(key)]) ^ ord(j)) for i, j in enumerate(text)]))
    print(''.join([chr(ord(key[i % len(key)]) ^ ord(j)) for i, j in enumerate(''.join([chr(ord(key[i % len(key)]) ^ ord(j)) for i, j in enumerate(text)]))]))
    img = qr.make_image(back_color="#EDF0F2")
    img.save('qr.png')
