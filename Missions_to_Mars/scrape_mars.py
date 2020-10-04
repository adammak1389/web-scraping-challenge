# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
import pandas as pd

def scrape():
    #Step 1 - Scraping
    # NASA Mars News

    # chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://mars.nasa.gov/news/'
        # Retrieve page with the requests module
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Parse the latest News Title and Paragraph Text
    news_title = soup.find("section", class_="grid_gallery module list_view").find("div", class_="grid_layout").find("li", class_="slide").find("div", class_="content_title").find("a").text

    news_paragraph = soup.find("div", class_="grid_layout").find("li", class_="slide" ).find("div", class_="article_teaser_body").text

    # soup instance for NASA JPL website
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # JPL Mars Space Images - Featured Image
    # scraping JPL mars site for featured image and building url
    featured_space_image_url = soup.find('a', class_="button fancybox")["data-fancybox-href"]
    featured_space_image_url = 'https://www.jpl.nasa.gov' + featured_space_image_url
    featured_space_image_url

    # Mars Facts
    url = 'https://space-facts.com/mars/'
    mars_facts_table = pd.read_html(url)
    mars_facts_table = pd.DataFrame(mars_facts_table[0])
    mars_facts_table.columns = ["Mars Profile Elements", "Element Values"]
    mars_facts_table = mars_facts_table.set_index("Mars Profile Elements")
    mars_facts_table

    # converting pandas dataframe to html
    mars_table_html = print(mars_facts_table.to_html())

    # Mars Hemispheres

    mars_hemispheres = ['Cerberus', 'Syrtis_Major', 'Valles_Marineris', 'Schiaparelli']

    mars_hemisphere_image_urls = []
    for hemispheres in mars_hemispheres:
    
        url = f'https://astrogeology.usgs.gov/search/map/Mars/Viking/{hemispheres}_enhanced'
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')

        imgLoc = soup.find('div', class_="downloads").find('a')['href']
        
        title = f'{hemispheres} Hemisphere'
        
        # titles and image urls into dictionary
        mars_hemisphere_data = {"title": title, "img_url": imgLoc}
        mars_hemisphere_image_urls.append(mars_hemisphere_data)

    mars_data = {"news_title": news_title, "news_paragraph": news_paragraph, "mars_featured_space_image":featured_space_image_url, "mars_table": mars_table_html, "mars_hemisphere_data":mars_hemisphere_image_urls }

    # Close Browser
    browser.quit()

    # Results
    return mars_data


def scrape_image():

    # chrome extension
    executable_path = {'executable_path': 'C:/Users/adamm/Downloads/chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemispheres = ['Cerberus', 'Syrtis_Major', 'Valles_Marineris', 'Schiaparelli']

    mars_hemisphere_image_urls = []
    for hemispheres in mars_hemispheres:
    
        url = f'https://astrogeology.usgs.gov/search/map/Mars/Viking/{hemispheres}_enhanced'
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')

        imgLoc = soup.find('div', class_="downloads").find('a')['href']
        
        title = f'{hemispheres} Hemisphere'
        
        # titles and image urls into dictionary
        mars_hemisphere_data = {"title": title, "img_url": imgLoc}
        mars_hemisphere_image_urls.append(mars_hemisphere_data)