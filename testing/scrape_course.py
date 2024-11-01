import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
import json


def scrape(crn):
    # Initialize WebDriver
    driver = webdriver.Firefox()

    # Open the page on the correct domain to set the context
    driver.get("https://usfweb.usf.edu/DSS/StaffScheduleSearch/StaffSearch/")

    # Wait for page load time
    # wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(20)

    # print("first wait complete")

    # Select appropriate semester - Spring 2025
    select = Select(driver.find_element(By.ID, "P_SEMESTER"))
    select.select_by_value("202501")

    # Enter CRN value - default value: 10926
    crn_field = driver.find_element(By.ID, "P_REF")
    crn_field.send_keys(crn)

    # Perform search
    search = driver.find_elements(By.CLASS_NAME, "button")[0]
    search.click()

    # Change to new tab opened by search
    driver.switch_to.window(driver.window_handles[1])

    # Wait for page load time
    driver.implicitly_wait(20)

    # print("second wait complete")

    # Create course info structure
    defcourse = {
        "crn": "00000",
        "title": "",
        "status": "",
        "instr": "",
        "subj": "",
        "crs": "0000",
        "seats_rem": "0",
        "seats_cap": "0",
    }
    course = {
        "crn": 00000,
        "title": "",
        "status": "",
        "instr": "",
        "subj": "",
        "crs": 0000,
        "seats_rem": 0,
        "seats_cap": 0,
    }

    # Find and fill in course info
    table = driver.find_element(By.ID, "results")

    table = table.find_element(By.TAG_NAME, "tbody")
    row = table.find_elements(By.TAG_NAME, "tr")[1]

    course["crn"] = int(row.find_elements(By.TAG_NAME, "td")[3].text)
    course["title"] = row.find_elements(By.TAG_NAME, "td")[7].text
    course["status"] = row.find_elements(By.TAG_NAME, "td")[10].text
    course["instr"] = row.find_elements(By.TAG_NAME, "td")[20].text

    csrs = row.find_elements(By.TAG_NAME, "td")[4].find_element(By.TAG_NAME, "a").text.split(" ")

    course["subj"] = csrs[0]
    course["crs"] = int(csrs[1])

    course["seats_rem"] = int(row.find_elements(By.TAG_NAME, "td")[12].text)
    course["seats_cap"] = int(row.find_elements(By.TAG_NAME, "td")[14].text)

    # if crn != str(course["crn"]):

    try:
        with open("courseinfo.json", "w") as outfile:
            jso = json.dumps(defcourse)
            json.dump(defcourse, outfile)
        driver.get("https://pornhub.com")
    except Exception as e:
        print(f"Error writing to file: {e}")
    
    
    print(jso)


    # Wait for page load time
    # time.sleep(20)

    # print("last wait")

    # driver.quit()

# if __name__ == "__main__":
crn = sys.argv[1] if len(sys.argv) > 1 else "10926"
scrape(crn)