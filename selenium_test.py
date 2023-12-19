from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


urls = ['https://www.google.com']
s = Service("/bin/google-chrome")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

# Exemple d'interaction : trouver un élément par son nom et envoyer une information
# element = driver.find_element_by_name('nom_element')
# element.send_keys('quelque chose', Keys.RETURN)

# Exemple pour récupérer du contenu de la page
# content = driver.find_element_by_id('id_element').text
# print(content)

# Fermer le navigateur une fois que vous avez terminé
driver.quit()
