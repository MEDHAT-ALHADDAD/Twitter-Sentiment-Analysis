import sys
import json

def create_scores(sent_file):
    scores = {} #init an empty dict
    for line in sent_file:
        term, score = line.split("\t") # files is tab-delimited. "\t"
        scores[term] = int(score)  #convert scores into an int
    # print scores
    return scores

def create_tweets(tweet_file):
    tweets = []
    temp = []
    for line in tweet_file:
        tweet = json.loads(line)
        if('text' in tweet):
            unicode_string = tweet['text']
            encoded_string = unicode_string.encode('utf-8')
            temp = encoded_string.split(" ") 
        tweets.append(temp)
    return tweets

def hw(scores, tweets):
    tweet_scores = []
    for tweet in tweets:
        tweet_score = 0
        for word in tweet:
            s =  str(word)
            if( s in scores):
                tweet_score = tweet_score + scores[str(s)]
        tweet_scores.append(tweet_score)
    return tweet_scores
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_scores(sent_file)
    tweets = create_tweets(tweet_file)
    tweets_scores = hw(scores, tweets)
    for score in tweets_scores:
        print score
if __name__ == '__main__':
    main()
