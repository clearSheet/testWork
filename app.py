import requests
from bs4 import BeautifulSoup


urls = [
    'https://ok.ru/group/50911509086355',
    'https://ok.ru/prizu',
    'https://ok.ru/stiihiya',
    'https://ok.ru/dobryesoveti',
    'https://ok.ru/buildingpostroytelo'
]

for i in range(len(urls)):
    req = requests.get(urls[i])
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    img_href = soup.find(class_='group-avatar_img')

    print(img_href['src'][2:])
