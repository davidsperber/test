from pages.rootObj import *

class PersonalArea(object):
    def __init__(self,driver):
        self.driver=driver

        #מזהה כפתור להורדה
        self.download='dl'

    def down_policy(self):
        m = Methodos(self.driver)
        m.Click(self.download)

        #זיהוי הודעה של הצלחת הורדה
        message_id='message'
        message=m.GetElementId(message_id)
        return message





