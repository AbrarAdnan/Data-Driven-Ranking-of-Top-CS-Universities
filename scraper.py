from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pycountry
import os
import argparse
import sys


columns = ['Rank', 'University Name', 'Country', 'Count', 'Faculty']
uni_list = []

def cleanup(uni_string,country):
    # Cleans up the string with the country name, university name, rank
    # Count and Faculty

    # Split the string into a list of words
    words = uni_string.split()
    
    # Split the words into a their respective parts
    rank = words[0]
    count = words[-2]
    faculty = words[-1]
    
    middle_str = words[1:-2]
    # remove the "►" from the middle string
    middle_str = [word for word in middle_str if word != "►"]

    # Join the remaining words into a single string for uni name
    uni_name = " ".join(middle_str)

    return (rank, uni_name, country, count, faculty)

def getCountry(c):
    # Extract the country name from the src attribute of an img element.

    img = c.find_element(By.TAG_NAME,"img")
    src = img.get_attribute("src")
        
    # Extract the file name from the src attribute
    file_name = src.split("/")[-1]
        
    # Split the file name into the country code and the extension
    country_code, extension = os.path.splitext(file_name)

    # Fixing a problem to recognize England
    if country_code =='uk':
        country_code = 'GB'

    # Look up the country name using the country code
    country_name = pycountry.countries.get(alpha_2=country_code)

    return country_name.name


def main():
    start_time = time.time()
    # Create the parser
    #parser = argparse.ArgumentParser(description="Specify a chromedriver path. For more information, see the documentation at https://github.com/AbrarAdnan/Week-6-Project/blob/master/README.md#how-to-build-the-source-code-and-run-it")
    parser = argparse.ArgumentParser()
    # Add the chromedriver path argument
    parser.add_argument("--chromedriver_path", type=str, help="Path to the chromedriver executable")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the chromedriver path
    webdriver_path = args.chromedriver_path
    
    try:
        # Create a Chrome webdriver
        driver = webdriver.Chrome(webdriver_path)

        # Set the url to visit
        url = f"https://csrankings.org/#/index?all&world"

        # Visit the url
        driver.get(url)
    
    except Exception as e:
        # Print an error message and exit if an exception occurs
        print("An error occurred with chromedriver, Please run the script again", e)
        sys.exit(1)

    # Block the sponsor popup if it appears randomly
    try:
        # Find the sponsor button
        sponsor = driver.find_element(By.XPATH, '//*[@id="sponsor"]/button[2]')
        # Click on the sponsor button
        sponsor.click()
    except:
        # If the sponsor button is not found or not displayed, do nothing
        pass


    try:
        # Find the dropdown menu for selecting the year range
        timeline =  driver.find_element(By.XPATH, '//*[@id="fromyear"]')
        # Find the options in the dropdown menu
        years = timeline.find_elements(By.TAG_NAME, "option")

        # Select the "2000" option
        for year in years:
            if year.text == "2000":
                print(">>>Selected year: 2000")
                time.sleep(3)
                year.click()
        # Find the "deselect all" button for the topic of focus
        all_button = driver.find_element(By.XPATH, "//*[@id='all_areas_off']")
        # Click the button to deselect all topics
        all_button.click()
        time.sleep(5)
    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred while selecting the year range and deselecting all topics:", e)
        sys.exit(1)

    try:
    # Find the checkboxes for each subject
        arch_checkbox = driver.find_element(By.XPATH,'//*[@id="arch"]')
        compnet_checkbox = driver.find_element(By.XPATH,'//*[@id="comm"]')
        sec_checkbox = driver.find_element(By.XPATH,'//*[@id="sec"]')
        ops_checkbox = driver.find_element(By.XPATH,'//*[@id="ops"]')
        proglang_checkbox = driver.find_element(By.XPATH,'//*[@id="plan"]')
        soft_checkbox = driver.find_element(By.XPATH,'//*[@id="soft"]')
        
        # Select the checkboxes
        checkboxes = [arch_checkbox, compnet_checkbox, sec_checkbox, ops_checkbox, proglang_checkbox, soft_checkbox]
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)
        
        print(">>>Selected subjects")

    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred while selecting the subjects:", e)
        sys.exit(1)

    try:
        # Find the scrollbar element
        scrollbar = driver.find_element(By.XPATH, '//*[@id="success"]/div')
        
        # Scroll to the bottom of the element
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbar)
        print(">>>Loaded all the university in the table")
        time.sleep(3)

    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred while scrolling the table:", e)
        sys.exit(1)

    try:
        # Find the table element
        ranking_table = driver.find_element(By.XPATH, "/html/body/div[5]/form/div/div[2]/div[2]/div/div/table/tbody")
        
        # Scroll to the bottom of the table
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ranking_table)
        time.sleep(3)
        
        # Find all the rows in the table
        rows = ranking_table.find_elements(By.TAG_NAME, "tr")
        
        print(">>>Raw data of universities found will be shown in real time below")
        # Iterate through the rows and get the country name for each row
        tick = 0
        for row in rows:
            if row.text:
                tick = tick + 1
                
                print(row.text)
                country_name = getCountry(row)
                uni_list.append(cleanup(row.text, country_name))
                if tick == 10:
                    break

    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred while scraping data from the table:", e)
        sys.exit(1)

    try:
        # Create a DataFrame from the list of university data
        df = pd.DataFrame(uni_list, columns=columns)
        
        # Save the DataFrame to a CSV file
        df.to_csv("best_uni_list.csv")
        print('Sucess: Saved the output data in the best_uni_list.csv file')
        
        # Calculate the total time taken to run the script
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken / 60} minutes")

    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred while saving the output data:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()