'''
Done by JOY KHULBE
University ID. 20011463 
Roll no. - 2018401
Section: D
Class Roll. 31
'''

import zipfile
from tqdm import tqdm

class colors_code:
    #ansi (basic) 
    ENDC = '\033[0m'  
    FAIL = '\033[91m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKORANGE = '\033[93m'
    


my_password_list = "pwd_list2.txt"



select_file = "zip_cracker.zip"





select_file = zipfile.ZipFile(select_file)

length = len(list(open(my_password_list, "rb")))


print("\n")

print(colors_code.OKCYAN + "Total passwords to test:", length)
print("\n")

with open(my_password_list, "rb") as my_password_list:
    for word in tqdm(my_password_list, total=length, unit="word"):
        try:
            select_file.extractall(path="Extracted Folder",pwd=word.strip())
        except:
            continue
        else:
            print(colors_code.ENDC)
            print("\n")
            print(colors_code.OKGREEN)
            print("[+] Password found: ", word.decode().strip())
            print(colors_code.ENDC)
            print("\n")
            print(colors_code.OKORANGE)
            print("All Files has been Extracted inside the New Directory i.e Extracted Folder\n\nPassword found at:")
            print("\n")
            exit(0)
            
print(colors_code.FAIL)
print("[!] Password not found, try other my_password_list.")