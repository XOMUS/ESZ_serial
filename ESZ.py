import serial
import os
import time

print("──────────────────────────────────────────────────")
print("─██████████████─██████████████─██████████████████─")
print("─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░░░██─")
print("─██░░██████████─██░░██████████─████████████░░░░██─")
print("─██░░██─────────██░░██─────────────────████░░████─")
print("─██░░██████████─██░░██████████───────████░░████───")
print("─██░░░░░░░░░░██─██░░░░░░░░░░██─────████░░████─────")
print("─██░░██████████─██████████░░██───████░░████───────")
print("─██░░██─────────────────██░░██─████░░████─────────")
print("─██░░██████████─██████████░░██─██░░░░████████████─")
print("─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░░░██─")
print("─██████████████─██████████████─██████████████████─")
print("──────────────────────────────────────────────────")

time.sleep(3)


def clear(): os.system('cls')


clear()


screen = ""
prompt = ""
now = time.localtime()


def serialk():
    try:
        k = input("Введите COM порт:")
        baud = input("Бод:")
        sera = serial.Serial(k, int(baud))
        return ser, port
    except serial.serialutil.SerialException:
        print("Попробуйте снова")
        exit(0)


ser, port = serialk()
clear()


def printToScreen(s):
    global screen, prompt
    clear()
    screen += (s + '\n')
    print(screen)
    print(prompt)


def promptToScreen(p):
    global screen, prompt
    clear()
    print(screen)
    s = input(p)
    prompt = p + s
    return s


time.sleep(3)


while True:
    read = ser.readline().decode('utf-8')[:-2]
    k = promptToScreen("<< ")
    if k == "/exit":
        printToScreen("-- " + k)
        exit(0)
    elif k == "/srl":
        printToScreen("--" + k)
        time.sleep(1)
        clear()
        serialk()
    elif k == "/info":
        printToScreen("--" + "Эта утилита для работы с serial V2.1")
        printToScreen("--" + "/info Эта команда")
        printToScreen("--" + "/exit Выход")
        printToScreen("--" + "/srl Повторный выбор COM порта с настройкой бода")
        printToScreen("--" + "/cls Очистка экрана")
    elif k == "/cls":
        clear()
    elif len(k) > 0 and not k == "/exit" and not k == "/srl" and not k == "/info" and not k == "/cls":
        print("(" + port + ") " + "[%H:%M:%S]", now, end="")
        printToScreen(" << " + k)
        ser.write(k)
    else:
        continue

    if len(read) > 0:
        print("(" + port + ") " + "[%H:%M:%S]", now, end="")
        printToScreen(" >> " + read)
    else:
        continue

