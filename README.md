# recipe_crawler
It is crawler for '10000 recipe(만개의 레시피)' web site.
<img width="1440" alt="스크린샷 2020-04-04 오후 10 09 27" src="https://user-images.githubusercontent.com/59409892/78451522-0d2c6380-76c1-11ea-95b5-af4a0bcd83d4.png">
(https://www.10000recipe.com/)

# About this Project
## Getting Started
You should install 'selenium', 'BeautifulSoup' and 'chronedriver.'
If you don't know how to install it and use Mac, you can refer my blog.
(https://blog.naver.com/paula23/221804021407)

After use it, you can get '.csv' file and it will include recipe name, recipe image(275*275) url, and ingredients in recipe detail page, for each 'category'. 
<img width="859" alt="스크린샷 2020-04-04 오후 10 18 42" src="https://user-images.githubusercontent.com/59409892/78451716-41545400-76c2-11ea-9d76-9ab8b4a015d1.png">
This is the example of csv file.

## How to use it
You should set 'category_dict', with those you want to get information.
In dictionary you should put 'category name:category number'.
Category number is in site url, after click category page.

Sometimes, this program can print 'error : ~'.
You can ignore it, because some recipes have different html and I didn't need it.
If you want to crawl more pages or get more information, refer code and find comment.
