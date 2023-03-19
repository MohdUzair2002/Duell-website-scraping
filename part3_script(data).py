from selenium import webdriver
import time
import requests
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

file=open("links.csv","r")
data=list(csv.reader(file,delimiter=','))
file.close()
# print(data)

chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())

chrome_options.add_argument("user-data-dir=C:/Users/Dell/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument('--profile-directory=Profile 1')

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://www.duell.se/af/en/login?back=my-account")
time.sleep(4)
login=driver.find_element(By.XPATH,"//button[@id='SubmitLogin']").click()

wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='homefeatured']")))

def scrap_data():
    try:
        product_name= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='pb-center-column col-xs-12 col-sm-4']/h1")))
        product_name = driver.find_element(By.XPATH,"//div[@class='pb-center-column col-xs-12 col-sm-4']/h1").text
        print(product_name)
    except:
        product_name = " "
        pass

    try:
        product_reference_no = driver.find_element(By.XPATH,"//p[@id='product_reference']/span").text
    except:
        product_reference_no = " "
        pass

    try:
        shortdescript = []
        product_short_descr = driver.find_element(By.XPATH,"//div[@id='short_description_block']").get_attribute('id')
        print(product_short_descr)
        if (product_short_descr == 'short_description_block'):
            short_description1 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[1]").text
            shortdescript.append(short_description1)

            short_description2 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[3]").text
            shortdescript.append(short_description2)

            short_description3 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[5]").text
            shortdescript.append(short_description3)

            short_description4 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[7]").text
            shortdescript.append(short_description4)

            short_description5 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[9]").text
            shortdescript.append(short_description5)

            short_description6 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[11]").text
            shortdescript.append(short_description6)

            short_description7 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[13]").text
            shortdescript.append(short_description7)

            short_description8 = driver.find_element(By.XPATH,"(//div[@id='short_description_block']/div/*)[16]").text
            shortdescript.append(short_description8)


            print(shortdescript)

    except:
        if type(shortdescript) != "<class 'list'>":
            shortdescript = " "
        pass


    try:
        fulldescript = []
        # product_full_descr = driver.find_element(By.XPATH,"//h3[@id='#fullDescription']").text
        # print(product_full_descr)
        # if (product_full_descr == 'More info'):
        #     product_full_descr.click()
        full_description = driver.find_element(By.XPATH,"//div[@id='fullDescription']").text
        fulldescript.append(full_description)
        print(fulldescript)
    except:
        # if type(fulldescript) != "<class 'list'>":
        fulldescript = " "
        pass

    try:
        listt_of_stock = []
        stock = driver.find_element(By.XPATH,"//p[@id='availability_statut']/span").text

        if (stock == 'In stock'):
            country_name = driver.find_element(By.XPATH,"(//div[@class='row']/div)[9]").text
            no_of_stock = driver.find_element(By.XPATH,"(//div[@class='row']/div)[11]").text
            listt_of_stock=[stock, country_name, no_of_stock]
        else:
            listt_of_stock = [stock]
    except:
        listt_of_stock = []
        pass

    try:
        get_price = driver.find_element(By.XPATH,"//div[@class='button-container retail_btn']")
        get_price.click()

        inprice = driver.find_element(By.XPATH,"(//p[@class='our_price_display']/span)[2]").text

    except:
        inprice = " "
        pass

    try:
        outprice = driver.find_element(By.XPATH,"(//p[@class='our_price_display']/span)[3]").text
    except:
        outprice=" "
        pass

    try:
        datasheet = driver.find_element(By.XPATH,"//h3[@id='#idTab8']")
        datasheet.click()
        barcode = driver.find_element(By.XPATH,"(//table[@class='table-data-sheet']/tbody/tr/td)[2]").text
        brand = driver.find_element(By.XPATH,"((//table[@class='table-data-sheet']/tbody/tr)[2]/td)[2]").text
    except:
        barcode = " "
        brand = " "
        pass

    try:

        oemm =""
        oem = driver.find_element(By.XPATH,"((//table[@class='table-data-sheet']/tbody/tr)[2]/td)[1]").text
        if oem == 'OEM':
            oemm = driver.find_element(By.XPATH,"((//table[@class ='table-data-sheet']/tbody/tr)[2]/td)[2]").text
    except:
        oemm = " "

    try:
        category = driver.find_element(By.XPATH,"(//span[@class='navigation_page']/span/a/span)[1]").text
    except:
        category = " "
        pass

    try:
        subcategory_1 = driver.find_element(By.XPATH,"(//span[@class='navigation_page']/span/a/span)[2]").text
    except:
        subcategory_1 = " "
        pass

    try:
        product_category = driver.find_element(By.XPATH,"(//span[@class='navigation_page']/span/a/span)[3]").text
    except:
        product_category = " "
        pass

    try:
        image_url_1 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[1]").get_attribute('href')
    except:
        image_url_1 = " "
        pass

    try:
        image_url_2 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[2]").get_attribute('href')
    except:
        image_url_2 = " "
        pass

    try:
        image_url_3 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[3]").get_attribute('href')
    except:
        image_url_3 = " "
        pass

    try:
        image_url_4 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[4]").get_attribute('href')
    except:
        image_url_4 = " "
        pass

    try:
        image_url_5 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[5]").get_attribute('href')
    except:
        image_url_5 = " "
        pass

    try:
        image_url_6 = driver.find_element(By.XPATH,"(//div[@id='thumbs_list']/ul/li/a)[6]").get_attribute('href')
    except:
        image_url_6 = " "
        pass

    try:
        compatible = driver.find_element(By.XPATH,"//h3[@id='#idTab6_1']")
        compatible.click()
        dataset = []
        r = driver.find_elements_by_xpath("//table[@class='product_compatible_with table']/tbody/tr")
        # to identify table columns
        c = driver.find_elements_by_xpath("//*[@class='product_compatible_with table']/tbody/tr[3]/td")
        # to get row count with len method
        rc = len(r)
        # to get column count with len method
        cc = len(c)
        # to traverse through the table rows excluding headers
        for i in range(2, rc + 1):
            # to traverse through the table column
            for j in range(1, cc + 1):
                # to get all the cell data with text method
                d = driver.find_element(By.XPATH,"//tr[" + str(i) + "]/td[" + str(j) + "]").text
                dataset.append(d)
                print(dataset)


    except:
        d=" "
        pass
    print(product_name)
    with open('data.csv', 'a', encoding='utf-8', newline='') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(
            [product_name,product_reference_no,shortdescript,fulldescript,listt_of_stock,inprice,outprice,barcode,brand,oemm,
             category,subcategory_1,product_category,image_url_1,image_url_2,image_url_3,image_url_4,image_url_5,image_url_6])
        f_object.close()
    
for i in data:
    driver.get(i[0])
    print(i[0])
    # time.sleep(5)
    scrap_data()
driver.quit()