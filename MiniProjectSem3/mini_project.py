'''
Done by: JOY KHULBE
University: GEHU
'''

from tkinter import *
from tkinter.filedialog import askopenfilename


import zipfile
from tqdm import tqdm


class color_code:
    #ansi (basic) 
    ENDC = '\033[0m' 
     
    FAIL = '\033[91m'
    
    OKCYAN = '\033[96m'
    
    OKGREEN = '\033[92m'
    
    OKORANGE = '\033[93m'
    
    


def fun_zipper():
    
    my_password_list = "pwd_list2.txt"
    
    Tk().withdraw()  # dialog box 
    
    select_file = askopenfilename()

    
    select_file = zipfile.ZipFile(select_file) 

    length = len(list(open(my_password_list, "rb"))) # counting
    
    print(color_code.OKCYAN + "\nTotal passwords to test:", length)
    print("\n")
    with open(my_password_list, "rb") as my_password_list:
        
        for word in tqdm(my_password_list, total=length, unit="word"):
            try:
                select_file.extractall(path="Zip Extracted material", pwd=word.strip())
            except:
                continue
            else:
                print(color_code.ENDC)
                print("\n")
                print(color_code.OKGREEN)
                print("--> Password found:", word.decode().strip())
                print(color_code.ENDC)
                print("\n")
                print(color_code.OKORANGE)
                print("All Files has been Extracted inside the New Directory i.e Zip Extracted material\n\n\nPassword found at:")
                print("\n")
                exit(0)


    print(color_code.FAIL)
    print("[X] Password not found [X], try another passwordlist.")

# ui start
root = Tk()

root.geometry("400x200") #size
root.minsize(400, 200)
root.maxsize(400, 200)
root.title("Zip Password Cracker")

head = Label(text="Zip Password Cracker")
head.place(x = 141,y= 20)

root.configure(bg='grey')


create_button = Button(root, text="Choose zip file", width= 14,height=3,command=fun_zipper)

create_button.place(x=150, y=80)

root.mainloop()
#ui end