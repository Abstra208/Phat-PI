import scrollphathd as sphd
import time

file = open('info.txt', 'a')
text = file.read
sphd.clear()
sphd.write_string(text)
while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)