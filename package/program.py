import re
import time
import json
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

def connect_gspread(jsonf,key):
    scope           = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials     = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc              = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet       = gc.open_by_key(SPREADSHEET_KEY) # .sheet1 シートの指定
    return worksheet

# def url_encode(text):
#     text_encode = text.encode("UTF-8")
#     conversion = str(text_encode).replace('x', '').replace("'", '').lstrip('b').replace('\\', '%')
#     return conversion

def wiki_url(anime):
    url = 'https://ja.wikipedia.org/wiki/'
    
    text_encode = anime.encode("UTF-8")
    conversion = str(text_encode).replace('x', '').replace("'", '').lstrip('b').replace('\\', '%')

    coalescence = (url + conversion)
    coalescence_check = requests.get(coalescence)

    if coalescence_check != '<Response [200]>':
        link = f'=HYPERLINK("{coalescence}","{anime}")' # ページのurlをハイパーリンクにする（できない）
        # print(link)
        # return link
        return coalescence
    else:
        return 'null'

    # url_list = []
    # url_list.append(url + encode) # もし連続でしたいと起用にリストにしている（しなくてもいい）

    # for j in url_list:
    #     x = requests.get(j)
    #     if x != '<Response [200]>':
    #         link = f'=HYPERLINK("{j}","{anime}")' # ページのurlを直接取る
    #         print(link)
    #         # return link
    #         return j
    #     else:
    #         return 'null'

def official_url(title):
    goole_url   = "https://www.google.com/search?q="
    coalescence = (f'"{title}"　テレビアニメ')

    text_encode = title.encode("UTF-8")
    conversion = str(text_encode).replace('x', '').replace("'", '').lstrip('b').replace('\\', '%')

    search_url  = requests.get(f'{goole_url}{conversion}')
    soup        = BeautifulSoup(search_url.text, 'lxml')
    title_text = soup.select("div > a")

    for searchResult in title_text:
        title_text = searchResult.text
        url = re.sub("\/url\?q=","",searchResult.get('href')).split('&')[0] # subで/url\?q=を除外している
        if 'https://' in url or 'http://'in url:
            if not '' == title_text and title in title_text or '公式' in title_text:
                if not 'wiki' in url:
                    return url



# def official_url(title):
#     from selenium import webdriver
#     import chromedriver_binary

#     driver = webdriver.Chrome()
#     driver.get('https://www.google.com/')
#     search = driver.find_element_by_name('q')
#     search.send_keys(title) # search.send_keys(title + " " + '公式')
#     search.submit()
#     time.sleep(3)

#     class_g    = driver.find_element_by_class_name('g')
#     # title_text = class_g.find_element_by_class_name('LC20lb').text
#     title_url  = class_g.find_element_by_tag_name('a').get_attribute('href')

#     driver.quit()
    
#     return title_url
