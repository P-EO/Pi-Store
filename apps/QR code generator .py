import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "http://snipping-tool.io"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("mysnipping-tool.svg", scale = 8)
