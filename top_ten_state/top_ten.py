import sys
import json
import re

def create_hashtags(tweet_file):
    hashtags = []
    for line in tweet_file:
        tweet = json.loads(line)
        if('entities' in tweet):
            for item in tweet['entities']['hashtags']:
                unicode_string = item['text']
                encoded_string = unicode_string.encode('utf-8')
                hashtags.append(encoded_string)
    return hashtags

def hw(hashtags):
    hash_val = {}
    for hashtag in hashtags:
        if( hashtag in hash_val ):
            hash_val[hashtag] = int(hash_val[hashtag]) + 1
        else:
            hash_val[hashtag] = 1
    sorted_hashtags = sorted(hash_val.items(), key = lambda kv:(kv[1]), reverse = True)
    for i in range(10):
        print sorted_hashtags[i][0] + " " + str(sorted_hashtags[i][1])



def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hashtags = create_hashtags(tweet_file)
    top_hashtags = hw(hashtags)


if __name__ == '__main__':
    main()
