import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import pandas as pd
from  datetime import datetime

filename = datetime.now().strftime('%Y-%m-%d-%H-%M.csv')

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")


def get_data():
    browser = webdriver.Chrome('C:/Users/iad7kor/Documents/Sasi/chromedriver.exe', options = chromeOptions )
    browser.get("https://www.b.com/a/manage_jobs/?source=manage_jobs_tab")
    time.sleep(2)
    browser.find_element_by_id("email").send_keys("id")
    browser.find_element_by_id("pass").send_keys("pass")
    time.sleep(2)
    browser.find_element_by_id("loginbutton").click()
    time.sleep(3)
    number_of_profiles = int(input("press enter the number of agent details need to download: "))
    loops = number_of_profiles//10
    elements = number_of_profiles%10
    x, y = pyautogui.size()
    loop = 0
    df = pd.DataFrame()
    for i in range(loops+1):
        #elements are total number of loops or clicks that will process.
        element = 13
        if(i == loops or loops == 0):
            element = elements
        loop += 1
        
        locations = [(648*x//1920, 403*y//1080),(640*x//1920, 476*y//1080), (642*x//1920, 556*y//1080), 
                     (649*x//1920, 637*y//1080), (657*x//1920, 728*y//1080), (666*x//1920, 808*y//1080),
                     (666*x//1920, 897*y//1080), (664*x//1920, 959*y//1080), (673*x//1920, 1039*y//1080), 
                     (1908*x//1920, 1027*y//1080), (652*x//1920, 1043*y//1080), (1905*x//1920, 98*y//1080), 
                     (1532*x//1920, 271*y//1080)]
        for i in range(element):
            if(i in [9, 11, 12]):
                #for scroll and next page just a click is enoungh
                pyautogui.click(locations[i][0], locations[i][1])
                time.sleep(1)
            else:
                #for all the dialoug boxes the click along with data process is required.
                pyautogui.click(locations[i][0], locations[i][1])
                time.sleep(1)
                pop_up_html_code =BeautifulSoup(browser.page_source, 'lxml')
                mylist = pop_up_html_code.find_all("div", class_="_404t")
                for i,value in enumerate(mylist): 
                    if(i == 2):
                        c_name = value.find_all("div", class_="_2pid")
                        details = list()
                        for j in c_name:
                            details.append(j.text)
                        if(len(details) > 0):
                            df1 = pd.DataFrame([details])
                        df = pd.concat([df1, df], ignore_index=True)
                pyautogui.click(x=231, y=426)
                time.sleep(1)
        time.sleep(2)
    df.columns=['Name', 'Phone', 'Address']
    df.to_csv(filename, index=False)

get_data()



    