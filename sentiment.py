import tweepy
from textblob import TextBlob

def connectTwitterAPI():

	consumer_key = ''
	consumer_secret = ''

	access_token = ''
	access_token_secret = ''

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def analyse(tweets):
	analysis = []
	for tweet in tweets:
		analysis.append(TextBlob(tweet.text))
	return analysis

def main():
	api = connectTwitterAPI()

	phrase = input("What subject would you like to analyse? ")
	tweets = api.search(phrase)

	analysis = analyse(tweets)

	for tweet in analysis:
		print(tweet)
		print(tweet.sentiment)
		print()

main()