from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome('C:/automation/chromedriver')
# wait = WebDriverWait(driver, 15)
class Methodos(object):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 15)

    def SendText(self, _id, text):
        e = self.wait.until(EC.element_to_be_clickable(By.ID, _id))
        e.clear()
        e.send_keys(text)
        self.driver.implicitly_wait(5)

    def Click(self, id):
        e = self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        e.click()


    def GetElementId(self,idtext):
        return self.wait.until(EC.element_to_be_clickable(By.ID,idtext))

# def SendText(driver,wait,_id,text):
#     e= wait.until(EC.element_to_be_clickable(By.ID,_id))
#     e.clear()
#     e.send_keys(text)
#     driver.implicitly_wait(5)



# def Click(driver,wait,id):
#     e=wait.until(EC.element_to_be_clickable((By.ID,id)))
#     e.click()


