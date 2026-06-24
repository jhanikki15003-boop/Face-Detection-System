
from tkinter import *
from PIL import Image, ImageTk
import os

# -------------------------------
# Functions to open other scripts
# -------------------------------
def open_register():
    os.system("python register.py")

def open_train():
    os.system("python train.py")

def open_recognize():
    os.system("python recognize.py")

# -------------------------------
# Main GUI Window
# -------------------------------
class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600+100+50")
        self.root.title("Face Detection & Attendance System")

        # Title
        title = Label(self.root, text="FACE RECOGNITION & ATTENDANCE SYSTEM",
                      font=("Times New Roman", 28, "bold"),
                      bg="white", fg="darkblue", bd=5, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # Register Button
        btn_register = Button(self.root, text="Register Face",
                              command=open_register,
                              font=("Times New Roman", 20, "bold"),
                              bg="blue", fg="white", width=20)
        btn_register.place(x=250, y=150)

        # Train Data Button
        btn_train = Button(self.root, text="Train Model",
                           command=open_train,
                           font=("Times New Roman", 20, "bold"),
                           bg="orange", fg="white", width=20)
        btn_train.place(x=250, y=250)

        # Recognize Button (with attendance)
        btn_recognize = Button(self.root, text="Face Recognition + Attendance",
                               command=open_recognize,
                               font=("Times New Roman", 20, "bold"),
                               bg="green", fg="white", width=25)
        btn_recognize.place(x=200, y=350)

        # Exit Button
        btn_exit = Button(self.root, text="Exit", command=root.quit,
                          font=("Times New Roman", 20, "bold"),
                          bg="red", fg="white", width=20)
        btn_exit.place(x=250, y=450)


# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
