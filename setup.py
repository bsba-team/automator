import os

file = "config.py"

def warn():
    print("If you see those texts as symbols or byte codes, please execute command below in Powershell as admin:")
    print("Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1")


def start():
    print("Setup Process is still in beta phase!")
    print("For any further problems or bugs,")
    print("Please, contact with the creator:")

def backup(file):
    if os.path.exists(file):
        os.replace(file, file + ".backup")
    else:
        print("There is no older file to backup")

def setup(file):
    bot_token = input(
        "Copy and paste here Telegram bot's token: ")
    bot_username = input(
        "Enter bot's username: ")
    bot_id = input(
        "Enter bot's chat id: ")
    admin_username = input(
        "Enter admin's username: ")
    admin_id = input(
        "Enter admin's chat id: ")
    admin_nickname = input(
        "Enter admin's nickname: ")

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
