from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv
import time

# make CSV column
def make_csv(filename) :
    file = open(filename, 'w', encoding='utf-8')
    wtr = csv.writer(file, delimiter=',')
    wtr.writerow(['name','ingredients','url'])

# function that change list to string in csv file
def list_to_str(words):
    words = str(words)
    words = words.replace("'","")
    words = words.replace('[','')
    words = words.replace(']','')
    return words

# If you want to crawl other category, you can change 'category dict'.
# 밥/죽/떡:cat4=52, 찌개:cat4=55, 술안주:cat2=19, 디저트:cat2=17
category_dict = {"rice" : "cat4=52", "stew" : "cat4=55", "alcohol" : "cat2=19", "dessert" : "cat2=17"} 
url = "https://www.10000recipe.com/recipe/list.html?"
url_dict = {}
for category in category_dict:
    # save CSV
    csv_file = 'recipe_'+category+'.csv'
    make_csv(csv_file)
    url_dict[category] = url+category_dict[category]+"&order=reco&page=1"
    # If you want to crawl more, refer under line.
    #url_list.append(url+category_dict[category]+"&order=reco&page=2") #by change last number(2) you can crawl more.
print("crawling category:", url_dict)

driver = webdriver.Chrome('/') #put 'chromedriver' path
for category in category_list[1:]:
    url = url_dict[category]
    #csvfile 만들고 작성
    file = open('recipe_'+category+'.csv','w',encoding='utf-8')
    wtr = csv.writer(file, delimiter=',')
    wtr.writerow(['name','ingredients','url'])
    
    list_to_csv=[]
    #beautiful soup 불러오기
    driver.get(url+category_dict[category])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(category)
    menu_list = soup.find_all("a", {"class" : "thumbnail"})
    print("menu_list_len : ", len(menu_list))
    for menu_num, menu in enumerate(menu_list):
        try:
            #recipe name
            save_list = []
            name = menu.find("h4",{"class":"ellipsis_title2"}).text
            save_list.append(name)
            #image url
            url = menu.find("img").get("src")
            save_list.append(url)
            #recipe href
            href = menu.get("href")
            href = 'https://www.10000recipe.com'+href
            #move detail page
            driver.get(href)
            href_html = driver.page_source
            href_soup = BeautifulSoup(href_html, 'html.parser')
            #ingredients
            ingredients = href_soup.find("div", {"class" : "ready_ingre3"})
            ingredient_list = []
            for ingredient in ingredients.find_all('li'):
                ingredient = ingredient.text.strip()
                ingredient_list.append(ingredient.split('\n')[0].strip())
            ingredient_str = list_to_str(ingredient_list)
            save_list.insert(1,ingredient_str)
            print("saved : ",save_list)
            wtr.writerow(save_list)
        except:
            print("error : ",category,menu_num)
            continue
    file.close()