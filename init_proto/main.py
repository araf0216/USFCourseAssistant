import time
import subprocess
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


crntofind = input("Enter your Course Registration Number: ")
semester = input("Enter the semester of the class (Fall, Spring, Summer): ")
username = input("Enter your USF email: ")
password = input("Enter your password: ")

def login_and_save_cookies(driver, wait):
    driver.get('https://bannersso.usf.edu/ssomanager/c/SSB')
    
    # Login process
    wait.until(EC.element_to_be_clickable((By.ID, 'i0116'))).send_keys(username + Keys.ENTER)
    wait.until(EC.element_to_be_clickable((By.ID, 'i0118'))).send_keys(password + Keys.ENTER)
    wait.until(EC.element_to_be_clickable((By.ID, 'signInAnotherWay'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idSubmit_SAOTCC_Continue')))
    
    MFA = input('Enter your code here: ')
    
    driver.find_element(By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(MFA + Keys.ENTER)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')))
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))


def check_seats(driver, wait, semester, crntofind):
    seats = 0
    try:
        while seats < 1:
            driver.get('https://usfweb.usf.edu/DSS/StaffScheduleSearch')
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select')))
            
            if semester == "Fall":
                driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[2]').click()
            elif semester == "Spring":
                driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[1]').click()
            elif semester == "Summer":
                driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[3]').click()

            driver.find_element(By.XPATH, '//*[@id="P_REF"]').send_keys(crntofind)
            driver.find_element(By.CLASS_NAME, "button").click()
            
            wait.until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])
            
            element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]')))
            seats_text = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]').text
            seats = int(seats_text)
            
            print(f'There are currently {seats} seats available')

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    
    return seats

def main():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    
    login_and_save_cookies(driver, wait)
    
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print("Cookies saved:", cookies)

    seats = check_seats(driver, wait, semester, crntofind)
    
    if seats > 0:
        subprocess.run(["python3", "auth.py", crntofind, semester, username, password])
        

if __name__ == "__main__":
    main()


# cd = {}

# for i in range(10000):
#     try: 
#         crn = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[" + str(i +2) + "]/td[4]").text
#         seats = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[" + str(i + 2) + "]/td[13]").text
#         cd[crn] = seats
#     except Exception:
#         break

# print(cd)

#foundcrn = int(cd[crntofind])























# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time
# import subprocess
# import pickle
# import sys

# crntofind = input("Enter your Course Registration Number: ")
# semester = input("Enter the semester of the class (Fall, Spring, Summer):")
# username = input("Enter your USF email: ")
# password = input("Enter your password: ")

# driver = webdriver.Firefox()
# wait = WebDriverWait(driver, 15)

# def main():
#     driver.get('https://bannersso.usf.edu/ssomanager/c/SSB')
#     wait = WebDriverWait(driver, 15)
#     element = wait.until(EC.element_to_be_clickable((By.ID, 'i0116')))
#     driver.find_element(By.ID, "i0116").send_keys(username + Keys.ENTER)
#     element = wait.until(EC.element_to_be_clickable((By.ID, 'i0118')))
#     driver.find_element(By.ID, "i0118").send_keys(password + Keys.ENTER)
#     element = wait.until(EC.element_to_be_clickable((By.ID, 'signInAnotherWay')))
#     driver.find_element(By.ID, "signInAnotherWay").click()
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div')))
#     driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div").click()
#     element = wait.until(EC.element_to_be_clickable((By.ID, 'idSubmit_SAOTCC_Continue')))
#     MFA = input('Enter your code here:')
#     time.sleep(15)
#     driver.find_element(By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(MFA + Keys.ENTER)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]')))
#     driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    

# main()


# cookies = pickle.load(open("cookies.pkl", "rb"))
# print(cookies)

# seats = 0

# try:
#     while seats < 1:
#         driver.get('https://usfweb.usf.edu/DSS/StaffScheduleSearch')
        
#         wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select')))
        
#         if semester == "Fall":
#             driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[2]').click()
#         elif semester == "Spring":
#             driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[1]').click()
#         elif semester == "Summer":
#             driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[3]').click()

#         driver.find_element(By.XPATH, '//*[@id="P_REF"]').send_keys(crntofind)
#         driver.find_element(By.CLASS_NAME, "button").click()

#         wait.until(EC.number_of_windows_to_be(2))
#         driver.switch_to.window(driver.window_handles[1])

#         element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]')))
        
#         seats_text = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]').text
#         seats = int(seats_text)
        
#         print(f'There are currently {seats} seats available')


#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     driver.quit()

# if seats > 0:
#     subprocess.run(["python", "auth.py", crntofind, semester, username, password, cookies])



















# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import subprocess

# crntofind = input("Enter your Course Registration Number: ")
# semester = input("Enter the semester of the class (Fall, Spring, Summer):")
# username = input("Enter your usf email:")
# password = input("Enter your password:")

# driver = webdriver.Firefox()
# wait = WebDriverWait(driver, 10)

# seats = 0

# while seats < 1:
#     driver.get('https://usfweb.usf.edu/DSS/StaffScheduleSearch')
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[2]')))

#     if semester == "Fall":
#         driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[2]").click()
#     elif semester == "Spring":
#         driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[1]").click()
#     elif semester == "Summer":
#         driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/div/div[1]/select/option[3]").click()

#     driver.find_element(By.XPATH, '//*[@id="P_REF"]').send_keys(crntofind)

#     driver.find_element(By.CLASS_NAME, "button").click()

#     time.sleep(0.5)

#     driver.switch_to.window(driver.window_handles[1])

#     element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]')))

#     seats = int(driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[2]/td[13]').text)

#     print(f'There are currently {seats} available')

#     time.sleep(2)

#     driver.quit()

# subprocess.run(["python", "auth.py", crntofind, semester, username, password])


# if seats > 0:

# else:
#     print("No seats left")

# driver.quit()



# cd = {}

# for i in range(10000):
#     try: 
#         crn = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[" + str(i +2) + "]/td[4]").text
#         seats = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/div/p[2]/table/tbody/tr[" + str(i + 2) + "]/td[13]").text
#         cd[crn] = seats
#     except Exception:
#         break

# print(cd)

#foundcrn = int(cd[crntofind])

#print(foundcrn)