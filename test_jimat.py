import time
# importing webdriver from selenium
#Perlu download webdriver dahulu
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#Time ialah masa untuk website response
import time
import csv

import openpyxl
#openpyxl function untuk analyse csv file dalam python
#File csv akan dicipta dalam folder code ini
#Selepas XPATH main Categories di ubah,nama file excel perlu diubah mengikut namanya
def testjimat():
    f = open('Bakery And Breakfast.csv', 'w') #Contoh naming ikut categories
    writer = csv.writer(f)

    # Here Chrome  will be used
    driver = webdriver.Chrome()
    driver.maximize_window()
    # URL of website
    url = "https://www.jimatbiz.com"
    # Opening the website
    driver.get(url)
    time.sleep(4)
    #For mouse hover(pergerakan mouse)
    a = ActionChains(driver)

    #Hover to Main Category for drop down to appear
    def testcategory():
        MainCategory = driver.find_element(By.XPATH, '/html/body/nav/nav/div/div[3]/ul[1]/li[1]/div[1]/div')
        a.move_to_element(MainCategory).perform()
        time.sleep(2)


        #Choose the category from drop down of the main category
        #After this code finish run, change the XPATH by inspect element the other categories.
        #Default categories for this code is BAKERY & BREAKFAST
        Category =driver.find_element(By.XPATH, '/html/body/nav/nav/div/div[3]/ul[1]/li[1]/div[2]/div/a[1]')
        Category.click()
        time.sleep(2)

        #Both of this variable related to the XPATH
        #To diffferentiate different xpath for same class name
        counterPage = 1
        counter= 1
        loop = True
        #Set loop Condition
        while loop == True:
            #Boleh baca try except python di internet
            try:
                #Find XPATH based on Product nama,highlight name and inspect element,copy full XPATH
                productName = driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[{counter}]/div/div/h5')
                print(productName.text)
                time.sleep(0.5)

                productImage = driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[{counter}]/div/img')
                print(productImage.get_attribute("src"))
                time.sleep(0.5)

                productStock = driver.find_element(By.XPATH,
                                                f'/html/body/main/div[2]/div/div[2]/div/div[{counter}]/div/div/div/div[1]/p[1]')
                print(productStock.text)
                time.sleep(0.5)

                productPrice = driver.find_element(By.XPATH,
                                                f'/html/body/main/div[2]/div/div[2]/div/div[{counter}]/div/div/div/div[2]/p[1]')
                print(productPrice.text)
                time.sleep(0.5)

                writer.writerow([productName.text, productImage.get_attribute("src"), productStock.text, productPrice.text])

                counter += 1

            except:
                counter = 1
                print(counter)
                try:
                    counterPage += 1
                    nextPage= driver.find_element(By.XPATH, f'/html/body/main/div[2]/div/div[3]/div/div[2]/nav/ul/li[{counterPage}]/a')
                    nextPage.click()
                    time.sleep(3)
                except:
                    print("Scrapping Completed")
                    loop = False





        f.close()
        #Setelah code ini selesai di run,file csv sepatutnya mempunyai data yang diperlukan berdasarkan category iaitu nama,image,stok dan harga
        #Main category sahaja perlu diubah XPATH keran XPATH lain sudah standard.
        #Bagi quantity dan berat memerlukan cleaning dari nama item..boleh cuba menggunakan excel seperti text to column,right left function dan lain2.