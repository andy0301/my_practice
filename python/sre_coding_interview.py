from collections import Counter
import re

class LogFileWork:
    
    def processLogfile(self, logFileList, limit):
        ipaddressList = []
        for i, line in enumerate(logFileList):
            ipaddressList.append(line.split(" ")[0])
            #print(lineSplit[0])
            
        print(ipaddressList)
        counter = Counter(ipaddressList)
        print(counter)
        
        output = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        print(output)
        
        
        
        topIps =  output[:limit]
        print(topIps)
        
        return topIps
        
            
        

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


logFile = """13.66.139.0 - - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
157.48.153.185 - - [19/Dec/2020:14:08:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 233 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
157.48.153.185 - - [19/Dec/2020:14:08:08 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
216.244.66.230 - - [19/Dec/2020:14:14:26 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" "-"
54.36.148.92 - - [19/Dec/2020:14:16:44 +0100] "GET /index.php?option=com_phocagallery&view=category&id=2%3Awinterfotos&Itemid=53 HTTP/1.1" 200 30662 "-" "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)" "-"
92.101.35.224 - - [19/Dec/2020:14:29:21 +0100] "GET /administrator/index.php HTTP/1.1" 200 4263 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)" "-"
73.166.162.225 - - [19/Dec/2020:14:58:59 +0100] "GET /apache-log/access.log HTTP/1.1" 200 1299 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" "-"
73.166.162.225 - - [19/Dec/2020:14:58:59 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" "-"
54.36.148.108 - - [19/Dec/2020:15:09:30 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)" "-"
54.36.148.1 - - [19/Dec/2020:15:09:31 +0100] "GET /index.php?option=com_phocagallery&view=category&id=2%3Awinterfotos&Itemid=53 HTTP/1.1" 200 30618 "-" "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)" "-"
162.158.203.24 - - [19/Dec/2020:15:16:50 +0100] "GET /apache-log/access.log HTTP/1.1" 200 2164 "-" "-" "-"
35.237.4.214 - - [19/Dec/2020:15:22:40 +0100] "GET /administrator/%22 HTTP/1.1" 404 226 "-" "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)" "-"
42.236.10.125 - - [19/Dec/2020:15:23:10 +0100] "GET / HTTP/1.1" 200 10479 "http://baidu.com/" "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00"""


logFileList = logFile.splitlines()
print(len(logFileList))

logFileWork = LogFileWork()
assert logFileWork.processLogfile(logFileList, 3)  == [('157.48.153.185', 2), ('73.166.162.225', 2), ('13.66.139.0', 1)]


 


# Most frequently accessed IP address in this log file
# tail
# tail -n20 access_log
# tail -c<byte> access_log
# 


def tailLog(logfile, num):
    linePos = 0
    logList = []
    for line in reversed(list(open("filename"))):
        #print(line.rstrip())
        logList.insert(0, line)
        linePos += 1
        if linePos >= num:
            break
    print(logList)
    
    
import os
from filelock import FileLock

def getBlocks(logfile, byteCount):
    logList = []
    with FileLock(logfile):
        fileSize = os.path.getsize(logfile) - 1
        startPos = fileSize - byteCount - 1
        f = open(logfile, 'r')
        f.seek(startPos, fileSize)
        for line in f:
             logList.append(line)  
        f.close()
               
    print(logList)
        
