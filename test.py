from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


# Utilisation de WebDriver Manager pour gérer automatiquement GeckoDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

block_class = 'a9l-box-content'
block_Exercice = 'a9l-box-test'


block_toggle = 'dropdown-toggle'
block_toggle_item = 'dropdown-item'
block_lessons_Xpath = '/gymglish/workbook/episodes'
block_lessons_and_episodes = '//a[@href=\'/gymglish/workbook/episodes\']'
block_Actual_episode = 'Voir l\'épisode'
block_story_scripts = "/html/body/div[1]/section[1]/div/div/div/div[3]/div[4]"



# Aller à une page web
driver.get('https://fra01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.gymglish.com%2Fgymglish%2Fworkbook%2Flogin%3Fusername%3Dgabriel.qaddaha%2540ecole-hexagone.com%26password%3DGVLykJYt%26idnlm%3D4d5451784e5463344d4445344d6a59344d7a413d0a&data=05%7C01%7Cgabriel.qaddaha%40ecole-hexagone.com%7C13aa66cfe93c4ebfe0c408db56bca595%7C612a8c655cc64b8ea801220c8d86acc8%7C0%7C0%7C638199140460849657%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=s4rBe1MCxRct1%2Bf5IFzR66UbqzaCA1mrpt%2BAIy5KROY%3D&reserved=0')

# Select the element with class name "workbook-link" only
new_lecon = driver.find_element(By.CSS_SELECTOR, ".workbook-link:not([class*=' '])")
new_lecon.click()

if driver.find_element(By.CLASS_NAME, block_class):
    # Find the questions
    questions_answers = driver.find_elements(By.CLASS_NAME, block_Exercice)
    #audio_subtitles_track = driver.find_elements(By.CLASS_NAME, block_script)
    

    #question écrite et choix multiple 
    for question_answer in questions_answers:
        with open('questions_answers.txt', 'a') as f:
            f.write(question_answer.text + '\n')
            f.write('--------------------- fin -------------------\n\n')
            f.close()


if driver.find_element(By.CLASS_NAME, block_toggle):
    toggle = driver.find_element(By.CLASS_NAME, block_toggle)
    toggle.click()
    toggle_item = driver.find_element(By.CLASS_NAME, block_toggle_item)
    toggle_item.click()
    # Perform actions in the new tab
else:
    print("not found toggle")

time.sleep(2)

for handle in driver.window_handles:
    driver.switch_to.window(handle)
 
lessons_episodes_Xpath = driver.find_element(By.XPATH, block_lessons_and_episodes)
lessons_episodes_Xpath.click()

time.sleep(1)

Actual_episode = driver.find_element(By.LINK_TEXT, block_Actual_episode)
Actual_episode.click()

time.sleep(2)

if driver.find_element(By.CLASS_NAME, block_story_scripts):

    story_scripts = driver.find_element(By.CLASS_NAME, block_story_scripts)

    for story_script in story_scripts:
        with open('story_scripts.txt', 'a') as f:
            f.write(story_script.text + '\n')
            f.write("-----------------------------------------------\n\n")
            f.close()



        
time.sleep(5)
driver.quit()
