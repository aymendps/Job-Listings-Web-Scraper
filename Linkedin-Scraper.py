from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('headless')
s = Service(executable_path=r"C:\Users\xxyou\PycharmProjects\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=option)
driver.get("https://www.linkedin.com/jobs/search?keywords=&location=Tunis%2C%20Tunis%2C%20Tunisia&geoId=104991847&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
content = driver.page_source

no_of_jobs = int(driver.find_element(By.CSS_SELECTOR, 'h1>span').get_attribute('innerText'))
i = 2
while i <= int(no_of_jobs/100)+1:
    print(i)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight );")
    i = i + 1
    try:
        driver.find_element(By.XPATH, '/html/body/div/div/main/section/button').click()
        time.sleep(2)
    except:
        pass
        time.sleep(2)

job_lists = driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
jobs = job_lists.find_elements(By.TAG_NAME, 'li')
print(len(jobs))

job_id = []
job_title = []
company_name = []
location = []
date = []
job_link = []
for job in jobs:

    job_id.append(job.get_attribute('data - id'))
    job_title.append(job.find_element(By.CSS_SELECTOR, 'h3').get_attribute('innerText'))
    company_name.append(job.find_element(By.CSS_SELECTOR, 'h4').get_attribute('innerText'))
    location.append(job.find_element(By.CSS_SELECTOR, '[class="job-search-card__location"]').get_attribute('innerText'))
    date.append(job.find_element(By.CSS_SELECTOR, 'div > div > time').get_attribute('datetime'))
    job_link.append(job.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

job_data = pd.DataFrame({
    'ID': job_id,
    'Date': date,
    'Company': company_name,
    'Title': job_title,
    'Location': location,
    'Link': job_link
})
job_data.to_csv("JobListingLinkedin.csv")
