from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.sst.dk/da/corona/status-for-epidemien/tal-og-overvaagning")

# Find totale antal prøver
TotalProver = driver.find_element_by_xpath("/html/body/main/main/article/div[3]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]").get_attribute('innerHTML')

# Find Førstegangs testede siden i går
firstestsidenigaar = driver.find_element_by_xpath("/html/body/main/main/article/div[3]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]").get_attribute("innerHTML")

#Find Smittede siden i går:
smittedesidenigaar = driver.find_element_by_xpath("/html/body/main/main/article/div[3]/div/div[2]/div[2]/table/tbody/tr[4]/td[2]").get_attribute("innerHTML")

#Total Smittede og overstået infektion:
totalsmitte = driver.find_element_by_xpath("/html/body/main/main/article/div[3]/div/div[2]/div[1]/table/tbody/tr[4]/td[2]").get_attribute("innerHTML")
klaretinfektion = driver.find_element_by_xpath("/html/body/main/main/article/div[3]/div/div[2]/div[1]/table/tbody/tr[5]/td[2]").get_attribute("innerHTML")




# Vi beregner nuværende smittede i danmark:
totalsmittenumber = totalsmitte.replace('.', '')
klaretinfektionnumber = klaretinfektion.replace('.', '')
smittenu = int(totalsmittenumber) - int(klaretinfektionnumber)

# Vi laver vores teksstrenge klar til print
totalproverstreng = "Total Antal prøver: " + TotalProver
firstestsidenigaarstreng = "Førstegangs testede personer siden i går: " + firstestsidenigaar
smittedesidenigaarstreng = "Smittede siden i går: " + smittedesidenigaar
totalsmittestreng = "Total Smittede: " + totalsmitte
klaretinfektionstreng = "Overstået infektion: " + klaretinfektion
smittenustreng = "Smittede på nuværende tidspunkt i Danmark: " + str(smittenu)


# Vi lukker browseren
driver.close()


#Print vores strenge:
print(totalproverstreng)
print(firstestsidenigaarstreng)
print(smittedesidenigaarstreng)
print(totalsmittestreng)
print(klaretinfektionstreng)
print(smittenustreng)


def write():
    now = datetime.now() # current date and time

    year = now.strftime("%Y")
#     print("year:", year)

    month = now.strftime("%m")
#     print("month:", month)

    day = now.strftime("%d")
#     print("day:", day)

    filename = day + "_" + month + "_" + year + ".txt"
    print(filename)
    f= open(filename,"w+")
    f.write(totalproverstreng + "\n")
    f.write(firstestsidenigaarstreng + "\n")
    f.write(smittedesidenigaarstreng + "\n")
    f.write(totalsmittestreng + "\n")
    f.write(klaretinfektionstreng + "\n")
    f.write(smittenustreng + "\n")
    f.close()


write()
