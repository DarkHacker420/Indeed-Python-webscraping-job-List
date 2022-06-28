import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_extract(page):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    url = f"https://pk.indeed.com/jobs?q=python%20developer&l=Islamabad&start={page}&vjk=74e7aac9057da2c9"
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='cardOutline')
    # return len(divs)
    for items in divs:
        titles = items.find('a').text
        # print(titles)
        companyName = items.find('span', class_='companyName').text
        # print(companyName)
        companyLocation = items.find('div', class_='companyLocation').text
        # print(companyLocation)
       
        try:
           salary = items.find('div', class_='salaryOnly').text
        except:
            salary = ' '
        summary = items.find('table', class_='jobCardShelfContainer').text
        job = {
            'titles'            : titles,
            'companyName'       : companyName,
            'companyLocation'   : companyLocation,
            'salary'            : salary,
            'summary'           : summary


        }
        joblist.append(job)

    return

joblist = []

for i in range(0,40, 10):
    print(f'Get Pages: {i}')
    c = get_extract(0)
    # print(transform(c))
    transform(c)
# print(len(joblist))

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv("JobList.csv")