import os
import time
import schedule

def Greetings():
    print("Namaskaram.....!")

def main():
    schedule.every().day.at("9:00").do(Greetings)

    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()