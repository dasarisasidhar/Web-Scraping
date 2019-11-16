import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
def login():
    driver = webdriver.Chrome('path of chrome drive', options = chromeOptions )
    driver.get("")
    id = driver.find_element_by_name('loginfmt') 
    time.sleep(1)
    id.clear()
    id.send_keys("") 
    #submit = driver.find_elements_by_xpath('//*[@id="idSIButton9"]')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(7)
    password = driver.find_element_by_name('Password') 
    time.sleep(1)
    password.clear()
    password.send_keys("") 
    time.sleep(1)
    #submit = driver.find_elements_by_xpath('//*[@id="idSIButton9"]')
    driver.find_element_by_id("submitButton").click()
    time.sleep(2)
    try:
        stay_signed_id = driver.find_element_by_xpath("//input[@type='submit']")
        if(stay_signed_id):
            stay_signed_id.click()
        else:
            pass
    except:
        print("exception: stay_signed_id")
    time.sleep(3)
    #Create VM
    search = driver.find_element_by_name("__azc-textBox0")
    search.send_keys("Virtual machines")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(7)
    addnewvm_symbol = driver.find_element_by_xpath("//*[@id='web-container']/div[5]/main/div[4]/div[2]/section/div/div[1]/div[1]/div/ul/li[1]").click() # Add new vm
    #"fxs-commandBar-item fxs-portal-border msportalfx-command-like-button fxs-portal-hover"  # review + create 
    time.sleep(10)
    rg = driver.find_element_by_xpath("//*[/html/body/div[1]/div[5]/main/div[4]/div[2]/section[2]/div/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[6]/div[2]/div/div[1]/div/div[2]/div/div/div/input]")
    rg.select_by_index(1)
    vm_name = driver.find_element_by_id('__azc-textBox13')
    vm_name.send_keys("totestadatvm2")
    time.sleep(1)
    #region_drop_down = Select(driver.find_element_by_id("azc-form-guid-22caabb1-fd41-40aa-8f6a-1344a1bb10b3textbox"))
    #options = region_drop_down.options
    #for index in range(0, len(options) - 1):
    #   region_drop_down.select_by_index(index)
    #   driver.find_element_by_id("azc-form-guid-22caabb1-fd41-40aa-8f6a-1344a1bb10db-link").click()
    #   time.sleep(10)
    
 
    

login()

def vm():
    try:
        pass
    except:
        return "exception: vm"
vm()

def close_chrome():
    driver.quit()

close_chrome()