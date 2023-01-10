# Data-Driven Ranking of Top CS Universities

## Introduction
The goal of this project was to gather and analyze data on the top computer science institutions and their faculties around the world, as ranked by the website [CS Rankings](https://csrankings.org/#/index?all&world) which is a metrics-based ranking of top computer science institutions around the world. We gathered our data into two files. The first data we gathered includes information about university rankings, the count of geometric mean papers published across all areas, and the number of faculty members who have published papers in our areas of concern (Computer Architecture, Computer Networks, Computer Security, Operating Systems, Programming Languages, and Software Engineering). The other data file containted the names of the faculties of our conceren universities along with university name, pubs and adj. We took the ranking of the whole world from 2000 to 2022 and found approximately 500 universities.

## Data Collection
To gather the data, we used a Python script and the [Selenium](https://selenium-python.readthedocs.io/) library to scrape the CS Rankings website. The example of the raw data files obtained from the website are shown below:
<br><br>
![image](https://user-images.githubusercontent.com/52294804/209989670-7b18be8a-5922-4c5d-bcb5-04109728c44a.png)
<br>
![image](https://user-images.githubusercontent.com/52294804/211547670-325fe859-0200-41d4-9c43-76c4b721f78a.png)
<br><br>

## Data Analysis
We used our scraped data to answer the following questions:

1. What are the top 10 universities in terms of ranking?
2. What are the top 10 countries with the most number of publications (i.e. count score)?
3. What are the top 10 countries with most universities?
4. Is there any correlation between the ranking of universities and the count and faculty number?
5. Which faculties had the most number of publications?

## Findings
We used [Tableau](https://www.tableau.com/) to visualize and analyze our data. Some of our findings include:
1. American universities have the highest ranks, with Carnegie Mellon University having the highest rank.
2. America has highest number of publication score with other countries at weighing at one sixth of America's publication points.
3. America takes the first position by a huge margin with 172 universities, followed by Germany with 57 universities.
4. There is a strong correlation between the ranking and the count score but relatively weaker correlation between rank and the number of faculty members.
5. From the list of top faculties based on publications, two from ETH Zurich and Univ. of California - Santa Barbara made into the list while the others were from different universities.

Check the interactive [Tableau dashboard](https://public.tableau.com/app/profile/abrar.faiaz.adnan/viz/CSrankingsdemoproject/Dashboard1?publish=yes) to get more information of each datapoint

![image](https://user-images.githubusercontent.com/52294804/210097706-6a95e8ec-61d4-4d91-ad24-d11d5f7bb02a.png)

Here is the second interactive [Tableau dashboard](https://public.tableau.com/app/profile/abrar.faiaz.adnan/viz/TopfacultiesfromCSRankingswebsite/Dashboard1?publish=yes)
![image](https://user-images.githubusercontent.com/52294804/211546894-7867de6d-b93b-4798-b2da-6cbb675a299a.png)

## Building and Running the Source Code


1. Open the command prompt (Windows) or terminal (Linux/Mac) and navigate to the desired directory.

2. Clone the repository on your computer using the following command:
```bash
git clone https://github.com/AbrarAdnan/Data-Driven-Ranking-of-Top-CS-Universities.git
```

3. Navigate to the downloaded project folder\
```bash
cd Data-Driven-Ranking-of-Top-CS-Universities
```
4. Initialize and activate the virtual environment after navigating into the project folder

On Windows:
```bash
virtualenv venv
venv\Scripts\activate
```
On Mac/Linux:
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
5. Install Dependencies
```bash
pip install -r requirements.txt
```
   
6. Run the scraper
```bash
python scraper.py
```
(OPTIONAL) You can add an argument to choose your desired browser for scraping.<br>
For example: python scraper.py --browser firefox
<br>
You can put firefox chrome or edge as a choice but firefox has faster scraping speed and it's used by default

7. After the script has finished running, it will save the scraped data in a file called best_uni_list.csv in the project directory.

# Notes
1. The chromedriver file is included in the repository
2. The code needs python to run. Download python for [Windows](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe), [Linux](https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz) or [MAC OS](https://www.python.org/ftp/python/3.11.0/python-3.11.0-macos11.pkg).
3. While running the code, a window of Chrome will appear. You can see the website it is working on in real time. You can also check the console/terminal for additional output messages to get a better understanding of what is happening in real time.
4. The script will take approximately 46 minutes on firefox to run and produce output. Time may vary depending on the browser.
5. While loading the csv file into tableau, Taiwan needs to be identified manually or it'll not be recognized with Tableau's country database.
