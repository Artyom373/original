from selenium import webdriver
# driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
# driver.get('https://coinmarketcap.com')
# p_element = driver.find_element_by_id(id_='intro-text')
# print(p_element.text)

# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
#
# url = "<URL>"
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# with Chrome(options=chrome_options) as browser:
#      browser.get(url)






# from selenium.webdriver import Chrome # pip install selenium
# from selenium.webdriver.chrome.options import Options
#
# url = "http://servername/views/workbookname/dashboard1?:refresh=yes"
#
# #Make it headless i.e. run in backgroud without opening chrome window
# chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# # use Chrome to get page with javascript generated content
# with Chrome(executable_path="./chromedriver", options=chrome_options) as browser:
#      browser.get(url)
#      page_source = browser.page_source