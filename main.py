from ast import For
import platform
import socket
import requests
from pyfiglet import Figlet
from colorama import Fore, init
import tkinter as tk
from pyautogui import screenshot
import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar
import msvcrt
import numpy as np
import cv2
import pywhatkit
import smtplib
from email.message import EmailMessage
from datetime import datetime
import getpass
from playsound import playsound


os.chdir(sys.path[0]) 
root = tk.Tk()
root.withdraw()
os.system("cls")
init()


class Weather():
    def __init__(self):
        
        options = Options()
        options.page_load_strategy = 'none'
        self.browser = webdriver.Firefox(options=options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)


    def get_weather(self, city):
        wait = WebDriverWait(self.browser, 5)
        self.browser.get("https://www.google.com/search?q=weather+" + city)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wob_dc')))
        self.browser.execute_script("window.stop();")

        self.browser.find_element(by=By.CSS_SELECTOR, value="div.vk_bk:nth-child(2) > span:nth-child(1)").click()
        temperature_C = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_tm").text
        temperature_F = str(int(int(temperature_C) * 1.8 + 32))

        city_name = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_loc").text
        last_update = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_dts").text
        precipitation = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_pp").text
        humidity = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_hm").text
        wind = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_ws").text
        caption = self.browser.find_element(by=By.CSS_SELECTOR, value="#wob_dc").text
        air_quality, air_quality_caption = self.air_quality(city)

        return [city_name, temperature_C, temperature_F, caption, precipitation, humidity, wind, air_quality, air_quality_caption, last_update]


    def air_quality(self, city):
        self.browser.get("https://www.google.com/search?q=google+air+quality+" + city)
        sleep(2)
        self.browser.find_element(by=By.CSS_SELECTOR, value="div.g:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(2)").click()
        sleep(5)
        q = self.browser.find_element(by=By.CSS_SELECTOR, value=".aqi-value__value").text
        caption = self.browser.find_element(by=By.CSS_SELECTOR, value=".aqi-status__text").text
        return q, caption


    def end(self):
        self.browser.close()


def start():
    f = Figlet(font='doom')
    print(Fore.GREEN + f.renderText('python apps'))

    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}1. {Fore.WHITE}Weather', f'{Fore.GREEN}2. {Fore.WHITE}Calender', f'{Fore.GREEN}3. {Fore.WHITE}Coins'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}4. {Fore.WHITE}Screenshot', f'{Fore.GREEN}5. {Fore.WHITE}Screen recorder', f'{Fore.GREEN}6. {Fore.WHITE}Whatsapp message'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}7. {Fore.WHITE}Email', f'{Fore.GREEN}8. {Fore.WHITE}Calculator', f'{Fore.GREEN}9. {Fore.WHITE}Ip address'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}10. {Fore.WHITE}Alarm', f'{Fore.GREEN}11. {Fore.WHITE}Clock', f'{Fore.GREEN}12. {Fore.WHITE}Corona statistics'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}13. {Fore.WHITE}Base converter', f'{Fore.GREEN}14. {Fore.WHITE}Text to morse code', f'{Fore.GREEN}15. {Fore.WHITE}Convert images to pdf'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}16. {Fore.WHITE}Random number', f'{Fore.GREEN}17. {Fore.WHITE}Text to speech', f'{Fore.GREEN}18. {Fore.WHITE}Internet connection'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}19. {Fore.WHITE}Hangman', f'{Fore.GREEN}20. {Fore.WHITE}Notes', f'{Fore.GREEN}21. {Fore.WHITE}Convert to zip file'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}22. {Fore.WHITE}Calculate age', f'{Fore.GREEN}23. {Fore.WHITE}Password generator', f'{Fore.GREEN}24. {Fore.WHITE}Tic Tac Toe'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}25. {Fore.WHITE}BMI', f'{Fore.GREEN}26. {Fore.WHITE}Image to ascii', f'{Fore.GREEN}27. {Fore.WHITE}Read text'))
    print()


def choose():
    a = input("\n" + Fore.RED + ">> " + Fore.WHITE + "Enter the number of the program you want to run | 0 for exit: ")
    try:
        a = int(a)
        if not 0 <= a < 28:
            raise Exception
    except:
        print((Fore.YELLOW + "! " + Fore.WHITE + 'Please Enter valid number'))
        choose()
    return a


def screen_shot():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Screenshot'))
    path = input(Fore.WHITE + "Enter the image path and file name: ")
    screen = screenshot(path)
    return screen


def weather():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Weather'))
    city = input(Fore.WHITE + "Enter the name of the city: ")

    bot = Weather()
    city_name, temperature_C, temperature_F, caption, precipitation, humidity, wind, air_quality, air_quality_caption, last_update = bot.get_weather(city)
    bot.end()

    # print(Fore.GREEN + city_name)
    print(Fore.MAGENTA + temperature_C + " C\t" + temperature_F + " F")
    print(Fore.WHITE + caption + "\n")

    print(Fore.CYAN + "Precipitation: " + Fore.WHITE + precipitation)
    print(Fore.CYAN + "Humidity: " + Fore.WHITE + humidity)
    print(Fore.CYAN + "Wind: " + Fore.WHITE + wind + "\n")

    print(Fore.MAGENTA + "Air quality: " + Fore.WHITE + air_quality + " - " + air_quality_caption + "\n")


def show_calendar():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Calendar') + Fore.WHITE)
    month = datetime.now().month
    year = datetime.now().year
    print(calendar.month(year, month))


def coins():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Coins') + Fore.WHITE)
    coin = input("Enter your coin name: ")
    url = f"https://api.coincap.io/v2/assets/{coin}"
    data = requests.get(url).json()["data"]
    print(Fore.CYAN + "Name: " + Fore.WHITE + data['id'])
    print(Fore.CYAN + "Symbol: " + Fore.WHITE + data['symbol'])
    print(Fore.CYAN + "Price: " + Fore.WHITE + data['priceUsd'][:8] + "$")


def record():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Reccord screen') + Fore.WHITE)
    path = input("Enter the path: ")
    print(Fore.CYAN + "Recording started. stop with Enter")
    count = 0
    img_array = []
    status = True

    while status:
        count += 1
        if msvcrt.kbhit():
            status = False

        img = screenshot()
        img = np.array(img) [:, :, ::-1]
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
    else:
        os.chdir(path)
        out = cv2.VideoWriter('screen-recorder.avi',
                                cv2.VideoWriter_fourcc(*'DIVX'), 24, size)
        for i in img_array:
            out.write(i)
        
        out.release()


def send_whatsapp_message():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Whatsapp message') + Fore.WHITE)
    h, m = [int(i) for i in input("Enter the time to send the message(e.g 22:04): ").split(":")]
    phone_number = input("Enter the recipient's phone number(e.g +98xxxxxxxxx): ")
    message = input("Enter the message: ")
    pywhatkit.sendwhatmsg(phone_number, message, h, m)
    print(Fore.GREEN + "Message sent successfully")


def mail():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Send email') + Fore.WHITE)

    msg = EmailMessage()

    msg['From'] = input("Enter your email address: ")
    msg['To'] = input("Enter the recipient's email address: ")
    password = getpass.getpass('Enter your email password: ')
    msg['Subject'] = input('Enter your email subject: ')
    msg.set_content(input("Enter your message: "))

    with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
        smtp.login(msg['From'], password)
        smtp.send_message(msg)


def calculator():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Calc') + Fore.WHITE)
    a = input("Enter the math expression: ")
    print(Fore.CYAN + "Answer: " + Fore.WHITE + str(eval(a)))



def ip():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Ip') + Fore.WHITE)

    os_name = platform.system()
    ip_ = socket.gethostbyname(socket.gethostname())    
    print(Fore.WHITE + "Your ip: " + Fore.CYAN + str(ip_))
    print(Fore.WHITE + "Your OS name: " + Fore.CYAN + str(os_name))


def alarm():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Alarm') + Fore.WHITE)
    h, m = [int(i) for i in input("Enter the alarm time: ").split(":")]
    while True:
        now_m = datetime.now().minute
        now_h = datetime.now().hour
        if now_m == m and now_h == h:
            os.system('Alarm05.wav')
            break
        sleep(5)


def clock():
    f = Figlet(font='standard')
    print(Fore.WHITE  + f.renderText(f'{datetime.now().hour} : {datetime.now().minute}') + Fore.WHITE)
    print(Fore.WHITE + datetime.now().strftime("%d/%m/%Y") + "\t" + Fore.CYAN + datetime.today().strftime('%A') + Fore.WHITE)

    

start()
while True:
    selected = choose()

    if selected == 0:
        sys.exit()
    elif selected == 1:
        weather()
    elif selected == 2:
        show_calendar()
    elif selected == 3:
        coins()
    elif selected == 4:
        screen_shot()
    elif selected == 5:
        record()
    elif selected == 6:
        send_whatsapp_message()
    elif selected == 7:
        mail()
    elif selected == 8:
        calculator()
    elif selected == 9:
        ip()
    elif selected == 10:
        alarm()
    elif selected == 11:
        clock()
    elif selected == 12:
        pass
    elif selected == 13:
        pass
    elif selected == 14:
        pass
    elif selected == 15:
        pass
    elif selected == 16:
        pass
    elif selected == 17:
        pass
    elif selected == 18:
        pass
    elif selected == 19:
        pass
    elif selected == 20:
        pass
    elif selected == 21:
        pass
    elif selected == 22:
        pass
    elif selected == 23:
        pass
    elif selected == 24:
        pass
    elif selected == 25:
        pass
    elif selected == 26:
        pass
    elif selected == 27:
        pass

    sleep(1)
