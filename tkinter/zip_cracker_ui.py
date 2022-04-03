from tkinter import *
from tkinter.filedialog import askopenfilename
#from tkinter import Tk    # from tkinter import Tk for Python 3.x

def fun(): 
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    zip_file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(zip_file)  
# # gui logic

root = Tk()
root.geometry("200x100")
root.minsize(400,200)
root.maxsize(1920,1080)
root.title("Zip Password Cracker")
head = Label(text ="Zip Password Cracker")
head.pack() #fixed the content of head text

  


b = Button(root,text = "Choose zip",command =fun)
b.place(x=170,y=80)   




root.mainloop()