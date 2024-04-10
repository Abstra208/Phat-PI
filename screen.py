import scrollphathd as sphd
import time
import json

while True:
    with open("screen.json", "r") as file:
        json_string = file.read()
    data = json.loads(json_string)
    text = data['text']
    text_lenght = len(text)
    opacity = data['opacity']
    speed = data['speed']
    
    sphd.clear()
    sphd.flip(x=True,y=True)
    sphd.set_brightness(float(opacity))
    sphd.write_string(text+' ')
    time.sleep(1)
    for _ in range(text_lenght*5+(text_lenght)+5):
        sphd.show()
        sphd.scroll(1)
        time.sleep(float(speed))
