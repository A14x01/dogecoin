import requests
from bs4 import BeautifulSoup

def parse_ssr():
    response = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('a', {'href': '/currencies/dogecoin/markets/'}).text
    return data

if __name__ == '__main__':
    print('Dogecoint rate:', parse_ssr())