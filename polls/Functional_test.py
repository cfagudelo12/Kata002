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

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Carlos Felipe')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Agudelo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tuposDeServicio']/option[text()='Desarrollador Web])").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3182762011')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('cf.agudelo12@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:/Users/cfagu/Documents/GitHub/Kata02Preparacion/polls/templates/img/031.jpeg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('cf.agudelo12')

        nombreUsuario = self.browser.find_element_by_id('id_password')
        nombreUsuario.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Carlos Felipe Agudelo"]')
        self.assertIn('Carlos Felipe Agudelo', span.text)