from requests_html import HTMLSession
import re

def crawler(token):
    session = HTMLSession()
    request = session.get("https://google.com/search?q="+token)
    for link in request.html.links:
        if re.search("stick=",link):
            crawler2("https://google.com"+link)

def crawler2(url):
    session = HTMLSession()
    request = session.get(url)
    for root in (request.html.find('.cXedhc')):
        try:
            ele = root.find('.dbg0pd')[0]
            print(ele.text)
            #for title in root.find('.dbg0pd'):
            #print(title.find('div')[0].text)
            #for phone in root.find('rllt__details'):
            #print(phone.text)
            fileBurner(ele.text,re.search("\+([0-9]*\s)*",root.find('.rllt__details')[0].text).group(0))
        except Exception as e:
            print(e)


titles = ["A&T DUNGAWALLA","AA WHOLESALES","ABDEIBRAHIMEGGE,UB33BX","AFC FOOD UK LTD","AIM SALES LTD t/a KD wholesale","ALL THINGS NICE VENDING L"]
titles1 = ["ALLEN MARMOT (EUROPEAN) LTD","ALLMAKE MOTOR PARTS LTD","AL-PASHA TRADING LTD","AMBICAN (UK) LTD","ANCHOR PACKAGING","ANGLIAN SWEET AND DRINK C","ANSWERPAK LIMITED"]
titles2 = ["APPLEWADE LTD","AVICA UK LTD","BAGMAN OF CANTLEY","BARTON JONES PACKAGING LI","BLUE JIGSAW LTD","BONUS TRADING UK LIMITED","BRAY DESIGNLTD T/A COPYST"]
titles3 = ["BUNZL UK LTD T/A LEE BROT","CARLTON PACKAGING","CASTLEBAR CATERING SUPPLIES LTD","CATER FOR YOU LTD","CATERED 4 LTD","CFN PACKAGING GROUP LTD","CLEAN SUPPLY LIMITED"]
titles4 = ["CLENA SYSTEMS","COLPAC LTD"]
titles.extend(titles1)
titles.extend(titles2)
titles.extend(titles3)
titles.extend(titles4)


def fileBurner(title,phone):
    f = open("dumpfile.csv","a")
    # f.write(title+"\n"+phone+"\n\n")
    f.write(title+", "+phone+"\n")
    f.close()  

for title in titles:
    print("Triggering -> "+title)
    crawler(title)
