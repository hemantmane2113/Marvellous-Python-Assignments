import os
import schedule
import time

def FileLogging():

    FileName = "Marvellous.txt"

    fobj = open(FileName,'a')

    current_time = time.ctime()

    fobj.write(str(current_time)+ "\n")# write expects string while current_time is float

    print("noted..!")

    fobj.close()


def main():

    schedule.every(5).minutes.do(FileLogging)


    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()