from bs4 import BeautifulSoup
import urllib2

def downfromurl(url):
            r=urllib2.urlopen(url)
            print r.read()




if __name__=='__main__':
            downfromurl('http://www.baidu.com')
            
