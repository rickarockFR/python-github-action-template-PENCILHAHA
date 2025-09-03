import requests
import os

def get_image(x,y):
    img_data = requests.get(f'https://backend.wplace.live/files/s0/tiles/{x}/{y}.png').content
    while b'The owner of this website (backend.wplace.live) has banned you temporarily from accessing this website.' in img_data:
        print('rate')
        time.sleep(12)
        print('rate-end')
        img_data = requests.get(f'https://backend.wplace.live/files/s0/tiles/{x}/{y}.png').content
    if not b'404 Not Found' in img_data:
        return img_data

files = os.listdir()
i = 1
while f'{i}.png' in files:
    i+=1

with open(f'{i}.png', 'wb') as f:
    f.write(str(get_image(1189,1174)))

