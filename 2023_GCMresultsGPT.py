'''
This code exports the results to a CSV file called "race_results.csv" in the same directory as the Python script.
The index=False argument in the to_csv() method ensures that the index column is not included in the exported file.
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

# Set up the driver
driver = webdriver.Chrome()

# Set the base URL for the race results
base_url = 'https://runsignup.com/Race/Results/'

# Set the race ID and result set ID
race_id = '22766'
result_set_id = '376660'

# Set the number of pages of results to scrape
num_pages = 21

# Initialize an empty list to store the results
all_results = []

# Loop through each page of results and scrape the data
for i in range(num_pages):
    # Set the URL for the current page of results
    url = f'{base_url}{race_id}?resultSetId={result_set_id}&page={i+1}'

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

    # Append the data to the results list
    all_results.extend(data)

# Create the dataframe
results = pd.DataFrame(all_results, columns=headers)

# Export the results to a CSV file
results.to_csv('race_results.csv', index=False)

# Print the first and last five rows of the results
print(results.head())
print(results.tail())
