from bs4 import BeautifulSoup
import pandas
import requests

def find_all_jobs():
    url = "https://www.indeed.com/jobs?q=all&l=United%20States"
    jobs_title = []
    companies_name = []
    locations = []
    #Extract Data
    print("INDEED: Scraping all..")
    sum=0
    while sum<=10:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', 'job_seen_beacon')
        sum=sum+1
        for job in jobs:
            job_title = job.find('div', attrs={'class': "heading4 color-text-primary singleLineTitle tapItem-gutter"})
            company_name = job.find('span', attrs={'class': "companyName"})
            location = job.find('div', attrs={'class': "companyLocation"})

            jobs_title.append(job_title.text.strip())
            companies_name.append(company_name.text.strip())
            locations.append(location.text.strip())

        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': "Next"}).get('href')
        except AttributeError:
            break

    #Save result
    df = pandas.DataFrame({"Jobs title": jobs_title, "Company title": companies_name, "Locations": locations})
    df.to_csv("./results/INDEED_A_Results.csv")
    print("INDEED: Finished scraping.")

def find_keyword_jobs(keyword):
    url = "https://www.indeed.com/jobs?q=" + keyword + "&l=United%20States"
    jobs_title = []
    companies_name = []
    locations = []
    #Extract Data
    print("INDEED: Scraping by keyword..")
    sum=0
    while sum<=10:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', 'job_seen_beacon')
        sum=sum+1
        for job in jobs:
            job_title = job.find('div', attrs={'class': "heading4 color-text-primary singleLineTitle tapItem-gutter"})
            company_name = job.find('span', attrs={'class': "companyName"})
            location = job.find('div', attrs={'class': "companyLocation"})

            jobs_title.append(job_title.text.strip())
            companies_name.append(company_name.text.strip())
            locations.append(location.text.strip())

        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': "Next"}).get('href')
        except AttributeError:
            break

    #Save result
    df = pandas.DataFrame({"Jobs title": jobs_title, "Company title": companies_name, "Locations": locations})
    df.to_csv("./results/INDEED_K_Results.csv")
    print("INDEED: Finished scraping.")