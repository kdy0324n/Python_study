from PIL import Image,ImageTk
import tkinter as tk


Window = tk.Tk()
canvas = tk.Canvas(Window,width=500,height=500)
canvas.pack()
photo_path = "C:/Users/kdy03/Desktop/프로그래밍기초_파이썬/두근두근파이썬/chapter12/lenna.png"
img = Image.open(photo_path)
out = img.rotate(45)

tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250,250,image=tk_img)

Window.mainloop()