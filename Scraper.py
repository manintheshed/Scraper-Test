
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
url = 'https://www.airbnb.ca/s/Algonquin--Ontario--Canada/homes?flexible_trip_lengths%5B%5D=one_week&query=Algonquin%2C%20ON%20K6V%205T2%2C%20Canada&place_id=ChIJcTOgRmWnzUwR30llwV1zzjY&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&checkin=2022-08-02&checkout=2022-08-05&adults=8&source=structured_search_input_header&search_type=filter_change'
page = requests.get(url)
page
soup = BeautifulSoup(page.text, 'lxml')
soup

df = pd.DataFrame({'Links':[''], 'Title':[''], 'Details':[''], 'Price':[''], 'Rating':['']})

while True:
    
    postings = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
    for post in postings:
        try:
            link = post.find('a', class_ = 'lwm61be dir dir-ltr').get('href')
            link_full = 'https://www.airbnb.ca' +link
            title = post.find('a', class_ = 'lwm61be dir dir-ltr').get('aria-label')
            price = post.find('span', class_ = 'a8jt5op dir dir-ltr').text
            rating = post.find('span', class_ = 't5eq1io r4a59j5 dir dir-ltr').text
            details = post.find_all('div', class_ = 'f15liw5s s1cjsi4j dir dir-ltr')[0].text
            df = df.append({'Links':link_full, 'Title':title, 
                            'Details':details, 'Price':price, 'Rating':rating})
            
        except:
            pass
        
    next_page = soup.find('a', {'aria-label':'Next'}).get('href')
    next_page_full = 'https://www.airbnb.ca'+next_page
    next_page_full
    
    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
