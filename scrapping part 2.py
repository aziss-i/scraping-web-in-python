#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import lxml
import pandas

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

#mengambil https request
page = requests.get(base_url)
#print(type(page))
#print(page.status_code)

#memverifikasi bahwa kita sudah berhasil memanggil web
if page.status_code == requests.codes.ok:
    
    #mengambil seluruh web dengan beautiful soup
    #print(page.text) : ini untuk mengecek saja
    bs = BeautifulSoup(page.text, 'lxml')
    
#Untuk menemukan sesuatu yang spesifik yang sedang dicari
all_of_players = bs.find('table',class_='multicol').find('ul').find_all('li')
last_ten_players = all_of_players[-10:]

#untuk menyimpan data
data = {
    'tahun': [],
    'negara': [],
    'pemain': [],
    'tim': []
}

#player = last_ten_players[0]
#print(player)

#scraping 10 pemain terbaik
for list_item in last_ten_players:
    
    tahun = list_item.find('span').previousSibling.split()[0]
    if tahun:
        data['tahun'].append(tahun)
    else:
        data['tahun'].append(none)    
        
    negara = list_item.find('a')['title']
    if negara:
        data['negara'].append(negara)
    else:
        data['negara'].append(none)
        
    pemain = list_item.find_all('a')[1].text
    if pemain:
        data['pemain'].append(pemain)
    else:
        data['pemain'].append(none)
        
    tim = list_item.find_all('a')[2].text
    #untuk dimasukkan ke data tim
    if tim:
        data['tim'].append(tim)
    else:

tabel_data = pandas.DataFrame(data, columns=['tahun', 'negara','pemain','tim'])
tabel_data.index = tabel_data.index+1
        data['tim'].append(none)
print(tabel_data)
tabel_data.to_csv('10_pemain_terbaik.csv', sep=',', index=False, encoding='utf-8')



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[61]:


import requests
from bs4 import BeautifulSoup
import lxml
import pandas
base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

#Get https request
page = requests.get(base_url)

#Verification that we have gotten web data
if page.status_code == requests.codes.ok:
    
    #get all web data by using Beautifulsoup
    bs = BeautifulSoup(page.text, 'lxml')

#Searching what we want for example the best players
all_of_players = bs.find('div',id='mw-content-text').find('div',class_="mw-parser-output").find_all('div')
dummy = all_of_players[6].find('ul').find_all('li')
last_ten_players=dummy[-10:]

#save data
data = {
    'Year': [],
    'Country': [],
    'Player': [],
    'Tim': []
}

#Scrapping data for only ten last the best player
for list_item in last_ten_players:
    
    Year = list_item.find('span').previousSibling.split()[0]
    if Year:
        data['Year'].append(Year)
    else:
        data['Year'].append(none) 
        
    Country = list_item.find('a')['title']
    if Country:
        data['Country'].append(Country)
    else:
        data['Country'].append(none)
        
    Player = list_item.find_all('a')[1].text
    if Player:
        data['Player'].append(Player)
    else:
        data['Player'].append(none)
        
    Tim = list_item.find_all('a')[2].text
    if Tim:
        data['Tim'].append(Tim)
    else:
        data['Tim'].append(none)
        
tabel_data = pandas.DataFrame(data, columns=['Year', 'Country','Player','Tim'])
tabel_data.index = tabel_data.index+1
print(tabel_data)

#save data in csv format
tabel_data.to_csv('10_the_best_player.csv', sep=',', index=False, encoding='utf-8')
   
        
   

    


# In[ ]:





# In[ ]:


negara = list_item.find('a')['title']
   if negara:
       data['negara'].append(negara)
   else:
       data['negara'].append(none)
       
   pemain = list_item.find_all('a')[1].text
   if pemain:
       data['pemain'].append(pemain)
   else:
       data['pemain'].append(none)
   
tahun = last_ten_players.find('span').previousSibling.split()[0]

