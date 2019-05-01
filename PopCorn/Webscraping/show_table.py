# show_table - title, release_date, duration, discriptiion, image, country, budget, boc, status, avg_rating, num_rating, trailer, type, taglines

import csv

with open('combined_csv2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('show_table.csv', 'w') as new_file:

        fieldnames = ['\ufefftitle1', 'release_date', 'country', 'poster', 'link_trailer', 'story', 'final_genres', 'taglines', 'runtime_final', 'earning', 'final_budget', 'language', 'final_writers', 'director', 'final_actors', 'imdb']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=['id', 'title', 'release_date', 'duration', 'discription', 'image', 'country', 'budget', 'boc', 'status', 'avg_rating', 'num_rating', 'trailer', 'type', 'taglines'])
        
        csv_writer.writeheader()
        # final_l = []

        count = 0
        for line in csv_reader:
            new_dict = {}
            # print(line['\ufefftitle1'])
            # # # print(line)

            new_dict['id'] = count
            new_dict['title'] = line['\ufefftitle1']
            new_dict['release_date'] =  line['release_date']
            new_dict['duration'] = line['runtime_final']
            new_dict['discription'] = line['story']
            new_dict['image'] = line['poster']
            new_dict['country'] = line['country']
            new_dict['budget'] = line['final_budget']
            new_dict['boc'] = line['earning']
            new_dict['status'] = 'NA'
            new_dict['avg_rating'] = 0.0
            new_dict['num_rating'] = 0.0
            new_dict['trailer'] = line['link_trailer']
            new_dict['type'] = 'M'    
            new_dict['taglines'] = line['taglines']
            print(new_dict)
            # break
            count += 1
            csv_writer.writerow(new_dict)

 
csv_file.close()