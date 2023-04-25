import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

# Set up the driver
driver = webdriver.Chrome()

# Set url variable with targeted website
url = 'https://runsignup.com/Race/Results/22766#resultSetId-376660;perpage:5000'

# Use the driver and url
driver.get(url)

# Add a delay to allow the web page to fully load
time.sleep(5)

# Get the page source after the delay
html = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the table element by ID
table = soup.find('table', {'id': 'resultsTable'})

# Extract the table headers
headers = []
for th in table.thead.find_all('th'):
    headers.append(th.text.strip())

# Extract the table data
data_rows = table.tbody.find_all('tr')
data = []
for tr in data_rows:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    data.append(row)

# Create the dataframe
results = pd.DataFrame(data, columns=headers)

# Export the dataframe to a csv file
results.to_csv('D:\Documents\Kevin_Portfolio\\2023_GCM_HM_Times\GCMresults20230423.csv', index=False)

print(results.tail())