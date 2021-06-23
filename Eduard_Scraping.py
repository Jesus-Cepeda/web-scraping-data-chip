import numpy as np
import pandas as pd
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

url_1 = 'https://www.chip.gov.co/schip_rt/index.jsf'
browser = webdriver.Chrome()
browser.get(url_1)

municipio = pd.read_stata('Cod_Municipio.dta')
municipio = np.array(municipio)
# municipio = ["210111001","210108002","210108001"]

meses = ["47","43","39","35","31","27","23","19","15","11","7","3"]
for i in municipio:
    for j in meses:
        time.sleep(2)
        # Hacemos click en el primer enlace y lo abrimos en una pestaña nueva
        browser.find_element_by_xpath('//*[@id="j_idt17:j_idt19:j_idt30"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="j_idt17:j_idt19:j_idt30:InformacionEnviada:out"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="frm1:SelBoxEntidadCiudadano_input"]').click()
        time.sleep(2)

    
        busqueda = browser.find_element_by_id('frm1:SelBoxEntidadCiudadano_input')
        busqueda.send_keys(i)
        time.sleep(2)
        busqueda.send_keys(Keys.ENTER)


        time.sleep(2)
    
        browser.find_element_by_xpath('//*[@id="frm1:SelBoxCategoria"]').click()
        time.sleep(2)
    
        trs  = Select(browser.find_element_by_xpath('//*[@id="frm1:SelBoxCategoria"]'))
    
        print(str(len(trs.options)))
        if len(trs.options) == 0:
            continue
        else:
            browser.find_element_by_xpath('//*[@id="frm1:SelBoxCategoria"]/option[20]').click()
            time.sleep(2)
            busqueda.send_keys(Keys.ENTER)

            time.sleep(2)
            ategoria = "OCT A DIC - 2009"
            browser.find_element_by_xpath('//*[@id="frm1:SelBoxPeriodo"]').click()
            time.sleep(2)
            
            # Aca itera 'j' el segundo Loop con los años 
            browser.find_element_by_xpath(f'//*[@id="frm1:SelBoxPeriodo"]/option[{meses}]').click()
            time.sleep(2)

            trs  = Select(browser.find_element_by_xpath('//*[@id="frm1:SelBoxPeriodo"]'))
            if len(trs.options) == 0:
                continue
            else:
                time.sleep(2)  
                busqueda.send_keys(Keys.ENTER)


                time.sleep(2)
                categoria = "GASTOS_DE_INVERSION"
                browser.find_element_by_xpath('//*[@id="frm1:SelBoxForma"]').click()
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="frm1:SelBoxForma"]/option[2]').click()
                time.sleep(2)
                busqueda.send_keys(Keys.ENTER)

                # --- dar enter 
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="frm1:BtnConsular"]').click()

                # descargar datos 
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="frm1:_t197"]').click()

    
    
print("Fin!!")
    # 210105004210105044






