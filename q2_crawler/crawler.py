import json
import os
import requests
from bs4 import BeautifulSoup

def get_disease_by_specialty(url, specialty):
    """Get the disease structure of the specialty.
    """

    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    result = {}

    # target specialty
    target = soup.find('a', text = specialty)

    if target is not None:

        result[specialty] = {}

        sub_specialty = None
        current_tag = target.find_parent('h3')

        while current_tag.next_sibling.name != 'h3':

            current_tag = current_tag.next_sibling

            if current_tag.name == 'h4':
                # sub specialty
                sub_specialty = current_tag.find('a').string
                result[specialty][sub_specialty] = []

            if current_tag.name == 'p':

                if sub_specialty is None:
                    sub_specialty = specialty
                    if sub_specialty not in result[specialty]:
                        result[specialty][sub_specialty] = []

                # diseases
                diseases = current_tag.find_all('a')
                for d in diseases:
                    result[specialty][sub_specialty].append(d.string)

    return result

def get_disease_url_by_specialty(url, specialty):
        """Get disease links of the specialty.
        """

    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    result = {}

    # target specialty
    target = soup.find('a', text = specialty)

    if target is not None:

        result[specialty] = {}

        current_tag = target.find_parent('h3')

        while current_tag.next_sibling.name != 'h3':

            current_tag = current_tag.next_sibling

            if current_tag.name == 'p':

                # diseases
                diseases = current_tag.find_all('a', href = True)
                for d in diseases:
                    result[specialty][d.string] = d['href']

    return result

def get_disease_detail(url):
    """Get disease detail from the disease page.
    """

    response = requests.get(url)
    response.encoding = 'utf-8'

    html = response.text

    # remove redundant info
    html = html.split('<!-- firstHeading -->')[1]
    html = html.split('<div id="fromlink">')[0]
    html = html.split('<span class="mw-headline" id=".E5.8F.82.E7.9C.8B">参看</span>')[0]
    html = html.split('<span class="mw-headline" id=".E5.8F.82.E8.80.83">参考</span>')[0]

    soup = BeautifulSoup(html, 'lxml')
    [s.extract() for s in soup('script')]
    soup.find('div', {'id': 'jump-to-nav'}).decompose()

    # remove table of contents
    toc = soup.find('table', {'id': 'toc'})
    if toc:
        toc.decompose()

    # remove navigation bar at the top
    nav = soup.find_all('table', {'class': 'nav'})
    for n in nav:
        n.decompose()

    # remove navigation box at the bottom
    navbox = soup.find_all('table', {'class': 'navbox'})
    for n in navbox:
        n.decompose()

    return soup.get_text()

if __name__== "__main__":

    url = 'http://www.a-hospital.com/w/%E7%96%BE%E7%97%85'

    # get all diseases under '内科疾病'
    internal_medicine = get_disease_by_specialty(url, '内科疾病')

    with open('internal_medicine.json', 'w', encoding = 'utf8') as json_file:
        json.dump(internal_medicine, json_file, ensure_ascii = False)

    # get all diseases under '外科疾病'
    # surgery = get_disease_by_specialty(url, '外科疾病')
    #
    # with open('surgery.json', 'w', encoding = 'utf8') as json_file:
    #     json.dump(surgery, json_file, ensure_ascii = False)

    # get all diseases under '儿科疾病'
    # pediatrics = get_disease_by_specialty(url, '儿科疾病')
    #
    # with open('pediatrics.json', 'w', encoding = 'utf8') as json_file:
    #     json.dump(pediatrics, json_file, ensure_ascii = False)

    # get disease details under '内科疾病'
    dir = 'disease_detail/'
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except Error as e:
            print('Can not create folder: {}. Error: {}'.format(dir, e))
            exit()

    urls = get_disease_url_by_specialty(url, '内科疾病')
    for name, url in urls['内科疾病'].items():

        url = 'http://www.a-hospital.com{}'.format(url)

        detail = get_disease_detail(url)

        with open(dir + name + '.txt', 'w', encoding = 'utf8') as file:
            file.write(detail)
