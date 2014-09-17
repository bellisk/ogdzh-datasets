#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json
import csv

def get_group_names():
    r = requests.get('https://data.integ.stadt-zuerich.ch/api/3/action/package_list', verify=False)
    ids = json.loads(r.text)['result']

    datasets = []

    for id in ids:
        r = requests.get("https://data.integ.stadt-zuerich.ch/api/3/action/package_show?id=" + id, verify=False)
        dataset = json.loads(r.text)
        if dataset['result']['type'] == 'dataset':
            dataset_row = []
            title = dataset['result']['title']
            dataset_row.append(title.encode('utf-8'))
            for group in dataset['result']['groups']:
                dataset_row.append(group['title'].encode('utf-8'))
            print dataset_row
            datasets.append(dataset_row)

    with open(u'Open Data Zürich datasets.csv', 'w') as f:
        writer = csv.writer(f)
        for dataset_row in datasets:
            writer.writerow(dataset_row)

if __name__ == '__main__':
    get_group_names()
