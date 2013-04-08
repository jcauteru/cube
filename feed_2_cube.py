from pymongo import Connection as connect
from random import randint
import tweetstream, urllib2, json, time


#con = connect("localhost", 27017)
twitter_username =  'MYUSRN'
#my_collection = con.twitter_bd.tweets

url = 'http://localhost:1080/1.0/event/put'
out = 'http://localhost:1081/1.0/metric/out'

with tweetstream.SampleStream('MYUSRN', 'MYPASWRD') as stream:
    for doc in stream:
        #x = json.dumps([{"type": 'tweets', "data":{"rand":randint(0,30)}}])##   #type var name of underlying mongo db
        x = json.dumps([{"type": 'tweet2', "time": time.time(), "data":{"rand": randint(0,10)}}])
        #data = urllib.urlencode(x)
        req = urllib2.Request(url, x)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page