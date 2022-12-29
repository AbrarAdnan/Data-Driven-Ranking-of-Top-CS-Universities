# Statistical analysis of top CS Universities

## Problem Statement
The goal of the project is to gather data from the website [CS Rankings](https://csrankings.org/#/index?all&world)<br/>
This is a metrics-based ranking of top computer science institutions around the world.

The data we gathered are the information of the university rankings, 
count(Geometric mean count of papers published across all areas)
and number of faculties published papers in our areas of concern.
We chose these area of topics 
Computer Acrhitecture, Computer Networks, Computer Security, Operating Systems, Programming Languages and Software Engineering
We took the ranking of the whole world from the year 2000 to 2022. In our search we found a little less then 500 universities.

The raw data scraped from the website looked like this
INSERT IMAGE OF CSV FILE

We used our scraped data to find answers to some questions.
1. Top 10 universities are best in ranking (along with their country name).
2. Top 10 countries with most number of universities
3. Average ranking of universities of all countries
4. Correlation of ranking of universities with count and faculty number.

## From our findings in [Tableau](https://public.tableau.com/app/profile/abrar.faiaz.adnan/viz/CSrankingsdemoproject/Dashboard1?publish=yes)
we found out that
1. American Universities have highest ranks with Carnegie Mellon University scoring the highest rank.
2. America has the highest number of universities with 172 leaving other countries in far off. Our 2nd place holder was Germany with 57 Universities
3. In average rankings of the top universities per country Brazil, Norway, Finland,Czech Republic, Hungary, Malta, Greece, Turkey, Iran, UAE has average rating of over 300
4. The ranking of universities are highly correlated with the count and faculty number

## How to build the source code and run it


1. Open command prompt(windows) or termial(Linux) and additionally you can go to a directory of your choice after opening it

2. Clone the repository in your pc with this code git clone 
```bash
https://github.com/AbrarAdnan/Week-6-Project.git
```
3. Initialize and activate the virtual environment

Windows: 
```bash
virtualenv venv
venv\Scripts\activate
```
MAC/Linux:
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
4. Install Dependencies
```bash
pip install -r requirements.txt
```
   
5. Run the scraper
```bash
python scraper.py --chromedriver_path <Location to the chromedriver>
```
   eg. python scraper.py --chromedriver_path "C:\Users\Adnan\Desktop\chromedriver.exe"
6. After the script has finished running it'll save a our scraped data into file called best_uni_list.csv in the project directory.

# Notes
1. The chromedriver file is included in the repository
2. The code needs python to run. Download python from here [Windows](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe) [Linux](https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz) [MAC OS](https://www.python.org/ftp/python/3.11.0/python-3.11.0-macos11.pkg)
