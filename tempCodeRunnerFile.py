import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
from employee_db import create_db

class Register:

      def __init__(self, root):
            self.root = root
            self.root.title("Registration Window")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="white")

            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

            # ================= Background Image =================
            bg_path = os.path.join(BASE_DIR, "Images", "b2.jpg")
            bg_img = Image.open(bg_path).resize((1350, 700), Image.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_img)
            Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            # ================= Left Card Image =================
            left_path = os.path.join(BASE_DIR, "Images", "side.png")
            left_img = Image.open(left_path).resize((400, 500), Image.LANCZOS)
            self.left = ImageTk.PhotoImage(left_img)
            Label(self.root, image=self.left, bg="white").place(x=80, y=100)

            # ================= Register Frame =================
            form_frame = Frame(self.root, bg="white")
            form_frame.place(x=480, y=100, width=700, height=500)

            title = Label(
                form_frame,
                text="REGISTER HERE",
                font=("times new roman", 25, "bold"),
                bg="white",
                fg="green"
            )
            title.place(x=200, y=20)

            # ===== Row 1 =====
            f_name=Label(form_frame, text="First Name", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=50, y=80)
            self.txt_fname=Entry(form_frame, font=("times new roman", 15), bg="lightgray")
            self.txt_fname.place(x=50, y=110, width=250)

            l_name=Label(form_frame, text="Last Name", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=370, y=80)
            self.txt_lname=Entry(form_frame, font=("times new roman", 15),bg="lightgray")
            self.txt_lname.place(x=370, y=110, width=250)

            # ===== Row 2 =====
            contact=Label(form_frame, text="Contact No", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=50, y=160)
            self.txt_contact=Entry(form_frame, font=("times new roman", 15),bg="lightgray")
            self.txt_contact.place(x=50, y=190, width=250)

            email=Label(form_frame, text="Email", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=370, y=160)
            self.txt_email=Entry(form_frame, font=("times new roman", 15),bg="lightgray")
            self.txt_email.place(x=370, y=190, width=250)

            # ===== Row 3 =====
            question=Label(form_frame, text="Security Question", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=50, y=240)

            self.cmb_quest = ttk.Combobox(
                form_frame,
                font=("times new roman", 13),
                state="readonly"
            )
            self.cmb_quest["values"] = (
                "Select",
                "Your First Pet Name",
                "Your Birth Place",
                "Your Best Friend Name"
            )
            self.cmb_quest.place(x=50, y=270, width=250)
            self.cmb_quest.current(0)

            answer=Label(form_frame, text="Answer", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=370, y=240)
            self.txt_answer=Entry(form_frame, font=("times new roman", 15),bg="lightgray")
            self.txt_answer.place(x=370, y=270, width=250)

            # ===== Row 4 =====
            password=Label(form_frame, text="Password", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=50, y=320)
            self.txt_password=Entry(form_frame, font=("times new roman", 15),bg="lightgray", show="*")
            self.txt_password.place(x=50, y=350, width=250)

            cpassword=Label(form_frame, text="Confirm Password", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=370, y=320)
            self.txt_cpassword=Entry(form_frame, font=("times new roman", 15),bg="lightgray", show="*")
            self.txt_cpassword.place(x=370, y=350, width=250)

            # ===== Terms =====
            self.var_chk=IntVar()
            chk=Checkbutton(
                form_frame,
                text="I Agree The Terms & Conditions",
                variable=self.var_chk,
                onvalue=1,
                offvalue=0,
                bg="white",
                font=("times new roman", 12)
            ).place(x=50, y=400)

            # ===== Register Button =====
            btn_img_path = os.path.join(BASE_DIR, "Images", "register.png")
            self.btn_img = ImageTk.PhotoImage(Image.open(btn_img_path))
            Button(form_frame, image=self.btn_img,
                   bd=0, cursor="hand2").place(x=50, y=430)

            Button(
                form_frame,
                text="Register Now",
                font=("times new roman", 15, "bold"),
                fg="green",
                bg="white",
                bd=0,
                cursor="hand2",
                command=self.register_data
            ).place(x=230, y=440)

      def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0,END)

            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)



      def register_data(self):
            if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                  messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            elif self.txt_password.get()!= self.txt_cpassword.get():
                  messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
            elif self.var_chk.get()==0:
                  messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)      
            else:
                  try:
                        con=sqlite3.connect("employee.db")
                        cur=con.cursor()
                        cur.execute("Select *from employee where email=?",self.txt_email.get())
                        row=cur.fetchone()
                        if row!=None:
                              messagebox.showerror("Error","User already exist, please try with another eamil",parent=self.root)
                        else:
                              cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password)values(?,?,?,?,?,?,?)",
                                                     (self.txt_fname.get(),
                                                     self.txt_lname.get(),
                                                     self.txt_contact.get(),
                                                     self.txt_email.get(),
                                                     self.cmb_quest.get(),
                                                     self.txt_answer.get(),
                                                     self.txt_password.get()
                                                     ))
                              con.commit()
                              con.close()
                              messagebox.showinfo("Successs","Register Successful",parent=self.root)    
                              self.clear()                    
     
                  except Exception as es:
                        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 
                  finally:
                        con.close()      


# ================= Run App =================
if __name__ == "__main__":
      create_db()
      root = Tk()
      app = Register(root)
      root.mainloop()
    