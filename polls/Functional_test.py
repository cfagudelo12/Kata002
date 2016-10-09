from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test01_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test02_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(10000)
        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Carlos Felipe')
        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Agudelo')
        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')
        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3182762011')
        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('cf.agudelo12@uniandes.edu.co')
        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:/Users/cfagu/Documents/GitHub/Kata002/polls/templates/img/IMG_0282.jpg')
        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('cf.agudelo12')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('clave123')
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(10000)
        span = self.browser.find_element(By.XPATH, '//span[text()="Carlos Felipe Agudelo"]')
        self.assertIn("Carlos Felipe Agudelo", span.text)

    def test03_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Carlos Felipe Agudelo"]')
        span.click()
        self.browser.implicitly_wait(10000)
        h2=self.browser.find_element(By.XPATH, '//h2[text()="Carlos Felipe Agudelo"]')
        self.assertIn("Carlos Felipe Agudelo",h2.text)

    def test04_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(10000)
        nombreUsuario = self.browser.find_element_by_id('id_username_login')
        nombreUsuario.send_keys('cf.agudelo12')
        password = self.browser.find_element_by_id('id_password_login')
        password.send_keys('clave123')
        botonLogin = self.browser.find_element_by_id('id_but_login')
        botonLogin.click()
        self.browser.implicitly_wait(10000)
        bienvenida=self.browser.find_element_by_id('id_bienvenida')
        self.assertIsNotNone(bienvenida)