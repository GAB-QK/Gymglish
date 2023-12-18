from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the web page
driver.get('https://fra01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.gymglish.com%2Fgymglish%2Fworkbook%2Flogin%3Fusername%3Dgabriel.qaddaha%2540ecole-hexagone.com%26password%3DGVLykJYt%26idnlm%3D4d5451784e5463344d4445344d6a59344d7a413d0a&data=05%7C01%7Cgabriel.qaddaha%40ecole-hexagone.com%7C13aa66cfe93c4ebfe0c408db56bca595%7C612a8c655cc64b8ea801220c8d86acc8%7C0%7C0%7C638199140460849657%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=s4rBe1MCxRct1%2Bf5IFzR66UbqzaCA1mrpt%2BAIy5KROY%3D&reserved=0')

# Find the new lecon button
new_lecon = driver.find_element(By.CLASS_NAME, 'workbook-link')
new_lecon.click()

block_class = 'a9l-box-content'
block_Exercice = 'a9l-box-test'


# Find the green block with the questions
if driver.find_element(By.CLASS_NAME, block_class):
    # Find the questions
    questions_answers = driver.find_elements(By.CLASS_NAME, block_Exercice)
    audio_subtitles_track = driver.find_elements(By.XPATH, '//track[@kind="subtitles"]')
    for question_answer in questions_answers:
        
        # redirect the output in a txt file and add to this file the question and the answer
        with open('questions_answers.txt', 'a') as f:
            f.write(question_answer.text + '\n')
            f.write('--------------------- fin -------------------\n\n')
            f.close()

    for audio_subtitles in audio_subtitles_track:
        
        subtitle_links = []
        subtitle_links.append(audio_subtitles.get_attribute('src'))
        print(subtitle_links)
    
        """ for subtitle_link in subtitle_links:
            print(subtitle_link) """
        """ count = 1
        # curl the web page in subtitle
        curl_subtitle = driver.get(subtitle_link)
        subtitle = driver.find_element(By.XPATH, '//pre').text

        with open('audio_subtitles.txt', 'a') as f:
            f.write('--------------------- audio ' + str(count) + ' -------------------\n')
            f.write(subtitle + '\n')
            f.write('--------------------- fin -------------------\n\n')
            f.close()
            count += 1 """
                


# don't close the web page until the user presses a key
input('Press any key to continue...')
driver.quit()



""" # Submit the answers
submit_button = driver.find_element(By.ID, 'submit-button')
submit_button.click()

# Perform cleanup
driver.quit()
 """