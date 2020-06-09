import sys
import json
import re

def create_tweets(tweet_file):
    tweets = []
    temp = []
    temp_final = []
    for line in tweet_file:
        tweet = json.loads(line)
        if('text' in tweet):
            unicode_string = tweet['text']
            encoded_string = unicode_string.encode('utf-8')
            encoded_string = encoded_string.lower()
            encoded_string = encoded_string.replace('\n', '')
            encoded_string = re.sub('[^a-zA-Z_\s]' , '', encoded_string)
            temp = encoded_string.split(" ")
        tweets.append(temp)
    return tweets

def hw( tweets ):
    total = 0
    term_lists = {}  # new terms
    for tweet in tweets:
        for word in tweet:
            s =  str(word)
            if( s in term_lists):
                term_lists[s]['rep'] = int(term_lists[s]['rep']) + 1
                total = total + 1
            elif (s == "" or s == "\n" or s == "\t"):
                pass
            else:
                term_lists[s] = {'rep': 1 }
                total = total + 1
    # freq = no of reptiontions ina all tweets / no of reptions of all terms ina all tweets
    for key in term_lists.keys():
         print key + " " + str(float(term_lists[key]['rep'])/total)
    
def main():
    tweet_file = open(sys.argv[1])
    tweets = create_tweets(tweet_file)
    hw( tweets )

if __name__ == '__main__':
    main()
