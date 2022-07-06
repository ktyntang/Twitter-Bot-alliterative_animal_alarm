import tweepy
from string import ascii_lowercase
from random import choice
from wonderwords import RandomWord
# from icrawler.builtin import GoogleImageCrawler

def random_letter():
    return choice(ascii_lowercase)


def alliterative_content(letter):

    with open('animals.txt') as myfile:
        animals = myfile.read().splitlines()

    animal_generator = RandomWord(animal=animals)

    w= RandomWord()
    adjective = w.word(starts_with = letter, include_categories=["adjective"])
    verb_1 = w.word(starts_with = letter, include_categories=["verb"])
    verb_2 = w.word(starts_with = letter, include_categories=["verb"])
    animal = animal_generator.word(starts_with = letter)

    content = (
        f'''tick tock! it's {letter.upper()} o'clock!
        {verb_1.upper()} & {verb_2.upper()} MY {adjective.upper()} {animal.upper()}S!'''
        )

    #IMAGE when Twitter V2 API allows it
    # google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\ktynt\Desktop\Py_Projects\twitter_bot'})
    # google_Crawler.crawl(keyword = f'{adjective} {animal}', max_num = 1)
    return content

def post_tweet(content):
    client = tweepy.Client(consumer_key='RGqpj7mID6idhtpklXO219eab', consumer_secret='5sTRD02qtLmAbhruVEnLDny5LegOL3ykRwPevD8Hocx4d0nTh5', access_token='1465738470068871170-1aodaw0786b5a8uDRH1q3ISUzcz0bO', access_token_secret='ddzYusNniUX4oy4PZ1sff25Q6NyPQY2ZdtF1DKkt9Q3Jj')
    client.create_tweet(text = content)

def main():
    post_tweet(alliterative_content(random_letter()))

if __name__ == '__main__':
    main()


