import pyqrcode
import png
from pyqrcode import QRCode

QRstring = input("write what you want to qr: ")

name = input('write file name: ') +'.png'

url = pyqrcode.create(QRstring)

url.png(name, scale =8)

#url.png('qr.png', scale =8)
