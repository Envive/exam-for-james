import json
import requests
from bs4 import BeautifulSoup

def get_disease_by_specialty(specialty):

    url = 'http://www.a-hospital.com/w/%E7%96%BE%E7%97%85'
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

if __name__== "__main__":

    # get all diseases under '内科疾病'
    internal_medicine = get_disease_by_specialty('内科疾病')

    with open('internal_medicine.json', 'w', encoding = 'utf8') as json_file:
        json.dump(internal_medicine, json_file, ensure_ascii = False)

    # get all diseases under '外科疾病'
    # surgery = get_disease_by_specialty('外科疾病')
    #
    # with open('surgery.json', 'w', encoding = 'utf8') as json_file:
    #     json.dump(surgery, json_file, ensure_ascii = False)

    # get all diseases under '儿科疾病'
    # pediatrics = get_disease_by_specialty('儿科疾病')
    #
    # with open('pediatrics.json', 'w', encoding = 'utf8') as json_file:
    #     json.dump(pediatrics, json_file, ensure_ascii = False)
