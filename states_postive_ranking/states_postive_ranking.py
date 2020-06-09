import sys
import json
import re

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def create_scores(sent_file):
    scores = {} #init an empty dict
    for line in sent_file:
        term, score = line.split("\t") # files is tab-delimited. "\t"
        scores[term] = int(score)  #convert scores into an int
    return scores

def create_tweets(tweet_file):
    tweets = []
    temp = []
    temp_place = []
    for line in tweet_file:
        tweet = json.loads(line)
        if('place' in tweet and tweet['place']):
            if(tweet['place']['country_code'] == "US"):
                place = tweet['place']['full_name']
                place = place.lower()
                place = place.replace(' ', '')
                place = place.replace('\t', '')
                temp_place = place.split(",") 
                if('text' in tweet):
                    unicode_string = tweet['text']
                    encoded_string = unicode_string.encode('utf-8')
                    encoded_string = encoded_string.lower()
                    encoded_string = encoded_string.replace('\n', '')
                    encoded_string = re.sub('[^a-zA-Z_\s]' , '', encoded_string)
                    temp = encoded_string.split(" ")
                final_temp = [temp , temp_place]
                # print final_temp[0]
                # print final_temp[1]
                tweets.append(final_temp)
    return tweets

def hw(scores, tweets):
    state_list = states
    state_val = {}
    for key in state_list.keys():
        state_val[key] = 0
    for tweet in tweets:
        tweet_score = 0
        for word in tweet[0]:
            s =  str(word)
            if( s in scores):
                tweet_score = tweet_score + scores[str(s)]
        for place in tweet[1]:
            if( place.upper() in state_list.keys() or place.upper() in state_list.values()):
                state_val[place.upper()] = state_val[place.upper()] + tweet_score
                # print place.upper() + " : " + str(tweet_score)
            elif (place.capitalize() in state_list.values()):
                for key, value in state_list.items(): 
                    if place.capitalize() == value: 
                        # print key + " : " + str(tweet_score)
                        state_val[key] = state_val[key] + tweet_score
    states_sent = sorted(state_val.items(), key = lambda kv:(kv[1]), reverse = True)
    # for item in states_sent:
    #     print item
    print states_sent[0][0]
                
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_scores(sent_file)
    tweets = create_tweets(tweet_file)
    states_sent = hw(scores, tweets)


if __name__ == '__main__':
    main()
