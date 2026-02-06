# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LearnPythonSelenium import Utility
driver=webdriver.Chrome()
driver.get("https://dummyflights.com/")
driver.maximize_window()
dataFile="C:\\Users\\Mehta\\OneDrive\\Documents\\Python Selenium\\TravelDetails.xlsx"
excelUtil = Utility.ExcelUtility(dataFile,"Sheet1",driver)
excelUtil.setRowColumn()
row=excelUtil.rowCount
col=excelUtil.columnCount
print(row)
print(col)
time.sleep(2)
myWait=WebDriverWait(driver,10)
myWait.until(EC.presence_of_element_located((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"tab_text").click()
driver.find_element(By.XPATH,"//*[@id='select2-departure-city-container']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@aria-controls='select2-departure-city-results']").send_keys("Ranchi")
time.sleep(2)
airportList=driver.find_elements(By.XPATH,"//*[@class='select2-results__options']/li")
list_len=len(airportList)
print(list_len)
for i in range(1,list_len+1):
    portName=driver.find_element(By.XPATH,"//*[@class='select2-results__options']/li["+str(i)+"]/span").text
    print(portName)
    if portName=="Birsa Munda Airport, IXR (Ranchi, IN )":

        driver.find_element(By.XPATH, "//*[@class='select2-results__options']/li["+str(i)+"]/span").click()
        break;

time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='select2-destination-city-container']").click()
driver.find_element(By.XPATH,"//*[@aria-controls='select2-destination-city-results']").send_keys("Mumbai")
time.sleep(2)
airportDestinatioList=driver.find_elements(By.XPATH,"//*[@class='select2-results__options']/li")
list_len1=len(airportDestinatioList)
for i in range(1,list_len1+1):
    portDesName=driver.find_element(By.XPATH,"//*[@class='select2-results__options']/li["+str(i)+"]/span").text
    print(portDesName)
    if portDesName=="Chhatrapati Shivaji International Airport, BOM (Mumbai, IN )":

        driver.find_element(By.XPATH, "//*[@class='select2-results__options']/li["+str(i)+"]/span").click()
        break;

departureDate ="30/Mar/2026"
depDate=departureDate.split('/')
monthYear=depDate[1]+ " " + depDate[2]
day=depDate[0]
print(monthYear)
print(day)
calMonthYear=""
driver.find_element(By.XPATH,"//*[@id='flight-departure-date']").click()
time.sleep(2)
while True:
    print("Inside Loop")
    calMonthYear = driver.find_element(By.XPATH, "//*[@class='drp-calendar left']/div/table/thead/tr/th[2]").text
    print(calMonthYear)
    if calMonthYear==monthYear:
        break;
    else:
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@class='drp-calendar left']/div/table/thead/tr/th[3]").click()

enabledState=driver.find_element(By.XPATH,"//td[(not(contains(@class,'off'))) and text()='"+day+"']").is_enabled()
print(enabledState)
if enabledState:
    driver.find_element(By.XPATH, "//td[(not(contains(@class,'off'))) and text()='"+day+"']").click()
    driver.find_element(By.XPATH, "//td[(not(contains(@class,'off'))) and text()='" + day + "']").click()
    time.sleep(2)
else:
    print("Not enabled")


time.sleep(2)
destinationDate ="5/Apr/2026"
desDate=destinationDate.split('/')
monthYearDes=desDate[1]+ " " + desDate[2]
dayDes=desDate[0]
print(monthYearDes)
print(dayDes)
calMonthYearDes=""
driver.find_element(By.XPATH,"//*[@id='flight-return-date']").click()
while True:
    print("Inside Loop for departure")
    calMonthYearDes = driver.find_element(By.XPATH, "//*[@class='drp-calendar left']/div/table/thead/tr/th[2]").text
    print(calMonthYear)
    if calMonthYearDes==monthYearDes:
        break;
    else:
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@class='drp-calendar left']/div/table/thead/tr/th[3]").click()

enabledStateDes=driver.find_element(By.XPATH,"//td[(not(contains(@class,'off'))) and text()='"+day+"']").is_enabled()
print(enabledStateDes)
if enabledStateDes:
    driver.find_element(By.XPATH, "//td[(not(contains(@class,'off'))) and text()='"+day+"']").click()
    driver.find_element(By.XPATH, "//td[(not(contains(@class,'off'))) and text()='" + day + "']").click()
    time.sleep(2)
else:
    print("Not enabled")

time.sleep(2)
driver.find_element(By.ID,"flight-search-btn").click()

time.sleep(2)
driver.quit()

