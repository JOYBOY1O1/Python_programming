import zipfile
from tqdm import tqdm

# the password list path you want to use, must be available in the current directory
wordlist = "pwd_list.txt"
# the zip file you want to crack its password
zip_file = "zip_cracker.zip"
#To read the zip file in Python, we use the zipfile.ZipFile class that has methods to open, read, write, close, list and extract zip files (we will only use extractall()

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords

print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            print(f"!..Scanning complete {round((word/n_words)*100, 2)}%")
            print("!!!FAIL!!!\n")
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")