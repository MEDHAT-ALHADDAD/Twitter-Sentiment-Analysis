import sys
import json
import re

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

def hw(scores, tweets):
    term_lists = {}  # new terms
    for tweet in tweets:
        tweet_score = 0
        for word in tweet:
            s =  str(word)
            if( s in scores):
                tweet_score = tweet_score + scores[str(s)]
        for word in tweet:
                s =  str(word)
                if( s in term_lists and s not in scores):
                    term_lists[s]['val'] = int(term_lists[s]['val']) + (1 * tweet_score) 
                    term_lists[s]['rep'] = int(term_lists[s]['rep']) + 1
                elif (s == "" or s == "\n" or s == "\t"):
                    pass
                else:
                    term_lists[s] = {'val': tweet_score , 'rep': 1 }
    for key in term_lists.keys():
         print key + " " + str(int(term_lists[key]['val'])/int(term_lists[key]['rep']))
    temp = {}
    for item in term_lists.keys():
        # print item['val']
        # temp[item] = item['val'] / item['rep']
        pass
    # print temp

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_scores(sent_file)
    tweets = create_tweets(tweet_file)
    terms = hw(scores, tweets)
    # print terms
if __name__ == '__main__':
    main()
