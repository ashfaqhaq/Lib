from bs4 import BeautifulSoup
import urllib.request
text ='Data Structures Through C In Depth'
book = text.replace(" ",'+')
url = 'https://www.goodreads.com/search?q='+book
oururl = urllib.request.urlopen(url)
soup = BeautifulSoup(oururl,'html.parser')
phref=soup.table.tr.td.a['href']
s=phref.find("w/")
e=phref.find(".")
book_id = phref[s+2:e]
print(book_id)
new_url = 'https://www.goodreads.com'+phref
new_oururl = urllib.request.urlopen(new_url)
soup = BeautifulSoup(new_oururl,'html.parser')
x=soup.find_all('div',{'class':'elementList'})
for i in x[0].div.find_all('a'):
	print(i.text)