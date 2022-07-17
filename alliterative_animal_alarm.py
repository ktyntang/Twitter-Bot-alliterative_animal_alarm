from string import ascii_lowercase
from random import choice
from wonderwords import RandomWord
import tweepy
# from icrawler.builtin import GoogleImageCrawler

client = tweepy.Client(
            bearer_token = 'AAAAAAAAAAAAAAAAAAAAAD9leQEAAAAAY7ktUuHP5cdsxSspLB6jgSxdvNk%3DtZbwf3ir8TkuaEJ83HcIDVqTfLrCD1K0613fzwhCq0BGYXB0xk',
            consumer_key = 'RGqpj7mID6idhtpklXO219eab',
            consumer_secret = '5sTRD02qtLmAbhruVEnLDny5LegOL3ykRwPevD8Hocx4d0nTh5',
            access_token = '1465738470068871170-1aodaw0786b5a8uDRH1q3ISUzcz0bO',
            access_token_secret = 'ddzYusNniUX4oy4PZ1sff25Q6NyPQY2ZdtF1DKkt9Q3Jj')


def letter_picker():

    tweets = client.get_users_tweets(id='1465738470068871170', max_results = 5)
    recent_letters = [tweet.text[16].lower() for tweet in tweets.data]
    new_letter = choice([l for l in ascii_lowercase if l not in recent_letters])

    return new_letter
   

def alliterative_content(letter):

    with open('animals.txt','r') as myfile:
        animals = myfile.read().splitlines()

    animal_generator = RandomWord(animal=animals)
    animal = animal_generator.word(starts_with = letter)

    rw= RandomWord()
    adjective = rw.word(starts_with = letter, include_categories=["adjective"])
    verb_1 = rw.word(starts_with = letter, include_categories=["verb"])
    verb_2 = rw.word(starts_with = letter, include_categories=["verb"])

    while verb_1 == verb_2:
        verb_2 = rw.word(starts_with = letter, include_categories=["verb"])

    content = (
        f'''tick tock! it's {letter.upper()} o'clock!
        {verb_1.upper()} & {verb_2.upper()} MY {adjective.upper()} {animal.upper()}S!'''
        )

    #IMAGE when Twitter V2 API allows it
    # google_Crawler = GoogleImageCrawler(
    # storage = {'root_dir': r'C:\Users\ktynt\Desktop\Py_Projects\twitter_bot'}
    # )
    # google_Crawler.crawl(keyword = f'{adjective} {animal}', max_num = 1)
    return content

def post_tweet():
    content = alliterative_content(letter_picker())
    client.create_tweet(text = content)

if __name__ == '__main__':
    post_tweet()
    print('tweet tweet!')
