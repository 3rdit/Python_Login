#login user interface + input/output command(wip)

command_text = None

try:
    import time
    import Tkinter
    from Tkinter import Frame, Text, Tk
    from Tkconstants import YES, BOTH
    from Tkinter import messagebox
except ImportError: #python 3 uses tkinter with lowercase, catch "importerror" and then perform following code to import correct information
    import time
    import tkinter
    from tkinter import Frame, Text, Tk
    from tkinter.constants import YES, BOTH
    from tkinter import messagebox

window = tkinter.Tk()
window.configure(background="#a1dbcd") #"configure" the background to hex code

password = "password" #widget needs string to function (i mean i could just add it in but it's nicer this way)

class custom_textentry(Frame): #basically a class that creates a textbox with width/height and sets settings automatically
    def __init__(self, master, width=0, height=0, **kwargs): #**kwargs = dictionary
        self.width = width
        self.height = height

        Frame.__init__(self, master, width=self.width, height=self.height)
        self.text_widget = Text(self, **kwargs)
        self.text_widget.pack(expand=YES, fill=BOTH)

    def pack(self, *args, **kwargs):
        Frame.pack(self, *args, **kwargs) #packs the frame (initializes it)
        
        self.pack_propagate(False) #disable resize of widget on font change

    def grid(self, *args, **kwargs):
        Frame.grid(self, *args, **kwargs)
        self.grid_propagate(False)


def run_command():
	return 0 #i still have to finish this


def create_command_ui(): #work in progress
    print("main called successfully")

    window.destroy()
    main_window = tkinter.Tk()

    #make symetrical to the login window
    main_window.title("Login Gui")
    main_window.geometry("400x200")
    main_window.wm_iconbitmap('datboi.ico')
    main_window.configure(background="#a1dbcd")
        
    #set all widgets
    output_textfield = custom_textentry(main_window, width=350, height=170).pack() #output field
    input_textfield = tkinter.Entry(main_window) #username field
    command_text = input_textfield.get()

    execute_button = tkinter.Button(main_window, text="EXE", command=run_command) #create a button widget, submit button with the command

    input_textfield.pack()
    main_window.mainloop()


def authentication():
    #todo: make an actual authentication server sided
    usernametext = username_textfield.get()
    passwordtext = password_textfield.get()
    
    if usernametext == "azulx" or usernametext == "tyquan" and passwordtext == password: #"password"
        #unable to create the window earlier in code due to setting something to the tk function causing the window to pop up -_-
        
        print("authorized user, opening secondary window")
        create_command_ui()
        
    else:
        messagebox.showinfo("authentication error!", "username or password was incorrect!")
        return 0
        

#widgets for the application
label = tkinter.Label(window, text="Enter your username and password")
username_textfield = tkinter.Entry(window) #username field
password_textfield = tkinter.Entry(window, textvariable=password, show='*') #set variable to the password so the showed text is "*"

def button_callback():
    authentication()

submit_button = tkinter.Button(window, text="Submit", command=button_callback) #create a button widget, submit button with the command

#my misc stuff todo with the application
window.title("Login Gui") #name of the simple user interface
window.geometry("200x100") #set size elements of the ui
window.wm_iconbitmap('datboi.ico') #set icon, ico file must be located in the same directory as the python source file (.py)

#"pack" (load) the widgets into the window
label.pack()
username_textfield.pack() 
password_textfield.pack()
submit_button.pack()

#create the window
window.grab_set()
window.focus()
window.mainloop()
