import os, sys
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, init
import tkinter as tk


tk.Tk().withdraw()
os.chdir(sys.path[0]) 
os.system("cls")
init()


class Weather():
    def __init__(self):
        from selenium.webdriver.firefox.options import Options
        from selenium import webdriver

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.page_load_strategy = 'none'
        self.browser = webdriver.Firefox(options=options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)


    def get_weather(self, city):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

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
        # air_quality, air_quality_caption = self.air_quality(city)

        return [city_name, temperature_C, temperature_F, caption, precipitation, humidity, wind, last_update]


    def air_quality(self, city):
        from selenium.webdriver.common.by import By

        self.browser.get("https://www.google.com/search?q=air+quality+" + city + "+site:iqair.com")
        sleep(2)
        self.browser.find_element(by=By.CSS_SELECTOR, value="#rso > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(2)").click()
        sleep(5)
        q = self.browser.find_element(by=By.CSS_SELECTOR, value=".aqi-value__value").text
        caption = self.browser.find_element(by=By.CSS_SELECTOR, value=".aqi-status__text").text
        return q, caption

    def end(self):
        self.browser.close()


def start():
    f = Figlet(font='doom')
    print(Fore.GREEN + f.renderText('python apps'))

    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}1. {Fore.WHITE}Clock', f'{Fore.GREEN}2. {Fore.WHITE}Calender', f'{Fore.GREEN}3. {Fore.WHITE}Alarm'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}4. {Fore.WHITE}Weather', f'{Fore.GREEN}5. {Fore.WHITE}Coins', f'{Fore.GREEN}6. {Fore.WHITE}Corona statistics'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}7. {Fore.WHITE}Base converter', f'{Fore.GREEN}8. {Fore.WHITE}Calculator', f'{Fore.GREEN}9. {Fore.WHITE}Random number'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}10. {Fore.WHITE}Images to pdf', f'{Fore.GREEN}11. {Fore.WHITE}Image to ascii', f'{Fore.GREEN}12. {Fore.WHITE}Convert to zip'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}13. {Fore.WHITE}Ip address', f'{Fore.GREEN}14. {Fore.WHITE}System info', f'{Fore.GREEN}15. {Fore.WHITE}Keylogger'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}16. {Fore.WHITE}Internet connection', f'{Fore.GREEN}17. {Fore.WHITE}TODO', f'{Fore.GREEN}18. {Fore.WHITE}Password generator'))
    print("%-33s %-33s %-33s" % (f'{Fore.GREEN}19. {Fore.WHITE}Email', f'{Fore.GREEN}20. {Fore.WHITE}Whatsapp message', f'{Fore.GREEN}21. {Fore.WHITE}Hangman'))
    print("%-33s %-33s" % (f'{Fore.GREEN}22. {Fore.WHITE}ScreenShot', f'{Fore.GREEN}23. {Fore.WHITE}Screen recorder'))
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
    from pyautogui import screenshot

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Screenshot'))
    path = input(Fore.WHITE + "Enter the image path and file name: " + Fore.CYAN)
    screen = screenshot(path)
    return screen


def weather():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Weather'))

    city = input(Fore.WHITE + "Enter the name of the city: " + Fore.CYAN)

    bot = Weather()
    city_name, temperature_C, temperature_F, caption, precipitation, humidity, wind, last_update = bot.get_weather(city)
    bot.end()

    # print(Fore.GREEN + city_name)
    print(Fore.CYAN + temperature_C + " C\t" + temperature_F + " F")
    print(Fore.WHITE + caption + "\n")

    print(Fore.CYAN + "Precipitation: " + Fore.WHITE + precipitation)
    print(Fore.CYAN + "Humidity: " + Fore.WHITE + humidity)
    print(Fore.CYAN + "Wind: " + Fore.WHITE + wind + "\n")

    # print(Fore.MAGENTA + "Air quality: " + Fore.WHITE + air_quality + " - " + air_quality_caption + "\n")


def show_calendar():
    from datetime import datetime
    import calendar

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Calendar') + Fore.WHITE)

    month = datetime.now().month
    year = datetime.now().year
    print(calendar.month(year, month))


def coins():
    import requests

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Coins') + Fore.WHITE)

    coin = input(Fore.WHITE + "Enter your coin name: " + Fore.CYAN).lower()
    url = f"https://api.coincap.io/v2/assets/{coin}"
    data = requests.get(url).json()["data"]
    print(Fore.CYAN + "Name: " + Fore.WHITE + data['id'])
    print(Fore.CYAN + "Symbol: " + Fore.WHITE + data['symbol'])
    print(Fore.CYAN + "Price: " + Fore.WHITE + data['priceUsd'][:8] + "$")


def record():
    import msvcrt
    from pyautogui import screenshot
    import numpy as np
    import cv2

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Reccord screen') + Fore.WHITE)

    path = input("Enter the path: " + Fore.CYAN)
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
        
        height, width = img.shape[:2]
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
    import pywhatkit

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Whatsapp message') + Fore.WHITE)

    h, m = [int(i) for i in input("Enter the time to send the message(e.g 22:04): " + Fore.CYAN).split(":")]
    phone_number = input(Fore.WHITE + "Enter the recipient's phone number(e.g +98xxxxxxxxx): " + Fore.CYAN)
    message = input("Enter the message: ")
    pywhatkit.sendwhatmsg(phone_number, message, h, m)
    print(Fore.GREEN + "Message sent successfully")


def mail():
    import getpass
    import smtplib
    from email.message import EmailMessage

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Send email') + Fore.WHITE)

    msg = EmailMessage()

    msg['From'] = input(Fore.WHITE + "Enter your email address: " + Fore.CYAN)
    msg['To'] = input(Fore.WHITE + "Enter the recipient's email address: " + Fore.CYAN)
    password = getpass.getpass(Fore.WHITE + 'Enter your email password: ' + Fore.CYAN)
    msg['Subject'] = input(Fore.WHITE + 'Enter your email subject: ' + Fore.CYAN)
    msg.set_content(input(Fore.WHITE + "Enter your message: " + Fore.CYAN))

    with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
        smtp.login(msg['From'], password)
        smtp.send_message(msg)


def calculator():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Calc') + Fore.WHITE)

    a = input(Fore.WHITE + "Enter the math expression: " + Fore.CYAN)
    print(Fore.CYAN + "Answer: " + Fore.WHITE + str(eval(a)))


def ip():
    import socket

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Ip') + Fore.WHITE)

    ip_ = socket.gethostbyname(socket.gethostname())    
    print(Fore.WHITE + "Your ip: " + Fore.CYAN + str(ip_))


def alarm():
    from datetime import datetime

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Alarm') + Fore.WHITE)

    h, m = [int(i) for i in input(Fore.WHITE + "Enter the alarm time: " + Fore.CYAN).split(":")]
    while True:
        now_m = datetime.now().minute
        now_h = datetime.now().hour
        if now_m == m and now_h == h:
            os.system('Alarm05.wav')
            break
        sleep(5)


def clock():
    from datetime import datetime

    f = Figlet(font='standard')
    print(Fore.WHITE  + f.renderText(f'{datetime.now().hour} : {datetime.now().minute}') + Fore.WHITE)
    print(Fore.WHITE + datetime.now().strftime("%d/%m/%Y") + "\t" + Fore.CYAN + datetime.today().strftime('%A') + Fore.WHITE)


def covid():
    from covid import Covid

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Covid 19') + Fore.WHITE)

    covid = Covid()
    country = input(Fore.WHITE + 'Enter your country: ' + Fore.CYAN)
    data = covid.get_status_by_country_name(country)
    print(Fore.RED + "Deaths: " + str(data['deaths']) + Fore.CYAN + "\t Confirmed: " + str(data['confirmed']))


def timer():
    import time

    t = int(input())
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print( Fore.CYAN + 'Timer completed!')


def base_converter():
    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Base converter') + Fore.WHITE)

    a, b, b2 = input(Fore.WHITE + "Enter the number, the base of the number and the base of the destination with a space: " + Fore.CYAN).split()
    b, b2 = int(b), int(b2)
    n = int(a, b)

    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    
    while n:
        result += a[n % b2]
        n //= b2
    result = result[::-1]
    print(Fore.WHITE + "Result: " + Fore.CYAN + str(result))


def images_to_pdf():
    from tkinter.filedialog import askopenfilenames
    import img2pdf

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('PDF converter') + Fore.WHITE)

    files = askopenfilenames(filetypes=[("Text Files", "*.jpg *.png"), ("All Files", "*.*")])
    result_name = input(Fore.WHITE + "Enter result file path and file name(e,.g C:/result.pdf): " + Fore.CYAN)

    with open(f"{result_name}", 'ab') as f:
        f.write(img2pdf.convert(files))


def system_info():
    import platform

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('System info') + Fore.WHITE)

    my_system = platform.uname()
    print(f"{Fore.CYAN}System: {Fore.WHITE}{my_system.system}")
    print(f"{Fore.CYAN}Node Name: {Fore.WHITE}{my_system.node}")
    print(f"{Fore.CYAN}Release: {Fore.WHITE}{my_system.release}")
    print(f"{Fore.CYAN}Version: {Fore.WHITE}{my_system.version}")
    print(f"{Fore.CYAN}Machine: {Fore.WHITE}{my_system.machine}")
    print(f"{Fore.CYAN}Processor: {Fore.WHITE}{my_system.processor}")


def random_number():
    import random

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Random') + Fore.WHITE)

    a, b = map(int, input(Fore.WHITE + "Enter a range of numbers(e.g 1 100): " + Fore.CYAN).split())
    print(Fore.WHITE + "Random number: " + Fore.CYAN + str(random.randint(a, b)))



def internet_connection():
    import speedtest

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Speed Test') + Fore.WHITE)

    test = speedtest.Speedtest()
    download = test.download()
    upload = test.upload()
    print(f"{Fore.CYAN}Download speed: {Fore.WHITE}{download}")
    print(f"{Fore.CYAN}Upload speed: {Fore.WHITE}{upload}")


def image_to_ascii():
    from tkinter.filedialog import askopenfilename
    from PIL import Image

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Image to ascii') + Fore.WHITE)

    image_path = askopenfilename(filetypes=[("Text Files", "*.jpg *.png"), ("All Files", "*.*")])

    img = Image.open(image_path)

    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    pixels = img.getdata()

    chars = ["B","S","#","&","@","$","%","*","!",":","."]

    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)


def convert_to_zip():
    from zipfile import ZipFile
    from tkinter.filedialog import askopenfilenames

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Zip converter') + Fore.WHITE)

    files = askopenfilenames(filetypes=[("All Files", "*.*")])
    result = input(Fore.WHITE + "Enter result file path: " + Fore.CYAN)

    z = ZipFile(result , 'w')
    z.close()

    z = ZipFile(result , 'w')
    for f in files:
        z.write(f)

    z.close()


def keylogger():
    import keyboard

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Keylogger') + Fore.WHITE)

    print("You can stop keylogger with press 'esc'")
    r = keyboard.record(until="esc")
    keyboard.play(r, speed_factor=2)


def todo():
    from terminaltables import AsciiTable

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('TODO') + Fore.WHITE)

    data = open("TODO.txt", "r+", encoding='utf8')
    ls = data.readlines()

    table_data = [
        ["TODO", "Done"]
    ]
    table_data2 = [
        ["TODO", "Done"]
    ]

    print(f"{Fore.CYAN}Add{Fore.WHITE}")
    print(f"{Fore.CYAN}Delete{Fore.WHITE}")
    print(f"{Fore.CYAN}Done{Fore.WHITE}")
    print(f"{Fore.CYAN}show{Fore.WHITE}")
    print(f"{Fore.CYAN}exit{Fore.WHITE}")

    for i in ls:
        try:
            item, ok = i.split(" | ")

            if "✓" in ok:
                ok = "✓" + "\n"
                ok2 = Fore.GREEN + "✓" + Fore.WHITE + "\n"
            else:
                ok = "✘" + "\n"
                ok2 = Fore.RED + "✘" + Fore.WHITE + "\n"

            table_data.append([item, ok])
            table_data2.append([item, ok2])
        except: pass

    table = AsciiTable(table_data2)
    print("\n" + table.table + "\n")

    l = True
    while l:
        a = input(Fore.WHITE + "\nEnter code: " + Fore.CYAN).split()
        print(Fore.WHITE, end="")

        if a[0].lower() == "add":
            text = input(Fore.WHITE + "Enter your TODO: " + Fore.CYAN)
            table_data.append([text, f"✘\n"])
            table_data2.append([text, f"{Fore.RED}✘{Fore.WHITE}\n"])
        elif a[0].lower() == "delete":
            n = int(input(Fore.WHITE + "Enter the TODO number you want to delete: " + Fore.CYAN))
            del table_data[n]
            del table_data2[n]
        elif a[0].lower() == "done":
            n = int(input(Fore.WHITE + "Enter the number of the todo you did: " + Fore.CYAN))
            table_data[n][1] = "✓"
            table_data2[n][1] = f"{Fore.GREEN}✓{Fore.WHITE}"
        elif a[0].lower() == "show":
                table = AsciiTable(table_data2)
                print(f"{Fore.WHITE}\n" + table.table + "\n")
        elif a[0].lower() == "exit":
            l = False

    r = '\n'.join([f"{item} | {ok}"  for item, ok in table_data[1:]])
    data.write(r)
    data.close()


def password():
    from random import choice

    f = Figlet(font='standard')
    print(Fore.CYAN  + f.renderText('Password generator') + Fore.WHITE)

    characters = "4!@597#6$%^8&*1(0)32_+"
    result = ""
    
    n = int(input(Fore.WHITE + "Enter the number of characters: " + Fore.CYAN))
    for i in range(n):
        result += choice(list(characters))
    print("Result: " + Fore.WHITE + result)
    

class Hangman():
    def __init__(self) -> None:
        f = Figlet(font='standard')
        print(Fore.CYAN  + f.renderText('Hangman') + Fore.WHITE)

        self.animals = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'horse']
        self.numbers = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.colors = ['red', 'blue', 'white', 'black', 'green', 'yellow', 'orange', 'cyan']

        self.word = []
        self.correct_word = ''
        self.l = 0


    def select_word(self):
        import random

        group = input("Enter the group of words(numbers, colors, animals): " + Fore.CYAN)
        print(Fore.WHITE, end="")
        if 'animals' in group.lower():
            self.correct_word = random.choice(self.animals)
        elif 'numbers' in group.lower():
            self.correct_word = random.choice(self.numbers)
        else:
            self.correct_word = random.choice(self.colors)
        
        self.word = ['-'] * len(self.correct_word)


    def hangman_drawer(self):
        print(Fore.WHITE + "life: ", 5 - self.l)
        if self.l == 1:
            print(Fore.RED + "   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        elif self.l == 2:
            print(Fore.RED + "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        elif self.l == 3:
            print(Fore.RED + "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    / \ \n"
                "  |      \n"
                "__|__\n")
        elif self.l == 4:
            print(Fore.RED + "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |      \n"
                "__|__\n")
        elif self.l == 5:
            print(Fore.WHITE + "life: ", 5 - self.l)
            print(Fore.RED + "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
            print(Fore.RED + "You lose!")
            print(f'{Fore.WHITE}The word was: {Fore.CYAN}{self.correct_word}')
            return False
        return True


    def guess(self):
        w = ' '.join(self.word)
        print(f'\n{Fore.CYAN}{w}')
        letter = input(Fore.WHITE + "Guess a letter: " + Fore.CYAN).lower()

        if letter in self.correct_word:
            j = 0
            for i in self.correct_word:
                if i == letter:
                    self.word[j] = letter.capitalize()
                j += 1
            print(Fore.GREEN + f"Yes! {letter.capitalize()} is in the word :)\n")
        else:
            print(Fore.RED + f"No! {letter.capitalize()} is not in the word :(\n")
            self.l += 1
            return self.hangman_drawer()

        if ''.join(self.word).lower() == self.correct_word:
            print(f"\n{Fore.GREEN}You have won!{Fore.WHITE}")
            return False
        return True


start()
while True:
    selected = choose()

    if selected == 0:
        break
    elif selected == 1:
        clock()
    elif selected == 2:
        show_calendar()
    elif selected == 3:
        alarm()
    elif selected == 4:
        weather()
    elif selected == 5:
        coins()
    elif selected == 6:
        covid()
    elif selected == 7:
        base_converter()
    elif selected == 8:
        calculator()
    elif selected == 9:
        random_number()
    elif selected == 10:
        images_to_pdf()
    elif selected == 11:
        image_to_ascii()
    elif selected == 12:
        convert_to_zip()
    elif selected == 13:
        ip()
    elif selected == 14:
        system_info()
    elif selected == 15:
        keylogger()
    elif selected == 16:
        internet_connection()
    elif selected == 17:
        todo()
    elif selected == 18:
        password()
    elif selected == 19:
        mail()
    elif selected == 20:
        send_whatsapp_message()
    elif selected == 21:
        hangman = Hangman()
        hangman.select_word()
        life = True
        while life:
            life = hangman.guess()
    elif selected == 22:
        screen_shot()
    elif selected == 23:
        record()

print(Fore.RED + "Good bye :)")
