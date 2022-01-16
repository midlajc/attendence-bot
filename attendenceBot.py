from selenium import webdriver
from time import sleep
from links import links

class attendenceBot:
    def __init__(self):
        self.driver = webdriver.Chrome()        

    def _add_Attendence(self,name,rollNo,link):
        self.driver.get(link)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")\
            .send_keys(rollNo)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")\
            .send_keys(name)
        sleep(1)   
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")\
             .click()
        sleep(2)

    def _add_Attendence1(self,name,rollNo,link):
        self.driver.get(link)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")\
            .send_keys(name)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")\
            .send_keys(rollNo)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")\
             .click()
        sleep(2)


my_bot=attendenceBot()   
my_bot._add_Attendence("Midlaj C",41,links["link1"]) 
my_bot._add_Attendence1("Midlaj C",41,links["link2"])
my_bot._add_Attendence("Midlaj C",41,links["link3"])   
my_bot._add_Attendence("Midlaj C",41,links["link4"])
my_bot._add_Attendence("Midlaj C",41,links["link5"])

