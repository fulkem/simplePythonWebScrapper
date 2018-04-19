# -*- coding: utf-8 -*-
from urllib.request import urlopen
import urllib.response
import re
from bs4 import BeautifulSoup

def get_details(packageName):
    link="http://screenshots.debian.net/package/"
    link1=link+packageName
    page = urlopen(link1)
    soup1 = BeautifulSoup(page,"html.parser").find_all(class_="bigpanel")
    soup = soup1[0].get_text()
    splittedSoup=soup.split(" ")
    text=""
    for s in splittedSoup[2:]:
        if (s=='Upload'):
            break
        if (len(s.split("\n")) != 1):
            for t in s.split("\n"):
                text+=t
                text+=" "
            continue
        text+=s
        text+=" "
    return text

def get_stats(packageName):
    link="http://screenshots.debian.net/package/"
    link1=link+packageName
    page = urlopen(link1)
    flag=0
    soup1 = BeautifulSoup(page,"html.parser").find_all(class_="bigpanel")[0].get_text()
    text=""
    if "Statistics" in soup1:
        for s in soup1.split(" "):
            if (s!="Statistics" and flag==0):
                continue
            else:
                if (len(s.split("\n")) != 1):
                    for t in s.split("\n"):
                        text += t
                        text += " "
                    continue
                flag=1
                text+=s
                text+=" "
    else:
        return "No statistics available"
    return text[11:]

print(get_stats("goplay"))
print(get_details("goplay"))


