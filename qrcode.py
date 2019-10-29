import pyqrcode
import cv2
import pyzbar.pyzbar as bar
from tkinter import filedialog
from tkinter import simpledialog,messagebox
from tkinter import *
def createqr():
    str = simpledialog.askstring('Data', 'Enter String')
    if str!=None:
        file = filedialog.asksaveasfile(mode='w', defaultextension='.jpg')
        dir = file.name
        try:
            qr=pyqrcode.create(str)
            qr.png(dir,scale=7)
        except:
            messagebox.showwarning('Error','Not possible due to Large data or some Technical error')
def scan():
    cap = cv2.VideoCapture(0)
    while True:

        res,frame=cap.read()
        decoded=bar.decode(frame)
        for obj in decoded:
            cv2.putText(frame,str(obj.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

        cv2.imshow('Frame',frame)

        key=cv2.waitKey(1)
        if key==27:
            break
    cv2.destroyAllWindows()

def browse():
    file=filedialog.askopenfile(mode='r')
    mat=cv2.imread(file.name)
    try:
        dec=bar.decode(mat)
        for obj in dec:
            messagebox.showinfo('Data',obj.data)
    except:
        messagebox.showerror('Error',"Can't decode")





root = Tk()
root.title('QRcode Generator')
root.geometry('600x200')
root.config(bg='#213345')
b1=Button(root,text='Create',command=createqr,width=10,)
b1.place(x=100,y=100)
b2=Button(root,text='Scan',width=10,command=scan)
b2.place(x=500,y=100)
b3=Button(root,text='Browse QRCode',command=browse)
b3.place(x=300,y=100)

root.mainloop()
