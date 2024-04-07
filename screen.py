import scrollphathd as sphd
import time
import json

while True:
    file = open('screen.txt', 'a')
    json_string = file.read
    data = json.loads(json_string)
    text = data['text']
    text_lenght = len(text)
    opacity = data['opacity']
    speed = data['speed']
    
    sphd.clear()
    sphd.write_string(text)
    sphd.set_brightness(opacity)
    for _ in range(text_lenght):
        sphd.show()
        sphd.scroll(1)
        time.sleep(speed)

    file.close()