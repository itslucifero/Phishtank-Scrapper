from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup
import requests
import re
from colorama import Fore
from colorama import Style
from colorama import init


init(autoreset=True)
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT




b = '''
PHISH TANK SCRAPPER LALALALLA
100 pages scrapper 
'''
for x in range(1, 100):
	r = requests.get(f'https://phishtank.org/phish_search.php?page={x}&active=y&verified=u')

	soup = BeautifulSoup(r.content,"html.parser")

	table = soup.find("table",{"class": "data"})

	tr = table.find_all("tr")

	for each_tr in tr:
		td = each_tr.find_all('td')
		
		gg = []
		for each_td in td:
			
			gg.append(each_td.text)
		if gg == []:
			pass
		else:
			bb = []
			bb.append(gg[1])
			urls = [i.split('added', 1)[0] for i in bb]
			url = urls
			
			def checker(url):
				try:
					response = requests.get(url, timeout=10)
					if response.status_code == 200:
						print("\033[42;1m -- VALID URL -- \033[0m "+url)
						with open('validurls.txt', 'a') as file:
							file.write(url + '\n')
					else:
						print(url, 'TRASH URL')
						pass		
				except Exception as e:
					pass
			mp = Pool(10)	
			mp.map(checker, url)
			mp.close()
			mp.join()		