

import re
import requests
from bs4 import BeautifulSoup
import OpenSSL
import os


alphabet_1=None  # alphabet_1 list is initalized
alphabet_2=None  # alphabet_2 list is initalized
Number=None      # Number list is initalized
value_list=[]    # value_list list is initalized 
for iter_1 in range(97,123):   #These loops is for used to create all prntscr naming
    alphabet_1=str(chr(iter_1))
    for iter_2 in range(97,123):
        alphabet_2=str(chr(iter_2))
        for iter_3 in range(9999):
            Number=str(iter_3)
            #print (alphabet_1+alphabet_2+Number)
            value_list.append(alphabet_1+alphabet_2+Number)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}   #User agent need for scraping

# Create folder if not already they
if os.path.isdir('Pics_folder'):
    pass
else:
    os.mkdir('Pics_folder')

# Main Loop for scraping
for i in range(1000,1100):
    site = f'https://prnt.sc/{value_list[i]}' # Main url to scrap with variable name
    response = requests.get(site,headers=headers) # requests.get for url
    soup = BeautifulSoup(response.text, 'html.parser') # parse the response.text
    img_tags = soup.img
    if (img_tags['src']=='//st.prntscr.com/2022/09/11/1722/img/0_173a7b_211be8ff.png' or 'imageshack' in img_tags['src']): #if it include the string in img_tags then skip this name
        pass
    else:       
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', img_tags['src']) # Search file extension in file 
        filename_ext=str(filename) # convert it string
        if not filename:
            print("Regex didn't match with the url: {}".format(img_tags['src']))
            continue
        #print (filename_ext[-6:-2])
        #f = open('Pics_folder/'+str(i)+filename_ext[-6:-2], "wb")
        #proxies = {'https': 'http://182.253.105.123:8080'}
        responses=None
        try: # Try requests for specify img_tags['src']  
            responses = requests.get(img_tags['src'],headers=headers)
        except:
            f=open("my_file.txt", "a")
            f.write("cant scrap this photo\n")
            f.write(site+'\n')
            f.write(img_tags['src']+'\n')
            continue
        f = open('Pics_folder/'+str(value_list[i])+filename_ext[-6:-2], "wb") # Create the file
        f.write(responses.content) # Write to it

