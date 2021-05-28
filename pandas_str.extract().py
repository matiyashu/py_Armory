"""
TABLE

     Country_Feature        Observation
0    AUSpop                 24.99
1    AUSage                 37.00
2    AUSinc                 65687.00
3    BELpop                 11.46
4    BELage                 41.30

Task

where the first 3 letters of Country_Feature indicate the country and the last 3 letters indicate the variable:

pop for population in millions
age for age in years
inc for income in thousands of dollars
Use regular expressions to extract and separate the two values from the Country_Feature column. Then add 
these columns back to the data set country and drop unnecessary columns. Lastly, the columns of the data set to be 
Country, Feature, and then Observation and print the data set.

DOC: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html
"""

import pandas as pd

country = pd.read_csv("country.csv")

# Extract Country abbreviation and Feature from 'Country_Feature' using regular expressions
sep = country["Country_Feature"].str.extract("(\D{3})(\D{3})")

# Name Columns "Country" and "Feature"
sep.columns = ["Country", "Feature"]

# Merge country and sep
country = pd.concat([country, sep], axis = 1)

# Drop 'Country_Feature' column
country = country.drop(['Country_Feature'], axis = 1)

# Sort Columns to 'Country', 'Feature', and 'Observation'
country = country[["Country", "Feature", "Observation"]]

# Print country
print(country)


"""
Output:
Country Feature  Observation
0      AUS     pop        24.99
1      AUS     age        37.00
2      AUS     inc     65687.00
3      BEL     pop        11.46
4      BEL     age        41.30
5      BEL     inc     30364.00
6      CAN     pop        37.59
7      CAN     age        40.90
8      CAN     inc     53336.00
9      DNK     pop         5.81
10     DNK     age        41.50
11     DNK     inc     29606.00
12     ENG     pop        55.98
13     ENG     age        40.50
14     ENG     inc     40231.00
"""
