from tkinter import *
from tkinter.ttk import *
import os


from PIL import ImageTk, Image

# Define colors
bg_color = 'grey'
col = '#f2f2f2'
col2 = '#DD4141'

# Create the main window
window = Tk()
window.title("Alarm")
window.geometry('400x200')
window.configure(bg=bg_color)

style = Style()
style.configure('TFrame', background= col2)

# Create a frame with the specified background color using the variable
frame_body = Frame(window, width=400, height=5, style='TFrame')
frame_body.grid(row=1, column=0)

#configuring frame body
image_path = 'icons8-clock-64.png'
if os.path.exists(image_path):
    try:    
        img = Image.open('icons8-clock-64.png')
        img_resized = img.resize((100, 100), Image.LANCZOS)
        app_img = ImageTk.PhotoImage(img_resized)

        app_image_label = Label(frame_body, image=app_img)
        app_image_label.image = app_img
        app_image_label.place(x=10, y=10)
    except Exception as e:
        print(f"Error opening image: {e}")
else:
    print("Image not found")            

name = Label(frame_body, text="Alarm", font=('Ivy 18 bold'), background=col2, foreground=col)

name.place(x=120, y=30)

hour = Label(frame_body, text="hour", font=('Ivy 18 bold'), background=col2, foreground=col)

hour.place(x=120, y=30)

c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.place(x=130, y=58)

# Start the Tkinter main loop
window.mainloop()

