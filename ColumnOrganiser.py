print("Hello world!")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
def EnergyConfigOpener():
    driver.get('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=108707')
    username = driver.find_element_by_id('username')
    username.send_keys('gregory.greenfield@christie.nhs.uk')
    password = driver.find_element_by_id('password')
    password.send_keys('pepyspepys4')
    loginBtn = driver.find_element_by_id('loginBtn')
    loginBtn.click()
def FindPageFirst(web):
    driver.get(web)
    JumpTo = driver.find_element_by_id('JumpTo')
    JumpTo.send_keys('F')
    FilterBoxOpen = driver.find_element_by_class_name('filterLinkPopup')
    FilterBoxOpen.click()
    SearchBox = driver.find_element_by_id('tableHeaderName')
    SearchBox.send_keys('EnergyConfiguration.txt')
    SearchGo = driver.find_element_by_id('submitButton')
    SearchGo.click()
    StartSort = driver.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td/table[2]/tbody[2]/tr[1]/td[3]/a')
    StartSort.click()    
def FindPage(web):
    driver.get(web)
    JumpTo = driver.find_element_by_id('JumpTo')
    JumpTo.send_keys('F')
    SearchBox = driver.find_element_by_id('tableHeaderName')
    SearchBox.send_keys('EnergyConfiguration.txt')
    SearchGo = driver.find_element_by_id('submitButton')
    SearchGo.click()    
def NewTab():
    driver.execute_script("window.open('web');")
    driver.switch_to.window(driver.window_handles[-1]) 
driver = webdriver.Chrome(r'W:\RTSG Tools\ConfigSweeper\EnergyConfigSelenium\chromedriver.exe')
EnergyConfigOpener()
FindPageFirst('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=108707') # S2
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=122631') # S1
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=112759') # S3
NewTab()
#FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=112449') # S4
#NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=112631') # S5
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=114960') # S6
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=125986') # S8
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=114283') # S10
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=116751') # S11
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=114225') # S12
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=113639') # S01
NewTab()
FindPage('https://elekta.axeda.com/drm/actions/service/device/overview?app_name=service&device_id=114419') # S02