import time
from mysql import connector
from selenium import webdriver
import mysql.connector


def get_number():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='whatsapp')  # replace your values
    mycursor = mydb.cursor()
    query = '''SELECT name, mobile FROM mobile'''  # Change Query as per your database
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result


def basic():
    path = r'D:\CODE\whatsapp\library\chromedriver.exe'  # Download chromedriver.exe file and use path of file here
    driver = webdriver.Chrome(path)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    qr = r'http://web.whatsapp.com/'
    driver.get(qr)
    input('Press Enter after scanning QR Code')
    send(driver, get_number())


def send(driver, number):
    total_time = 0
    count = 0
    for i in number:
        start_time = time.time()
        name = i[0]
        no = i[1]
        msg = 'Hello {}'.format(name)  # write your message here
        nurl = '''https://wa.me/{}?text={}'''.format(no, msg)
        driver.get(nurl)
        while 1:
            try:
                button = driver.find_element_by_id('action-button')
                button.click()
                break
            except Exception:
                time.sleep(0.5)
        while 1:
            try:
                text = 'Phone number shared via url is invalid.'
                if text in driver.page_source:
                    print(text)
                    break
                button = driver.find_element_by_class_name('_35EW6')
                button.click()
                time.sleep(1)
                while 1:
                    try:
                        element = '''<path fill="#859479" d="M9.75 7.713H8.244V5.359a.5.5 0 0 0-.5-.5H7.65a.5.5 0 0 
                        0-.5.5v2.947a.5.5 0 0 0 .5.5h.094l.003-.001.003.002h2a.5.5 0 0 0 .5-.5v-.094a.5.5 0 0 
                        0-.5-.5zm0-5.263h-3.5c-1.82 0-3.3 1.48-3.3 3.3v3.5c0 1.82 1.48 3.3 3.3 3.3h3.5c1.82 0 
                        3.3-1.48 3.3-3.3v-3.5c0-1.82-1.48-3.3-3.3-3.3zm2 6.8a2 2 0 0 1-2 2h-3.5a2 2 0 0 1-2-2v-3.5a2 
                        2 0 0 1 2-2h3.5a2 2 0 0 1 2 2v3.5z"></path> '''
                        driver.find_element(element)
                    except Exception:
                        break
                break
            except Exception:
                time.sleep(0.5)
        exe_time = time.time() - start_time
        total_time = total_time + exe_time
        count += 1
        print("Mobile : {} \nMessage : {} \nTime : {}s\n ".format(no, msg, exe_time))
    print("AvgTime : {}\n ".format(total_time / count))


basic()
