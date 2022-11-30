from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

img_resized = None

def open_file():
    finename = filedialog.askopenfilename()
    return finename


def load_img():
    global img_resized, window, img
    # open image
    img = Image.open(open_file())
    watermark = Image.open('watermark.png')
    # resizing watermark
    watermark = watermark.resize((100, 100))
    # resizing image
    width = 300
    # change height according to width to maintain aspect ratio
    height = int(width * (img.size[1]) / img.size[0])
    img_resized = img.resize((width, height), Image.ANTIALIAS)

    # add watermark and using mask to remove black background from png
    img_resized.paste(watermark, (0, 0), mask=watermark)

    img = ImageTk.PhotoImage(img_resized)
    window.update()
    img_area = Label(window, image=img)
    img_area.pack()


def savefile():
    global img_resized
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    img_resized.save(filename)



window = Tk()
window.title("Watermarking images")
window.geometry('800x600')
my_font = ('helvetica', 18, 'bold')
main_label = Label(text='upload and image to add a watermark ', width=30, font=my_font)
main_label.pack()

# added "lamda" so that the button doesn't start automatically == try removing it
open_img_button = Button(text="Upload File", width=20, command=lambda: load_img()).pack()
save_button = Button(text="Save File", width=20, command=lambda: savefile()).pack()

window.mainloop()
