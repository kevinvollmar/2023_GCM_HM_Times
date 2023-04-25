import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the and read the csv file
file = pd.read_csv('GCMresults20230423.csv')

# Subset data where Age equals 29
file_age_29 = file[file['Age'] == 29]

# Convert Chip Time to seconds
file['Chip Time'] = pd.to_timedelta(file['Chip Time']).dt.total_seconds()

# Convert Chip Time to minutes
file['Chip Time'] = file['Chip Time'] / 60

# Select the columns to be used in the dataframe
cols = ['Age', 'Chip Time']

# Create the plot
sns.scatterplot(x='Age', y='Chip Time', hue='Gender', data=file)

# Show the plot
plt.show()