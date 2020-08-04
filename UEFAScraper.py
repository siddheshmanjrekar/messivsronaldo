# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:35:28 2020
@author: Sid Pc
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def run(url):
    fw= open('goals.txt','w')
    html= None
    pageLink=url
    
    for i in range(5):
            try:
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content
                break
            except Exception as e:
                print ('failed attempt',i,e)
                time.sleep(2) 
                
    soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
    
    reviews= soup.find('tbody')

    for x in reviews.findAll('td'):
        i+= 1
        text= ""
        if(x.text.strip()== ''):
            text= "N/A"
        else:
            text= x.text
        
        if(i%5==0):
            fw.write(text + "\n")
        else:
            fw.write(text + ",")
        
    fw.close()

if __name__=='__main__':
    url='https://www.uefa.com/uefachampionsleague/news/0252-0cda365e6b04-04063053215a-1000--messi-vs-ronaldo-goal-for-goal/'
    run(url)