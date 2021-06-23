import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PolyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/automation/chromedriver')
        url = 'https://www.migdal.co.il/mymigdal/process/login'
        self.driver.get(url)
        self.driver.maximize_window()

    #בדיקה 1 נתונים חוקיים
    def test_login(self,tz,phone):
        from pages.login_page import login
        l=login(self.driver)
        l.send_tz_phone(id_text1=tz,num=phone)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

    #בדיקה 2 נתונים לא חוקיים
    def test_login1(self,tz="XX",phone="TC"):
        from pages.login_page import login
        l=login(self.driver)
        l.send_tz_phone(id_text1=tz,num=phone)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

        # בדיקה 3 שדות ריקים
    def test_login2(self, tz=None, phone=None):
        from pages.login_page import login
        l = login(self.driver)
        l.send_tz_phone(id_text1=tz, num=phone)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

        #בדיקה קוד ריק
    def test_code1(self, code=None):
        from pages.code_page import Code_Page
        CP = Code_Page(self.driver)
        CP.send_code(code)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

        #בדיקה קוד תקין
        #בהנחה XXX זה הקוד שהתקבל
    def test_code2(self, code='xxx'):
        from pages.code_page import Code_Page
        CP = Code_Page(self.driver)
        CP.send_code(code)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

        # בדיקה קוד שגוי
        # בהנחה XXX זה הקוד שהתקבל
    def test_code3(self, code='12x'):
        from pages.code_page import Code_Page
        CP = Code_Page(self.driver)
        CP.send_code(code)
        #יש להשוות כאן תגובה להגדרה מראש על מנת לוודא אם הטסט עבר או לא
        # assert In reasualts

        #בדיקה של הורדת קובץ
    def test_download(self):
        from pages.personal_area_page import PersonalArea
        p=PersonalArea(self.driver)

        #קבלת ההודעה אחרי הורדת הקובץ
        mp=p.down_policy().text

        #השןןאת ההודעה להודעה שאמורה להיות
        self.assertIs("Done successfully", mp)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()