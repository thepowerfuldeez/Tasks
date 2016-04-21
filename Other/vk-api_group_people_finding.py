from selenium import webdriver
from time import sleep as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://vk.com/search?c%5Bgroup%5D=40390768&c%5Bsection%5D=people"

driver = webdriver.Chrome("/Users/george/Dropbox/Projects/PyCharmProjects/Tasks/Other/chromedriver")

driver.get(url)
findquerry = driver.find_element_by_xpath('//*[@id="search_query"]')
button = driver.find_element_by_xpath('//*[@id="search_submit"]')

file = open("/Users/george/users_table_vtsh.csv")

for line in file:
    name = " ".join(line.split(";")[0].split()[:2])
    city = line.split(";")[1]

    findquerry.send_keys(name)
    try:
        button.click()
        wait(0.85)
        if not "Ничего не найдено" in driver.find_element_by_tag_name("body").text:
            h_name = driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div[1]/a[1]')
            # h_city = driver.find_element_by_xpath('//*[@id="results"]/div/div[2]/div[2]')
            #
            # if h_city.text == city:
            #     print(h_name.text)
            print(h_name.text)
    except:
        pass
    finally:
        findquerry.clear()
driver.quit()