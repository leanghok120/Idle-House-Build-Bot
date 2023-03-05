import pyautogui
import keyboard
import time
import win32api, win32con

"""
A python bot that plays Idle Build House
This is made by Leanghok

My socials
{
    GitHub: https://github.com/leanghok120
    Discord: Astrox#2678
}

Cords
{
    The coordinates of the house: X:  660 Y:  559 RGB: (222, 121,  89)
    The coordinates of the collect button: X: 1254 Y:  557 RGB: (255, 250, 190)
    The coordinates of the House size upgrade button: X: 1386 Y:  383 RGB: ( 30, 180,  30)
    The coordinates of the Bricks per click upgrade button: X: 1387 Y:  308 RGB: ( 30, 180,  30)
    The coordinates of the Play button: X:  792 Y:  571 RGB: (104,  66, 255)
    The coordinates of the first collect button: X:  791 Y:  577 RGB: (104,  66, 255)
}
"""

bot = False
time.sleep(5)


# The main bot loop
def main():
    print(
        """                                                                                                                                  
,--.   ,--.,--.           ,--.  ,--.                                 ,-----.          ,--.,--.   ,--.    ,-----.           ,--.   
|  | ,-|  ||  | ,---.     |  '--'  | ,---. ,--.,--. ,---.  ,---.     |  |) /_ ,--.,--.`--'|  | ,-|  |    |  |) /_  ,---. ,-'  '-. 
|  |' .-. ||  || .-. :    |  .--.  || .-. ||  ||  |(  .-' | .-. :    |  .-.  \|  ||  |,--.|  |' .-. |    |  .-.  \| .-. |'-.  .-' 
|  |\ `-' ||  |\   --.    |  |  |  |' '-' ''  ''  '.-'  `)\   --.    |  '--' /'  ''  '|  ||  |\ `-' |    |  '--' /' '-' '  |  |   
`--' `---' `--' `----'    `--'  `--' `---'  `----' `----'  `----'    `------'  `----' `--'`--' `---'     `------'  `---'   `--'   
                                                                                                                                  """
    )
    print("\n(+) Bot: Enabled\nPress shift+r to toggle bot\nPress Esc to exit")

    redirectWebsite()
    while not keyboard.is_pressed("Esc"):
        if bot:
            autoBuild()
            autoUpgrade()

    print("(+) Bot: Disabled\n")


# This function will turn on the bot when you press shift+r
def toggle_bot():
    global bot
    bot = not bot


keyboard.add_hotkey("shift+r", toggle_bot)


# This function will click on the house and press enter when the collect button appears
def autoBuild():
    click(660, 559)
    if pyautogui.pixelMatchesColor(1254, 557, (255, 250, 190)):
        keyboard.press_and_release("enter")
        time.sleep(0.5)


# This function will redirect you to the Idle house build website
def redirectWebsite():
    print("(+) Going the website...")
    keyboard.press_and_release("ctrl+l")
    time.sleep(0.5)
    keyboard.write("https://www.crazygames.com/game/idle-house-build")
    time.sleep(0.5)
    keyboard.press_and_release("enter")
    time.sleep(2.5)
    click(792, 571)
    time.sleep(7)
    click(791, 577)


# This function will click on the upgrade
def autoUpgrade():
    if pyautogui.pixelMatchesColor(1386, 383, (30, 180, 30)):
        click(1386, 383)
        time.sleep(0.5)
    if pyautogui.pixelMatchesColor(1387, 308, (30, 180, 30)):
        click(1387, 308)
        time.sleep(0.5)
    if pyautogui.pixelMatchesColor(
        1386, 383, (30, 180, 30)
    ) and pyautogui.pixelMatchesColor(1387, 308, (30, 180, 30)):
        click(1387, 308)
        time.sleep(0.5)


# Just a normal click function
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.00001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


if __name__ == "__main__":
    main()
