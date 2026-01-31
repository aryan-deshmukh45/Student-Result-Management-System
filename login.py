from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
import math
import os
import sqlite3
from tkinter import messagebox,ttk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1000x550")
        self.root.config(bg="#0b3c5d")

        # ===== Main Frame =====
        main_frame = Frame(self.root, bg="white")
        main_frame.place(x=100, y=50, width=800, height=450)

        # ===== Left Clock Frame =====
        left_frame = Frame(main_frame, bg="#0b1c2d")
        left_frame.place(x=0, y=0, width=300, height=450)

        Label(
            left_frame,
            text="Analog Clock",
            font=("times new roman", 20, "bold"),
            bg="#0b1c2d",
            fg="white"
        ).pack(pady=20)

        self.lbl_clock = Label(left_frame, bg="white", bd=5, relief=RIDGE)
        self.lbl_clock.pack(pady=20)

        # ===== Right Login Frame =====
        right_frame = Frame(main_frame, bg="white")
        right_frame.place(x=300, y=0, width=500, height=450)

        Label(
            right_frame,
            text="LOGIN HERE",
            font=("times new roman", 25, "bold"),
            fg="#1f8acb",
            bg="white"
        ).place(x=150, y=40)

        Label(right_frame, text="Email", bg="white", font=("arial", 12)).place(x=80, y=120)
        self.txt_email = Entry(right_frame, font=("arial", 14), bg="#eaeaea")
        self.txt_email.place(x=80, y=150, width=330, height=35)

        Label(right_frame, text="Password", bg="white", font=("arial", 12)).place(x=80, y=210)
        self.txt_pass = Entry(right_frame, font=("arial", 14), bg="#eaeaea", show="*")
        self.txt_pass.place(x=80, y=240, width=330, height=35)

        Button(
            right_frame,
            text="Login",
            font=("arial", 20, "bold"),
            bg="#c2185b",
            fg="white",
            bd=0,
            cursor="hand2",
            command=self.login
        ).place(x=80, y=310, width=150, height=40)

        Button(
            right_frame,
            text="Register New Account?",
            font=("ariel",10),
            fg="#B00857",
            bg="white",
            cursor="hand2",
            command=self.register_window
        ).place(x=80, y=370)
        Button(
            right_frame,
            text="Forget Password ?",
            font=("ariel",10),
            fg="red",
            bg="white",
            cursor="hand2",
            command=self.forget_password_window
        ).place(x=240, y=370)

        # ===== Clock setup =====
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.clock_bg = os.path.join(self.BASE_DIR, "Images", "cl.jpg")

        self.update_clock()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pss.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_email.delete(0,END)


    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pss.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con= sqlite3.connect("employee.db")
                cur = con.cursor()
                cur.execute("Select *from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_pss.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset, Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}",parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password",parent=self.root)
        else:
            try:
                con= sqlite3.connect("employee.db")
                cur = con.cursor()
                cur.execute("Select *from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset the password",parent=self.root)
                else:
                    con.close() 
                    self.root2=Toplevel()  
                    self.root2.title("Forget Password") 
                    self.root2.geometry("350x400+495+150") 
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
            
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
            
                    Label(self.root2, text="Security Question", bg="white").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, state="readonly")
                    self.cmb_quest["values"] = (
                        "Select",
                        "Your First Pet Name",
                        "Your Birth Place",
                        "Your Best Friend Name"
                    )
                    self.cmb_quest.current(0)
                    self.cmb_quest.place(x=50, y=130, width=250)
            
                    Label(self.root2, text="Answer", bg="white").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)
            
                    Label(self.root2, text="New Password", bg="white").place(x=50, y=260)
                    self.txt_new_pss = Entry(self.root2, bg="lightgray")
                    self.txt_new_pss.place(x=50, y=290, width=250)
            
                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)     
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}",parent=self.root)

        

    def register_window(self):
        self.root.destroy()
        from register import Register
        root = Tk()
        Register(root)
        root.mainloop()

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con= sqlite3.connect("employee.db")
                cur = con.cursor()
                cur.execute("Select *from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Error","Welcome",parent=self.root)  
                    self.root.destroy()
                    from dashboard import RMS
                    root = Tk()
                    RMS(root)
                    root.mainloop()
                con.close()      
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to : {str(es)}",parent=self.root)        
            

    # ===== Clock Drawing =====
    def draw_clock(self, hr, min_, sec_):
        img = Image.new("RGB", (220, 220), "white")
        draw = ImageDraw.Draw(img)

        bg = Image.open(self.clock_bg).resize((200, 200), Image.LANCZOS)
        img.paste(bg, (10, 10))

        cx, cy = 110, 110

        # Hour hand
        hour_angle = (hr % 12 + min_ / 60) * 30
        draw.line(
            (cx, cy,
             cx + 40 * math.sin(math.radians(hour_angle)),
             cy - 40 * math.cos(math.radians(hour_angle))),
            fill="black", width=5
        )

        # Minute hand
        min_angle = min_ * 6
        draw.line(
            (cx, cy,
             cx + 60 * math.sin(math.radians(min_angle)),
             cy - 60 * math.cos(math.radians(min_angle))),
            fill="blue", width=3
        )

        # Second hand
        sec_angle = sec_ * 6
        draw.line(
            (cx, cy,
             cx + 75 * math.sin(math.radians(sec_angle)),
             cy - 75 * math.cos(math.radians(sec_angle))),
            fill="red", width=2
        )

        draw.ellipse((105, 105, 115, 115), fill="black")

        return img

    def update_clock(self):
        now = datetime.now()
        img = self.draw_clock(now.hour, now.minute, now.second)
        self.tk_img = ImageTk.PhotoImage(img)
        self.lbl_clock.config(image=self.tk_img)
        self.root.after(1000, self.update_clock)


# ===== Run App =====
if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
