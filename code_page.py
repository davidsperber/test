# הנחת יסוד
#  מזהה שדה מסוג ID = input_code
#  מזהה שדה מסוג ID = button
# הנחת יסוד שהפוקוס מוגדר כמצו שציך ונשאר כל הזמן על החלון הפעיל
# הנחת יסוד שלבדיקות יש קוד קבוע
from pages.rootObj import *

class Code_Page(object,):
    def __init__(self, driver):
        self.driver = driver

        # שדה הכנסת קוד מסוג ID
        self.input_Code_id = 'input_code'

        # מזהה כפתור מסוג ID
        self.button_id = 'button'

    def send_code(self,code):
        if code != None:
            # הבאת מתודות
            m = Methodos(self.driver)

            #הגדרת אלמנט להזנת קוד
            m.SendText(_id=self.input_Code_id,text=code)

            #לחיצה על כפתור לשליחת הקוד
            m.Click(id=self.button_id)
        else:
            print ("Enter Code not Null")


