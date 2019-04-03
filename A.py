from bs4 import BeautifulSoup
import requests, os

#Akses URL
req = requests.get('https://www.python.org/success-stories/')

domain = 'https://www.python.org' #Menyimpan Domain

soup = BeautifulSoup(req.text, "lxml")
path = os.getcwd()  + '\A'  #windows '\', Linux '/'
if not os.path.exists(path):
    os.mkdir(path)

for div in soup.find_all("div", class_="shrubbery"):
    path = div.find('a',href=True) # Get Sub Domain
    link = domain + path['href'] 

    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")
    content = soup.find('article')

    tittle =  (content.h1.string) 
   	
    name = tittle + ".txt"
    with open("A/" + name, "w") as file :
    	file.write(str(content.text))

print ('Sukses!')
