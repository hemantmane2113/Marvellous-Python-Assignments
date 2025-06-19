import os
import time
import schedule

def SaySomething():

    print("Do Coding.....!")


def main():

    schedule.every(30).minutes.do(SaySomething)


    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()