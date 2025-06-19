import schedule
import time
import datetime
import shutil


def BackUp():

    SourceFile = 'Marvellous.txt'
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    BackUpFile = f"backup_log_{timestamp}.txt"


    shutil.copy2(SourceFile,BackUpFile)

    

    print(f"Backup completed : {BackUpFile}.")

    

def main():

    schedule.every(20).seconds.do(BackUp)

    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()