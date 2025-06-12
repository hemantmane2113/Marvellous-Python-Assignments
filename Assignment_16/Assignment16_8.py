import os

def File_Handling(Name_Of_File1,Name_Of_File2):

    ret = os.path.exists(Name_Of_File1)

    if ret == True:
        print(f"File { Name_Of_File1} exists.")

        fobj1 = open(Name_Of_File1,'r')

        data1 = fobj1.read()
        fobj1.seek(0)

        print("The data with blank lines is as follows: ")
        print(data1)

        cleaned_lines = []
        """
        In a file after every line the is "\n" at the end by default(Which we can't see in file)
        there for when we use for loop to traverse through lines, after every line the cursor
        automatically goes down.
        """
        for line in fobj1:
            if line.strip() != "":
                """ 
                line.strip() will convert "   " --> ""  (remove white spaces)
            for other lines ,line.strip() will have no effect as strip() removes 
            all extra whitespace characters (like spaces, tabs, and newlines) 
            only from the beginning and end of a line — not from the middle.
            so "India is my country." --> "India is my country."
            """
                cleaned_lines.append(line)
        
        data2 = "".join(cleaned_lines)

        """
        sample data in cleaned_lines = ["India is my country.\n","I am proud of my country.\n",...]


        """

        """ 
        .join() is used to combine elements from a list (or other iterable) 
        into a single string, by inserting a separator between them.
        syntax  = separator.join(iterable)#can be list,string etc
        As there is no need to have any seprator between two lines,we have used no separator
        Also by default each line has "\n" by default at the end of each line.Therefore in data2
        the data gets printed one below the other.
        """
        

        fobj2 = open(Name_Of_File2,'w')

        fobj2.write(data2)

        print(f"The blank lines from the file {Name_Of_File1} are removed successfully.")
        print(f"The new data is successfully saved in {Name_Of_File2}")
        print("The data in new file is: ")
        print(data2)


    else:
        print(f"File { Name_Of_File} does not exists.")
        

def main():
    print("Enter the name of file to be cleaned: ")
    Fname1 = input()

    print("Enter the name of new file : ")
    Fname2 = input()


    File_Handling(Fname1,Fname2)

if __name__ == "__main__":
    main()