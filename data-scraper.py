# Automation Workflow
# Website
#     │
#     ▼
# Download HTML
#     │
#     ▼
# Parse HTML
#     │
#     ▼
# Extract Data
#     │
#     ▼
# Save Results

#------------------------------------------------------------
# Import required modules
#------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

#------------------------------------------------------------
# Download the webpage
#------------------------------------------------------------

response=requests.get("https://example.com")
#print(response.status_code)

if response.status_code==200:
    print("Website loaded")
else:
    print("Error")
#------------------------------------------------------------
# Parse the html
#------------------------------------------------------------

soup=BeautifulSoup(response.text,"html.parser")

title=soup.title.text #extract the title 
#print(title)

heading=soup.find('h1').text #extract the main heading
#print(heading)

paragraph=soup.find('p').text #extract the paragraph
#print(paragraph)

#------------------------------------------------------------
# save the data to text file
#------------------------------------------------------------

with open("websitedata.txt","w") as file:
    file.write(f"Title:{title}\n\n")
    file.write(f"Heading:{heading}\n\n")
    file.write(f"paragraph:{paragraph}")

