#הנחת יסוד
#  מזהה שדה מסוג ID = input_code
#  מזהה שדה מסוג ID = button
#הנחת יסוד שהפוקוס מוגדר כמצו שציך ונשאר כל הזמן על החלון הפעיל
#הנחת יסוד שלבדיקות יש קוד קבוע
#הנחת יסוד מדובר באותו כפתור ששולח נתונים וגורם לקבלת קוד חפ

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.rootObj import *

class login(object):
    def __init__(self,driver):
        #self.wait = WebDriverWait(driver, 15)
        self.driver=driver

        #tz זיהוי אלמנט
        self.tz_id='tz'

        #phone זיהוי אלמנט
        self.phone_id='phone'

        #button  -זיהוי אלמנט
        self.button_id='button'


    def send_tz_phone(self,id_text1,num):
        m = Methodos(self.driver)
        m.SendText(self.tz_id,id_text1)
        m.SendText(self.phone_id, num)
        m.Click(self.button_id)
