from bs4 import BeautifulSoup
import requests
import time

print('put some skill that you are not familiar with')
unfamiliar_skills =input('>')
print(f'filtering out {unfamiliar_skills}')

def find_jobs():
  
   cheta_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
   soup = BeautifulSoup(cheta_text,'lxml')

   jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

   for job in jobs:
      published_date=job.find( 'span', class_='sim-posted').span.text
      if 'few' in published_date:
         company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace('','')
         skills =job.find('span', class_= 'srp-skills').text.replace('','')
         more_info =job.header.h2.a['href']
         if unfamiliar_skills not in skills:
    
            print(f"companyname: {company_name.strip()}")
            print(f"required skill:  {skills.strip()}")
            print(f"moreinfo:  {more_info.strip()}")
            print('')

if __name__== '__main__':
   while True:
      find_jobs()
      time_wait =10
      print(f'waiting {time_wait} seconds....')
      time.sleep(time_wait*60)
    















