"""
    Basic Description: This is a common work on Web scrapping, 
    to allow any new memeber import the module 
    and start scrpping the webpage.
    I used ABC, just to show how to write the abstract classes.
    
    Status: InProgress
"""

import requests,json
from abc import abstractmethod,ABCMeta

class GenericScrapper(object):
    '''
        Don't worry about this class. It is a simple ABC.
        Just to force the child classes to have the basic methods invoked. 
    '''
    __metaclass__ = ABCMeta
    @abstractmethod
    def start_scrapping_method(self,url):
        pass

class HttpbinScrapper(GenericScrapper):
        def __init__(self,url):
            self.url = url

        def start_scrapping_method(self):
            try:
                Handler = requests.get(self.url)
            except requests.ConnectionError as e:
                return False,e
            if Handler.status_code == 200:
                return True,Handler
            else:
                return False,Handler.status_code
            
if __name__=="__main__":
    obj= HttpbinScrapper("http://httpbin.org/ip")
    (stat, data) = obj.start_scrapping_method()
    if stat:
        print "Connection Successful. Getting the complete page below."
        print data.json()
        
    else:
        print "Failed connection."
        