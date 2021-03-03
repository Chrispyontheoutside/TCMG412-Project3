#import log file

import urllib.request

print('Beginning download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log' 

urllib.request.urlretrieve(url, 'http3.log')

#count total requests

COUNT = 0
for line in open("http3.log"):

    COUNT = COUNT +1

print("There are " + str(COUNT) + " total requests.")



#count request made in last year

TOTAL = 0
YEAR = 0


for line in open("http3.log"):

    items = line.split()
    if len(items) < 9:
        continue
    year = items[3].split(':')[0][-4:]
    if year == '1995':
        YEAR += 1
    TOTAL += 1
    
print("There were " + str(YEAR) + " requests made in the past year." )

#import re

import re

logfile = open(http3.log)

pattern = '\[([^:]*):(.*) .*\] \"([A-Z]*) (.*) HTTP.*\" ([2345]\d\d)'

regex = re.compile(pattern)

parts = regex.split(logfile)

