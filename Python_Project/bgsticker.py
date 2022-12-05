#import module
import tkinter as tk
from PIL import ImageTk, Image

#define tkinter
root = tk.Tk()

#set tkinter 
root.geometry('240x50')
root.attributes("-topmost", False)

#count number for list
num_count = 0

#tanjiro gif sticker window
def tanjiro_sticker_class():
    tanjiro_sticker = tk.Toplevel(root)
    tanjiro_sticker.wm_attributes('-transparentcolor', '#595F96')
    tanjiro_sticker.overrideredirect(True)
    tanjiro_sticker.attributes("-topmost", True)
    tanjiro_sticker.geometry("-1-1")

    #load tanjiro image
    tanjiro_img = Image.open("taniro_sprites.png")

    #sprites image list
    first_img = []
    second_img = []

    #slice tanjiro png to sprites
    for height in range(0, 270, 269):
        for width in range(0, 901, 300):
            first_img.append(tanjiro_img.crop([width,height,width + 300,height + 269]).convert("RGBA"))
    
    #second slice tanjiro sprites
    for i in  range(0, 8):
        second_img.append(first_img[i].crop([5,5,300,269]).convert("RGBA"))

    #changing png to gif
    def animation(num_count):
        num_count+= 1
        if num_count >= 8:
            num_count = 0

        main_img = ImageTk.PhotoImage(second_img[num_count])
        label.configure(image=main_img , borderwidth=0)

        label.image=main_img
        tanjiro_sticker.after(100, animation, num_count)  

    img1= ImageTk.PhotoImage(second_img[0])
    
    label= tk.Label(tanjiro_sticker,image= img1, borderwidth=0)
    label.pack()

    tanjiro_sticker.after(0, animation, 0)
    tanjiro_sticker.mainloop()

#main_screen_class
def main():
    text_label = tk.Label(root, text="using tanjiro sticker on your computer!!")
    text_label.grid(row=0, column= 0, columnspan=4)

    #start sticker button
    tanjiro_Button = tk.Button(root, text="Tstart sticker", command=tanjiro_sticker_class)
    tanjiro_Button.grid(row=1, column=0)

    #stop sticker button
    stop_button = tk.Button(root, text="stop sticker", command=root.destroy)
    stop_button.grid(row=1, column=1)

    root.mainloop()

#ain class
if __name__ == "__main__":
    main()