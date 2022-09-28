from requests import get
from bs4 import BeautifulSoup
import pandas as pd 

# Initializing the series that the loop will populate
episodes = []

rating_average = dict()

# Series id
seriesID = "tt4158110"

query = "https://www.imdb.com/title/" + seriesID + "/episodes?season="

def getSeasonAverage(seriesID, seasons):
    query = "https://www.imdb.com/title/" + seriesID + "/episodes?season="
    for sn in range(1, int(seasons)+1):
        response = get(query + str(sn))
        page_html = BeautifulSoup(response.text, 'html.parser')

        episode_containers = page_html.find_all('div', class_ = 'info')

        episode_count = len(episode_containers)
        rating_sum = 0

        for episode in episode_containers:
            rating = episode.find('span', class_='ipl-rating-star__rating').text
            rating_sum += float(rating)

        rating_average[sn] = round((rating_sum / episode_count), 1)
    return rating_average

t = getSeasonAverage(seriesID, 4)

# # For every season in the series-- range depends on the show
# for sn in range(1, seasons+1):
#     # Request from the server the content of the web page by using get(), and store the server’s response in the variable response
#     response = get(query + str(sn))
#     # Parse the content of the request with BeautifulSoup
#     page_html = BeautifulSoup(response.text, 'html.parser')

#     # Select all the episode containers from the season's page
#     episode_containers = page_html.find_all('div', class_ = 'info')

#     episode_count = len(episode_containers)
#     rating_sum = 0

#     # For each episode in each season
#     for episode in episode_containers:
#             # Get the info of each episode on the page
#             season = sn
#             episode_number = episode.meta['content']
#             title = episode.a['title']
#             airdate = episode.find('div', class_='airdate').text.strip()
#             rating = episode.find('span', class_='ipl-rating-star__rating').text

#             rating_sum += float(rating)

#             total_votes = episode.find('span', class_='ipl-rating-star__total-votes').text
#             desc = episode.find('div', class_='item_description').text.strip()
#             # Compiling the episode info
#             episode_data = [season, episode_number, title, airdate, rating, total_votes, desc]

#             # Append the episode info to the complete dataset
#             episodes.append(episode_data)
#     rating_average[sn] = round((rating_sum / episode_count), 1)
    

# # Create panda dataframes
# episodes = pd.DataFrame(episodes, columns=['season', 'episode_number', 'title', 'airdate', 'rating', 'total_votes', 'desc'])
# rating_average = pd.DataFrame.from_dict(rating_average, orient='index')

# # Remove , ( ) from votes
# def remove_str(votes):
#     for r in ((',',''), ('(',''),(')','')):
#         votes = votes.replace(*r)
        
#     return votes

# episodes['total_votes'] = episodes.total_votes.apply(remove_str).astype(int)

# # Parse rating as float
# episodes['rating'] = episodes.rating.astype(float)

# # Parse airdate as datetime
# episodes['airdate'] = pd.to_datetime(episodes.airdate)

# # Save to csv
# episodes.to_csv('Episodes_IMDb_Ratings.csv', index=False)
# rating_average.to_csv('Average_Season_IMD_Ratings.csv', header=False)