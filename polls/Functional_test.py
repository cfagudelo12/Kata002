from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(10000)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Carlos Felipe')
        self.browser.implicitly_wait(10000)

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Agudelo')
        self.browser.implicitly_wait(10000)

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')
        self.browser.implicitly_wait(10000)

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        self.browser.implicitly_wait(10000)
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3182762011')
        self.browser.implicitly_wait(10000)
        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('cf.agudelo12@uniandes.edu.co')
        self.browser.implicitly_wait(10000)
        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:/Users/cfagu/Documents/GitHub/Kata002/polls/templates/img/IMG_0282.jpg')
        self.browser.implicitly_wait(10000)
        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('cf.agudelo12')
        self.browser.implicitly_wait(10000)
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('clave123')
        self.browser.implicitly_wait(10000)
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(10000)
        self.browser.implicitly_wait(10000)
        span = self.browser.find_element(By.XPATH, '//span[text()="Carlos Felipe Agudelo"]')
        self.assertIn("Carlos Felipe Agudelo", span.text)