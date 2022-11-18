import requests
import io

from bs4 import BeautifulSoup
from pprint import pprint


class Police:
    def __init__(self):
        self.base_url = 'https://info.police.ge/'
        self.session = requests.Session()
        self.version = 1.0
        self.data = {}

    def __str__(self):
        return f'<PoliceInfo v{self.version}>'

    def getInfo(self):
        response = self.session.get(f'{self.base_url}page?id=115')
        soup = BeautifulSoup(response.content, 'html.parser')
        results = {}

        for link in soup.findAll('div', {'class': 'links'}):
            atag = link.find('a')
            title = atag.text.strip().split('სტატისტიკა ')[1]
            year = title.replace(' წელი', '')
            url = atag.get('href')

            if ' -' in title:
                title = title.split(' -')[1]

            results[year] = {}

            if url.endswith('.pdf'):
                results[year] = self.parsePdf(url)

            else:
                response = self.session.get(f'{self.base_url}{url}')
                soup = BeautifulSoup(response.content, 'html.parser')

                for data in soup.findAll('div', {'style': 'padding: 0 20px;'}):
                    for atag in data.findAll('a'):
                        link = atag.get('href')
                        title = atag.text

                        month = title.split('(')[1].split(')')[0]
                        results[year][month] = self.parsePdf(url)

        return results


    def parsePdf(self, pdfurl):
        return pdfurl
