import requests, urllib.request, socket
from bs4 import BeautifulSoup
from colorama import Fore,Style

from pyfiglet import figlet_format
from rich import print


class Main:
    def __init__(self, quantity=10):
        self.quantity = quantity

    def is_bad_proxy(self, pip):
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': pip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            req=urllib.request.Request('http://www.bing.com')  # change the URL to test here
            sock=urllib.request.urlopen(req, timeout=10)

        except urllib.error.HTTPError as e:
            return False
        except Exception:
            return False
        return False


    def scrap_proxy(self):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')
        rows = table.find_all('tr')
        proxy_list = []

        for row in range(self.quantity+1):
            cols = rows[row].find_all('td')
            if len(cols) > 0:
                anonmity = cols[6].text.strip()
                ip = cols[0].text.strip()
                port = cols[1].text.strip()
                if anonmity != 'transparent':
                    proxy_list.append(f'{ip}:{port}')
        return proxy_list
    
    def get_proxy(self):
        socket.setdefaulttimeout(10)
        for currentProxy in self.scrap_proxy():
            if self.is_bad_proxy(currentProxy):
                pass
            else:
                print(Fore.GREEN+currentProxy)



if __name__=="__main__":
    title = figlet_format('PScrap', font='isometric2')
    print(f'[red]{title}[/red]\n\t\t[red]Created by ROHIT[/red]')
    
    try:
        proxy_quan = int(input(Fore.MAGENTA+"How many proxies you want: "))
        obj = Main(proxy_quan)
        obj.get_proxy()
    except ValueError:
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'Only NUMBERIC value is valid.')
        
        