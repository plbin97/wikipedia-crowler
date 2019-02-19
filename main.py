# -*- coding:utf-8 -*-

import lib
import config
import time
import queue

pageNum = 0

pageQueue = queue.Queue()
pageQueue.put(["Information_retrieval","Information retrieval"])
pageQueue.put(["Search_engine_(computing)","Search engine (computing)"])
crowed = []

while (pageNum < config.numberOfPage) and (not pageQueue.empty()) :

    getValue = pageQueue.get()
    time.sleep(0.1)
    if getValue[0] in crowed:
        print("Crowed")
        continue
    page = lib.getWebpage(getValue[0])
    print(str(pageNum) + " " + getValue[1])
    lib.savePage(page,getValue[1])
    crowed.append(getValue[0])

    links = lib.getLinkAndTitleFromPage(page)
    matchesLinks = lib.getMatches(links)
    pageNum = pageNum + 1
    for matchesLink in matchesLinks:
        pageQueue.put(matchesLink)

