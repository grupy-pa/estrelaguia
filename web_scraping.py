import requests
from bs4 import BeautifulSoup as soup

def scraper(signo):
    resp = requests.get( f"https://www.horoscopovirtual.com.br/horoscopo/{signo}" )

    html = soup(resp.text, 'html.parser')

    hoje_div= html.find('div', attrs={'class': 'days-wrapper'})
    hoje = hoje_div.find('p')
    hoje = hoje.text

    horoscopo_div = html.find('p', attrs={'class': 'text-pred'})
    horoscopo = horoscopo_div.text.strip()

    horoscopo = horoscopo.replace("Compartilhar", horoscopo)

    return f"Seu horoscopo de hoje ({hoje}) é: {horoscopo}"