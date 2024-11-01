from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Firefox()
driver.get("https://bannersso.usf.edu/ssomanager/c/SSB")

userinfo = {
    "user": input("Enter user email"),
    "pass": input("Enter user password")
}

of = open("allcookies.json", "w")

time.sleep(5)

driver.find_element(By.TAG_NAME, "input").send_keys(userinfo["user"] + Keys.ENTER)
n = 0

time.sleep(2)

pin = driver.find_elements(By.TAG_NAME, "input")[9].send_keys(userinfo["pass"] + Keys.ENTER)

time.sleep(3)

n += 1
print(n, json.dumps(driver.get_cookies()), "\n")

time.sleep(5)

print(n, json.dumps(driver.get_cookies()), "\n")
json.dump(driver.get_cookies(), of)