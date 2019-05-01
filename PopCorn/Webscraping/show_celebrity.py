import csv
import requests
import pprint
from bs4 import BeautifulSoup


dict1 = {}
with open('celebrity.csv', 'r') as celeb:
        csv_reader = csv.DictReader(celeb)
        fieldnames2 = ['id', 'name']
        
        for line in csv_reader:
            # print(line)
            dict1[line['name']] = int(line['id'])  

with open('combined_csv2.csv', 'r') as new_file1:

    csv_reader1 = csv.DictReader(new_file1)

    fieldnames1 = ['final_writers', 'director', 'final_actors']


    with open('show_celeb.csv', 'w') as csv_file:
        fieldnames = ['showID', 'celebID', 'role']
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        count = 0
        for line in csv_reader1:
            dictNew = {}
            # list5 = []
            writers = line['final_writers'].split('-')
            director = line['director'].split('-')
            actor = line['final_actors'].split('-')
            # print(list5)
            for items in writers:
                try:
                    dictNew['showID'] = count
                    dictNew['celebID'] = dict1[items]
                    dictNew['role'] = 'W'
                    csv_writer.writerow(dictNew)
                except:
                    pass
            for items in director:
                try:
                    dictNew['showID'] = count
                    dictNew['celebID'] = dict1[items]
                    dictNew['role'] = 'D'
                    csv_writer.writerow(dictNew)
                except:
                    pass
            for items in actor:
                try:
                    dictNew['showID'] = count
                    dictNew['celebID'] = dict1[items]
                    dictNew['role'] = 'A'
                    csv_writer.writerow(dictNew)
                except:
                    pass
            count += 1
            # break
            # print(line)

            # break
csv_file.close()