from PIL import Image, ImageTk
import tkinter as tk


class Timer:
    def __init__(self, window):
        # creating window
        # setting attribute
        imgTemp = Image.open("./images/image.jpg")
        imgTemp = imgTemp.resize((1920, 1080))

        self.img = ImageTk.PhotoImage(imgTemp)
        self.background_label = tk.Label(window, image=self.img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.after(1000, self.update_image)


    def update_image(self):
        self.img = ImageTk.PhotoImage(Image.open("./images/image.jpg"))
        self.background_label.configure(image=self.img)
        self.background_label.after(1000, self.update_image)


if __name__ == "__main__":
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    window.configure(background='black')
    timer = Timer(window)
    window.mainloop()
