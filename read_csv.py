from pandas import *
from bs4 import BeautifulSoup
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
# read csv file and transform it into a list of url
file = read_csv('url_list.csv')
links = file['url'].tolist()

final_data = []
data = {}
i= 0
# Scraping process
for link in links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        site_url = soup.find('a', class_='flex space-x-2 py-1 px-2 rounded-md flex-1 transition-all text-primary-500 hover:bg-slate-200')['href']
    except:
        site_url = None
    try:
        site_name = soup.find('h1', class_='self-end inline-block text-4xl font-bold md:text-5xl').get_text()
    except:
        site_name = None

    data = {
        "Site Name": site_name,
        "URL": site_url
    }
    final_data.append(data)
    print(f'Scraping for link number {i+1}')
    i += 1

# Create csv file
df = DataFrame(final_data)
df.to_csv('final_data.csv', index=False)
print("Data created success")
print("Total rows", len(final_data))




