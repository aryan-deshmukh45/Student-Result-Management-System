from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
import os
import sqlite3
from tkinter import messagebox

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # ================= TITLE BAR =================
        title_bar = Frame(self.root, bg="#003b5c", height=60)
        title_bar.pack(side=TOP, fill=X)

        logo_path = os.path.join(BASE_DIR, "Images", "logo_.p.png")
        self.logo = Image.open(logo_path)
        self.logo = self.logo.resize((45, 45), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)

        Label(
            title_bar,
            image=self.logo,
            bg="#003b5c"
        ).place(x=400, y=180,width=920,height=35)

        Label(
            title_bar,
            text="Student Result Management System",
            font=("goudy old style", 22, "bold"),
            bg="#003b5c",
            fg="white"
        ).place(x=500, y=12)

        # ================= MENU BAR =================
        menu_frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
        )
        menu_frame.place(x=10, y=70, width=1330, height=90)

        btn_style = {
            "font": ("goudy old style", 14, "bold"),
            "bg": "#0b5377",
            "fg": "white",
            "cursor": "hand2",
            "bd": 2
        }

        Button(menu_frame, text="Course", **btn_style,command=self.add_course).place(x=20, y=15, width=200, height=40)
        Button(menu_frame, text="Student", **btn_style,command=self.add_student).place(x=240, y=15, width=200, height=40)
        Button(menu_frame, text="Result", **btn_style,command=self.add_result).place(x=460, y=15, width=200, height=40)
        Button(menu_frame, text="View Student Results", **btn_style,command=self.add_report).place(x=680, y=15, width=220, height=40)
        Button(menu_frame, text="Logout", **btn_style,command=self.logout).place(x=920, y=15, width=180, height=40)
        Button(menu_frame, text="Exit", **btn_style, command=self.exit_).place(x=1120, y=15, width=180, height=40)

        # ================= BACKGROUND IMAGE =================
        bg_path = os.path.join(BASE_DIR, "Images", "bg.png")
        self.bg_img = Image.open(bg_path)
        self.bg_img = self.bg_img.resize((900, 360), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        Label(
            self.root,
            image=self.bg_img,
            bg="white"
        ).place(x=400, y=180, width=900, height=360)

        # ================= STAT BOXES =================
        box_style = {
            "font": ("goudy old style", 20),
            "bd": 8,
            "relief": RIDGE,
            "fg": "white"
        }

        self.lbl_course=Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            bg="#e74c3c",
            **box_style
        )
        self.lbl_course.place(x=420, y=560, width=280, height=100)

        self.lbl_student=Label(
            self.root,
            text="Total Students\n[ 0 ]",
            bg="#2980b9",
            **box_style
        )
        self.lbl_student.place(x=720, y=560, width=280, height=100)

        self.lbl_result=Label(
            self.root,
            text="Total Results\n[ 0 ]",
            bg="#16a085",
            **box_style
        )
        self.lbl_result.place(x=1020, y=560, width=280, height=100)

        # ================= FOOTER =================
        footer = Label(
            self.root,
            text="SRMS - Student Result Management System | Contact: 987xxxx001 | Email: WebCode867@gmail.com",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select *from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total courses\n[{str(len(cr))}]")

            cur.execute("select *from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Student\n[{str(len(cr))}]")

            cur.execute("select *from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 
        self.root.after(200,self.update_details)    



    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)  
        if op==True:
            self.root.destroy()
            from login import LoginWindow
            root = Tk()
            LoginWindow(root)
            root.mainloop()
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)  
        if op==True:
            self.root.destroy()


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    app = RMS(root)
    root.mainloop()
