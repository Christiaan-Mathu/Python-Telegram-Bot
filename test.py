from PIL import Image, ImageTk
import tkinter as tk


class Timer:
    def __init__(self, window):
        # creating window
        # setting attribute
        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))
        window.resizable(False, False)
        temp = Image.open("./images/image.jpg")
        temp2 = temp.resize((width, height))
        self.img = ImageTk.PhotoImage(temp2)


        self.background_label = tk.Label(window, image=self.img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.after(1000, self.update_image)


    def update_image(self):

        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()
        
        temp = Image.open("./images/image.jpg")
        temp2 = temp.resize((width, height))
        self.img = ImageTk.PhotoImage(temp2)


        ## place image on background and fill the screen
        self.background_label.configure(image=self.img)
        self.background_label.after(1000, self.update_image)


if __name__ == "__main__":
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    window.configure(background='black')
    timer = Timer(window)
    window.mainloop()
