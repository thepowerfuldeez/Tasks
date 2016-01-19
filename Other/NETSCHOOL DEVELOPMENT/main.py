import csv
import time

from selenium import webdriver

driver = webdriver.Chrome(
    '/Users/thepowerfuldeez/Downloads/chromedriver')

USERNAME = "григорьевгг"
PASSWORD = "321321321z"


def auth(driver, username_, password_):
    driver.get('http://net.citycheb.ru')

    time.sleep(1.5)  # Загрузка страницы

    message_form = driver.find_element_by_id("message")  # Окно авторизации

    sft = message_form.find_element_by_id("funcs")  # Тип ОО
    sft_options = sft.find_elements_by_tag_name("option")
    sft_options[2].click()  # Общеобразовательная

    time.sleep(0.3)

    scid = message_form.find_element_by_id("schools")  # Образовательная организация
    scid_options = scid.find_elements_by_tag_name("option")
    scid_options[5].click()

    time.sleep(0.3)

    username = message_form.find_element_by_name("UN")
    username.send_keys(username_)

    password = message_form.find_element_by_name("PW")
    password.send_keys(password_)

    message_form.find_element_by_class_name("submit-button").click()

    time.sleep(0.3)

    if driver.current_url == "http://net.citycheb.ru/asp/SecurityWarning.asp":  # Если вылезает SecurityWarning
        driver.find_element_by_class_name("buttons-panel").find_elements_by_tag_name("button")[1].click()
        time.sleep(0.5)


def sessionisover(driver):
    driver.get(driver.current_url);
    return driver.current_url == "http://net.citycheb.ru" or driver.current_url == "http://net.citycheb.ru/about.asp?AL=Y"


def view_announcements(driver):

    if sessionisover(driver):  # Проверка на конец сессии
        auth(driver, USERNAME, PASSWORD)

    driver.find_element_by_class_name("icon-bullhorn").click()  # Переход ко вкладке "Объявления"

    time.sleep(1.5)

    results = []  # Массив объявлений

    ads_container = driver.find_element_by_class_name("adver-container")
    ads = ads_container.find_elements_by_class_name("advertisement")

    for ad in ads:
        subj = ad.find_element_by_tag_name("h3").text[5:]  # Тема

        text = ad.find_element_by_class_name("adver-content").text  # Текст

        results.append({"Тема" : subj, "Текст" : text})

    return results


auth(driver, USERNAME, PASSWORD)
announcements = view_announcements(driver)
driver.quit()

csvtempfile = open("table.csv")

with open("table.csv", "a", newline="") as csvfile:  # Записать результаты в файл
    writer = csv.writer(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)

    for ad in announcements[::-1]:
        subj = ad["Тема"]
        text = ad["Текст"]
        if subj not in csvtempfile and text not in csvtempfile:
            writer.writerow([subj, text])