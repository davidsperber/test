import requests

#הנחת יסוד: השרת בודק את נתוני ההודעה שנשלחים אליו ולפי זה מחזיר תשובה תקין או משהו אחר
#הנחת יסוד השרת מבצע בדיקות מול
#DB על מנת לוודא תקינות נתונים

def sendData(tz,num):
    url = 'https://www.migdal.co.il/mymigdal/process/login'
    data={
        'id':tz,
        'phone':num
    }
    response = requests.post(url,data)

    #במידה וקוד תקינות משרת 200 אזי:
    if response.status_code==200:
        return (f" נתוני משתמש תקינים (phone: {num} tz: {tz})".format(tz, num))
    else:
        #במידה וישנה תשובה אחרת מחזיר את הקוד ססטוס עצמו
        return (response.status_code)



tz='035718592'
num='0556632661'
print(sendData(tz,num))

# if sendData(tz,num)==200:
#     print(f"נתוני משתמש תקינים (phone: {num} tz: {tz})".format(tz,num))
# else:
#     print(sendData())
#     print(f"נתוני משתמש לא תקינים (phone: {num} tz: {tz})".format(tz, num))

