from selenium import webdriver

website_url = 'https://google.com'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get(website_url)

driver.quit()

