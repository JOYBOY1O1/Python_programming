#Done by JOY KHULBE
#University ID. 20011463 
#Roll no. - 2018401
#Section: D
#Class Roll. 31


import zipfile

#file names
#inp = input("Enter the file name")
#if(inp==fopen())

pwd_filename = "pwd_list.txt"

zip_filename = "zip_cracker.zip"

#read passwords_list file in binary mode

with open(pwd_filename, "rb") as passwords:
    
    #convert all the passwords into a list 
    passwords_list = passwords.readlines()
    
    #total number of passwords
    total_passwords = len(passwords_list)

    #load zipfile
    my_zip_file = zipfile.ZipFile(zip_filename)
    
    for index, password in enumerate(passwords_list):
        #try if password is correct
        try:
            my_zip_file.extractall(path="Extracted Folder",  pwd=password.strip())
            print("\n +++++++++++++++++++SUCCESS+++++++++++++++++++++++")
            print("Password Found: ", password.decode().strip())
            print("All Files has been Extracted inside the New DIrectory Extracted Folder")
            break
        
        #if password fails
        except:
            
            print(f"!..Scanning complete {round((index/total_passwords)*100, 2)}%")
            print("!!!FAIL!!!\n")
            continue
