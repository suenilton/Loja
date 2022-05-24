from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RoupasTestCase(LiveServerTestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Chrome('D:\Suenilton\Pessoal\Projetos Python\Projeto loja jaqueline\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_vizualizando_a_pagina_principal(self):
        
        home_page = self.browser.get(self.live_server_url)
        brand_element = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual('Site de Roupas', brand_element.text)