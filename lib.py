# -*- coding:utf-8 -*-

import requests
import re
import config

def getWebpage(keyWord) :
    try:
        keyWord.replace(" ", "_")
        page = requests.get("https://en.wikipedia.org/wiki/" + keyWord)
        return page.text

    except Exception:
        print("Error in page : " + keyWord)
        return None

def getLinkAndTitleFromPage(page) :
    return re.findall("<a href=\"/wiki/([0-9a-zA-Z_()%-]*)\" .*?>([0-9a-zA-Z\s()%-]*)</a>", page)

def getMatches(arr) :
    returnArr = []
    for webdata in arr:
        for keyWord in config.relatedTerms:
            if webdata[1].upper().find(keyWord.upper()) != -1 :
                returnArr.append(webdata)
                break
    return returnArr

def savePage(page,pageName) :
    openFile = open(config.saveFolder + "/" + pageName, "w")
    openFile.write(page)
    openFile.close()