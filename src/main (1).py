
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




cls = "Python"
url = "https://blackboard.maltepe.edu.tr/"
analysis_course_url = "https://blackboard.maltepe.edu.tr/ultra/courses/_58063_1/outline"
python_course_url = "https://blackboard.maltepe.edu.tr/ultra/courses/_55516_1/outline"
Ata_course_url = "https://blackboard.maltepe.edu.tr/ultra/courses/_56636_1/outline"
driver_path = "chromedriver.exe"

driver = webdriver.Chrome(driver_path)
username="**********"
password="*********"

def close_policy_popup():
    try:
        driver.find_element_by_class_name("locationPane")
        driver.find_element_by_id("agree_button").click()
    except:
        print("Policy pop-up does not exist")


def login():
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "user_id")))
    driver.find_element_by_id("user_id").send_keys(username,login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("entry-login").click()
    # time.sleep(5)


def open_collaborate(lecture):
    if (lecture == "S.R.Analysis"):
        url = analysis_course_url
    elif (lecture == "Python"):
        url = python_course_url
    elif (lecture == "İnklap Tarihi"):
        url = Ata_course_url
    else:
        url = "https://google.com/"
    driver.get(url)
    try:
        print("sayfa yukleniyor....")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "sessions-list-dropdown")))
        # time.sleep(5)
        try:
            print("duyuru var mı yok mu kontrol ediliyor....20sn")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        "body > div.ms-Layer.ms-Layer--fixed.rootIsFixed_604b1c86 > div > div > div > div.ms-Dialog-main.main_3353f7ac.ms-modalExample-container.container-inherit.ms-FocusTrapZone > div > div.title-container > button")))
            duyuru = driver.find_element_by_css_selector(
                "body > div.ms-Layer.ms-Layer--fixed.rootIsFixed_604b1c86 > div > div > div > div.ms-Dialog-main.main_3353f7ac.ms-modalExample-container.container-inherit.ms-FocusTrapZone > div > div.title-container > button")
            duyuru.click()
        except:
            print("duyuru yok")
        driver.find_element(By.CSS_SELECTOR, "#sessions-list-dropdown > .blue-link").click()
        driver.find_element(By.CSS_SELECTOR, "#sessions-list span").click()
        driver.switch_to.window(driver.window_handles[-1])
    except:
        print("WebDriverWait çalışmadı")


def close_permisson_popup():
    try:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='techcheck-modal']/button")))
        driver.find_element_by_xpath("//*[@id='techcheck-modal']/button").click()
        print("izin 1 kapatıldı")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#announcement-modal-page-wrap > .close")))
        driver.find_element(By.CSS_SELECTOR, "#announcement-modal-page-wrap > .close").click()
        print("duyuru kapatıldı")
    except:
        print("permisson popup does not exist")


def open_students_page():
    try:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "side-panel-open")))
        driver.find_element(By.ID, "side-panel-open").click()
        print("Side panel open")
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "panel-control-participants")))
        # time.sleep(3)
        driver.find_element(By.ID, "panel-control-participants").click()
        print("student page opens")
    except:
        print("student page couldnt open")


def raise_your_hand():
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/button[2]").click()


def low_your_hand():
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/button[2]").click()


def attend_the_yoklama():
    while (True):
        hand = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/button[2]")
        hand_raised_students = driver.find_elements(By.CLASS_NAME, "status-hand-raised")
        count = len(hand_raised_students)
        if (count > 10):
            if (hand.get_attribute("aria-pressed") == "true"):
                print("Already raise your hand")
            else:
                raise_your_hand()
        elif (count < 9):
            if (hand.get_attribute("aria-pressed") == "false"):
                print("Already low your hand")
            else:
                low_your_hand()
        time.sleep(10)


driver.get(url)
close_policy_popup()
login()
open_collaborate("Python")
close_permisson_popup()
open_students_page()
time.sleep(5)
attend_the_yoklama()
