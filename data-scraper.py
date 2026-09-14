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

#------------------------------------------------------------
# Parse the html
#------------------------------------------------------------

soup=BeautifulSoup(response.text,"html.parser")

title=soup.title.text
print(title)

