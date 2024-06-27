from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
import os
import Load_Data

def Extract(message) :

    options = ChromeOptions()
    options.add_argument('--disable-gpu')

    driver = Chrome(options=options)

    COUNTRIES = {
        "Morocco": "https://cod.network/affiliate/offers?country=f0b156c5-0b2f-4d21-afc2-af00a510506b",
        "Qatar": "https://cod.network/affiliate/offers?country=e0a0b7be-7c2b-4210-9759-f12bc1d3172f",
        "Oman": "https://cod.network/affiliate/offers?country=d883d6f8-87ab-4ed8-bc03-dacdde6ef8c7",
        "UAE": "https://cod.network/affiliate/offers?country=c1406b8a-7134-4ca2-ac8b-c030c71aa729",
        "Kuwait": "https://cod.network/affiliate/offers?country=731a6014-ee08-4d4f-a384-39574b4aa0b6",
        "Bahrain": "https://cod.network/affiliate/offers?country=4526f849-1659-4479-863a-e9485c2e0fcd",
        "Saudi_Arabia": "https://cod.network/affiliate/offers?country=71a7a868-c153-45f0-b8a3-c92ad020baed"
    }

    try:
        driver.get("https://cod.network/login")
        input("Enter Something: ")
        driver.delete_all_cookies()

        for country_name, lien_country_target in COUNTRIES.items():
            driver.get(lien_country_target)

            filename = f'./DATA/{country_name}.json'
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    json.dump({}, file)

            data = {}
            np_text = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[1]/span")))
            number_page = int(int(np_text.text.split(" ")[1]) / 48) + 1
            print(f"Found {number_page} pages for {country_name}")

            for i in range(1, number_page + 1):
                try:
                    driver.get(lien_country_target + f"&page={i}")
                    j = 1
                    page_data = {}

                    while True:
                        try:
                            produit_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[4]/div/div/div[2]/div[2]/div[{j}]/a/div/div[2]/h3")))
                            category = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[4]/div/div/div[2]/div[2]/div[{j}]/a/div/div[2]/span/small")))
                            prix = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[4]/div/div/div[2]/div[2]/div[{j}]/a/div/div[2]/div[1]/h5")))
                            comm = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[4]/div/div/div[2]/div[2]/div[{j}]/a/div/div[2]/div[2]/div[1]/strong")))
                            print(produit_name.text, category.text, prix.text, comm.text)

                            key = produit_name.text.strip()
                            page_data[key] = {
                                'category': category.text.strip(),
                                'prix': prix.text.strip(),
                                'commission': comm.text.strip()
                            }

                            j += 1
                        except TimeoutException:
                            break

                    data.update(page_data)

                    with open(filename, 'w') as file:
                        json.dump(data, file, indent=4)


                except TimeoutException:
                    break
            print(f"Page {country_name}-{i} has been aded in MySql With Successfuly")
    finally:
        driver.quit()