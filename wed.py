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



#percent of requests are 4xx and 3xx
get3 = 0
get4 = 0

#not sure if this line to open file works in your code
for line in open("http3.log"):
    items2 = line.split()
    if '302' in items2[-2]:
        get3 += 1
    if '304' in items2[-2]:
        get3 += 1
    if '403' in items2[-2]:
        get4 += 1
    if '404' in items2[-2]:
        get4 += 1





#print(get3)
#print(get4)

get3final = (get3/726736)*100

get4final = (get4/726736)*100



print(round(get3final,2),"Percent of requests are redirected.") 

print(round(get4final,2),"Percent of requests are not successful.")





