import os
import schedule
import datetime
import time


def TimeTeller():
    print("The current date and time is: ",datetime.datetime.now())


def main():

    schedule.every(1).minutes.do(TimeTeller)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()