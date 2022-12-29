from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pandas as pd
import pycountry
import os
import pycountry

columns = ['Rank', 'University Name', 'Country', 'Count', 'Faculty']
def cleanup(s,country):
    # Split the string into a list of words
    words = s.split()

    rank = words[0]
    count = words[-2]
    faculty = words[-1]
    
    middle_str = words[1:-2]
    middle_str = [word for word in middle_str if word != "►"]

    # Join the remaining words into a single string
    uni_name = " ".join(middle_str)


    return (rank, uni_name, country, count, faculty)


def main():
    # Load Page
    webdriver_path = r"C:\Users\Adnan\Desktop\Data Science\Week 6 Project\chromedriver.exe"

    driver = webdriver.Chrome(webdriver_path)
    url = f"https://csrankings.org/#/index?all&world"
    driver.get(url)

    #ADBLOCK
    '''sponsor = driver.find_element(By.CLASS_NAME,"overlay")
    if sponsor.is_displayed():
        driver.execute_script("arguments[0].style.display='none'", sponsor)
        print("ADBLOCCD")
        time.sleep(5)
        '''

    # Get table of a region
    region = driver.find_element(By.XPATH, '//*[@id="regions"]')
    options = region.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "the world":
            option.click()
            time.sleep(5)
    # Set the timeline
    timeline =  driver.find_element(By.XPATH, '//*[@id="fromyear"]')
    years = timeline.find_elements(By.TAG_NAME, "option")
    for year in years:
        if year.text == "2000":
            year.click()
            time.sleep(5)
    # Deselect all topics of focus
    all_btn = driver.find_element(By.XPATH, "//*[@id='all_areas_off']")
    all_btn.click()

    # Select the specific subjects
    arch = driver.find_element(By.XPATH,'//*[@id="arch"]')
    arch.click()
    compnet = driver.find_element(By.XPATH,'//*[@id="comm"]')
    compnet.click()
    sec = driver.find_element(By.XPATH,'//*[@id="sec"]')
    sec.click()
    ops = driver.find_element(By.XPATH,'//*[@id="ops"]')
    ops.click()
    proglang = driver.find_element(By.XPATH,'//*[@id="plan"]')
    proglang.click()
    soft = driver.find_element(By.XPATH,'//*[@id="soft"]')
    soft.click()
    time.sleep(5)

    # Scrap data from the table into a variable and clean it
    ranking_table = driver.find_element(By.XPATH, "/html/body/div[5]/form/div/div[2]/div[2]/div/div/table/tbody")
    rows = ranking_table.find_elements(By.TAG_NAME, "tr")
    uni_list = []
    print(len(rows))
    for elements in rows:
        if elements.text:
            img = elements.find_element(By.TAG_NAME,"img")
            src = img.get_attribute("src")
            
            # Extract the file name from the src attribute
            file_name = src.split("/")[-1]
            
            # Split the file name into the country code and the extension
            country_code, extension = os.path.splitext(file_name)
            if country_code =='uk':# Fixing a problem to recognize England
                country_code = 'GB'
            country = pycountry.countries.get(alpha_2=country_code)
            print(elements.text)
            print(country.name)
            
            uni_list.append(cleanup(elements.text, country.name))
    df = pd.DataFrame(uni_list,columns=columns)
    df.to_csv("best_uni.csv")
    
if __name__ == "__main__":
    main()