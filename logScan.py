from urllib.request import urlopen
import os.path
from os import path

fileRequestsList = []
fileCountList = {

}
#Gets file requests
def fileRequests():
    f = open('local/log.txt', 'r')
    for line in f:
        if "GET" in line:
            line = line.split()
            fileRequestsList.append(line[6])
    f.close()
#Places file requests into dictionary and has each key include a count of occurences
def countFileRequests():
    exists = False
    fileName = ""
    for i in fileRequestsList:
        for key in fileCountList.keys():
            if (i == key):
                exists = True
                fileCountList[key] += 1
            
        if(not exists):
            fileCountList.update({i:1})
        exists = False

#Returns total GET requests
def getGETTotalRequests():
    getRequests = 0
    f = open('local/log.txt', 'r')
    for line in f:
        if "GET" in line:
            getRequests += 1
    f.close()
#Returns total GET requests for the previous year, 1995
def getGETRequestsPrevYear():
    f = open('local/log.txt', 'r')
    for line in f:
        if "GET" in line:
            getRequests += 1
            if "1995" in line:
                getRequestsPrevYear += 1
    f.close()


def getPercentage300():
    get3 = 0
    f = open('local/log.txt', 'r')
    for line in f: 
      items2 = line.split()
      if '302' in items2[-2]:
          get4 += 1
      if '304' in items2[-2]:
          get4 += 1
      f.close
    return(round((get4/len(fileRequestsList))*100))


def getPercentage400():
    get4 = 0
    f = open('local/log.txt', 'r')
    for line in f: 
      items2 = line.split()
      if '403' in items2[-2]:
          get4 += 1
      if '404' in items2[-2]:
          get4 += 1
      f.close
    return(round((get4/len(fileRequestsList))*100))
  

                
#Returns most requested file by finding the index of the max count from the values and indexes it from the list of values
def findMinRequestFile():
    return list(fileCountList.keys())[list(fileCountList.values()).index(max(list(fileCountList.values())))]
#Returns most requested file by finding the index of the min count from the values and indexes it from the list of values
def findMaxRequestFile():
    return list(fileCountList.keys())[list(fileCountList.values()).index(min(list(fileCountList.values())))]





def main():
    #Month names to seperate log file into several monthly log files
    monthNames = ["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    #statusMode is used to update user of application on current stage
    statusMode = "na"
    while(statusMode == "na"):
        statusMode = input("Status mode on (y) or off (n): ")
        if(statusMode == "y"):
            statusMode = True
        elif(statusMode == "n"):
            statusMode == False
        else:
            print("Error: entered invalid input")
        
    #Retrieve log file and write to file
    if(not path.exists('local/log.txt')):
        resourceUrl = urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
        f = open('local/log.txt','w')
        f.write(resourceUrl.read().decode('utf-8'))
        f.close()
    if(statusMode):
        print("Seperating log files into months...")
    #open and append monthly data to corresponding file
    f = open('local/log.txt', 'r')
    
    for line in f:
        for name in monthNames:
            if(name in line):
                monthFile = open((name+'.txt'),'a')
                monthFile.write(line+"")
                monthFile.close()
    f.close()
    print("Done.")
    print("Counting file requests...")
    fileRequests()
    countFileRequests()
    print("Done.")
    optionInput = ""
    while(not optionInput == "9"):
        print("Options for data:\n(1) Total Requests\n(2) Previous Year Requsets\n(3) How many requests were made on each day?\n(4) How many requests were made on a week-by-week basis? Per month? \n(5) What percentage of the requests were not successful (any 4xx status code)?\n(6)What percentage of the requests were redirected elsewhere (any 3xx codes)?\n(7) What was the most-requested file?\n(8)What was the least-requested file?\n(9) Exit\n(Enter the single digit number correlated with the option)")
        optionInput = input()
        if(optionInput == "1"):
            print(getGETTotalRequests())
        if(optionInput == "2"):
            print(getGETRequestsPrevYear())
        if(optionInput == "3"):
            pritn("Average number of requests for a day: ", round(len(fileRequestsList)/365))
        if(optionInput == "4"):
            print("Average number of requests for a month:", round(len(fileRequestsList)/12))
            print("Average number of requests for a week:", round(len(fileRequestsList)/52))
        if(optionInput == "5"):
            print("The percentage of 300-type errors: ",getPercentage300())
        if(optionInput == "6"):
            print("The percentage of 400-type errors: ",getPercentage400())
        if(optionInput == "7"):
            print("The most requested file: ",findMaxRequestFile())
        if(optionInput == "8"):
            print("The least requested file: ", findMinRequestFile())




  
if __name__ == "__main__":
    main()

