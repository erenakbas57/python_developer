from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "_erenakbas57"
password = "arthur1788"


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput = self.browser.find_element_by_css()
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(1)
        self.browser.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")

        followersCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count : {followersCount}")

        action = webdriver.ActionChains(self.browser)
        durum = True
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))
            print(newCount)
            if followersCount > newCount:
                break
            else:
                followersCount = newCount
                print(f"update count : {newCount}")
                time.sleep(2)

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            name = user.find_element_by_css_selector("a").get_attribute("href")
            print(name[26:-1])



instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()
