import os
from core import Colors

file = "config.py"

def warn():
    print(
        "If you see those texts as symbols or byte codes, please execute command below in Powershell as admin:")
    print(
        "Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1")


def start():
    print(
        Colors.BOLD + Colors.RED + "Setup Process is still in beta phase!" + Colors.END)
    print(
        Colors.BOLD + Colors.YELLOW + "For any further problems or bugs," + Colors.END)
    print(
        Colors.BOLD + Colors.YELLOW + "Please, contact with the creator:" + Colors.END)

def backup(file):
    if os.path.exists(file):
        os.replace(file, file + ".bak")
    else:
        print("There is no older file to backup")

def setup(file):
    bot_token = input(
        Colors.BOLD + Colors.BLUE + "Copy and paste here Telegram bot's token: " + Colors.END)
    bot_username = input(
        Colors.BOLD + Colors.BLUE + "Enter bot's username: " + Colors.END)
    bot_id = input(
        Colors.BOLD + Colors.BLUE + "Enter bot's chat id: " + Colors.END)
    admin_username = input(
        Colors.BOLD + Colors.BLUE + "Enter admin's username: " + Colors.END)
    admin_id = input(
        Colors.BOLD + Colors.BLUE + "Enter admin's chat id: " + Colors.END)
    admin_nickname = input(
        Colors.BOLD + Colors.BLUE + "Enter admin's nickname: " + Colors.END)

    if bot_id == ' ' or bot_id == '':
        return bot_id == 0
    pass

    if admin_id == ' ' or admin_id == '':
        return admin_id == 0

    open(file, "w").close()

    f = open(file, "a")
    f.write("# ======================================" + "\n")
    f.write("#              WARNING!!!               " + "\n")
    f.write("# Don't share your any info with anyone!" + "\n")
    f.write("# ======================================" + "\n")
    f.write("\n")
    f.write("# ======================================================" + "\n")
    f.write(f"TOKEN = '{bot_token}'" + "\n")
    f.write("# ======================================================" + "\n")
    f.write("\n")
    f.write("# =====================" + "\n")
    f.write("# Bot's Information" + "\n")
    f.write("# =====================" + "\n")
    f.write(f"BOT_USERNAME = '{bot_username}'" + "\n")
    f.write(f"BOT_CHATID = {bot_id}" + "\n")
    f.write("\n")
    f.write("# =====================" + "\n")
    f.write("# Admin's Information" + "\n")
    f.write("# =====================" + "\n")
    f.write(f"ADMIN_USERNAME = '{admin_username}'" + "\n")
    f.write(f"ADMIN_CHATID = {admin_id}" + "\n")
    f.write(f"ADMIN_NICKNAME = '{admin_nickname}'" + "\n")
    f.close()


warn()
start()
backup(file)
setup(file)
