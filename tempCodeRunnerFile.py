    def testproduct():
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