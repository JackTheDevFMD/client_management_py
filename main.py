# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
# Base switching templates frame edited from above link ^

import tkinter as tk 
import pandas as pd
import hashlib

# Sets the screensize as a global variable so it can be accessed anywhere
global SCREENSIZE
SCREENSIZE = "400x300"

# Sets the background colour as global so it can, again, be changed from anywhere
global BACKGROUND_COLOUR
BACKGROUND_COLOUR = "#bcbcbc"

global BUTTON_COLOUR
BUTTON_COLOUR = "#eeeeee"

global TEXT_COLOUR
TEXT_COLOUR = "#000000"

global USERLOGGED
USERLOGGED = 0

global SET_HEIGHT
SET_HEIGHT = 2

global SET_WIDTH
SET_WIDTH = 20

global CHOSENONE
CHOSENONE = None

# The function to set the new background colour outside of the class so the background is the same over all windows.
def setColour(back_colour, text_col, button):
    global BACKGROUND_COLOUR
    global TEXT_COLOUR
    global BUTTON_COLOUR
    BACKGROUND_COLOUR = back_colour
    TEXT_COLOUR = text_col
    BUTTON_COLOUR = button

def changeUName(name):
    global USERLOGGED
    USERLOGGED = name

def screenSizeChange(size):
    global SCREENSIZE
    SCREENSIZE = size

def buttonChange(height, width):
    global SET_HEIGHT
    SET_HEIGHT = height

    global SET_WIDTH 
    SET_WIDTH = width

def customerChoice(chosenOne):
    global CHOSENONE
    CHOSENONE = chosenOne

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(mainWindow)
        self.geometry(SCREENSIZE)
        self.configure(bg=BACKGROUND_COLOUR)
        # The self.configure allows the background to be changed as its tied to the global variable

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class mainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)
        # The bg=BACKGROUND_COLOUR means the background is the same as all other windows

        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")

        self.access = tk.Button(self, text="Accessiability features", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(accessWindow)).pack()
        # lambda: master.switch_frame(accessWindow) means you are accessing the parent class function switch_frame to change the frame to the accessiability window
        # The lambda function is a single line function that allows for aother one to be called. 

        self.login = tk.Button(self, text="Login", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(loginWindow)).pack()

        if USERLOGGED != 0:
            self.display_name = tk.Label(self, text="Welcome back: "+USERLOGGED, bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

            self.customerArea = tk.Button(self, text="Customer Panel", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(customerPanel)).pack()

            if USERLOGGED == "admin":
                self.adminArea = tk.Button(self, text="Admin Panel", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(adminPanel)).pack()

            self.logout = tk.Button(self, text="Logout", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.logout).pack()

    def close(self):
        self.master.destroy()

    def logout(self):
        USERLOGGED = 0
        changeUName(USERLOGGED)

        self.master.switch_frame(mainWindow)
        
class accessWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")
        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack(side="right")

        self.bgLabel = tk.Label(self, text="Background Colour", bg=BACKGROUND_COLOUR, height=SET_HEIGHT, width=SET_WIDTH, fg=TEXT_COLOUR).pack()

        self.darkButton = tk.Button(self, text="Dark mode", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.dark).pack()
        self.lightButton = tk.Button(self, text="Light mode", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.light).pack()

        self.bgLabel = tk.Label(self, text="Screensize", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.smallButton = tk.Button(self, text="Small", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.small_Screen).pack()
        self.mediumButton = tk.Button(self, text="Medium", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.medium_screen).pack()
        self.largeButton = tk.Button(self, text="Large", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.large_screen).pack()

        self.bgLabel = tk.Label(self, text="Button Size", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.smallBButton = tk.Button(self, text="Small", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.small_buttons).pack()
        self.mediumBButton = tk.Button(self, text="Medium", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.medium_buttons).pack()
        self.largeBButton = tk.Button(self, text="Large", height=SET_HEIGHT, width=SET_WIDTH, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.large_buttons).pack()

    def close(self):
        self.master.destroy()

    def dark(self):
        BACKGROUND_COLOUR = "#454242" # Dark grey
        TEXT_COLOUR = "#ffffff" # White
        BUTTON_COLOUR = "#575454" # Darker Grey
        setColour(BACKGROUND_COLOUR, TEXT_COLOUR, BUTTON_COLOUR)
        self.master.configure(bg=BACKGROUND_COLOUR)
        self.master.switch_frame(mainWindow)
        # Simply changing background colour, then running the function and finally changing the parent class background colour. 

    def light(self):
        BACKGROUND_COLOUR = "#bcbcbc" # Light grey
        TEXT_COLOUR = "#000000" # White
        BUTTON_COLOUR = "#eeeeee" # Dull white
        setColour(BACKGROUND_COLOUR, TEXT_COLOUR, BUTTON_COLOUR)
        self.master.configure(bg=BACKGROUND_COLOUR)
        self.master.switch_frame(mainWindow)
        # Simply changing background colour, then running the function and finally changing the parent class background colour.

    def small_Screen(self):
        SCREENSIZE = "400x300"
        # Set's the new size of the screen
        screenSizeChange(SCREENSIZE)
        # Changes it within a global function 
        self.master.geometry(SCREENSIZE)
        # Sets the master geometry to change the screensize

    def medium_screen(self):
        SCREENSIZE = "600x500"
        screenSizeChange(SCREENSIZE)
        self.master.geometry(SCREENSIZE)

    def large_screen(self):
        SCREENSIZE = "1000x900"
        screenSizeChange(SCREENSIZE)
        self.master.geometry(SCREENSIZE)

    def small_buttons(self):
        SET_HEIGHT = 2
        SET_WIDTH = 15
        buttonChange(SET_HEIGHT,SET_WIDTH)
        self.master.switch_frame(mainWindow)

    def medium_buttons(self):
        SET_HEIGHT = 2
        SET_WIDTH = 20
        buttonChange(SET_HEIGHT,SET_WIDTH)
        self.master.switch_frame(mainWindow)

    def large_buttons(self):
        SET_HEIGHT = 2
        SET_WIDTH = 25
        buttonChange(SET_HEIGHT,SET_WIDTH)
        self.master.switch_frame(mainWindow)

class loginWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        self.loginTitle = tk.Label(self, text="Login", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack(side="top")
        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")

        self.username = tk.Label(self, text="Username", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()
        self.usernameIn = tk.StringVar()
        usernameEntery = tk.Entry(self, textvariable = self.usernameIn).pack()

        self.passwordLb = tk.Label(self, text="Password", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()
        self.password = tk.StringVar()
        passwordEntery = tk.Entry(self, textvariable = self.password, show="*").pack(pady=10, padx=30)

        self.submitButton = tk.Button(self, text="Submit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.userpass_get).pack()

        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack()

        self.signup = tk.Button(self, text="Signup", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(signUpWindow)).pack()


    def userpass_get(self):
        username = str(self.usernameIn.get())
        password = str(self.password.get())

        salt = "hb43ifdvnjlrfe9i0evrhuwf490utb"
        password = password+salt
        hashedPassword = hashlib.md5(password.encode())
        password = hashedPassword.hexdigest()

        username_toggle = False
        password_toggle = False

        if len(username) < 1 or len(password) < 1:
            error = tk.Label(self, text="Please try again, something went wrong.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
        else:
            try:
                df = pd.read_csv('clients.csv')

                for x in range(0, len(df['Usernames'])):
                    if df['Usernames'][x] == username:
                        username_toggle = True
                    if df['Passwords'][x] == password:
                        password_toggle = True

                if username_toggle and password_toggle:
                    changeUName(username)
                    self.master.switch_frame(mainWindow)
                else:
                    error = tk.Label(self, text="We can not find you account, please try again or make a new one!", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
            except:
                error = tk.Label(self, text="Something went wrong, please try again.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
                
    def close(self):
        self.master.destroy()


class signUpWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        self.signupTitle = tk.Label(self, text="Sign Up", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack(side="top")
        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")
        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack(side="right")

        self.usernameLabel = tk.Label(self, text="Username", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack(padx=30)
        self.username = tk.StringVar()
        usernameEntery = tk.Entry(self, textvariable = self.username).pack()

        self.emailLabel = tk.Label(self, text="Email", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack(padx=30)
        self.email = tk.StringVar()
        emailEntery = tk.Entry(self, textvariable = self.email).pack()

        self.cemailLabel = tk.Label(self, text="Confirm Email", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack(padx=30)
        self.cemail = tk.StringVar()
        cemailEntery = tk.Entry(self, textvariable = self.cemail).pack()

        self.passwordLb = tk.Label(self, text="Password", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack(padx=30)
        self.password = tk.StringVar()
        passwordEntery = tk.Entry(self, textvariable = self.password, show="*").pack()

        self.submitButton = tk.Button(self, text="Submit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.submit).pack(pady=30, padx=30)
    
    def submit(self):
        username = str(self.username.get())
        email = str(self.email.get())
        cemail = str(self.cemail.get())
        password = str(self.password.get())

        if '@' not in list(email):
            error = tk.Label(self, text="Please try again, an email must contain an @ symbol.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()

        elif email != cemail:
            error = tk.Label(self, text="Please try again, your emails don't match up.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()

        elif len(username) > 25:
            error = tk.Label(self, text="Please try again, your username must be below 25 characters.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
        
        elif len(password) > 25:
            
            error = tk.Label(self, text="Please try again, your passwords must be below 25 characters.", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
        else:
            salt = "hb43ifdvnjlrfe9i0evrhuwf490utb"
            password = password+salt
            hashedPassword = hashlib.md5(password.encode())
            password = hashedPassword.hexdigest()
            
            try:
                writing = {'Usernames': [username], 'Emails': [email], 'Passwords': [password]}
                df = pd.DataFrame(writing)
                df.to_csv('clients.csv', mode='a', index=False, header=False)

                self.master.switch_frame(loginWindow)

            except:
                error = tk.Label(self, text="Please try again, something went wrong!", fg="#cc0000", bg=BACKGROUND_COLOUR).pack()
                
    def close(self):
        self.master.destroy()

class customerPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        userID = None

        self.careaLB = tk.Label(self, text="Customer area", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        self.display_name = tk.Label(self, text="Welcome back: "+USERLOGGED, bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")
        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack(side="right")

        df2 = pd.read_csv('client_info.csv', encoding='latin1')

        for x in range(0, len(df2)):
            if df2['Usernames'][x] == USERLOGGED:
                userID = x
                break

        if userID != None:

            self.display_name = tk.Label(self, text="Total spent: "+df2['Purchase Amount'][userID], bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()
            self.customerLevel = tk.Label(self, text="Customer Level: "+df2['Customer Level'][userID], bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()
            self.ProductsPurchased = tk.Label(self, text="Products purchased: ", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

            products_list = df2['Products'][userID].split(', ')
            
            for x in range(len(products_list)):
                self.ProductsPurchased = tk.Label(self, text="- "+products_list[x], bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()
        else:
            self.display_name = tk.Label(self, text="Your account has not been found.", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()
        
    def close(self):
        self.master.destroy()



class adminPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        userID = None

        self.careaLB = tk.Label(self, text="Admin area", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        self.display_name = tk.Label(self, text="Welcome back: "+USERLOGGED, bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")
        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack(side="right")

        df2 = pd.read_csv('client_info.csv', encoding='latin1')

        # Look at different customers

        amount_customers = str(len(df2['Usernames']))
        spent_amount = 0
        customers_names = []

        for x in range(len(df2['Purchase Amount'])):
            spent_amount += int(df2['Purchase Amount'][x])

        for y in range(len(df2['Usernames'])):
            customers_names.append(df2['Usernames'][y])

        self.custInfo = tk.Label(self, text="Customers information", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        self.customersAmount = tk.Label(self, text="Total customers: "+amount_customers, bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()
        self.spentAmount = tk.Label(self, text="Total amount spent: £"+str(spent_amount), bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.variable = tk.StringVar()

        self.variable.set(customers_names[0])

        customer_list = tk.OptionMenu(self, self.variable, *customers_names, command=self.chosen_customer).pack()

        self.output_label = tk.Label(self, foreground='red', bg=BACKGROUND_COLOUR).pack()
        
    def close(self):
        self.master.destroy()

    def chosen_customer(self, *args):
        customer_chosen = self.variable.get()
        customerChoice(customer_chosen)

        self.master.switch_frame(indCustomerPanel)


class indCustomerPanel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=BACKGROUND_COLOUR)

        self.careaLB = tk.Label(self, text=CHOSENONE+"s' area", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        df2 = pd.read_csv('client_info.csv', encoding='latin1')

        userID = None

        for x in range(0, len(df2)):
            if df2['Usernames'][x] == CHOSENONE:
                userID = x
                break

        self.customerArea = tk.Label(self, text="Customer Information:", fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        self.careaLB = tk.Label(self, text=CHOSENONE+" has spent in total: £"+str(df2['Purchase Amount'][userID]), fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()
        self.level = tk.Label(self, text=CHOSENONE+" is at a customer level: "+str(df2['Customer Level'][userID]), fg=TEXT_COLOUR, bg=BACKGROUND_COLOUR).pack()

        self.ProductsPurchased = tk.Label(self, text="Products purchased: ", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        products_list = df2['Products'][userID].split(', ')
            
        for x in range(len(products_list)):
            self.ProductsPurchased = tk.Label(self, text="- "+products_list[x], bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR).pack()

        self.quitButton = tk.Button(self, text="Quit", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=self.close).pack(side="right")
        self.backOne = tk.Button(self, text="Back one page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(adminPanel)).pack(side="right")
        self.back = tk.Button(self, text="Main page", height=SET_HEIGHT, width=SET_WIDTH-7, bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=lambda: master.switch_frame(mainWindow)).pack(side="right")
        
    def close(self):
        self.master.destroy()

app = MainApplication()
if __name__ == "__main__":
    app.mainloop()
