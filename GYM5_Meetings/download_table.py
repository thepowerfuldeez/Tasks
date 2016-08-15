#!/usr/bin/python3.4


def main():
    import time
    import os
    from pyvirtualdisplay import Display
    from selenium import webdriver
    from firebase import firebase

    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()

    USERNAME = ""
    PASSWORD = ""

    os.chdir("/home/thepowerfuldeez/Downloads/")
    files_to_delete = os.listdir()
    if len(files_to_delete) > 1:
        for file in files_to_delete[1:]:
            os.remove(file)

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

        message_form.find_element_by_class_name("button-login-title").click()

        time.sleep(0.3)

        if driver.current_url == "http://net.citycheb.ru/asp/SecurityWarning.asp":  # Если вылезает SecurityWarning
            driver.find_element_by_class_name("buttons-panel").find_elements_by_tag_name("button")[1].click()
            time.sleep(0.5)

    def sessionisover(driver):
        driver.get(driver.current_url)
        return driver.current_url == "http://net.citycheb.ru" or driver.current_url == "http://net.citycheb.ru/about.asp?AL=Y"

    def download_table(driver):

        if sessionisover(driver):  # Проверка на конец сессии
            auth(driver, USERNAME, PASSWORD)

        driver.find_element_by_class_name("icon-bullhorn").click()  # Переход ко вкладке "Объявления"

        time.sleep(1.5)

        for x in driver.find_elements_by_tag_name("a"):
            if "9-11" in x.text:
                x.click()
                time.sleep(5)
                break

        ads = driver.find_elements_by_class_name("advertisement")

        for ad in ads:
            subj = ad.find_element_by_tag_name("h3").text  # Тема

            if "Замен" in subj:
                content = ad.find_element_by_class_name("adver-content")
                text = subj + "\n\n" + content.text
                send_changes_list(text[5:])
                break

    def send_changes_list(list):
        firebase_ref = firebase.FirebaseApplication('https://gym5meetings.firebaseio.com', None)
        firebase_ref.delete("/schedule/changes", None)
        firebase_ref.put("/schedule/changes", "list", list)

    auth(driver, USERNAME, PASSWORD)
    download_table(driver)
    driver.quit()
    display.stop()

    os.chdir("/home/thepowerfuldeez/Downloads/")
    to_be_renamed = os.listdir()[0]
    os.rename(to_be_renamed, "table.xls")

main()