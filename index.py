import requests
from bs4 import BeautifulSoup
from csv import writer

# response = requests.get('http://books.toscrape.com/')

# el = soup.find_all(attrs={"data-event-action": "title"})

# el2 = soup.select('.Question__heading')

# for oltag in soup.find_all('ol', {'class': 'row'}):
#   for litag in oltag.find_all('li'):
#     for price in litag.find_all(class_="price_color"):
#       print(price.get_text()[2:])


response = requests.get('https://www.toddfichman.com/')

soup = BeautifulSoup(response.text, 'html.parser')

projects = soup.find_all('div', {'class': 'portfolio-section'})

# w for write to file
with open('projects.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link']
    csv_writer.writerow(headers)

    for project in projects:
      title = project.find('h3').get_text().replace('\n', '')
      link = project.find('a')['href']
      print(title, link) 
      csv_writer.writerow([title, link])


# titles = []

# for sections in soup.find_all('div', {'class': 'portfolio-section'}):
#   for title in sections.find_all('h3'):
#     # print(title)
#     titles.append(title.get_text())

 