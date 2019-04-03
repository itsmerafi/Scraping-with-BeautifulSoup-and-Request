import numpy as np
import multiprocessing as multi
from bs4 import BeautifulSoup
import requests
import time
import sys , os

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



def chunks(n, page_list):
    """Splits the list into n chunks"""
    return np.array_split(page_list,n)
 
path = os.getcwd()  + '\Bonus' #windows '\', Linux '/'
get_all_url()
if not os.path.exists(path):
    os.mkdir(path)

cpus = multi.cpu_count()
workers = []
page_bins = chunks(cpus, all_urls)

for cpu in range(cpus):
    sys.stdout.write("CPU " + str(cpu) + "\n")
    # Process that will send corresponding list of pages 
    # to the function perform_extraction
    worker = multi.Process(name=str(cpu), 
                           target=scrape, 
                           args=(page_bins[cpu],))
    worker.start()
    workers.append(worker)

for worker in workers:
    worker.join()

print ('Sukses!')
    



# p.map(scrape, all_urls)


# for url in all_urls:
#     scrape(url)
	
#def get_url_per_category():

# end = time.time()
# print(end - start)

