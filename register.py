import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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
        Label(form_frame, text="First Name", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=50, y=80)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray").place(x=50, y=110, width=250)

        Label(form_frame, text="Last Name", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=370, y=80)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray").place(x=370, y=110, width=250)

        # ===== Row 2 =====
        Label(form_frame, text="Contact No", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=50, y=160)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray").place(x=50, y=190, width=250)

        Label(form_frame, text="Email", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=370, y=160)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray").place(x=370, y=190, width=250)

        # ===== Row 3 =====
        Label(form_frame, text="Security Question", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=50, y=240)

        cmb_quest = ttk.Combobox(
            form_frame,
            font=("times new roman", 13),
            state="readonly"
        )
        cmb_quest["values"] = (
            "Select",
            "Your First Pet Name",
            "Your Birth Place",
            "Your Best Friend Name"
        )
        cmb_quest.place(x=50, y=270, width=250)
        cmb_quest.current(0)

        Label(form_frame, text="Answer", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=370, y=240)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray").place(x=370, y=270, width=250)

        # ===== Row 4 =====
        Label(form_frame, text="Password", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=50, y=320)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray", show="*").place(x=50, y=350, width=250)

        Label(form_frame, text="Confirm Password", font=("times new roman", 15, "bold"),
              bg="white", fg="gray").place(x=370, y=320)
        Entry(form_frame, font=("times new roman", 15),
              bg="lightgray", show="*").place(x=370, y=350, width=250)

        # ===== Terms =====
        Checkbutton(
            form_frame,
            text="I Agree The Terms & Conditions",
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
            cursor="hand2"
        ).place(x=230, y=440)


# ================= Run App =================
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()



    


