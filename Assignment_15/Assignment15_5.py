import os
import sys
import string

def File_Handling(Name_of_File,String):
    
    ret = os.path.exists(Name_of_File)


    if (ret == True):

        print(f"The file {Name_of_File} exists in the current directory.")

        fobj = open(Name_of_File,"r")

        data1  = fobj.read()

        words = data1.split()

        print(f"Data in the {Name_of_File } is: ",data1)

        data2 = String

        print(f"String to check is: ",data2)

        iCount = 0

        for word in words:

            clean_word = word.strip(string.punctuation)
            # Remove punctuation like '.', ',' etc both at beginning and at the end.
            # But will not remove if there is no space after punctuation
            #eg India ....sisters.India....
            ## in that case use:
            #import re
            #words = re.findall(r'\b\w+\b', data1) where words is a list of all the 
            # words in a file...use this line before the for loop.
            #to use clean_word = word.strip(string.punctuation),there should be space after the 
            #end of the sentence
            #for eg India ....sisters. India......
            
            if String.lower() == clean_word.lower():
                iCount = iCount + 1

        return iCount
     
    else:
        print(f"There is no such file by the name {Name_of_File} in the current directory.")
        return -1 # return error (have to return something)
    
    # return iCount --> can't write here because even else above must return something
    #because the function is called by a variable(iret) and it expects a return value.
    
def main():

    if(len(sys.argv) == 3):
        if((sys.argv[1] == '--h') or(sys.argv[1] == '--H')):
            print("This program is used count the frequency of the string in a file.")
            
        elif((sys.argv[1] == '--u') or(sys.argv[1] == '--U')):
            print("Use the given script as -------")
            print("ScriptName.py  FileName1    String")

        else:
             iret = File_Handling(sys.argv[1],sys.argv[2])
             
            #  if iret != -1:
            #     print(f"The word {sys.argv[2]} appears {iret} times in file {sys.argv[1]}")
             if iret == -1:
                print("There is a problem with the file.")
             else:
                print(f"The word {sys.argv[2]} appears {iret} times in file {sys.argv[1]}")
        # any of the if statements can be used
      
        
    else:
        print("Invalid number of arguements")
        print("Use the given flags as: ")
        print("--h: Use to display the help")
        print("--u: Use to display the usage")

    


if __name__ == "__main__":
    main()



#      return value	                  Meaning
#      return 0	              OK / Success (sometimes used)
#      return -1	     Error / File not found / Failure
#      return n	       A valid result (e.g., count, data, etc.)