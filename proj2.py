#proj2.py
# import urllib.parse
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import ssl

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
req = urllib.request.Request(base_url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()
soup = BeautifulSoup(response_str, "html.parser")

for item in soup.find_all(class_="story-heading")[:10]:
    print (item.get_text())

# for story_heading in soup.find_all(class_="story-heading")[:10]:
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())



#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com/'
req = urllib.request.Request(base_url)

response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()
soup = BeautifulSoup(response_str, "html.parser")

for item in soup.find_all(class_="view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266"):
    print (item.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
req = urllib.request.Request(base_url)

response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()
soup = BeautifulSoup(response_str, "html.parser")
for line in soup.find_all('img'):
    # print(line.get('alt'))
    if line.has_attr("alt"):
        print(line['alt'])
    else:
        print("No alternative text provided!")
# #### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here

base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
req = urllib.request.Request(base_url)

response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()
soup = BeautifulSoup(response_str, "html.parser")
n = 0
for i in range(6):
    base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'+"&"+"page="+str(i)
    req = urllib.request.Request(base_url)
    response_str = None
    with urllib.request.urlopen(req, context=ctx) as response:
    	response_str = response.read().decode()
    soup = BeautifulSoup(response_str, "html.parser")
    for line in soup.find_all(class_= "field field-name-contact-details field-type-ds field-label-hidden"):
        n += 1
        base_url = 'https://www.si.umich.edu'
        base_url = base_url + str(line.find("a").get('href'))
        # print(base_url)
        req1 = urllib.request.Request(base_url)
        response_str1 = None
        with urllib.request.urlopen(req1, context=ctx) as response1:
        	response_str1 = response1.read().decode()
        soup1 = BeautifulSoup(response_str1, "html.parser")
        # print(soup1)
        a = soup1.find(class_='field field-name-field-person-email field-type-email field-label-inline clearfix').find('a')
        # print(a)
        print(str(n) + ' ' +a.get_text())
