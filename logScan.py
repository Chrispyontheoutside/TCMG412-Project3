import urllib.request
import os.path
from os import paths
def main():
    getRequests = 0
    getRequestsPrevYear = 0
    if(not path.exists('local/log.txt')):
        resourceUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
        data = resourceUrl.read()
        f = open('local/log.txt','w')
        f.write(data)
        f.close
    f = open('local/log.txt', 'r')
    for line in f:
        if "GET" in line:
            getRequests += 1
            if "1995" in line:
                getRequestsPrevYear += 1
    print("Total GET requests: ",getRequests)
    print("GET requests from 1995: ",getRequestsPrevYear)

if __name__ == "__main__":
    main()
