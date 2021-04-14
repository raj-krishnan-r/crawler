import urllib
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re


def crawler(term):
    query = term.replace(' ','+')

    URL = "https://www.google.com/search?q="+query
    print(URL)

    #
    session = HTMLSession()
    print(session)
    r = session.get(URL)
    print(r.html)
    r.html.render()
    links = r.html.links

    for link in links:
        if re.search("stick=", link):
            print(link)
            #crawler2("https://google.com"+link)

def crawler2(URL):
    print(URL)
    return
    #query = term.replace(' ','+')

    #URL = "https://www.google.com/search?safe=strict&hl=en&tbm=lcl&rflfq=1&num=20&stick=H4sIAAAAAAAAAB2QO27bUBBFoSJBegYpWHEDBub_qd0kgIF4C4RC2UIMU6DkDWUFWVdWkUs1D3jzOXNmvnwehyhPJ4kwru7KaBq_skiaW1GSOGcGUY-DtSBLVeQmpRGtKCUyAMgpSLUqvHkcFHlSAzNMMqTNEPRyS1HTilAKwPf-tGzTtigJSWcrRNWjC_2p4RKZxj4ObZWKbyR6IcUQGNq1LI1SxNXCKHinskMABJLdrkxpHDyZE0hsaSEKhIyDCJeC4aBQJYwxScJDozk6KgSbCCaFskRRtcOhizR3f2nIwVezPe6Xwf5Z7lQkGIwLuncFSjG9IA5adquIxt2_EtpAN85Mwmz3UtkvouhNbFDO_Pdw-Hf49rysl7dlmt-u63Rd5u34Op3W7c8n_b7eLvPx9_SMZ345v79MP95_fVxv23m5Tk9Pj9PD9Lhul3Wbb8v083Q6H5f_ziFFwAACAAA&ved=2ahUKEwi7vuTZ2ubvAhUHilwKHYc8AQsQjHIwJnoECCAQDQ&rldimm=3283034418642762944&q="+query

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    # mobile user-agent
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    for div in soup.find_all('div'):
        if div.has_attr('class'):
            complete_class = " "
            complete_class = complete_class.join(div['class'])
            scopes = []
            if(complete_class=="VkpGBb"):
                try:
                    # all divs having class 
                    companyTitle = (div.a.div.div.div.get_text())
                    # print(div.a.div.div)
                    kiddos = list(div.a.div.span.children)
                    #print(list(kiddos[2])[2].get_text())
                    companyPhone = (kiddos[2].span.string)
                    fileBurner(companyTitle,companyPhone)
                except Exception as e:
                    print(e)

def fileBurner(title,phone):
    f = open("dumpfile.csv","a")
    # f.write(title+"\n"+phone+"\n\n")
    f.write(title+", "+phone+"\n")
    f.close()  

titles = ["A&T DUNGAWALLA","AA WHOLESALES","ABDEIBRAHIMEGGE,UB33BX","AFC FOOD UK LTD","AIM SALES LTD t/a KD wholesale","ALL THINGS NICE VENDING L"]
titles1 = ["ALLEN MARMOT (EUROPEAN) LTD","ALLMAKE MOTOR PARTS LTD","AL-PASHA TRADING LTD","AMBICAN (UK) LTD","ANCHOR PACKAGING","ANGLIAN SWEET AND DRINK C","ANSWERPAK LIMITED"]
titles2 = ["APPLEWADE LTD","AVICA UK LTD","BAGMAN OF CANTLEY","BARTON JONES PACKAGING LI","BLUE JIGSAW LTD","BONUS TRADING UK LIMITED","BRAY DESIGNLTD T/A COPYST"]
titles3 = ["BUNZL UK LTD T/A LEE BROT","CARLTON PACKAGING","CASTLEBAR CATERING SUPPLIES LTD","CATER FOR YOU LTD","CATERED 4 LTD","CFN PACKAGING GROUP LTD","CLEAN SUPPLY LIMITED"]
titles4 = ["CLENA SYSTEMS","COLPAC LTD"]
titles.extend(titles1)
titles.extend(titles2)
titles.extend(titles3)
titles.extend(titles4)

for title in titles:
    print("Triggering -> "+title)
    crawler(title)