from tkinter import *





# class Gui:


#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.geometry("300x200+10+20")




def main():
    width = 1000
    height = 600

    window = Tk()
    window.title('Hello')
    window.geometry(f'{width}x{height}')
    btn = Button(window, text="Search", fg='black', width=20)
    btn.place(x=((width/2) - 10), y=(height * .65))
    
    data = ["Current", "7 Days", "30 Days", "60 days"]
    lb = Listbox(window, height=5, selectmode='single', width=20)
    for num in data:
        lb.insert(END, num)
    lb.place(x=((width / 2) - 10), y=(height * .4))
    





    window.mainloop()



if __name__ == "__main__":
    main()

# gui = Gui()