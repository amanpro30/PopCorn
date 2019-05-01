import csv
import requests
import pprint
from bs4 import BeautifulSoup

with open('combined_csv2.csv', 'r') as new_file:

    csv_reader = csv.DictReader(new_file)
    with open('directors.csv', 'w') as csv_file:
        fieldnames = ['final_writers', 'director', 'final_actors']
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'bday', 'location', 'final', 'p'])

        csv_writer.writeheader()
        final_array = []
        for line in csv_reader:
            final_array.extend(line['final_writers'].split('-'))
            final_array.extend(line['director'].split('-'))
            final_array.extend(line['final_actors'].split('-'))
        for i in range(len(final_array)):
            final_array[i] = final_array[i].strip()
        final_array = set(final_array)
        final_array = list(final_array)
        for j in range(len(final_array)):
        
            if('credit' in final_array[j]):
                final_array[j] = '$'
            elif('credits' in final_array[j]):
                final_array[j] = '$'
            else:
                continue         
        final_array = set(final_array)
        final_array = list(final_array)
        try:
            final_array.remove('$')
        except:
            pass
        count = 0
        # print(final_array)
        for element in final_array:
            new_dict = {}
            l = []
            l = element.split(' ')
            name1 = ' '.join(l)
            new_dict['name'] =  name1
            name = '_'.join(l)
            line['name'] = name
            string = f"https://en.wikipedia.org/wiki/{name}"
            source = requests.get(string).text
            soup = BeautifulSoup(source, 'lxml')
            
            block = soup.find('div', class_='mw-parser-output')
            # table = block.find('tbody')
            try:    
                table = block.find('tbody')
            except:
                pass
            try:
                bday = table.find('span', class_='bday').text
            except:
                bday = None
            new_dict['bday'] = bday
            try:
                loop = table.find_all('tr')
            except:
                pass
            final = []
            try:
                del loop[0]
                lo = loop[0]
                lo = lo.td.a.img
                lo = lo['srcset']
                final = lo.split(',')
                del final[1:]
                final = final[0].split(' ')
                final.pop()
                final = final[0].split('//')
                del final[0]
                final = final[0].strip()
            except:
                final = None

            location = ''
            try:
                del loop[0]
                location = loop[0].a.text
                if(location == '[1]'):
                    location = None
                else:
                    pass
            except:
                location = None
            new_dict['location'] = location
            new_dict['final'] = final

            try:
            
                p = block.find_all('p')
                del p[0]
                p = p[0].text.strip()
            except:
                p = None
            new_dict['p'] = p
            
            print(new_dict)
            count += 1
            print(count)

            csv_writer.writerow(new_dict)