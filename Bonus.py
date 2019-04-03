from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import time
import sys
import os


# start = time.time()

#Akses URL
req = requests.get('https://www.python.org/success-stories/')
domain = 'https://www.python.org'
soup = BeautifulSoup(req.text, "lxml")

all_urls = list() 
num = 0
def get_all_url():
	for div in soup.find_all('div', class_= "small-widget success-story-category"):
		for link in div.find_all('a', href= True):
			all_urls.append(domain +link['href'])
			
	# for link in :

def scrape(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    content = soup.find('article')
    tittle =  (content.h1.string)
    tittle = tittle.replace(" ","_")
    tittle = tittle.replace("/","_")
    print (tittle)
    name = tittle + ".txt"
    with open("Bonus/" + name, "w") as file :
    	file.write(str(content.text))

# define the name of the directory to be created
path = os.getcwd()  + '\Bonus' #windows '\', Linux '/'
get_all_url()
if not os.path.exists(path):
    os.mkdir(path)

for url in all_urls:
    scrape(url)
# p = Pool(10)
# p.map(scrape, all_urls)
# p.terminate()
# p.join()
    


