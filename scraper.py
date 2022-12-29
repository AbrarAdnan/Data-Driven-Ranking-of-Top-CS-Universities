from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pycountry
import os
import argparse


columns = ['Rank', 'University Name', 'Country', 'Count', 'Faculty']
uni_list = []

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

def getCountry(c):
    img = c.find_element(By.TAG_NAME,"img")
    src = img.get_attribute("src")
        
    # Extract the file name from the src attribute
    file_name = src.split("/")[-1]
        
    # Split the file name into the country code and the extension
    country_code, extension = os.path.splitext(file_name)
    if country_code =='uk':# Fixing a problem to recognize England
        country_code = 'GB'
    country_name = pycountry.countries.get(alpha_2=country_code)
    return country_name.name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--chromedriver_path', type=str)
    args = parser.parse_args()

    if args.chromedriver_path is None:
        parser.error("Please specify a chromedriver path")

    webdriver_path = args.chromedriver_path
    

    driver = webdriver.Chrome(webdriver_path)
    url = f"https://csrankings.org/#/index?all&world"
    driver.get(url)

    #ADBLOCK
    sponsor = driver.find_element(By.XPATH, '//*[@id="sponsor"]/button[2]')
    if sponsor.is_displayed():
        print("==========Blocked a popup Ad===========")
        sponsor.click()
        time.sleep(3)
    # Get table of a region
    region = driver.find_element(By.XPATH, '//*[@id="regions"]')
    options = region.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "the world":
            print("==========The World=============")
            time.sleep(3)
            option.click()

    # Set the timeline
    timeline =  driver.find_element(By.XPATH, '//*[@id="fromyear"]')
    years = timeline.find_elements(By.TAG_NAME, "option")
    for year in years:
        if year.text == "2000":
            print("==========2000=============")
            time.sleep(3)
            year.click()
    # Deselect all topics of focus
    all_btn = driver.find_element(By.XPATH, "//*[@id='all_areas_off']")
    all_btn.click()
    time.sleep(5)

    # Select the specific subjects
    arch = driver.find_element(By.XPATH,'//*[@id="arch"]')
    arch.click()
    time.sleep(1)
    compnet = driver.find_element(By.XPATH,'//*[@id="comm"]')
    compnet.click()
    time.sleep(1)
    sec = driver.find_element(By.XPATH,'//*[@id="sec"]')
    sec.click()
    time.sleep(1)
    ops = driver.find_element(By.XPATH,'//*[@id="ops"]')
    ops.click()
    time.sleep(1)
    proglang = driver.find_element(By.XPATH,'//*[@id="plan"]')
    proglang.click()
    time.sleep(1)
    soft = driver.find_element(By.XPATH,'//*[@id="soft"]')
    soft.click()
    time.sleep(1)
    print("===========Selected subjects=========")

    # Scroll the table to load it fully
    scrollbar = driver.find_element(By.XPATH, '//*[@id="success"]/div')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbar)
    print("==========Scroll===========")
    time.sleep(3)

    # Scrap data from the table into a variable and clean it
    ranking_table = driver.find_element(By.XPATH, "/html/body/div[5]/form/div/div[2]/div[2]/div/div/table/tbody")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ranking_table)
    rows = ranking_table.find_elements(By.TAG_NAME, "tr")
    time.sleep(3)

    for elements in rows:
        if elements.text:
            
            country_name = getCountry(elements)
            print(elements.text)
            print(country_name)
            uni_list.append(cleanup(elements.text, country_name))

    df = pd.DataFrame(uni_list,columns=columns)
    df.to_csv("best_uni_list.csv")

if __name__ == "__main__":
    main()