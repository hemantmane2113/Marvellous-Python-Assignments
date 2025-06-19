import schedule
import time

def MySchedule():
    print("Jay Ganesh...!")

def main():

    schedule.every(2).seconds.do(MySchedule)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    


if __name__ == "__main__":
    main()


# task- asking my friend to remind me to drink water say after every 15 minutes.
#Python Code	                                                     Analogy
#schedule.every(15).minutes.do.(remainder)	             You telling your friend: “Remind me...”
#schedule.run_pending()	                                 Your friend checking the clock
#time.sleep(60)	                                         Your friend taking a break before checking
#time.sleep(60) tells friend as "check the clock after every 60 seconds and see whether 
#15 minutes are over or not.Without time.sleep(60) the friend will keep looking at the look
## continously and by doing this the friend will get exhausted.

#🟡 schedule.every(15).minutes.do(reminder)

#👉 This is you telling your friend the plan.
#🗓️ "Remind me every 15 minutes!"

#   It's just setting the schedule

#   Your friend remembers your instruction but does nothing yet

#🟢 schedule.run_pending()

#👉 This is your friend checking the clock.
#🕒 "Is it 15 minutes yet? Should I remind?"

#    He checks, and if the time matches, he tells you:
#    "Hey! Time to drink water!"

#🔵 time.sleep(t)

#👉 This is your friend taking a nap or relaxing before checking the clock again.

#    😴 Sleeps for t seconds to avoid looking at the clock every microsecond