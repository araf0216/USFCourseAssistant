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


# Initialize WebDriver
driver = webdriver.Firefox()

# Open the page on the correct domain to set the context
driver.get("https://bannersso.usf.edu/ssomanager/c/SSB")

# Wait for the URL to be stable
wait = WebDriverWait(driver, 20)
wait.until(EC.url_contains("login.microsoftonline.com"))

# Function to add a cookie to the current domain
def add_cookie(name, value):
    # add each cookie in exact format according to standards
    cookie_dict = {
        "name": name,
        "value": value,
        "domain": "login.microsoftonline.com",
        "path": "/",
        "secure": True,
        "httpOnly": True,
        "sameSite": "None"
    }
    driver.add_cookie(cookie_dict)
    print('\nAnnddd... Voila!\n')


# reference dict listing each cookie name and value
cookieref = {
    "ESTSAUTHPERSISTENT": "0.AQgA3vcbdOXi30aNZ4Jgffneqg400BQigSNJg8KZYc3yAdwIAAA.AgABFwQAAADW6jl31mB3T7ugrWTT8pFeAwDs_wUA9P_dy_m-uwTAhExPKLmwhV5PLQ5DoagLGr3_P8awTORUsFUjzH6wPDPM2n7oe7J6TfKQR8sTqG402TlDXi5V9_ytaixc8i6YcWy97H2DrF2aCPj1HHscnEOt-FrkqW7BE06Lhhy1VP1I0V_B_AeA9pv7KNvQb23I88UMlkwT93OSCVwjupb2C_9Rt3ZiSrEgRsd6C4GEFvPAwgVCdZKM36Ua-v5B-B1V-bEu8u_Dh1kZZ4Ja-JrxreZ005JbcTLhXY-fqyVKNAyVcZTWpZs6RHI5my7NbXwwMdZHOLrX_v8H9LY7ZOzRtNYSq2ji37E72mXza_frsI20fzGe3IyMQHogowwfaj14Y9j0s1xYwNVsrC-HpRdZGta_8USIvIsQcCkeg7I9-xRlYUTIGoHacFei5ap-Ysd826mThtCVTLLysgNgI1AMmVkRJ96CvHnWu3MhDNKXIk1S1-vEh6E_jH1ODJRqEEY6jsL7mw",
    "ESTSAUTH": "0.AQgA3vcbdOXi30aNZ4Jgffneqg400BQigSNJg8KZYc3yAdwIAAA.AgABFwQAAADW6jl31mB3T7ugrWTT8pFeAwDs_wUA9P9QjwMwQsDP2Mj12xm96wp9nbjWnFWj1FxIYv0Ha3DjD_GgPELrHn-rvdV5QoNm7oLmamRoFatWVLcahc45b2noxx0fg5SJakXTJsy_q0oG8CX_KQAYT2O2KB7Qh1MHNRd2NyR0S2zWUBTX3LJceSgtCJwK3dcNQmhA0XPrJBQk6NTLduInIe3e9OnE6-dte9utMNlrVRRL5WtSLQ6-p52nvB7I4lz7keoQ-w17GIfR6xlGR5evyyvtFaZjatmWkHzS4pXMYYNIhwJsljcO4e-oD5u5_49lEMVqn8lQFwJsgkSduMYW25Byh-BAJSq8H3LNERGaX0Wwgjs5USxX8QI5t10GHJQINUakbTjwU8GIa_cYRbiUbaTfSVj__yvnsbQP6vsvEiiuxRusdCqlzRbbnNitOye56qOURNeyIxqn9he2LblmbBKMp8YVZQmMHy3YN8raVmbUsA7dnmYlOF1h28i0TqubQab5Jg7cQ-kQUm68vJ7-G3lTFvzhjpffua3eQH5JvwyfKN5OMzBILXWrhQcClnLJAKOIA5CRz_YdHcBUFNp4m8g0suzDYcqOVCOLr_I0QopqaeaATP61FsNQZ72sH-TgMWq39aFAU9WGjOnsJDEn69kmgrpScN1_G-hYqvdLDpSF44moLtgXjHvNgA",
    "ESTSAUTHLIGHT": "+6f88e468-9fb4-49cc-a3db-354d3a21870b"
}

# add cookie for each listed in reference dict
for cookn, cookv in cookieref.items():
    add_cookie(cookn, cookv)


# Wait a bit to ensure cookies are set before refreshing
driver.implicitly_wait(5)

# Refresh the page to apply the cookies
driver.refresh()