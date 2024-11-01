import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from supabase import create_client, Client

# Initialize Supabase client
SUPABASE_URL = 'https://gbvlrslemvlcimbqjtum.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdidmxyc2xlbXZsY2ltYnFqdHVtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTcxMjU1MzMsImV4cCI6MjAzMjcwMTUzM30.Oc667WbOVxxPkyVH6ucUHvQ2y1OFdcZSw6HHN36T55M'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table('users').select('*').execute()
data = response.data

# supabase.table("users").update({'email': "user12"}).eq('email', 'user12').execute()




for user in data:

    estsauthlight = "+ef23b41d-8472-4ff1-b6ce-970c704bfdb9"
    estsauth = "0.AQgA3vcbdOXi30aNZ4Jgffneqg400BQigSNJg8KZYc3yAdwIAAA.AgABFwQAAAApTwJmzXqdR4BN2miheQMYAgDs_wUA9P8oBywWM4xSo5uetDwlRxkwEvBLpE58_lMp5ggx78LMTUi6aSRmgVjinGXNqhS6WuSywMH1P7QE70bflPYtjdjS8r1RtgL9u-i3ac4msHzyFW-JIBeXLmNjrF45IpKVABn4y67xtEw23UT_NoVvh2RKa6wUPVVLPagb_KO7xyVpkw8EJZ9kYMGHhwNtWDgbvO_vpxl8hXIqZAMYnCkcUcfRkRr7n9hA6Htl9wa4J1E6jC2K3gD4d2pIFW7cj9i3Tyr-ThAcsaVWWhN_4-1TibX8-KWiZ2UJkvBjHuW_V2hRjrC5V_j7bhtt7RT8yzJxN__i0ZkpntXQf77rxqYO4x5RtVwoFq-JYlfjT4ymt0ljsqLpvOQ7JnnB7izMjs_xzXAK9rnJy2amTE-gi_yhgofkcaLn97fHpGzyUuB92ltDVQl4KKu2gjS1YphqWmVvQnyI2l_1Ued7YQs6XZSLz46bw2xxSY5EYepRqOZoqK9bJM2b7AJWUlud9nDQdTcXEsUM1-KQEMdYjZ0SafMAbGwPIJ_kkVNvtuusalRmZO0RmYM5P4pp2_qyCG0xWOjReVxCa4_6F1GlthZXumG9Mm2Y_yB1InnFjgZia8WHj2IOXZtk1sWjKwjTmKc6uQmzwCY-KEMdtvOTbovkgxtsLbuNfw4xbuXbC2HcEYJBAfx_ExwexGAq83ha3R2rTOrW_mdLt_H7"
    estsauthpersistent = "0.AQgA3vcbdOXi30aNZ4Jgffneqg400BQigSNJg8KZYc3yAdwIAAA.AgABFwQAAAApTwJmzXqdR4BN2miheQMYAgDs_wUA9P_rhg5Qo3-Fg_JJPW-iB5YXWm5WUheVqOhbmWiuqVxwJKvZaRkz93sglDc53AhedllmAAWhdcDL5Xb1TXarF8-ff6og5ZtxdYoZlzHA62bD8-beKBrJF1i4I6WypyxOhUGCFK2bWVdQN6cqwwb9CpQaPrlvag7DgvrN2yYdNQ5mQKdQeOHG2nsgUDJq-O1Z09ECnLkoQ9GLCEIlRyR8RPqIG6ZAl9_UGofZMU56OcVZMzyDj5NeBT9ejv0zOQlb6YK6FmnHlAJJnlwUXUUCr9Uo0dJk_DKEzS_9KeykISYp7qkvhZd-bCm-cmdXTzP6J-fGXEQlnk4UnqDzIJwpFe-lJ9t81PFrIAeYYdqB7Um7joO3UXgpmLIJZ-S8tzSWLh3PP4p5NG7qaSmrz9lbZYZarKozCh9zLXqRNZQb6VL7JXNpkC4T60vD9b08QylsKVjGf6vq_66pBgjl6MOUjGoKgmxOKp1xYzfuts2TUA"
    username = user["email"]
    
    if estsauthlight != None and estsauth != None and estsauthpersistent != None and username == "aahmed16@usf.edu":
        print(estsauthlight, estsauth, estsauthpersistent, username)



        # Initialize WebDriver
        driver = webdriver.Firefox()

        # Open a page on the correct domain to set the context
        driver.get("https://bannersso.usf.edu/ssomanager/c/SSB")

        # Wait for the URL to be stable
        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_contains("login.microsoftonline.com"))

        # Function to add a cookie to the current domain
        def add_cookie(name, value):
            # if cookie:
            cookie_dict = {
                "name": name,
                "value": value,
                "domain": "login.microsoftonline.com",
                "path": "/",
                "secure": True,
                "httpOnly": True,
                "sameSite": "None"
            }
            # if "expiry" in cookie:
            # cookie_dict["expiry"] = cookie["expiry"]
            driver.add_cookie(cookie_dict)
            print('\nlogged in\n')

    

        cookieref = {}
        cookieref["ESTSAUTHLIGHT"] = estsauthlight
        cookieref["ESTSAUTHPERSISTENT"] = estsauthpersistent
        cookieref["ESTSAUTH"] = estsauth


        for cookn, cookv in cookieref.items():
            add_cookie(cookn, cookv)
        

        # Wait a bit to ensure cookies are set before refreshing
        driver.implicitly_wait(5)

        # Refresh the page to apply the cookies
        driver.refresh()

        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
    
        time.sleep(5)

        cookies = driver.get_cookies()
        
        for cookie in cookies:

            if cookie['name'] == "ESTSAUTHLIGHT":
                supabase.table("users").update({'authlight': cookie['value']}).eq("email", username).execute()
                # cooksel['authlight'] = cookie["value"]
            if cookie['name'] == "ESTSAUTHPERSISTENT":
                supabase.table("users").update({'authpcookie': cookie['value']}).eq("email", username).execute()
                # cooksel['authpcookie'] = cookie["value"]
            if cookie['name'] == "ESTSAUTH":
                supabase.table("users").update({'auth': cookie['value']}).eq("email", username).execute()
                # cooksel['auth'] = cookie["value"]
            else:
                continue

            print(cookie)
        
        # supabase.table("users").update(cooksel).eq("email", username).execute()
                #supabase.table("users").update({'email': "user12"}).eq('email', 'user12').execute()
        time.sleep(15)
        # Quit the driver
        driver.quit()




# time.sleep(100)
