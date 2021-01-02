from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/?hl=tr")

time.sleep(2)

username = browser.find_element_by_name("username")

password = browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")

loginButton.click()

time.sleep(3)

passButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")

passButton.click()

time.sleep(3)

notnowButton = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")

notnowButton.click()

time.sleep(3)


profileButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")

profileButton.click()

time.sleep(3)

followersButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")

followersButton.click()

time.sleep(5)
fBody  = browser.find_element_by_css_selector(".isgrP")
scroll = 0
while scroll < 80: # 3 defa scroll
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(1)
    scroll += 1
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollBy(0,50)
var LenOfPage = followers.scrollHeight;
return LenOfPage
"""
lenOfPage = browser.execute_script(jscommand)
match = False
while (match == False):
    Lastcount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if Lastcount == lenOfPage:
        match=True

followerslist = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for follower in followers:
    followerslist.append(follower.text)

with open ("Followers.txt","w",encoding= "UTF-8") as file:
    for follower in followerslist:
        file.write(follower + "\n")

time.sleep(3)


browser.close()

