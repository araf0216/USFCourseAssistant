import sys
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = sys.argv[3]
password = sys.argv[4]
CRN = sys.argv[1]
semester = sys.argv[2]
cookies = pickle.load(open("cookies.pkl", "rb"))

print(cookies)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
driver.get('https://usfonline.admin.usf.edu/pls/prod/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu')


for cookie in cookies:
    cookie['domain'] = '.usf.edu'
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

driver.get('https://usfonline.admin.usf.edu/pls/prod/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu')



try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')))
    
    # Navigate through the student portal
    driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a')))
    driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a').click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a')))
    driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a').click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[1]')))
    
    # Select the semester
    if semester == "Fall":
        driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[1]").click()
    elif semester == "Summer":
        driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[2]").click()
    elif semester == "Spring":
        print("Spring is not yet available to register for")
    
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/input')))
    driver.find_element(By.XPATH, '/html/body/div[3]/form/input').click()
    
    element = wait.until(EC.element_to_be_clickable((By.ID, 'crn_id1')))
    driver.find_element(By.ID, "crn_id1").send_keys(CRN)
    
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/input[19]')))
    driver.find_element(By.XPATH, "/html/body/div[3]/form/input[19]").click()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Registered for course")
    driver.quit()






















# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from flask import Flask, request, jsonify
# import sys
# import pickle
# import subprocess


# #signInAnotherWay -- ID
# #table-cell text-left content - CLASS


# username = sys.argv[3]
# password = sys.argv[4]
# CRN = sys.argv[1]
# semester = sys.argv[2]
# cookies = sys.argv[5]

# driver = webdriver.Firefox()
# wait = WebDriverWait(driver, 15)
# driver.get('https://bannersso.usf.edu/ssomanager/c/SSB')


# for cookie in cookies:
#     driver.add_cookie(cookie)


# # element = wait.until(EC.element_to_be_clickable((By.ID, 'i0116')))

# # # driver.switch_to.window(driver.window_handles[1])

# # #Enter username
# # driver.find_element(By.ID, "i0116").send_keys(username + Keys.ENTER)

# # element = wait.until(EC.element_to_be_clickable((By.ID, 'i0118')))

# # #Enter Password
# # driver.find_element(By.ID, "i0118").send_keys(password + Keys.ENTER)

# # element = wait.until(EC.element_to_be_clickable((By.ID, 'signInAnotherWay')))


# # #Click to sign in another way
# # driver.find_element(By.ID, "signInAnotherWay").click()

# # element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div')))

# # #Click Phone Number
# # driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div").click()

# # element = wait.until(EC.element_to_be_clickable((By.ID, 'idSubmit_SAOTCC_Continue')))
# # time.sleep(10)
# # #Verify Button 
# # driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

# # element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]')))

# # #Yes, keep me signed in
# # driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')))


# #student 
# driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a').click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a')))

# #registration 
# driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a').click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a')))

# #register, add, or drop classes 
# driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a').click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[1]')))

# if semester == "Fall":
#     driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[1]").click()
# elif semester == "Summer":
#     driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[1]/td[2]/select/option[2]").click()
# elif semester == "Spring":
#     print("Spring is not yet available to register for")

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/input')))

# #submit 
# driver.find_element(By.XPATH, '/html/body/div[3]/form/input').click()

# element = wait.until(EC.element_to_be_clickable((By.ID, 'crn_id1')))

# #crn input 1= id="crn_id1"
# driver.find_element(By.ID, "crn_id1").send_keys(CRN)

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/form/input[19]')))

# #submit changes xpath = /html/body/div[3]/form/input[19]
# driver.find_element(By.XPATH, "/html/body/div[3]/form/input[19]").click()


# driver.quit()



#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
    #driver.add_cookie(cookie)

#pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))