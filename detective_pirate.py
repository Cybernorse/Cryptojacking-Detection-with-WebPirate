import requests
from bs4 import BeautifulSoup
from urllib.request import urlparse,urljoin
import sys
import colorit
import argparse
import time 
import json
import difflib
import proxyscrape
import os

class cryptjack_detection:
    def __init__(self, *args, **kwargs):    
        self.internal_links=set()
        self.external_links=set()
        self.visited_links=[]
        self.proxy_app=[]
        self.proxy_dict={}
        self.protocol='https'
        self.url_count=1
        self.headers = {    

                    "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                    "User-agent":"Mozilla/5.0 (Linux NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
                }
        self.cookies={'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
        
        with open("{0}/seed.txt".format(os.getcwd()) , "r") as o_seed:
            take_seed=o_seed.read()
        self.parent_url=str(take_seed)
        print(colorit.color_front("[:%:] Crawler Engine Activated [:%:]",red=0,green=200,blue=200))
        print(colorit.color_front(f"[:%:] target : {self.parent_url} [:%:]",red=250,green=10,blue=10))
        print(colorit.color_front("[:%:] Activating Proxy... [:%:]",red=0,green=200,blue=200))
        print(colorit.color_back("[NOTE] :: It will take time depending on the website",red=250,green=10,blue=10))
        print(colorit.color_front("[:%:] Locating All the EndPoints [:%:]",red=0,green=200,blue=200),'\n')
        # "https://emobeginner.blogspot.com/"   
         
    def proxy(self):
        # self.collect_proxy=proxyscrape.create_collector('my-collection',[self.protocol])

        try:
            self.collect_proxy =proxyscrape.get_collector('proxy')
        except proxyscrape.errors.CollectorNotFoundError:
            self.collect_proxy = proxyscrape.create_collector('proxy', 'https')

        self.getproxy=self.collect_proxy.get_proxy({'code':('us','uk'),'anonymous':True})
            
        self.proxy_dict[self.getproxy[5]]=self.getproxy[0]+':'+self.getproxy[1]

        self.session=requests.Session()
        self.session.proxies=self.proxy_dict.values()

    def send_request(self):          #sending request and getting a domain 
        self.proxy()
        self.entry_point=self.parent_url 
        try :
            self.s_requests=self.session.get(self.entry_point,headers=self.headers,cookies=self.cookies)
        except:
            print(colorit.color_front(f"[:%:] {self.parent_url} was able to abort the connection or connection problem occured [:%:]",red=250,green=10,blue=10))
            self.get_cryptojacking()

        self.domain_name = urlparse(self.entry_point).netloc
        
        if self.domain_name.count('.')==2:
            self.dom1=self.domain_name[1+self.domain_name.index('.'):]
            self.dom2=self.dom1[:self.dom1.index('.')]
            
        if self.domain_name.count('.')==1:
            self.dom2=self.domain_name[:self.domain_name.index('.')]
        
    def extract_urls(self):   
        self.list_urls=[]                                #extracting links
        self.links=BeautifulSoup(self.s_requests.text,"lxml")
        for link in self.links.find_all('a'):
            self.urls=link.attrs.get('href')
            self.urls=urljoin(self.entry_point,self.urls)
            self.list_urls.append(self.urls)
    
    def evaluate_links(self):               #evaluate the internal and external links  
        for eval_url in self.list_urls:
            self.domains=urlparse(eval_url).netloc
            
            if self.domains.count('.')==2:
                doma1=self.domains[1+self.domains.index('.'):]
                self.sub_domains=doma1[:doma1.index('.')]
            
            if self.domains.count('.')==1:
                self.sub_domains=self.domains[:self.domains.index('.')]
            
            if self.dom2==self.sub_domains:
                self.internal_links.add(eval_url)
                
            else :
                self.external_links.add(eval_url)

        self.internal_links.discard('javascript:void(0)')
        self.internal_links.discard('javascript:;')
        self.external_links.discard('javascript:void(0)')
        self.external_links.discard('javascript:;')

    def iframe_ads(self):
        iframe=BeautifulSoup(self.s_requests.text,'lxml')
        for i in iframe.find_all('iframe'):
            ads=i.attrs.get('src')
            ads=urljoin(self.entry_point,ads)
            self.external_links.add(ads)

    def videos_ads(self):
        v_ads=BeautifulSoup(self.s_requests.text,'lxml')
        for i in v_ads.find_all('video'):
            va=i.attrs.get('src')
            va=urljoin(self.entry_point,va)
            self.external_links.add(va)

    def image_ads(self):
        i_ads=BeautifulSoup(self.s_requests.text,'lxml')
        for i in i_ads.find_all('img'):
            ia=i.attrs.get('src')
            ia=urljoin(self.entry_point,ia)
            self.external_links.add(ia)

    def next_url(self):
        self.parent_url=''
        
        try:
            self.parent_url=self.internal_links.pop()
        except:
            print(colorit.color_front(f"[!!] No Internal links found at this URL {self.entry_point}",red=250,green=10,blue=10))

            if self.external_links:
                print(colorit.color_front("\n[:%:] External Links Located {0}[:%:]".format(len(self.external_links)),red=0,green=200,blue=200))
                self.get_cryptojacking()
                print("Exiting")
                sys.exit()

        self.url_count+=1
        print(colorit.color_front(self.parent_url,red=0,green=300,blue=0))
        # print(self.url_count,sum(1 for i in self.internal_links))

        self.visited_links.append(self.parent_url)
        for i in self.visited_links:
            if i in self.internal_links:
                self.internal_links.discard(i)
        
        if not self.internal_links:
            print(colorit.color_front("\n[:%:] External Links Located {0} [:%:]".format(len(self.external_links)),red=0,green=200,blue=200))
            self.get_cryptojacking()
            print("Exiting")
            sys.exit()

    def get_cryptojacking(self):
        print(colorit.color_front("[:%:] All EndPoints Located [:%:]",red=0,green=200,blue=200))
        print(colorit.color_front("[:%:] Detecting Cryptojacking Malware [:%:]",red=0,green=200,blue=200))
        self.take_db=[]
        self.results=[]
        with open("{0}/dark_db.json".format(os.getcwd())) as json_big:
            data=json.load(json_big)
        for i in data:
            self.take_db.append(str(data[i]))
        
        for target in self.external_links:
            if target in self.take_db:
                self.results.append(target)
        
        print(":: Result ::")
        if not self.results:
            print(colorit.color_front("[:%:] No Cryptojacking Malware Detected at {0} [:%:]".format(self.entry_point),red=0,green=200,blue=200))
        else:
            for i in target:
                print(i)




    def core_engine(self):
        while True:
            crypt_obj.send_request()
            crypt_obj.extract_urls()
            crypt_obj.evaluate_links()
            crypt_obj.iframe_ads()
            crypt_obj.videos_ads()
            crypt_obj.image_ads()
            crypt_obj.next_url()

class cla_pirate(cryptjack_detection):
    def __init__(self):
        cla=argparse.ArgumentParser(description="This is web pirtate",prog='webpirate')
        cla.add_argument('URL',help='https://www.webpirate.com || http://webpirate.com')

        self.args=cla.parse_args()

    def parse_cla(self):
        global crypt_obj
        check_url=urlparse(self.args.URL)
        print(colorit.color_front("\n[:%:] Checking Seed URL [:%:]",red=0,green=200,blue=200))
        if (check_url.scheme and check_url.netloc) or check_url.params or check_url.password or check_url.path or check_url.port or check_url.query or check_url.username :
            with open("{0}/seed.txt".format(os.getcwd()),"w") as o_seed:
                o_seed.write(str(self.args.URL))
            print(colorit.color_front("OK",red=0,green=200,blue=200))
            crypt_obj=cryptjack_detection()
            crypt_obj.core_engine()

        else:
            print(colorit.color_front(f"[!!] Invalid URL schema || {self.args.URL}",red=250,green=10,blue=10))


if __name__=='__main__':
    obj=cla_pirate()
    obj.parse_cla()


