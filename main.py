from selenium import webdriver
from time import sleep
from secrets1 import pw


class FacebookBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()    
        self.username = username
        self.driver.get("https://facebook.com/me/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input")\
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label')\
            .click()
        sleep(4)
        self.driver.get("https://facebook.com/me/")

    def get_DOB(self):
        self.driver.find_element_by_xpath('//button[@type="Friends"]')\
            .click()
        account = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/account')]")\
            .click()
        info = self._get_names()
        DOB = [user for user in following if user not in followers]
        print(DOB)

    def _get_names(self):
        sleep(2)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
            .click()
        return names


my_bot = FacebookBot('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
my_bot.get_DOB()
