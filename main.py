from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

servico = Service(ChromeDriverManager().install())

# Disable Chrome notifications
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Acessa a primeira página do navegador e pede senha
navegador.get('LINK DO PRIMEIRO GRUPO QUE TAMBÉM SERVIRÁ DE ACERSSO À CONTA DO FACEBOOK')

sleep(3)

# Acessa o elemento de usuário e digita usuário:
navegador.find_element('xpath', '//*[@id="email"]').send_keys('USERNAME')
sleep(1)
# Acessa o elemento de senha e digita a senha e clica ENTER:
navegador.find_element('xpath', '//*[@id="pass"]').send_keys('PASSWORD' + Keys.ENTER)

# Pode ser que o facebook exija confirmação na sua página já logada em outra janela.
sleep(20)

# Clicar no campo para escrever e abrir o campo ativo para começar a digitar:
navegador.find_element('xpath', '//*[@id="mount_0_0_lj"]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div').click()

# Escrever no campo ativo que abriu:
navegador.find_element('xpath', '//*[@id="mount_0_0_Kx"]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys('CONTEÚDO')

# Clica no botão Eviar:
navegador.find_element('xpath', '//*[@id="mount_0_0_Kx"]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div').click()

sleep(5)

# #Loop para postar em outros grupos:
# grupos = ['link do grupo', 'link do grupo']

# for grupo in grupos:
#     #Acessa o link do grupo
#     navegador.get(grupo)
#     sleep(3)
#     # Clicar no campo para escrever e abrir o campo ativo para começar a digitar:
#     navegador.find_element('xpath', '//*[@id="mount_0_0_lj"]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div').click()
#     # Escrever no campo ativo que abriu:
#     navegador.find_element('xpath', '//*[@id="mount_0_0_Kx"]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys('CONTEÚDO')
#     # Clica no botão Eviar:
#     navegador.find_element('xpath', '//*[@id="mount_0_0_Kx"]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div').click()

# # Mantém a janela aberta até que ela seja fechada manualmente ou apertando ENTER no Terminal:
# input("Press Enter to close the browser...")