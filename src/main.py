import time
from multiprocessing import Pool

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import config


def login(driver):
    """
    Login to  https://adbs.uab.gov.tr/login, which uses turkiye.gov.tr
    :return:
    """
    driver.get("https://giris.turkiye.gov.tr/OAuth2AuthorizationServer/AuthorizationController?response_type=code"
               "&client_id=757dc02b-382a-4128-8e24-d3aff1f7a239&state=random_value&scope=Kimlik-Dogrula&redirect_uri"
               "=https://adbs.uab.gov.tr/giris")

    driver.find_element(By.ID, "tridField").send_keys(config.username)
    driver.find_element(By.ID, "egpField").send_keys(config.password)
    driver.find_element(By.NAME, "submitButton").click()

    try:
        WebDriverWait(driver, 10).until(EC.url_to_be("https://adbs.uab.gov.tr/users"))
    except TimeoutException:
        print("Please check your credentials in the src/config.py file")


def adb(driver):
    """
    Function to complete the ADB (Amatör Denizci Belgesi) course.
    :return:
    """
    driver.get("https://adbs.uab.gov.tr/users/my-educations/1")
    do_course(driver)
    print("Amatör Denizci Belgesi course completed")


def kmt(driver):
    """
    Function to complete the KMT (Kısa Mesafe Telsiz Operatörü) course.
    :return:
    """
    driver.get("https://adbs.uab.gov.tr/users/my-educations/2")
    do_course(driver)
    print("Kısa Mesafe Telsiz Operatörü course completed")


def do_course(driver):
    start_button = WebDriverWait(driver, 10) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'dx-button-mode-contained.dx-button-success')))
    driver.execute_script("arguments[0].click();", start_button)

    okay_button = WebDriverWait(driver, 10) \
        .until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Evet']")))
    driver.execute_script("arguments[0].click();", okay_button)

    while True:
        try:
            time.sleep(1)
            countdown_timer = driver.find_element(By.CLASS_NAME, "mb-0")
            countdown_time = int(countdown_timer.text.split(":")[0]) * 60 + int(countdown_timer.text.split(":")[1])
            print(f"Waiting for {countdown_time} seconds...")
            time.sleep(countdown_time)
        except Exception as e:
            print("waiting for countdown timer")

        try:
            next_button = WebDriverWait(driver, 10) \
                .until(EC.element_to_be_clickable((By.XPATH, '//dx-button[contains(@aria-label,"İleri")]')))
            driver.execute_script("arguments[0].click();", next_button)
        except Exception as e:
            print("next button not found")
            try:
                finish_button = WebDriverWait(driver, 10) \
                    .until(
                    EC.element_to_be_clickable((By.XPATH, '//dx-button[contains(@aria-label,"Eğitimi Tamamla")]')))
                driver.execute_script("arguments[0].click();", finish_button)
                break
            except Exception as e:
                print("finish button not found")


def get_adb():
    """
    Function to complete the ADB (Amatör Denizci Belgesi) course. In a thread
    """
    driver = webdriver.Chrome(service=service)
    login(driver)
    adb(driver)
    input("Press any key to exit the ADB course")
    driver.quit()


def get_kmt():
    """
    Function to complete the KMT (Kısa Mesafe Telsiz Operatörü) course. In a thread
    """
    driver = webdriver.Chrome(service=service)
    login(driver)
    kmt(driver)
    input("Press any key to exit the KMT course")
    driver.quit()


if __name__ == '__main__':
    service = ChromeService(executable_path=ChromeDriverManager().install())

    while True:
        lecture = input("Which lecture do you want to complete? (adb/kmt): ").lower()
        if lecture == "adb":
            get_adb()
            break
        elif lecture == "kmt":
            get_kmt()
            break
        else:
            print("Please enter a valid lecture name.")

 # TODO: index.html, create a javascript file to run the python script, manifest.json, icon.png, background.js
