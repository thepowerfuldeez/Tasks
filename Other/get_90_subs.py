from selenium import webdriver
import csv
from time import sleep as wait

w = csv.writer(open('90subs.csv', 'w', newline=''), delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

driver = webdriver.Chrome(
    '/Users/george/Dropbox/Projects/PyCharmProjects/Tasks/Other/chromedriver'
)

channel = "EeOneGuy"
driver.get("http://vspstats.com/ru/statistics/channel/{}".format(channel))

driver.find_element_by_xpath('//*[@id="ChannelActivitiesButtonShowMore"]/div[2]/button').click()
wait(0.5)
table = driver.find_element_by_xpath('//*[@id="ChannelActivities-pageSet"]/table')

for tr in table.find_elements_by_tag_name("tr")[::-1]:
    a = []
    for td in tr.find_elements_by_tag_name("td")[:2]:
        x = td.text
        if x[0] == "+":
            a.append(x.split()[0][1:])
        else:
            a.append(x)
    w.writerow(a)

driver.quit()
