#App for nutrition values

from tkinter import *
from tkinter import messagebox
import Functions


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("App calculating nutrition values")
        self.switch(Menu)

    def switch(self, frame_class):
        """Destroys current frame and replaces it with a chosen by the user"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Menu(Frame):
    """Main menu"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")
        self.master.config(bg = "black")
        self.master.geometry('350x350')


        label = Label(self, text = "Welcome in a nutrition calculator!\n Choose an option."\
                      , bg = "black", fg = "white")
        label.pack()
        button = Button(self, text = "Calculator", width = 20, command = lambda: master.switch(Calculator))
        button.pack(padx = 5, pady = 5)
        button2 = Button(self, text = "Add a product", width = 20, command = lambda: master.switch(File_Write))
        button2.pack()
        button3 = Button(self, text = "Exit", width = 20, command = self.close)
        button3.pack(padx = 5, pady = 5)

    def close(self):
        """Close the app"""
        self.destroy()
        exit()


class Calculator(Frame):
    """Writing nutritional values of the user defined food"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")
        self.master.config(bg = "black")
        self.master.geometry('350x350')

        def on_click():
            """Checking data and writing the results"""
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            #check if gram is integer and product is string
            try:
                gram = int(entryGram.get())
            except:
                messagebox.showerror("Error", "Please enter correct data!")
            try:
                x = int(product)
                messagebox.showerror("Error", "Please enter correct data!")
            except:
                Functions.file_open()
                Functions.add_product(product, gram)

                output.insert(END, Functions.result())


        label = Label(self, text ="Enter a product that you ate.", bg = "black", fg = "white")
        label.pack()
        # user input, product
        label2 = Label(self, text = "Name: ", bg = "black", fg = "white")
        label2.pack()
        entryProduct = Entry(self, width = 20, bg = "white")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text = "Amount: ", bg = "black", fg = "white")
        label3.pack()
        entryGram = Entry(self, width = 20, bg = "white")
        entryGram.pack()
        # submit
        submit = Button(self, text = "Submit", width = 8, command = on_click)
        submit.pack(padx = 5, pady = 5)
        # output
        label4 = Label(self, text = "These are the nutrinion values:", bg = "black", fg = "white")
        label4.pack()
        output = Text(self, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()

        #going back to menu
        self.button = Button(self, text = "Back", width = 8, command = lambda: master.switch(Menu))
        self.button.pack(padx = 5, pady = 5)


class File_Write(Frame):
    """User can add new new products and their values"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")
        self.master.config(bg = "black")
        self.master.geometry('350x350')

        def validate():
            """Checks is the user inputs correct data"""
            def write():
                """Writes to file"""
                file = open("Products.txt", "a")
                productValue = "%s %s:%s:%s:%s" % (productName.get(), kcal.get(), protein.get(), carb.get(), fat.get())
                file.write("\n" + productValue)
                file.close()
                #Emptying inputs
                productName.delete(0, END)
                kcal.delete(0, END)
                protein.delete(0, END)
                carb.delete(0, END)
                fat.delete(0, END)

            # checking if kcal, protein, carb and fat are integers and productName is a string
            try:
                x = int(productName.get())
                error = True
            except:
                 pass
            try:
                x = int(kcal.get())
                x = int(protein.get())
                x = int(carb.get())
                x = int(fat.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                #writing to a file
                write()


        label = Label(self, text ="Enter the product name and its nutritional "\
                "values per 100 gram", bg = "black", fg = "white")
        label.pack()
        label1 = Label(self, text = "Name:", bg = "black", fg = "white")
        label1.pack()
        productName = Entry(self, width = 20, bg = "white")
        productName.pack()

        label2 = Label(self, text = "Calories:", bg = "black", fg = "white")
        label2.pack()
        kcal = Entry(self, width = 20, bg = "white")
        kcal.pack()

        label3 = Label(self, text = "Protein:", bg = "black", fg = "white")
        label3.pack()
        protein = Entry(self, width = 20, bg = "white")
        protein.pack()

        label4 = Label(self, text = "Carbs:", bg = "black", fg = "white")
        label4.pack()
        carb = Entry(self, width = 20, bg = "white")
        carb.pack()

        label5 = Label(self, text = "Fat:", bg = "black", fg = "white")
        label5.pack()
        fat = Entry(self, width = 20, bg = "white")
        fat.pack()

        submit = Button(self, text = "Submit", width = 8, command = validate)
        submit.pack(padx = 5, pady = 5)

        button3 = Button(self, text = "Back", width = 20, command = lambda: master.switch(Menu))
        button3.pack(padx = 5, pady = 5)


if __name__ == "__main__":
    app = App()
    app.mainloop()

