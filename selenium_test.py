from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Liste des URLs à visiter
url = 'https://fra01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.gymglish.com%2Fgymglish%2Fworkbook%2Flogin%3Fusername%3Dgabriel.qaddaha%2540ecole-hexagone.com%26password%3DGVLykJYt%26idnlm%3D4d5451784e5463344d4445344d6a59344d7a413d0a&data=05%7C01%7Cgabriel.qaddaha%40ecole-hexagone.com%7C13aa66cfe93c4ebfe0c408db56bca595%7C612a8c655cc64b8ea801220c8d86acc8%7C0%7C0%7C638199140460849657%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=s4rBe1MCxRct1%2Bf5IFzR66UbqzaCA1mrpt%2BAIy5KROY%3D&reserved=0'


# Configuration du service Chrome
s = Service("/bin/google-chrome")


driver = webdriver.Chrome(service=s)
driver.get(urls)


driver.quit()
