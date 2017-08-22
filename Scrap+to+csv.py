
# coding: utf-8

# Python Version : 3.5.2
# 
# Details:
# #This is a scrapper code to extract State and City details from wiki = "http://www.mapsofindia.com/states/"
# 
# Input : wiki link (Hard Coded)
# OutPut: csv file named "India States & Cities.csv"
# 

# Import necessary libraries
import requests
import pandas as pd
import urllib.request as urllib2
from bs4 import BeautifulSoup
# Destination URL
wiki = "http://www.mapsofindia.com/states/"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,"lxml")
# Get the right table
my_table=soup.find('table', class_='tableizer-table')
#Generate list to store column data 
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
Country = []
List1 = []
for row in my_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==12: #Only extract table body not heading
        List1 = cells[5].find_all(text = True)
        str1 = ''.join(str(e) for e in List1)
        sp = []
        sp = str1.split(',')
        # Get cities in rows
        for st in sp:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(st)
            Country.append("INDIA")
    
#  Create dataframe to store Columns  
df=pd.DataFrame()
df['Country']=Country
df['State/UT']=A
# Store state in lower case for the data handling
df['State/UT'] = df['State/UT'].apply(lambda val: val.lower())
df['Admin_Capital']=B
df['Area']=C
df['Population']=D
df['Language']=E
df['Major Cities']=F
# Write to csv file
df.to_csv("India States & Cities.csv")

 

