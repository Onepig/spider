from bs4 import BeautifulSoup
import urllib2

def downfromurl(url):
            r=urllib2.urlopen(url)
            soup=BeautifulSoup(r.read())
##            print soup.title.string
            return soup.title.string




if __name__=='__main__':
            downfromurl('http://www.baidu.com')
            
