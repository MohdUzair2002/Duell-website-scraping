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

# links=[]

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

no_of_pages=2
j=0
while(j<no_of_pages):
    driver.get("https://www.duell.se/en/")

    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='homefeatured']")))

    driver.get(f"https://www.duell.se/af/en/1081-hjalmar#!/orderby:price/orderway:desc/page:{j+1}/")

    links_extracted= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class,'product_img_link')]")))
    links_extracted=driver.find_elements(By.XPATH,"//a[contains(@class,'product_img_link')]")
    # print(links_extracted[0].text)
    for i in range(len(links_extracted)):
        link=driver.find_elements(By.XPATH,"//a[contains(@class,'product_img_link')]")[i].get_attribute('href')
        # print(link)
        with open('links.csv', 'a', encoding='utf-8', newline='') as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(
                [link])
            f_object.close()
    j+=1
