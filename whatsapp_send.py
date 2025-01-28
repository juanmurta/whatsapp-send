from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import urllib
import os

# escolhendo e criando perfil selenium no navegador.
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile Selenium')

navegador = webdriver.Chrome(options=options)
navegador.get("https://web.whatsapp.com")

# importando tabela
tabela = pd.read_excel(r'E:\Python\python\Impressionador\Web-Scraping Selenium\Arquivos\Envios.xlsx')
print(tabela[['nome', 'mensagem', 'arquivo']])

# lendo por linha a tabela
for linha in tabela.index:
    nome = tabela.loc[linha, 'nome']
    mensagem = tabela.loc[linha, 'mensagem']
    arquivo = tabela.loc[linha, 'arquivo']
    telefone = tabela.loc[linha, 'telefone']

    # alterando o texto colocando nome das pessoas
    texto = mensagem.replace('fulano', nome)
    # formantando o texto para URL usando import urllib
    texto = urllib.parse.quote(texto)
    print(texto)

    link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'
    navegador.get(link)
    # esperar a tela do whatsapp carregar esperando o elemento aparecer
    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia

    # verificar se o numero do telefone está correto.
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(2)

        if arquivo != 'N':
            caminho_completo = os.path.abspath(fr'E:\Python\python\Impressionador\Web-Scraping Selenium\Arquivos\{arquivo}')
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input').send_keys(caminho_completo)
            time.sleep(2)
            navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()

        time.sleep(5)