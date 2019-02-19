# -*- coding:utf-8 -*-

import lib
import config
import sys
import time

# page = lib.getWebpage(config.seed)
# links = lib.getLinkAndTitleFromPage(page)
# matchesLinks = lib.getMatches(links)
# print(matchesLinks)

pageNum = 0

def run(thisLink,thisWord):
    global pageNum
    if pageNum > config.numberOfPage:
        sys.exit(0)

    pageNum = pageNum + 1

    page = lib.getWebpage(thisLink)

    lib.savePage(page,thisWord)

    links = lib.getLinkAndTitleFromPage(page)
    matchesLinks = lib.getMatches(links)
    for matchesLink in matchesLinks:
        time.sleep(0.1)
        run(matchesLink[0],matchesLink[1])

run("Information_retrieval","Information retrieval")