
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
import time
from re import search
import random
from random import randint
from lackey import *



search_query_list = ['elektromotor vsetko pre priemysel','vibracny motor vsetko pre priemysel','prevodovky vsetko pre priemysel', 'Ozubene kolesa vsetko pre priemysel' ]
proxy_list = ['78.141.107.75:8080', '78.141.98.82:8080' ,'217.119.114.86:8080', '94.229.32.83:3128', '78.41.174.196:8081', '178.143.191.149:8080', '78.41.174.197:8081', '176.101.177.253:8080', '85.237.238.57:8080', '195.168.22.42:8080', '95.105.222.213:8080' ] 

count = 0


for i in range(5000):
    count = count + 1
    proxy_list_query = random.choice(proxy_list)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy_list_query)
    driver= webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")
    #open tab
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    # You can use (Keys.CONTROL + 't') on other OSs

    # Load a page 
    driver.get("https://www.google.com/")
    search = driver.find_element_by_name("q")
    search.clear()
    search_query = random.choice(search_query_list)
    search.send_keys(search_query)
    search.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    
    #driver.find_element_by_xpath('//button[@id="introAgreeButton"]').click()
    #driver.find_elements_by_xpath('//button[text()="Súhlasím"]').click()
    #driver.find_element_by_xpath('//button[contains(text(), "introAgreeButton")]').click()
    #driver.find_element_by_xpath('//button[text()="Súhlasím"]').click()
    #driver.find_element_by_xpath("//[@id='introAgreeButton']")
    #WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("introAgreeButton").is_displayed())
    click("click.png")
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')  
    for i in range(randint(5,15)):
            # Load a page 
        driver.get("https://www.google.com/")
        search = driver.find_element_by_name("q")
        search.clear()
        search_query = random.choice(search_query_list)
        search.send_keys(search_query)
        search.send_keys(Keys.RETURN)
        time.sleep(randint(5,15))
        try:
            elems = driver.find_element_by_xpath('//a[starts-with(@href,"https://www.vsetkoprepriemysel.sk")]').click()
            time.sleep(randint(10,30))
        except:
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')         
        # close the tab
        # (Keys.CONTROL + 'w') on other OSs.
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.close()
    time.sleep(1)    
    print (count)
    print (proxy_list_query)
    
         
