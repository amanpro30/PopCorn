from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('most_popular_movies.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title1', 'release_date', 'country', 'poster', 'link_trailer', 'story', 'final_genres', 'taglines', 'runtime_final', 'earning', 'final_budget', 'language', 'final_writers', 'director', 'final_actors', 'imdb'])

top_rated_movies = f'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'
source = requests.get(top_rated_movies).text
soup = BeautifulSoup(source, 'lxml')

block = soup.find('tbody',class_="lister-list").find_all('tr')

for rows in block:

    try:
        passposter = rows.find('td', class_='posterColumn')
        poster = passposter.a.img['src']
    except Exception as e:
        poster = None

    print(poster)

    title = rows.find('td', class_='titleColumn')
    detail_movie = title.a
    movie_title = detail_movie.text

    print(movie_title)

    link = detail_movie['href']
    final_link = f'https://www.imdb.com/{link}'

    source = requests.get(final_link).text
    soup = BeautifulSoup(source, 'lxml')

    title = soup.find('div', class_='title_wrapper')
    title1 = title.h1.text
    
    country = title.find_all('a')
    country = country[len(country)-1].text
    release_date = country

    print(country)
    try:
        trailer = soup.find('div', class_='slate')
        link_trailer = trailer.a
        link_trailer = link_trailer['href']
        link_trailer = f'https://www.imdb.com{link_trailer}'
    except:
        link_trailer = None

    print(link_trailer)

    try:
        storyline = soup.find('div', class_='inline canwrap')
        story = storyline.p.span.text
    except:
        story = None

    print(story)

    try:
    
        genre = soup.find('div', id='titleStoryLine')
        types = genre.find_all('div', class_='see-more inline canwrap')
        types.pop(0)
        genres = types[0].find_all('a')
        listOfA = [] 
        for i in genres:
            listOfA.append(i.text)
        
        final_genres = ' '.join(listOfA)
        print(listOfA)
    
    except:
        genres = None

    try:
        tagline = soup.find('div', id='titleStoryLine')
        taglines = tagline.find('div', class_='txt-block').text.split(':')[1]

        try:
            span = taglines.find('span', class_='see-more inline')
            href = span.a
            href = href['href']
        except:
            pass
    except:
        taglines = None
    
    print(taglines)
    language1 = []
    
    try:
        titleDetails = soup.find('div', id='titleDetails')
        divs = titleDetails.find_all('div', class_='txt-block')
        divs.pop()
        divs.pop()
        divs.pop()
        
        runtime = divs[len(divs)-1]
        # time = runtime.split(' ')
        # final_runtime = time[0]
        
        divs.pop()
        divs.pop()
        divs.pop()
        
        total_grosss = divs[len(divs) -1]
        earning = total_grosss.text.split(':')[1]
        runtime_final = runtime.text.split(':')[1].split('|')
        runtime_final = runtime_final[0]
        print(runtime_final)
        print(earning)

        divs.pop()
        divs.pop()
        divs.pop()
        
        budget = divs[len(divs)-1]
        final_budget = budget.text.split(':')[1]
        final_budget = final_budget.split('(')
        final_budget = ' '.join(final_budget[0:2])
        
        divs.pop()
        divs.pop()
        divs.pop()
        divs.pop()
        
        language = divs[len(divs)-1].text.split(':')[1].split('|')
        for i in language:
            i=i.strip()
            language1.append(i)
        print(language1)
        print(final_budget)

    except:
        pass

    try:
        directors = soup.find_all('div', class_='credit_summary_item')
        director = directors[0].text.split(':')[1]
        if(len(directors) == 2):
            writers = []
        else:
            list_of_writers = []
            writers = directors[1].find_all('a')

            for i in writers:
                list_of_writers.append(i.text)

            final_writers = '-'.join(list_of_writers)
            print(list_of_writers)
    except:
        pass
    actors = directors[len(directors)-1].find_all('a')
    actors.pop()
    list_of_actors = []

    for i in actors:
        list_of_actors.append(i.text)

    final_actors = '-'.join(list_of_actors)

    print(list_of_actors)
    print(director)
    try:
        imdbRating = soup.find('div', class_='ratingValue')
        imdb = imdbRating.strong.span.text
    except:
        imdb = None
    print(imdb)
    # break
    csv_writer.writerow([title1,release_date, country, poster, link_trailer, story, final_genres, taglines, runtime_final, earning, final_budget, language1, final_writers, director, final_actors, imdb  ])

csv_file.close()
