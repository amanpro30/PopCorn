import csv
import requests
import pprint
from bs4 import BeautifulSoup

with open('combined_csv2.csv', 'r') as new_file:

    csv_reader = csv.DictReader(new_file)
    with open('genre2.csv', 'w') as csv_file:
        fieldnames = ['\ufefftitle1', 'final_genres']
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        # final_array = []
        count = 0
        for line in csv_reader:
            new_dict = {}
            new_dict['\ufefftitle1'] = count
            new_dict['final_genres'] = line['final_genres']
            new_dict['final_genres'] = new_dict['final_genres'].split(' ')
            new_dict['final_genres'] = set(new_dict['final_genres'])
            new_dict['final_genres'].remove('')
            # print(new_dict['final_genres'])
            for i in new_dict['final_genres']:
                new_dict1 = {}
                new_dict1['\ufefftitle1'] = count
                new_dict1['final_genres'] = i
                # print(new_dict1)
                csv_writer.writerow(new_dict1)
            count += 1
            # break
    
csv_file.close()