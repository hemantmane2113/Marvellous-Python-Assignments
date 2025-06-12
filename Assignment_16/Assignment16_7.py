import os

def File_Handling(Name_Of_File):

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File { Name_Of_File} exists.")

        fobj = open(Name_Of_File,'r')#when the file opens in the prog,cursor is at the beginning
        next(fobj)## move the cursor to the next line as first line is a heading

        student_list = []
        for line in fobj:# move cursor line by line(from second line)
            columns = line.split()# converts data in each line to list
            columns[1] = int(columns[1])#converts second column to int as they are marks
            if columns[1] > 75:#condition
                student_list.append(columns[0])# add name to  a list
            
        
        return student_list

    else:
        print(f"File { Name_Of_File} does not exists.")
        return -1


def main():
    print("Enter the name of file: ")
    Fname = input()

    #File_Handling(Fname)
    
    ret = File_Handling(Fname)

    if ret != -1:
        print("The name of students having marks more than 75 are: ")
        for name in ret:
            print(name)
    else:
        print("Failure")



if __name__ == "__main__":
    main()