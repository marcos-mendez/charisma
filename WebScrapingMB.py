#Importar as Bibliotecas
import pandas as pd
from csv import writer
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


service = Service('/path/to/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

#Local para salvar o arquivo em .csv
df = pd.read_csv('SentimentalAnalyticsMB/Clippagem 2022.csv', sep=';')

urls = df['URL']

for url in urls:
    data = {}
    driver.get(url)
    sleep(5)

    with open('SentimentalAnalyticsMB/dados.csv','a', encoding="utf-8", newline='') as s:
        csv_writer =writer(s)

        data = driver.find_element(By.TAG_NAME, "div")
        paragrafos = data.find_elements(By.XPATH, "//p[contains(text(), 'Mercado Bitcoin')]")
        sleep(5)

        retornar = ''
        for i in range(len(paragrafos)):
            paragrafo = paragrafos[i].text

            if i == len(paragrafos) - 1:
                retornar = retornar + paragrafo + ';'
            else:
                retornar = retornar + paragrafo 
            
        csv_writer.writerow([retornar])
    

