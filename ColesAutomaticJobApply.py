from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


#Open chrome browser
options = webdriver.ChromeOptions()

#import current chrome user profile
options.add_argument('user-data-dir=C:\\Users\\Sachet\\AppData\\Local\\Google\\Chrome\\User Data\\Default')

#disable infobar
options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(options=options)

#maximize windows
driver.maximize_window()

#launch coles website
driver.get('https://careers.colesgroup.com.au/')

#scrolling down
driver.execute_script("window.scrollTo(0, 540)")

#click on search jobs
searchJobs = driver.find_element_by_css_selector('#keywordsearch-button')
searchJobs.click()

#check job location
jobLocator = driver.find_elements_by_css_selector('#searchresults > tbody > tr:nth-child(1) > td.colLocation.hidden-phone > span')

#convert job location string into list
a= jobLocator[0].text.strip().replace(',', '')
PostCode = list(a.split(" "))
set_A = set(PostCode)

#list of coles nearby
ColesNearby = ['2135', '2257', '2000', '2137', '2148', '2050', '2023']
set_B = set(ColesNearby)

#check if the list of job location is in the list of coles nearby
check = False if (set_A.intersection(set_B) == set()) else True
if check == True:

    #if true, click on first suburb
    firstSuburb = driver.find_element_by_css_selector('#searchresults > tbody > tr:nth-child(1) > td.colTitle > span > a')
    firstSuburb.click()

    #scroll down and apply now
    driver.execute_script("window.scrollTo(0, 540)")
    firstApply = driver.find_element_by_css_selector('#content > div > div.jobDisplayShell > div > div.content > div.applylink.pull-right > a')
    firstApply.click()

    try:
        #scroll dowmn and wait until username appears and fill-up username and passwords
        driver.execute_script("window.scrollTo(0, 240)")
        formAppear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
         )
        email = driver.find_element_by_id('username')
        email.send_keys('elohistsachet07@gmail.com')
        password = driver.find_element_by_id('password')
        password.send_keys('y-CTy*rChc,N3#E')

    finally:
        #after that, sign-in
        driver.find_element_by_css_selector("#page_content > div:nth-child(7) > div > div > div.round.sfpanel > div > div > table > tbody > tr:nth-child(3) > td > span.aquabtn.active > span > button").send_keys(Keys.ENTER)       
        

    try:
        WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#\35 5\:headerLabel"))
         )        

    finally:
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(2)
    
        driver.execute_script("window.scrollTo(1500,1800);")
        driver.find_element_by_xpath("//*[@id='324:_select']/option[text()='Immediately available']").click()
        driver.find_element_by_xpath("//*[@id='336:_select']/option[text()='No']").click()
        driver.find_element_by_xpath("//*[@id='348:_select']/option[text()='Student Visa']").click()
        
        try:
            WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='352:_select']"))
             )
        finally:
            driver.find_element_by_xpath("//*[@id='352:_select']/option[text()='Restrition 8104']").click()


        driver.find_element_by_xpath("//*[@id='364:_select']/option[text()='No']").click()
       
        Monday = driver.find_element_by_xpath("//*[@id='209:_txtArea']")
        Monday.send_keys('Anytime but prefer Closing or Evening Shift.')

        driver.execute_script("window.scrollTo(2100,2700);")
        Tuesday = driver.find_element_by_xpath("//*[@id='213:_txtArea']/option[text()='No']").click()
        Tuesday.send_keys('Anytime but prefer Closing or Evening Shift.')

        Wednesday = driver.find_element_by_xpath("//*[@id='217:_txtArea']/option[text()='No']").click()
        Wednesday.send_keys('Anytime but prefer Closing or Evening Shift.')

        Thursday = driver.find_element_by_xpath("//*[@id='221:_txtArea']/option[text()='No']").click()
        Thursday.send_keys('Anytime but prefer Closing or Evening Shift.')

        Friday = driver.find_element_by_xpath("//*[@id='225:_txtArea']/option[text()='No']").click()
        Friday.send_keys('Anytime but prefer Closing or Evening Shift.')

        Saturday = driver.find_element_by_xpath("//*[@id='229:_txtArea']/option[text()='No']").click()
        Saturday.send_keys('Anytime but prefer Closing or Evening Shift.')

        Sunday = driver.find_element_by_xpath("//*[@id='233:_txtArea']/option[text()='No']").click()
        Sunday.send_keys('Anytime but prefer Closing or Evening Shift.')

        
else:
    print(check)

   

    #value= "45469"

#candLogin =WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/div/div[1]/div/div[1]/div/div[2]/div/a")))
#ActionChains(driver).move_to_element(candLogin).click(candLogin).perform()

