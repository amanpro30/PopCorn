import csv
import requests
import pprint
from bs4 import BeautifulSoup

with open('directors.csv', 'r') as new_file:

    csv_reader = csv.DictReader(new_file)
    with open('celebrity.csv', 'w') as csv_file:
        fieldnames=['name', 'bday', 'location', 'final', 'p']        
        csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'bday', 'location', 'final', 'p'])

        csv_writer.writeheader()

        count = 0
        for line in csv_reader:
            new_dict = {}
            new_dict['id'] = count
            new_dict['name'] = str(line['name'])
            new_dict['bday'] = str(line['bday'])
            new_dict['location'] = str(line['location'])
            new_dict['final'] = str(line['final'])
            new_dict['p'] = str(line['p'])
            print(new_dict)
            count+=1
            csv_writer.writerow(new_dict)
            # break
    
csv_file.close()