import schedule
import time


def CheckMails():

    print("Checking Mails.")


def main():

    schedule.every(10).minutes.do(CheckMails)

    while True:
        schedule.run_pending()
        time.sleep(5)



if __name__ == "__main__":

    main()