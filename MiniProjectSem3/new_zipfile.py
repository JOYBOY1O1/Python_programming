'''
Done by JOY KHULBE
University ID. 20011463 
Roll no. - 2018401
Section: D
Class Roll. 31
'''

import zipfile
from tqdm import tqdm

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKORANGE = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
    

# the password list path you want to use, must be available in the current directory
wordlist = "pwd_list2.txt"


# the zip file you want to crack its password
zip_file = "zip_cracker.zip"


#To read the zip file in Python, we use the zipfile.ZipFile class that has methods to open, read, write, close, list and extract zip files (we will only use extractall()


# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords

print("\n")
# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.OKCYAN + "Total passwords to test:", n_words)
print("\n")

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(path="Extracted Folder",pwd=word.strip())
        except:
            continue
        else:
            print(bcolors.ENDC)
            print("\n")
            print(bcolors.OKGREEN)
            print("[+] Password found: ", word.decode().strip())
            print(bcolors.ENDC)
            print("\n")
            print(bcolors.OKORANGE)
            print("All Files has been Extracted inside the New Directory Extracted Folder")
            print("\n")
            exit(0)
            
print(bcolors.FAIL)
print("[!] Password not found, try other wordlist.")