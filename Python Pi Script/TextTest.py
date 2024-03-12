import scrollphathd as sphd
import time
import sys
text = input("Text a afficher: ")

sphd.set_brightness(.25)
sphd.flip(x=True, y=True)
sphd.write_string(text+' ')
while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)