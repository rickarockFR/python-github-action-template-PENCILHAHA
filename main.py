import requests
import os
from time import gmtime, strftime

def get_image(x,y):
    img_data = requests.get(f'https://backend.wplace.live/files/s0/tiles/{x}/{y}.png').content
    while b'The owner of this website (backend.wplace.live) has banned you temporarily from accessing this website.' in img_data:
        print('rate')
        time.sleep(12)
        print('rate-end')
        img_data = requests.get(f'https://backend.wplace.live/files/s0/tiles/{x}/{y}.png').content
    if not b'404 Not Found' in img_data:
        return img_data

files = os.listdir(backups)
i = 1
while f'{i}-1.png' in files:
    i+=1

with open(f'backups/{i}-1.png', 'wb') as f:
    f.write(get_image(1189,1174))
with open(f'backups/{i}-2.png', 'wb') as f:
    f.write(get_image(1190,1174))
with open(f'backups/{i}.txt', 'w') as f:
    f.write(strftime("%H:%M", gmtime()))

