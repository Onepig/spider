# -*- coding: cp936 -*-
from bs4 import BeautifulSoup
import urllib2
from httphand import httphand

def downfromurl(url):
            '''r=urllib2.urlopen(url)
            print r.read()
            soup=BeautifulSoup(r.read())
            print soup.title.string'''
            tmp={}
            page=httphand()
            result=page.geturl(url)
            print result['data']
            sop=BeautifulSoup(result['data'])
##            print sop.find_all('a',{'href':True})
            
            '''for string in sop.stripped_strings:
                        print string
                        print '\n'''

# ��ȡ��ҳ���ӵı���
            titles=[]
            for link in sop.findAll("a",{'href':True}):# link ��tag ����
                        try:
                                    string =unicode(link.string)
                                    print string
                                    if string != 'None':
##                                                print link 
                                                print string
                        except:
                                    pass

            
            '''try:
                        title = sop.head.title.string
            except AttributeError:
                        title="NULL"
                        pass
            tmp['response']=result['response']
            tmp['title']=title
            tmp'[url']=url'''
            
            
                        

def get_urls(sop):
            links=[]
            for link in  sop.findAll("a", {'href':True}):
                        links.append(link.get('href'))
            return links


if __name__=='__main__':
##            print downfromurl('http://www.ifeng.com')
            downfromurl('http://www.ifeng.com')
##            get_urls('http://www.ifeng.com')
