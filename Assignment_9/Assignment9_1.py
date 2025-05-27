import threading
import time

def DisplayNumbers(iNo):
    for i in range(1,iNo+1):
        print(i,end = "")
        
    time.sleep(1)

   
def main():


    thread1 = threading.Thread(target = DisplayNumbers,args = (5,))
    
    thread2 = threading.Thread(target = DisplayNumbers,args = (5,))
    
    thread3 = threading.Thread(target = DisplayNumbers,args = (5,))

    start_time1 = time.time()
    thread1.start()
    thread1.join()
    time.sleep(1)
    end_time1 = time.time()

    total_time1 = end_time1 - start_time1


    start_time2 =  time.time()
    thread2.start()
    thread2.join()
    time.sleep(1)
    end_time2 = time.time()

    total_time2 = end_time2 - start_time2

    start_time3 =  time.time()
    thread3.start()
    thread3.join()
    time.sleep(1)
    end_time3 = time.time()

    total_time3 = end_time3 - start_time3


    print(total_time1,total_time2,total_time3)

if __name__ == "__main__":
    main()