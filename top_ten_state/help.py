import sys
import json
import re


def create_tweets(tweet_file):
    tweets = []
    for line in tweet_file:
        tweet = json.loads(line)
        tweets.append(tweet)
    return tweets

def main():
    tweet_file = open(sys.argv[1])
    tweets = create_tweets(tweet_file)
    for key in tweets[5]:
        print key  
if __name__ == '__main__':
    main()
    

{
    "created_at":"Sun Aug 16 21:41:13 +0000 2015",
    "id":633030779610775552,
    "id_str":"633030779610775552",
    "text":"RT @oihanamarre: PTDDDDDDDDR LE PAUVRE http:\/\/t.co\/HUvnDpgggb",
    "source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e",
    "truncated":false,
    "in_reply_to_status_id":null,
    "in_reply_to_status_id_str":null,
    "in_reply_to_user_id":null,
    "in_reply_to_user_id_str":null,
    "in_reply_to_screen_name":null,
    "user":{
        "id":991387886,
        "id_str":"991387886",
        "name":"bellamy",
        "screen_name":"osnapitzlvn",
        "location":"solene  #c",
        "url":"https:\/\/vine.co\/v\/OJ9aQxIAL1E",
        "description":"just another name of silly kids in another nation 2\/5",
        "protected":false,
        "verified":false,
        "followers_count":2718,
        "friends_count":434,
        "listed_count":23,
        "favourites_count":59339,
        "statuses_count":68413,
        "created_at":"Wed Dec 05 17:18:37 +0000 2012",
        "utc_offset":7200,
        "time_zone":"Amsterdam",
        "geo_enabled":true,
        "lang":"fr",
        "contributors_enabled":false,
        "is_translator":false,
        "profile_background_color":"343838",
        "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/498782324847149056\/ZuT219W-.jpeg",
        "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/498782324847149056\/ZuT219W-.jpeg",
        "profile_background_tile":true,
        "profile_link_color":"E3D496",
        "profile_sidebar_border_color":"FFFFFF",
        "profile_sidebar_fill_color":"F6F6F6",
        "profile_text_color":"333333",
        "profile_use_background_image":true,
        "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/629660936534663168\/20RVP1ZK_normal.jpg",
        "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/629660936534663168\/20RVP1ZK_normal.jpg",
        "profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/991387886\/1439546205",
        "default_profile":false,
        "default_profile_image":false,
        "following":null,
        "follow_request_sent":null,
        "notifications":null},
        "geo":null,
        "coordinates":null,
        "place":null,
        "contributors":null,
        "retweeted_status":{
            "created_at":"Tue Jun 09 17:45:12 +0000 2015",
            "id":608329009500459009,
            "id_str":"608329009500459009",
            "text":"PTDDDDDDDDR LE PAUVRE http:\/\/t.co\/HUvnDpgggb",
            "source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e",
            "truncated":false,
            "in_reply_to_status_id":null,
            "in_reply_to_status_id_str":null,
            "in_reply_to_user_id":null,
            "in_reply_to_user_id_str":null,
            "in_reply_to_screen_name":null,
            "user":{
                "id":983185040,
                "id_str":"983185040",
                "name":"sorgina",
                "screen_name":"oihanamarre",
                "location":"fb:oihanamarre;snap:oihanaplus",
                "url":"https:\/\/www.youtube.com\/channel\/UC4XTTXX0PbWyvDTL5k-WONg",
                "description":"Oi ! Youtubeuse bizarre... ptetre une artiste tt s'que vous faites pas, j'laurai fait.. sinn j'aime la baston POGO #antiFa #FhaiNe #keuponne",
                "protected":false,
                "verified":false,
                "followers_count":1652,
                "friends_count":825,
                "listed_count":12,
                "favourites_count":14134,
                "statuses_count":81342,
                "created_at":"Sat Dec 01 19:29:25 +0000 2012",
                "utc_offset":7200,
                "time_zone":"Amsterdam",
                "geo_enabled":true,
                "lang":"fr",
                "contributors_enabled":false,
                "is_translator":false,
                "profile_background_color":"8B542B",
                "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/605302214865907712\/ZgOGRMou.jpg",
                "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/605302214865907712\/ZgOGRMou.jpg",
                "profile_background_tile":true,
                "profile_link_color":"000000",
                "profile_sidebar_border_color":"000000",
                "profile_sidebar_fill_color":"DDEEF6",
                "profile_text_color":"333333",
                "profile_use_background_image":true,
                "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/617672195028946944\/9Wo9hiM__normal.jpg",
                "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/617672195028946944\/9Wo9hiM__normal.jpg",
                "profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/983185040\/1435267361",
                "default_profile":false,
                "default_profile_image":false,
                "following":null,
                "follow_request_sent":null,
                "notifications":null
            },
            "geo":null,
            "coordinates":null,
            "place":{
                "id":"5d97230e9480f783",
                "url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/5d97230e9480f783.json",
                "place_type":"city",
                "name":"Saint-Vincent-de-Tyrosse",
                "full_name":"Saint-Vincent-de-Tyrosse, Aquitaine",
                "country_code":"FR",
                "country":"France",
                "bounding_box":{
                    "type":"Polygon",
                    "coordinates":[
                        [
                            [-1.3359115,43.6343639],
                            [-1.3359115,43.6915002],
                            [-1.2665497,43.6915002],
                            [-1.2665497,43.6343639]
                        ]
                    ]
                },
                "attributes":{

                }
            },
            "contributors":null,
            "retweet_count":176,
            "favorite_count":52,
            "entities":{
                "hashtags":[],
                "trends":[],
                "urls":[],
                "user_mentions":[],
                "symbols":[],
                "media":[
                    {
                    "id":608328997274021888,
                    "id_str":"608328997274021888",
                    "indices":[22,44],
                    "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                    "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                    "url":"http:\/\/t.co\/HUvnDpgggb",
                    "display_url":"pic.twitter.com\/HUvnDpgggb",
                    "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
                    "type":"photo",
                    "sizes":{
                        "small":{"w":340,"h":330,"resize":"fit"},
                        "thumb":{"w":150,"h":150,"resize":"crop"},
                        "medium":{"w":600,"h":583,"resize":"fit"},
                        "large":{"w":639,"h":621,"resize":"fit"}
                        }
                    }
                ]
            },"extended_entities":{
                "media":[
                    {"id":608328997274021888,
                    "id_str":"608328997274021888",
                    "indices":[22,44],
                    "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                    "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                    "url":"http:\/\/t.co\/HUvnDpgggb",
                    "display_url":"pic.twitter.com\/HUvnDpgggb",
                    "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
                    "type":"photo",
                    "sizes":{
                        "small":{"w":340,"h":330,"resize":"fit"},
                        "thumb":{"w":150,"h":150,"resize":"crop"},
                        "medium":{"w":600,"h":583,"resize":"fit"},
                        "large":{"w":639,"h":621,"resize":"fit"}
                        }
                    }
                ]
            },
            "favorited":false,
            "retweeted":false,
            "possibly_sensitive":false,
            "filter_level":"low","lang":"fr"
        },
        "retweet_count":0,
        "favorite_count":0,
        "entities":{
            "hashtags":[],
            "trends":[],
            "urls":[],
            "user_mentions":
            [
                {"screen_name":"oihanamarre",
                "name":"sorgina",
                "id":983185040,
                "id_str":"983185040",
                "indices":[3,15]
                }
            ],
            "symbols":[],
            "media":
            [
                {"id":608328997274021888,
                "id_str":"608328997274021888",
                "indices":[39,61],
                "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
                "url":"http:\/\/t.co\/HUvnDpgggb",
                "display_url":"pic.twitter.com\/HUvnDpgggb",
                "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
                "type":"photo",
                "sizes":{
                    "small":{"w":340,"h":330,"resize":"fit"},
                    "thumb":{"w":150,"h":150,"resize":"crop"},
                    "medium":{"w":600,"h":583,"resize":"fit"},
                    "large":{"w":639,"h":621,"resize":"fit"}
                },
                "source_status_id":608329009500459009,
                "source_status_id_str":"608329009500459009"
            }
        ]
    },
    "extended_entities":{
        "media":
        [
            {"id":608328997274021888,
            "id_str":"608328997274021888",
            "indices":[39,61],
            "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "url":"http:\/\/t.co\/HUvnDpgggb",
            "display_url":"pic.twitter.com\/HUvnDpgggb",
            "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
            "type":"photo",
            "sizes":{
                "small":{"w":340,"h":330,"resize":"fit"},
                "thumb":{"w":150,"h":150,"resize":"crop"},
                "medium":{"w":600,"h":583,"resize":"fit"},
                "large":{"w":639,"h":621,"resize":"fit"}
            },
            "source_status_id":608329009500459009,
            "source_status_id_str":"608329009500459009"
        }
    ]},
    "favorited":false,
    "retweeted":false,
    "possibly_sensitive":false,
    "filter_level":"low",
    "lang":"fr",
    "timestamp_ms":"1439761273659"
}



"created_at":"Tue Jun 09 17:45:12 +0000 2015",
    "id":608329009500459009,
    "id_str":"608329009500459009",
    "text":"PTDDDDDDDDR LE PAUVRE http:\/\/t.co\/HUvnDpgggb",
    "source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e",
    "truncated":false,
    "in_reply_to_status_id":null,
    "in_reply_to_status_id_str":null,
    "in_reply_to_user_id":null,
    "in_reply_to_user_id_str":null,
    "in_reply_to_screen_name":null,
    "user":{
        "id":983185040,
        "id_str":"983185040",
        "name":"sorgina",
        "screen_name":"oihanamarre",
        "location":"fb:oihanamarre;snap:oihanaplus",
        "url":"https:\/\/www.youtube.com\/channel\/UC4XTTXX0PbWyvDTL5k-WONg",
        "description":"Oi ! Youtubeuse bizarre... ptetre une artiste tt s'que vous faites pas, j'laurai fait.. sinn j'aime la baston POGO #antiFa #FhaiNe #keuponne",
        "protected":false,
        "verified":false,
        "followers_count":1652,
        "friends_count":825,
        "listed_count":12,
        "favourites_count":14134,
        "statuses_count":81342,
        "created_at":"Sat Dec 01 19:29:25 +0000 2012",
        "utc_offset":7200,
        "time_zone":"Amsterdam",
        "geo_enabled":true,
        "lang":"fr",
        "contributors_enabled":false,
        "is_translator":false,
        "profile_background_color":"8B542B",
        "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/605302214865907712\/ZgOGRMou.jpg",
        "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/605302214865907712\/ZgOGRMou.jpg",
        "profile_background_tile":true,
        "profile_link_color":"000000",
        "profile_sidebar_border_color":"000000",
        "profile_sidebar_fill_color":"DDEEF6",
        "profile_text_color":"333333",
        "profile_use_background_image":true,
        "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/617672195028946944\/9Wo9hiM__normal.jpg",
        "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/617672195028946944\/9Wo9hiM__normal.jpg",
        "profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/983185040\/1435267361",
        "default_profile":false,
        "default_profile_image":false,
        "following":null,
        "follow_request_sent":null,
        "notifications":null
    },
    "geo":null,
    "coordinates":null,
    "place":{
        "id":"5d97230e9480f783",
        "url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/5d97230e9480f783.json",
        "place_type":"city",
        "name":"Saint-Vincent-de-Tyrosse",
        "full_name":"Saint-Vincent-de-Tyrosse, Aquitaine",
        "country_code":"FR",
        "country":"France",
        "bounding_box":{
            "type":"Polygon",
            "coordinates":[
                [
                    [-1.3359115,43.6343639],
                    [-1.3359115,43.6915002],
                    [-1.2665497,43.6915002],
                    [-1.2665497,43.6343639]
                ]
            ]
        },
        "attributes":{

        }
    },
    "contributors":null,
    "retweet_count":176,
    "favorite_count":52,
    "entities":{
        "hashtags":[],
        "trends":[],
        "urls":[],
        "user_mentions":[],
        "symbols":[],
        "media":[
            {
            "id":608328997274021888,
            "id_str":"608328997274021888",
            "indices":[22,44],
            "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "url":"http:\/\/t.co\/HUvnDpgggb",
            "display_url":"pic.twitter.com\/HUvnDpgggb",
            "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
            "type":"photo",
            "sizes":{
                "small":{"w":340,"h":330,"resize":"fit"},
                "thumb":{"w":150,"h":150,"resize":"crop"},
                "medium":{"w":600,"h":583,"resize":"fit"},
                "large":{"w":639,"h":621,"resize":"fit"}
                }
            }
        ]
    },"extended_entities":{
        "media":[
            {"id":608328997274021888,
            "id_str":"608328997274021888",
            "indices":[22,44],
            "media_url":"http:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "media_url_https":"https:\/\/pbs.twimg.com\/media\/CHE3__0WcAA52EJ.jpg",
            "url":"http:\/\/t.co\/HUvnDpgggb",
            "display_url":"pic.twitter.com\/HUvnDpgggb",
            "expanded_url":"http:\/\/twitter.com\/oihanamarre\/status\/608329009500459009\/photo\/1",
            "type":"photo",
            "sizes":{
                "small":{"w":340,"h":330,"resize":"fit"},
                "thumb":{"w":150,"h":150,"resize":"crop"},
                "medium":{"w":600,"h":583,"resize":"fit"},
                "large":{"w":639,"h":621,"resize":"fit"}
                }
            }
        ]
    },
    "favorited":false,
    "retweeted":false,
    "possibly_sensitive":false,
    "filter_level":"low","lang":"fr"