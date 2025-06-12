import os
import string


def File_Handling(Name_Of_File):

    ret = os.path.exists(Name_Of_File)

    if ret == True:
        print(f"File is successfully created by the name {Name_Of_File}")
    else:
        print("No such file exists.")

    fobj = open(Name_Of_File,'r') # write + read

    data = fobj.read()#cursor goes to the end of line
    fobj.seek(0)# bring back the cursor to original position so at to count
    # the number of lines in a file.

    line_counter = 0
    words_counter = 0
    char_counter = 0

    for line in fobj:
        line_counter = line_counter + 1
        
    
    words = data.split()
    for word in words:
        clean_word = word.strip(string.punctuation)# to remove '.'
        words_counter = words_counter + 1
        
    for character in data:
        char_counter = char_counter + 1
        if character == ' ':
            char_counter = char_counter - 1



    return line_counter,words_counter,char_counter

    
    #return one after other won't works because return exits the function.so once the 
    # code reaches the first return statement...it will return a and exit the function.
    # therefore will not be able to return b and c respectively.
    #return a
    #return b
    #return c
    
    fobj.close()

    
def main():


    print("Enter the name of file of which you want to count content:  \n")
    FileName = input()

    
    ret1,ret2,ret3 = File_Handling(FileName)

    print(f"The file {FileName} contains {ret1} lines, {ret2} words and {ret3} chararacters.")


if __name__ == "__main__":
    main()