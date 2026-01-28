import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from   PIL import Image, ImageTk
  
  
class Register:
      def __init__(self, root):

            self.root = root
            self.root.title("Registration Window")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="white")
    
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
            # ================= Background =================
            bg_path = os.path.join(BASE_DIR, "Images", "b2.jpg")
            bg_img = Image.open(bg_path).resize((1350, 700), Image.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_img)
            Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
    
            # ================= Left Image =================
            left_path = os.path.join(BASE_DIR, "Images", "side.png")
            left_img = Image.open(left_path).resize((400, 500), Image.LANCZOS)
            self.left = ImageTk.PhotoImage(left_img)
            Label(self.root, image=self.left, bg="white").place(x=80, y=100)
    
            # ================= Form =================
            frame = Frame(self.root, bg="white")
            frame.place(x=480, y=100, width=700, height=500)
    
            Label(frame, text="REGISTER HERE",
                  font=("times new roman", 25, "bold"),
                  bg="white", fg="green").place(x=200, y=20)
    
            # -------- Entries --------
            Label(frame, text="First Name", bg="white").place(x=50, y=80)
            self.txt_fname = Entry(frame, bg="lightgray")
            self.txt_fname.place(x=50, y=110, width=250)
    
            Label(frame, text="Last Name", bg="white").place(x=370, y=80)
            self.txt_lname = Entry(frame, bg="lightgray")
            self.txt_lname.place(x=370, y=110, width=250)
    
            Label(frame, text="Contact No", bg="white").place(x=50, y=160)
            self.txt_contact = Entry(frame, bg="lightgray")
            self.txt_contact.place(x=50, y=190, width=250)
    
            Label(frame, text="Email", bg="white").place(x=370, y=160)
            self.txt_email = Entry(frame, bg="lightgray")
            self.txt_email.place(x=370, y=190, width=250)
    
            Label(frame, text="Security Question", bg="white").place(x=50, y=240)
            self.cmb_quest = ttk.Combobox(frame, state="readonly")
            self.cmb_quest["values"] = (
                "Select",
                "Your First Pet Name",
                "Your Birth Place",
                "Your Best Friend Name"
            )
            self.cmb_quest.current(0)
            self.cmb_quest.place(x=50, y=270, width=250)
    
            Label(frame, text="Answer", bg="white").place(x=370, y=240)
            self.txt_answer = Entry(frame, bg="lightgray")
            self.txt_answer.place(x=370, y=270, width=250)
    
            Label(frame, text="Password", bg="white").place(x=50, y=320)
            self.txt_password = Entry(frame, bg="lightgray", show="*")
            self.txt_password.place(x=50, y=350, width=250)
    
            Label(frame, text="Confirm Password", bg="white").place(x=370, y=320)
            self.txt_cpassword = Entry(frame, bg="lightgray", show="*")
            self.txt_cpassword.place(x=370, y=350, width=250)
    
            self.var_chk = IntVar()
            Checkbutton(frame, text="I Agree The Terms & Conditions",
                        variable=self.var_chk, bg="white").place(x=50, y=390)
    
            Button(frame, text="Register Now",
                   font=("times new roman", 15, "bold"),
                   bg="green", fg="white",
                   cursor="hand2",
                   command=self.register_data).place(x=230, y=430)
    
      # ==  =============== Register Logic =================
      def   register_data(self):
            if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" \
               or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" \
               or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
    
            elif self.txt_password.get() != self.txt_cpassword.get():
                messagebox.showerror("Error","Passwords do not match",parent=self.root)
    
            elif self.var_chk.get() == 0:
                messagebox.showerror("Error","Please agree to terms",parent=self.root)
    
            else:
                  try:  
                        con = sqlite3.connect("employee.db")
                        cur = con.cursor()
        
                        cur.execute("SELECT * FROM employee WHERE email=?",
                                    (self.txt_email.get(),))
                        row = cur.fetchone()
        
                        if row:
                            messagebox.showerror("Error","User already exists",parent=self.root)
                        else:  
                              cur.execute("""
                                  INSERT INTO employee
                                  (f_name,l_name,contact,email,question,answer,password)
                                  VALUES (?,?,?,?,?,?,?)
                              """, (
                                  self.txt_fname.get(),
                                  self.txt_lname.get(),
                                  self.txt_contact.get(),
                                  self.txt_email.get(),
                                  self.cmb_quest.get(),
                                  self.txt_answer.get(),
                                  self.txt_password.get()
                              ))
          
                              con.commit()
                              con.close()
                              messagebox.showinfo("Success","Registration Successful",parent=self.root)
                              self.clear()
        
                  except Exception as e:
                        messagebox.showerror("Error", f"Error due to {e}", parent=self.root)
    
      def   clear(self):
            self.txt_fname.delete(0, END)
            self.txt_lname.delete(0, END)
            self.txt_contact.delete(0, END)
            self.txt_email.delete(0, END)
            self.txt_answer.delete(0, END)
            self.txt_password.delete(0, END)
            self.txt_cpassword.delete(0, END)
            self.cmb_quest.current(0)
            self.var_chk.set(0)
    
  
if __name__ == "__main__":
      root = Tk()
      app = Register(root)
      root.mainloop()
