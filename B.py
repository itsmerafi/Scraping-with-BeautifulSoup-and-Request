from bs4 import BeautifulSoup
import requests

#Akses URL
url = 'https://blog.python.org/'
num = 10 #jumlah konten
while True :
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "lxml")
	for div in soup.find_all("div", class_="date-outer"):
	    # print (div.text)
	    # print (div.h3.a.string)
	    # Create File Content
	    name_file = div.h3.a.string + '.txt'
	    with open("B/" + name_file, "w") as file :
	    	file.write(str(div.text))
	    
	    num -= 1
	    #jika sudah sesuai num
	    if num == 0:
	    	break

	# Get link to older page
	# Jika jumlah belum sesuai num
	if num > 0:	
		next_page =  soup.find(id="blog-pager-older-link")
		link = next_page.find('a', href = True)
		url = link['href']

	else :
		print ('Sukses!')
		break