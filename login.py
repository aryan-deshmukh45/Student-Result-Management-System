from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
import math
import os


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
            cursor="hand2"
        ).place(x=80, y=310, width=150, height=40)

        Button(
            right_frame,
            text="Register New Account?",
            font=("ariel",10),
            fg="#B00857",
            bg="white",
            cursor="hand2"
        ).place(x=80, y=370)

        # ===== Clock setup =====
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.clock_bg = os.path.join(self.BASE_DIR, "Images", "cl.jpg")

        self.update_clock()

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
