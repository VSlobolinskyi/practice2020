from twitter_scraper import get_tweets, get_trends, Profile
from time import time
import csv 

def tweets_to_csv():
    tweet_columns = ['tweetId', 'tweetUrl', 'username', 'userId', 'isRetweet', 'isPinned', 'time', 'text', 'replies', 'retweets', 'likes', 'entries']
    with open('csv_tweets.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=tweet_columns)
        for tweet in get_tweets('elonmusk', pages=10):
            writer.writerow(tweet)
def print_profile_and_trends():
    print(get_trends())
    profile = Profile('vitaliis')
    print(profile.to_dict())
start = time()
tweets_to_csv()
end = time()
print("Execution time", end-start)
print_profile_and_trends()

