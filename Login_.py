from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
import pymysql.cursors
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from PIL import Image, ImageTk  # Use PIL for better image
# Global variable to store the logged-in account number
logged_in_acc_no = None

lwin=Tk()
lwin.config(bg="#53b5a1")
lwin.resizable(False,False)
lwin.geometry("700x480")
lwin.title("Account creation")

def validate_contact(contact_no):
    # Check if the entered contact number has exactly 10 digits and is numeric
    if contact_no.isdigit() and len(contact_no) == 10:
        return True
    else:
        messagebox.showerror("Invalid Input", "Contact number must be exactly 10 digits.")
        return False
    
def toggle_pin():
    """Toggle between showing and hiding the PIN."""
    if tb22.cget('show') == '*':
        tb22.config(show='')  # Show the actual PIN
        show_hide_btn.config(text="Hide Password")
    else:
        tb22.config(show='*')  # Mask the PIN
        show_hide_btn.config(text="Show Password")
        



        
def login():
    lid=us.get()
    lpin=us1.get()
    try:
       conn=pymysql.connect(host="localhost",user="root",password='',db='bank')
       a=conn.cursor()
       a.execute("SELECT acc_no, name, amount FROM users WHERE email ='"+lid+"'  AND password = '"+lpin+"'")
       result=a.fetchone()
       if result:
             # acc_no
           logged_in_acc_no = result[0]  # acc_no
           name = result[1]# name
           balance=result[2]
           lwin.withdraw()
           #messagebox.showinfo("Success", "Login successfully")
           main_page(logged_in_acc_no,name, balance)
       else:
          messagebox.showerror("Error", "Invalid email or password.")

    except pymysql.MySQLError as e:
        messagebox.showerror("Error", f"Connection error: {e}")
    conn.close()

def login2():
    global rewin
    global login_win
    rewin.withdraw()
    login_win = Tk()
    login_win.config(bg="#53b5a1")
    login_win.geometry("700x490")
    login_win.title("Login")

    def toggle_pin1():
        if text_2.cget('show') == '*':
            text_2.config(show='')  # Show the actual PIN
            show_hide_btn1.config(text="Hide Password")
        else:
            text_2.config(show='*')  # Mask the PIN
            show_hide_btn1.config(text="Show Password")

    def verify_login():
        account_no=text_1.get()
        lpin=text_2.get()
        try:
           conn=pymysql.connect(host="localhost",user="root",password='',db='bank')
           a=conn.cursor()
           a.execute("SELECT acc_no, name, amount FROM users WHERE email ='"+account_no+"'  AND password = '"+lpin+"'")
           result=a.fetchone()
           if result:
               logged_in_acc_no = result[0]  # acc_no
               name = result[1]# name
               balance=result[2]
               lwin.withdraw()
               #messagebox.showinfo("Success", "Login successfully")
               main_page(logged_in_acc_no,name, balance)

           else:
               messagebox.showerror("Error", "Invalid email or Password.")

        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Connection error: {e}")
        conn.close()

    lg=StringVar()
    lg1=StringVar()

    lb=Label(login_win, text="BANK MANAGEMENT", bg="white", relief="sunken",bd=10,width=27,font=("Times New Roman",33))
    lb.place(x=10, y=10)
    lb=Label(login_win, text="---ACCOUNT LOGIN---", bg="#53b5a1", font=("Times New Roman",33),width=25)
    lb.place(x=50, y=100)

    lb1=Label(login_win, text="Enter email:", font=("Times New Roman",15), bg="#53b5a1")
    lb1.place(x=90, y=200)

    lb2=Label(login_win, text="Enter password:", bg="#53b5a1", font=("Times New Roman",15))
    lb2.place(x=90, y=270)

    bt=Button(login_win,text="Login", font=("Times New Roman",13), bd=10, bg="white",width=20, command=verify_login)
    bt.place(x=220, y=330)

    bt=Button(login_win,text="Don't have an account? Register here", font=("Times New Roman",10), fg="blue", bg="white", command=registration)
    bt.place(x=90, y=410)

    show_hide_btn1 = Button(login_win, text="Show Password", command=toggle_pin1)
    show_hide_btn1.place(x=530, y=270)

    text_1= Entry(login_win, textvariable=us,width=25)
    text_1.place(x=370, y=200)

    text_2= Entry(login_win, textvariable=us1,width=25, show='*')
    text_2.place(x=370, y=270)
    
def registration():
    global rewin
    lwin.withdraw()
    rewin=Tk()
    rewin.config(bg="#53b5a1")
    rewin.resizable(False,False)
    rewin.geometry("750x740")
    rewin.title("Account creation")

    def toggle_pin8():
        """Toggle between shorewing and hiding the PIN."""
        if tb66.cget('show') == '*':
            tb66.config(show='')  # Show the actual PIN
            show_hidebtn.config(text="Hide Password")
        else:
            tb66.config(show='*')  # Mask the PIN
            show_hidebtn.config(text="Show Password")
        
    def users():
        uid=tb1.get()
        uname=tb2.get()
        uamount= tb3.get()
        uaddress= tb4.get()
        ucontact= tb5.get()
        upass= tb66.get()
        upass2= tb77.get()
        uemail= tb8.get()
        if not all([uid, uname, uamount, uaddress, ucontact, upass, upass2, uemail]):
            messagebox.showerror("Error", "All fields must be filled.")
            return

    # Validate contact number
        if not validate_contact(ucontact):
            return

    # Check if password is at least 6 characters long
        if len(upass) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return

    # Check if passwords match
        if upass != upass2:
            messagebox.showerror("Error", "New Password and Confirm Password do not match.")
            return

        
        try:
            conn= pymysql.connect(host="localhost",user="root", password="", db="bank")
            a=conn.cursor()
            a.execute("insert into users values('"+uid+"','"+uname+"','"+uamount+"','"+uaddress+"','"+ucontact+"','"+upass+"','"+uemail+"')")
            conn.commit()
            messagebox.showinfo("message","registration successful")
        except:
            conn.rollback()
            messagebox.showinfo("message","unsuccessful")
        conn.close()
        

    def clear():
        tb1.delete(0, END)
        tb2.delete(0, END)
        tb3.delete(0, END)
        tb4.delete(0, END)
        tb5.delete(0, END)
        tb66.delete(0, END)
        tb77.delete(0, END)
        tb8.delete(0, END)

    
    us=StringVar()
    us1=StringVar()
    us2=StringVar()
    us3=StringVar()
    us4=StringVar()
    us5=StringVar()
    us6=StringVar()
    us7=StringVar()


    lb=Label(rewin, text="REGISTRATION", bg="white", font=("Times New Roman",30),width=23, bd=10, relief="raised")
    lb.place(x=120, y=50)

    lb1=Label(rewin, text="Enter account number:", font=("Times New Roman",15), bg="#53b5a1")
    lb1.place(x=200, y=150)

    lb2=Label(rewin, text="Enter name:", bg="#53b5a1", font=("Times New Roman",15))
    lb2.place(x=200, y=200)

    lb3=Label(rewin, text="Enter amount:", bg="#53b5a1", font=("Times New Roman",15))
    lb3.place(x=200, y=250)

    lb4=Label(rewin, text="Enter address:", bg="#53b5a1", font=("Times New Roman",15))
    lb4.place(x=200, y=300)

    lb5=Label(rewin, text="Enter contact:", bg="#53b5a1", font=("Times New Roman",15))
    lb5.place(x=200, y=350)

    lb6=Label(rewin, text="password(more than 6 words):", bg="#53b5a1", font=("Times New Roman",15))
    lb6.place(x=200, y=400)

    lb7=Label(rewin, text="Confirm password:", bg="#53b5a1", font=("Times New Roman",15))
    lb7.place(x=200, y=450)

    lb8=Label(rewin, text="Enter email:", bg="#53b5a1", font=("Times New Roman",15))
    lb8.place(x=200, y=500)

    bt=Button(rewin, text="Submit", bg="white", bd= 10, relief="raised", font=("Arial", 10, "bold"), width=10, command=users)
    bt.place(x=350, y=570)

    bt=Button(rewin, text="Clear", bg="white", bd= 10, relief="raised", font=("Arial", 10, "bold"), width=10, command=clear)
    bt.place(x=200, y=570)

    bt=Button(rewin, text="Already have an account? Login here", bg="white", fg="blue", relief="raised", font=("Arial", 8, "bold"), width=30, command=login2)
    bt.place(x=200, y=640)

    show_hidebtn = Button(rewin, text="Show Password", command=toggle_pin8)
    show_hidebtn.place(x=600, y=405)

    tb1= Entry(rewin, textvariable=us)
    tb1.place(x=450, y=155)

    tb2= Entry(rewin, textvariable=us1)
    tb2.place(x=450, y=205)

    tb3= Entry(rewin, textvariable=us2)
    tb3.place(x=450, y=255)

    tb4= Entry(rewin, textvariable=us3)
    tb4.place(x=450, y=305)

    tb5= Entry(rewin, textvariable=us4)
    tb5.place(x=450, y=355)

    tb66= Entry(rewin, textvariable=us5, show="*")
    tb66.place(x=450, y=405)

    tb77= Entry(rewin, textvariable=us6, show="*")
    tb77.place(x=450, y=455)

    tb8= Entry(rewin, textvariable=us7)
    tb8.place(x=450, y=505)


def fetch_transactions(account_no):
    connection = pymysql.connect(host='localhost', user='root', password='', db='bank')
    cursor = connection.cursor()
    
    # Fetch the transactions for the given account number
    query = "SELECT date_time, transaction_type, receiver_acc_no, amount FROM transactions WHERE Account_no = %s"
    cursor.execute(query, (account_no,))
    transactions = cursor.fetchall()
    
    connection.close()
    return transactions

def fetch_user_balance(account_no):
    connection = pymysql.connect(host='localhost', user='root', password='', db='bank')
    cursor = connection.cursor()

    # Fetch the balance for the given account number
    query = "SELECT amount FROM users WHERE acc_no = %s"
    cursor.execute(query, (account_no,))
    balance = cursor.fetchone()[0]
    
    connection.close()
    return balance

def detect_low_balance_periods(transactions, balance, threshold=1000, limit=3):
    low_balance_count = 0
    if balance < threshold:
        low_balance_count += 1

    for transaction in transactions:
        transaction_type = transaction[1]
        amount = transaction[3]

        if transaction_type.lower() == 'debit':
            balance -= amount

        if balance < threshold:
            low_balance_count += 1

        if low_balance_count >= limit:
            return True
    return False

def detect_frequent_payees(transactions, limit=3):
    payee_count = {}

    for transaction in transactions:
        payee = transaction[2]
        if payee in payee_count:
            payee_count[payee] += 1
        else:
            payee_count[payee] = 1

    frequent_payees = [payee for payee, count in payee_count.items() if count >= limit]
    return frequent_payees

def generate_recommendations(account_no):
    transactions = fetch_transactions(account_no)
    balance = fetch_user_balance(account_no)

    recommendations = []
    if detect_low_balance_periods(transactions, balance):
        recommendations.append("‣Your balance often \ndrops below the threshold.\n You may want to consider\n setting a savings goal\n or reviewing your \nspending habits.")
    
    frequent_payees = detect_frequent_payees(transactions)
    if frequent_payees:
        recommendations.append(f"\n\n‣You frequently \ntransfer to {frequent_payees[0]}\n. Would you like to\n make a transfer now?")
    
    return recommendations

def show_recommendations(frame, account_no):
    recommendations = generate_recommendations(account_no)
    if recommendations:
        recommendations_text = "\n".join(recommendations)
    else:
        recommendations_text = "No recommendations at the \nmoment."

    rec_label = Label(frame, text="Recommendations", font=("Arial", 14, "bold"), bg="#53b5a1")
    rec_label.place(x=890, y=250)
    
    recommendations_label = Label(frame, text=recommendations_text, font=("Arial", 12), bg="#53b5a1", wraplength=300)
    recommendations_label.place(x=880, y=300)



def fetch_balance_history(logged_in_acc_no):
    transaction_dates = []
    balance_history = []

    try:
       connection = pymysql.connect(
           host="localhost",
           user="root",
           password="",
           database="bank"  
           )
       h = connection.cursor()

    # Query to fetch the transaction date and balance for a specific account number
    
       h.execute("SELECT date_time, amount FROM transactions WHERE Account_no = %s ORDER BY date_time", logged_in_acc_no)
       result = h.fetchall()

       current_balance = 0  # Starting balance is 0; we'll accumulate it based on deposits/withdrawals
       for row in result:
           transaction_dates.append(row[0].strftime('%Y-%m-%d %H:%M:%S'))  # Format dates as strings
           amount = row[1] if row[1] else 0  # Handle NULL deposits
           current_balance += amount  # Calculate the balance after each transaction
           balance_history.append(current_balance)

           
    except pymysql.MySQLError as e:
        messagebox.showerror("Error", f"Connection error: {e}")
    connection.close()
    return transaction_dates, balance_history
 
# Function to plot balance trend
def plot_balance_trend(frame, account_number):
    transaction_dates, balance_history = fetch_balance_history(account_number)

    if not transaction_dates or not balance_history:
        messagebox.showinfo("No Data", "No transaction data found for the given account.")
        return

    # Create the figure for plotting
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    #ax = fig.add_subplot(111)

    # Plot the balance history as a line chart
    ax.plot(transaction_dates, balance_history, marker='o', linestyle='-', color='blue')

    # Set chart title and labels
    ax.set_title('Balance Trend Over Time')
    ax.set_xlabel('Date and time')
    ax.set_ylabel('Balance (₹)')

    fig.tight_layout()
    fig.autofmt_xdate()

# Set font size for date and time labels
    ax.tick_params(axis='x', labelsize=8)

    # Rotate date labels for better readability
    plt.xticks(rotation=30)

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


def show_account_details(account_no):
    account_win = Toplevel(lwin)
    account_win.title("Account Details")
    account_win.geometry("600x400")
    account_win.config(bg="#53b5a1")

    conn = pymysql.connect(
           host="localhost",
           user="root",
           password="",
           database="bank"  
           )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT acc_no, name, amount, address, contact, email FROM users WHERE acc_no=%s", (account_no,))
        account_data = cursor.fetchone()

        if account_data:
            Framee=Frame(account_win, bg="white",  bd=10, relief="raised", width=500, height=300)
            Framee.place(x=50, y=50)
            Label(Framee, text="Account No:", font=("Times New Roman", 15), bg="white").place(x=30, y=30)
            Label(Framee, text=account_data[0], font=("Times New Roman", 15), bg="white").place(x=200, y=30)

            Label(Framee, text="Name:", font=("Times New Roman", 15), bg="white").place(x=30, y=70)
            Label(Framee, text=account_data[1], font=("Times New Roman", 15), bg="white").place(x=200, y=70)

            Label(Framee, text="Balance:", font=("Times New Roman", 15), bg="white").place(x=30, y=110)
            Label(Framee, text=account_data[2], font=("Times New Roman", 15), bg="white").place(x=200, y=110)

            Label(Framee, text="Address:", font=("Times New Roman", 15), bg="white").place(x=30, y=150)
            Label(Framee, text=account_data[3], font=("Times New Roman", 15), bg="white").place(x=200, y=150)

            Label(Framee, text="Contact:", font=("Times New Roman", 15), bg="white").place(x=30, y=190)
            Label(Framee, text=account_data[4], font=("Times New Roman", 15), bg="white").place(x=200, y=190)

            Label(Framee, text="Email:", font=("Times New Roman", 15), bg="white").place(x=30, y=230)
            Label(Framee, text=account_data[5], font=("Times New Roman", 15), bg="white").place(x=200, y=230)
        else:
            messagebox.showerror("Error", "Account details not found!")

    except pymysql.MySQLError as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to open the account details window on logo button click
def open_account_details(account_no):
    #global logged_in_acc_no  # Access the logged-in account number
    show_account_details(account_no)

    
def main_page(logged_in_acc_no, name, balance):
    global mwin
    mwin=Tk()
    mwin.config(bg="#53b5a1")
    mwin.resizable(False,False)
    mwin.geometry("1100x700")
    mwin.title("Main Page")

    lb1=Label(mwin, text="DASHBOARD", bg="white", relief="raised",bd=10,width=53,font=("Times New Roman",27))
    lb1.place(x=5, y=80)

    lb2=Label(mwin, text=f"--------------------WELCOME BACK, {name}--------------------", bg="#53b5a1",width=35,font=("Felix Titling",26))
    lb2.place(x=150, y=20)

    lb_balance = Label(mwin, text=f"Current Balance: {balance} INR", bg="white", relief="raised", bd=8, width=43, font=("Times New Roman", 20))
    lb_balance.place(x=315, y=150)

    def update_balance():
        # Fetch the new balance from the database
        new_balance = get_balance_from_database(logged_in_acc_no)  # Implement this function to fetch the balance
        lb_balance.config(text=f"Current Balance: {new_balance} INR")
        # Repeat every 5 seconds
        mwin.after(5000, update_balance)

    update_balance() 

    graph_frame = Frame(mwin, bd=5, bg="#53b5a1")
    graph_frame.place(x=350, y=250)

    # Call the function to create the balance trend graph
    plot_balance_trend(graph_frame, logged_in_acc_no)

    frame1=Frame(mwin,bg= "#c42d67", bd=10, relief="raised", width=300, height=550)
    frame1.place(x=5, y=140)

    show_recommendations(mwin, logged_in_acc_no)


    bt=Button(frame1, text="View Transaction History", bg="white", bd= 10, relief="raised", font=("Times New Roman", 15), width=20, height=2, command= statement)
    bt.place(x=10, y=10)

    bt=Button(frame1, text="Transfer funds within bank", bg="white", bd= 10, relief="raised", font=("Times New Roman", 15), width=20, height=2, command=lambda: internal_external(logged_in_acc_no))
    bt.place(x=10, y=110)

    bt=Button(frame1, text="Transfer to other banks", bg="white", bd= 10, relief="raised", font=("Times New Roman", 15), width=20, height=2, command= transfer_funds)
    bt.place(x=10, y=220)

    bt=Button(frame1, text="Manage Payees", bg="white", bd= 10, relief="raised", font=("Times New Roman", 15), width=20, height=2, command=lambda: manage_payees(logged_in_acc_no))
    bt.place(x=10, y=330)

    bt=Button(frame1, text="Update Profile", bg="white", bd= 10, relief="raised", font=("Times New Roman", 15), width=20, height=2, command= profile )
    bt.place(x=10, y=440)

    bt=Button(mwin, text="Log Out", bg="white", fg="red", bd= 5, relief="raised", font=("Times New Roman",10), width=8, command= logout)
    bt.place(x=1020, y=660)

    bt=Button(mwin, text="Account", bg="white", bd= 5, relief="raised", font=("Times New Roman",15),command=lambda: open_account_details(logged_in_acc_no))
    bt.place(x=990, y=150)

    mwin.mainloop()


def get_balance_from_database(account_no):
    # Database connection parameters
    db_host = 'localhost'  # Change if necessary
    db_user = 'root'  # Replace with your DB username
    db_password = ''  # Replace with your DB password
    db_name = 'bank'  # Replace with your database name

    try:
        # Establish a database connection
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        
        with connection.cursor() as cursor:
            # SQL query to get the current balance
            sql = "SELECT amount FROM users WHERE acc_no = %s"  # Adjust table and column names if necessary
            cursor.execute(sql, (account_no,))
            result = cursor.fetchone()

            # Check if result is not None and return the balance
            if result:
                return result[0]  # Assuming amount is the first column in the result
            else:
                return 0  # Return 0 if no record is found
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return 0  # Return 0 or handle the error as needed
    finally:
        # Ensure the connection is closed
        if connection:
            connection.close()

  
def transfer_funds():
    win0=Tk()
    win0.resizable(False,False)
    win0.geometry("700x400")
    win0.title("Welcome to the transfer page")
    win0.config(bg='#53b5a1')

    def choosebank():
        win0.withdraw()
        uid=tby.get()
        upin=tbz.get()

        try:
            conn=pymysql.connect(host="localhost",user="root",password='',db='bank')
            a=conn.cursor()
            a.execute("SELECT * FROM users WHERE email ='"+uid+"'  AND password = '"+upin+"'")
            result=a.fetchone()
            if result:
                global win1
                win1=Toplevel(win0)
                win1.resizable(False,False)
                win1.geometry("700x500")
                win1.title("Welcome to transfer page")
                win1.config(bg='#53b5a1')


                lb=Label(win1, text="SELECT THE OPTION", font=("Times New Roman",30), bg="#53b5a1")
                lb.place(x=150, y=100)


                bt1=Button(win1, text="HDFC", font=("Times New Roman",25), bg="white",width=10, bd=10, command=transfer_bank)
                bt1.place(x=100, y=200)

                bt2=Button(win1, text="STATE", font=("Times New Roman",25), bg="white",width=10, bd=10, command=transfer_bank)
                bt2.place(x=380, y=200)

                bt3=Button(win1, text="PNB", font=("Times New Roman",25), bg="white",width=10, bd=10, command=transfer_bank)
                bt3.place(x=100, y=350)

                bt4=Button(win1, text="ICICI", font=("Times New Roman",25), bg="white",width=10, bd=10, command=transfer_bank)
                bt4.place(x=380, y=350)
            else:
                messagebox.showerror("Error", "Invalid Account Number or Old PIN1.")

        except pymysql.MySQLError as e:
            messagebox.showerror("Error", f"Connection error: {e}")
        conn.close()
    

    def transfer_bank():
        global win1
        win1.withdraw()
        win2=Toplevel(win0)
        win2.resizable(False,False)
        win2.geometry("800x700")
        win2.title("Welcome to transfer page")
        win2.config(bg='#53b5a1')

        def toggle_pin():
            """Toggle between showing and hiding the PIN."""
            if tbl.cget('show') == '*':
                tbl.config(show='')  # Show the actual PIN
                show_hide_btn2.config(text="Hide Password")
            else:
                tbl.config(show='*')  # Mask the PIN
                show_hide_btn2.config(text="Show Password")

        def transfer():
            tid=tbk.get()
            tpin=tbl.get()
            trec=tbn.get()
            tamount=tbm.get()
            try:
               conn=pymysql.connect(host="localhost",user="root",password='',db='bank')
               a=conn.cursor()
               a.execute("SELECT * FROM users WHERE acc_no = %s AND password = %s", (tid, tpin))
               result = a.fetchone()
               if result:
                  a.execute("insert into transactions(Account_no, date_time, transaction_type, receiver_acc_no, amount) values('"+tid+"', now(), 'external transfer ','"+trec+"','"+tamount+"')")
                  a.execute("UPDATE users SET amount = amount - %s WHERE acc_no = %s", (tamount, tid))
                  conn.commit()
                  messagebox.showinfo("message","money transfered successfully")
               else:
                  messagebox.showerror("Error", "Invalid Account Number or Old Password.")

            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Connection error: {e}")
            conn.close()
    
        ab= StringVar()  
        ab1= StringVar()   
        ab2= StringVar()
        ab3= StringVar()
        ab4= StringVar()


        lb=Label(win2, text="Enter card number from", font=("Times New Roman",20), bg="#53b5a1")
        lb.place(x=150, y=100)

        lb=Label(win2, text="Enter password", font=("Times New Roman",20), bg="#53b5a1")
        lb.place(x=150, y=200)

        lb=Label(win2, text="Enter amount", font=("Times New Roman",20), bg="#53b5a1")
        lb.place(x=150, y=300)

        lb=Label(win2, text="Enter card number to", font=("Times New Roman",20), bg="#53b5a1")
        lb.place(x=150, y=400)

        lb=Label(win2, text="Enter isfc", font=("Times New Roman",20), bg="#53b5a1")
        lb.place(x=150, y=500)

        bt=Button(win2, text="deposit", font=("Times New Roman",15), bg="white", width=10, height=1, bd=10, command=transfer)
        bt.place(x=160, y=580)

        show_hide_btn2 = Button(win2, text="Hide password", command=toggle_pin)
        show_hide_btn2.place(x=680, y=205)

        tbk=Entry(win2, textvariable=ab)
        tbk.place(x=500, y=110)

        tbl=Entry(win2, textvariable=ab1)
        tbl.place(x=500, y=210)

        tbm=Entry(win2, textvariable=ab2)
        tbm.place(x=500, y=310)

        tbn=Entry(win2, textvariable=ab3)
        tbn.place(x=500, y=410)

        tbo=Entry(win2, textvariable=ab4)
        tbo.place(x=500, y=510)


    us= StringVar()
    us1= StringVar()   


    lb=Label(win0, text="Enter email:", font=("Times New Roman",20), bg="#53b5a1")
    lb.place(x=100, y=100)

    lb=Label(win0, text="Enter password:", font=("Times New Roman",20), bg="#53b5a1")
    lb.place(x=100, y=200)


    bt=Button(win0, text="show", font=("Times New Roman",15), bg="white", width=10, height=1, bd=10, command=choosebank)
    bt.place(x=160, y=280)

    tby=Entry(win0, textvariable=us, width=35)
    tby.place(x=350, y=110)

    tbz=Entry(win0, textvariable=us1, show="*", width=35)
    tbz.place(x=350, y=210)

def internal_external(sender_acc_no):
    def get_payees(sender_acc_no):
        # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = conn.cursor()

        try:
            # Fetch payees for the sender account
            cursor.execute("SELECT payee_account_no, payee_name FROM payees WHERE account_no=%s", (sender_acc_no,))
            payees = cursor.fetchall()
            return [f"{payee[0]} - {payee[1]}" for payee in payees]
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Failed to retrieve payees: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def on_receiver_selection(event):
        selected_value = receiver_combo.get()
        if selected_value == "Other":
            receiver_acc_entry.config(state="normal")
        else:
            receiver_acc_entry.delete(0, END)
            receiver_acc_entry.insert(0, selected_value.split(' - ')[0])  # Insert account number
            receiver_acc_entry.config(state="disabled")

    def transfer_fundss():
        receiver_acc_no = receiver_acc_entry.get()  # Use receiver_acc_entry for manual entry or dropdown selection
        transfer_type = transfer_type_combo.get()  # Get the selected transfer type from the Combobox
        amount = amount_entry.get()

        if not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount!")
            return

        amount = int(amount)

        # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = conn.cursor()

        try:
            # Check if sender has enough balance
            cursor.execute("SELECT amount FROM users WHERE acc_no=%s", (sender_acc_no,))
            sender_balance = cursor.fetchone()

            if not sender_balance:
                messagebox.showerror("Error", "Sender account not found!")
                return

            sender_balance = sender_balance[0]

            if sender_balance < amount:
                messagebox.showerror("Error", "Insufficient balance!")
                return

            # Internal Transfer (Own account)
            if transfer_type == "Internal":
                cursor.execute("SELECT acc_no, name FROM users WHERE acc_no=%s", (receiver_acc_no,))
                receiver = cursor.fetchone()

                if receiver is None:
                    messagebox.showerror("Error", "Receiver account not found in the bank system!")
                    return

                receiver_name = receiver[1]  # Fetch the receiver's name from the result

                # Check if the receiver is already in the payees table
                cursor.execute("SELECT payee_account_no FROM payees WHERE account_no=%s AND payee_account_no=%s", 
                               (sender_acc_no, receiver_acc_no))

                if cursor.fetchone() is None:
                    # Add the receiver as a payee if not already present
                    try:
                        cursor.execute("INSERT INTO payees (account_no, payee_account_no, payee_name) VALUES (%s, %s, %s)", 
                                       (sender_acc_no, receiver_acc_no, receiver_name))
                        conn.commit()
                        messagebox.showinfo("Info", f"Payee '{receiver_name}' added to your list of payees.")
                    except pymysql.MySQLError as e:
                        messagebox.showerror("Database Error", f"Failed to add payee: {e}")
                        conn.rollback()
                        return

                # Perform the transfer for internal accounts
                cursor.execute("UPDATE users SET amount = amount - %s WHERE acc_no = %s", (amount, sender_acc_no))
                cursor.execute("UPDATE users SET amount = amount + %s WHERE acc_no = %s", (amount, receiver_acc_no))

                # Log the transaction
                cursor.execute(
                    "INSERT INTO transactions (Account_no, date_time, transaction_type, receiver_acc_no, amount) VALUES (%s, now(), %s, %s, %s)",
                    (sender_acc_no, "Internal Transfer", receiver_acc_no, amount)
                )
                conn.commit()
                messagebox.showinfo("Success", "Internal transfer successful!")

            # External Transfer (Another user's account)
            elif transfer_type == "External":
                cursor.execute("SELECT acc_no, name FROM users WHERE acc_no=%s", (receiver_acc_no,))
                receiver = cursor.fetchone()

                if receiver is None:
                    messagebox.showerror("Error", "Receiver account not found in the bank system!")
                    return

                receiver_name = receiver[1]

                cursor.execute("SELECT payee_account_no FROM payees WHERE account_no=%s AND payee_account_no=%s", 
                               (sender_acc_no, receiver_acc_no))

                if cursor.fetchone() is None:
                    try:
                        cursor.execute("INSERT INTO payees (account_no, payee_account_no, payee_name) VALUES (%s, %s, %s)", 
                                       (sender_acc_no, receiver_acc_no, receiver_name))
                        conn.commit()
                        messagebox.showinfo("Info", f"Payee '{receiver_name}' added to your list of payees.")
                    except pymysql.MySQLError as e:
                        messagebox.showerror("Database Error", f"Failed to add payee: {e}")
                        conn.rollback()
                        return

                # Perform the external transfer
                cursor.execute("UPDATE users SET amount = amount - %s WHERE acc_no = %s", (amount, sender_acc_no))
                cursor.execute("UPDATE users SET amount = amount + %s WHERE acc_no = %s", (amount, receiver_acc_no))

                # Log the transaction as an external transfer
                cursor.execute(
                    "INSERT INTO transactions (Account_no, date_time, transaction_type, receiver_acc_no, amount) VALUES (%s, now(), %s, %s, %s)",
                    (sender_acc_no, "External Transfer", receiver_acc_no, amount)
                )
                conn.commit()
                messagebox.showinfo("Success", "External transfer successful!")# Similar code for External Transfer...
                

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    # Tkinter setup
    root = Tk()
    root.title("Transfer Funds within Bank")
    root.geometry("700x440")
    root.config(bg="#53b5a1")

    # Sender Account
    Label(root, text="Sender Account No:", font=("Times New Roman", 20), bg="#53b5a1").place(x=100, y=70)
    sender_acc_entry = Entry(root, font=("Times New Roman", 11))
    sender_acc_entry.insert(0, sender_acc_no)  # Pre-fill with the sender's account number
    sender_acc_entry.config(state='readonly')  # Make it readonly
    sender_acc_entry.place(x=420, y=75) 
    # Receiver Account Dropdown
    Label(root, text="Select Receiver Account:", font=("Times New Roman", 20), bg="#53b5a1").place(x=100, y=120)
    receiver_combo = ttk.Combobox(root, state="readonly", values=get_payees(sender_acc_no) + ["Other"])
    receiver_combo.bind("<<ComboboxSelected>>", on_receiver_selection)
    receiver_combo.place(x=420, y=125)

    # Receiver account (for manual input when "Other" is selected)
    Label(root, text="Enter Receiver Account:", font=("Times New Roman", 20), bg="#53b5a1").place(x=100, y=170)
    receiver_acc_entry = Entry(root)
    receiver_acc_entry.place(x=420, y=175)

    # Transfer type dropdown
    Label(root, text="Transfer Type:", font=("Times New Roman", 20), bg="#53b5a1").place(x=100, y=220)
    transfer_type_combo = ttk.Combobox(root, state="readonly", values=["Internal", "External"])
    transfer_type_combo.place(x=420, y=225)

    # Amount to transfer
    Label(root, text="Amount:", font=("Times New Roman", 20), bg="#53b5a1").place(x=100, y=270)
    amount_entry = Entry(root)
    amount_entry.place(x=420, y=275)

    # Transfer button
    submit_btn = Button(root, text="Transfer", bg="white", width=15, height=1, bd=10, command=transfer_fundss)
    submit_btn.place(x=250, y=340)

    root.mainloop()

  


def statement():
    show=Tk()
    show.resizable(False,False)
    show.geometry("500x300")
    show.title("Mini statement")
    show.config(bg='#53b5a1')
        
    def showmini():
        if True:
            show.withdraw()
            acc=tb10.get()
            conn=pymysql.connect(host='localhost', user='root', password='', db='bank')
            b=conn.cursor()
            b.execute("select amount from users where acc_no='"+acc+"'")
            v= b.fetchone()
            if not v:
                messagebox.showerror("Error", "Account not found!")
                return
            else:
                b.execute("select * from transactions where Account_no='"+acc+"'")
                v= b.fetchall()
                show_win=Tk()
                show_win.resizable(False,False)
                show_win.geometry("800x700")
                show_win.title("Mini statement")
                show_win.config(bg='#53b5a1')
                vary=80
                headlb=Label(show,text="customer details", font=("Times New Roman",25),bg="light gray").grid(row=0, column=1, padx=200)
                #####--------label of the table----------#####
                lb1 = Label(show_win, text="Account", width=20, bg='white', bd=5).place(x=22, y=50)
                lb2 = Label(show_win, text="Date_time", width=20, bg='white', bd=5).place(x=172, y=50)
                lb3 = Label(show_win, text="Transaction type", width=20, bg='white', bd=5).place(x=322, y=50)
                lb4 = Label(show_win, text="Reciever's account", width=20, bg='white', bd=5).place(x=472, y=50)
                lb5 = Label(show_win, text="amount", width=19, bg='white', bd=5).place(x=622, y=50)

                for i in range(0,b.rowcount):
                    lb1 = Label(show_win, text=v[i][0], width=19, bg='white', bd=5).place(x=22, y=vary)
                    lb2 = Label(show_win, text=v[i][1], width=20, bg='white', bd=5).place(x=169, y=vary)
                    lb3 = Label(show_win, text=v[i][2], width=19, bg='white', bd=5).place(x=322, y=vary)
                    lb4 = Label(show_win, text=v[i][3], width=19, bg='white', bd=5).place(x=472, y=vary)
                    lb5 = Label(show_win, text=v[i][4], width=19, bg='white', bd=5).place(x=622, y=vary)
                    vary+=30
            
                conn.commit()
        else:
            conn.rollback()
            messagebox.showerror("error","exception occured")


   
    mi= StringVar()

    lb=Label(show, text="Enter account number", font=("Times New Roman",18), bg="#53b5a1")
    lb.place(x=100, y=80)


    tb10=Entry(show, textvariable=mi, width=30)
    tb10.place(x=100, y=130)

    bt=Button(show, text="show", font=("Times New Roman",13),bd=10, command=showmini)
    bt.place(x=100, y=180)

def logout():
    global mwin
    global login_win
    mwin.destroy()
    if 'login_win' in globals():
        login_win.deiconify()  # Show the login window again
    else:
        lwin.deiconify()

def profile():
    cpwin=Tk()
    cpwin.resizable(False,False)
    cpwin.geometry("580x500")
    cpwin.title("Welcome to transfer page")
    cpwin.config(bg='#53b5a1')

    def update_cont():
        ucwin=Tk()
        ucwin.resizable(True,True)
        ucwin.geometry("600x410")
        ucwin.title("CHANGE CONTACT")
        ucwin.config(bg='#53b5a1')

        def changecon():
            uid=tbg.get()
            uold=tbi.get()
            unew=tbj.get()
            if not validate_contact(unew):
                return

    
            try:
               conn=pymysql.connect(host="localhost",user="root",password='',db="bank")
               a=conn.cursor()
               a.execute("SELECT * FROM users WHERE acc_no ='"+uid+"' and contact='"+uold+"'")
               result=a.fetchone()
               if result:
                   a.execute("Update  users set contact='"+unew+"' where acc_no='"+uid+"'")
                   conn.commit()
                   messagebox.showinfo("message","contact updated successfully")
               else:
                   messagebox.showerror("Error", "Invalid Account Number or old contact")

            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Connection error: {e}")
        
            conn.close()
    
    
        us= StringVar()
        us2= StringVar()   
        us3= StringVar()   

        lb=Label(ucwin, text="Enter The Following Details:", font=("Times New roman",20),bg='#53b5a1')
        lb.place(x=70, y=40)

        lb=Label(ucwin, text="Enter Account number", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=100)


        lb=Label(ucwin, text="Enter current contact number", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=170)

        lb=Label(ucwin, text="Enter new contact number", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=240)

        bt=Button(ucwin, text="Update contact", bg="white",font=("Times New roman",13), width=13, height=1, bd=10, command=changecon)
        bt.place(x=200, y=310)

        tbg=Entry(ucwin, textvariable=us)
        tbg.place(x=380, y=100)

        tbi=Entry(ucwin, textvariable=us2)
        tbi.place(x=380, y=170)

        tbj=Entry(ucwin, textvariable=us3)
        tbj.place(x=380, y=240)

    def update_pass():
        upwin=Tk()
        upwin.resizable(True,True)
        upwin.geometry("700x500")
        upwin.title("CHANGE PASSWORD")
        upwin.config(bg='#53b5a1')

        def toggle_pin():
            if tbe.cget('show') == '*':
                tbe.config(show='')  # Show the actual PIN
                show_hide_btn2.config(text="Hide Password")
            else:
                tbe.config(show='*')  # Mask the PIN
                show_hide_btn2.config(text="Show Password")
        
        def changepass():
            uid=tbc.get()
            uold=tbd.get()
            unew=tbe.get()
            uconfirm=tbf.get()

            if len(unew) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long.")
                return
            
            if unew != uconfirm:
                messagebox.showerror("Error", "New PIN and Confirm Password do not match.")
                return

        
            try:
               conn=pymysql.connect(host="localhost",user="root",password='',db="bank")
               a=conn.cursor()
               a.execute("SELECT * FROM users WHERE acc_no ='"+uid+"'  AND password = '"+uold+"'")
               result=a.fetchone()
               if result:
                   a.execute("Update  users set password='"+uconfirm+"' where acc_no='"+uid+"'")
                   conn.commit()
                   messagebox.showinfo("message","password updated successfully")
               else:
                   messagebox.showerror("Error", "Invalid Account Number or Old Password.")

            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Connection error: {e}")
        
            conn.close()
    
    
        us= StringVar()
        us1= StringVar()   
        us2= StringVar()   
        us3= StringVar()   


        lb=Label(upwin, text="Enter Account number", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=100)

        lb1=Label(upwin, text="Enter current password", font=("Times New roman",16),bg='#53b5a1')
        lb1.place(x=100, y=170)

        lb=Label(upwin, text="Enter new password", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=240)

        lb=Label(upwin, text="confirm password", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=310)

        bt=Button(upwin, text="Change", bg="white", font=("Times New roman",12), width=10, height=1, bd=10,command=changepass)
        bt.place(x=200, y=400)

        show_hide_btn2 = Button(upwin, text="Hide Password", command=toggle_pin)
        show_hide_btn2.place(x=530, y=235)

        tbc=Entry(upwin, textvariable=us)
        tbc.place(x=350, y=100)

        tbd=Entry(upwin, textvariable=us1)
        tbd.place(x=350, y=170)

        tbe=Entry(upwin, textvariable=us2,)
        tbe.place(x=350, y=240)

        tbf=Entry(upwin, textvariable=us3, show="*")
        tbf.place(x=350, y=310)

    def update_email():
        uewin=Tk()
        uewin.resizable(True,True)
        uewin.geometry("650x330")
        uewin.title("CHANGE EMAIL")
        uewin.config(bg='#53b5a1')

        def changeemail():
            uid=tbx.get()
            unew=tby.get()
    
            try:
               conn=pymysql.connect(host="localhost",user="root",password='',db="bank")
               a=conn.cursor()
               a.execute("SELECT * FROM users WHERE acc_no ='"+uid+"'")
               result=a.fetchone()
               if result:
                   a.execute("Update  users set email='"+unew+"' where acc_no='"+uid+"'")
                   conn.commit()
                   messagebox.showinfo("message","email updated successfully")
               else:
                   messagebox.showerror("Error", "Invalid Account Number ")

            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Connection error: {e}")
        
            conn.close()
    
    
        us= StringVar()
        us2= StringVar()   
        us3= StringVar()   

        lb=Label(uewin, text="Updating email:", font=("Times New roman",20),bg='#53b5a1')
        lb.place(x=70, y=40)

        lb=Label(uewin, text="Enter Account number", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=100)

        lb=Label(uewin, text="Enter new email", font=("Times New roman",16),bg='#53b5a1')
        lb.place(x=100, y=170)

        bt=Button(uewin, text="Update email", bg="white",font=("Times New roman",13), width=13, height=1, bd=10, command=changeemail)
        bt.place(x=200, y=240)


        tbx=Entry(uewin, textvariable=us)
        tbx.place(x=360, y=100)

        tby=Entry(uewin, textvariable=us3, width="26")
        tby.place(x=360, y=170)


    lb=Label(cpwin, text="UPDATE YOUR ACCOUNT DETAILS", font=("Times New Roman",20), bg="#53b5a1")
    lb.place(x=60, y=50)


    bt1=Button(cpwin, text="Update contact", font=("Times New Roman",15), bg="white",width=20, bd=10, command=update_cont)
    bt1.place(x=160, y=150)

    bt2=Button(cpwin, text="Update password", font=("Times New Roman",15), bg="white",width=20, bd=10,command= update_pass)
    bt2.place(x=160, y=250)


    bt3=Button(cpwin, text="Update email", font=("Times New Roman",15), bg="white",width=20, bd=10, command=update_email)
    bt3.place(x=160, y=350)


def account_exists(account_no):
    conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE acc_no = %s", (account_no,))
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result > 0

# Function to check if a payee already exists
def payee_exists(account_no, payee_acc_no):
    conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM payees WHERE account_no = %s AND payee_account_no = %s", (account_no, payee_acc_no))
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result > 0

# Payees management window function (pass account_no directly from login/dashboard)
def manage_payees(account_no):
    if not account_exists(account_no):
        messagebox.showerror("Error", "Your account number is invalid!")
        return
    
    rootpay = Tk()
    rootpay.title("Manage Payees")
    rootpay.config(bg="#53b5a1")
    rootpay.geometry("610x490")

    Label(rootpay, text="MANAGE YOUR PAYEES", font=("Times New Roman", 18), bg="#53b5a1").place(x=190, y=40)

    # Payee Listbox (to display existing payees)
    Label(rootpay, text="Your Payees:", font=("Times New Roman", 15), bg="#53b5a1").place(x=50, y=100)
    payees_listbox = Listbox(rootpay, height=6, width=50)
    payees_listbox.place(x=180, y=100)

    # Fetch and display payees for the logged-in account
    def fetch_and_display_payees():
        payees_listbox.delete(0, END)  # Clear the existing listbox entries

        conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = conn.cursor()
        cursor.execute("SELECT payee_account_no, payee_name FROM payees WHERE account_no = %s ", (account_no,))
        payees = cursor.fetchall()
        cursor.close()
        conn.close()

        for payee in payees:
            payees_listbox.insert(END, f"{payee[0]} - {payee[1]}")  # Display payee_account_no and payee_name

    # Call fetch_and_display_payees when the window opens
    fetch_and_display_payees()

    # Payee Account No. and Name Input Fields
    Label(rootpay, text="Payee Account No:", font=("Times New Roman", 15), bg="#53b5a1").place(x=50, y=300)
    payee_acc_entry = Entry(rootpay)
    payee_acc_entry.place(x=250, y=300)

    Label(rootpay, text="Payee Name:", font=("Times New Roman", 15), bg="#53b5a1").place(x=50, y=350)
    payee_name_entry = Entry(rootpay)
    payee_name_entry.place(x=250, y=350)

    # Function to add a new payee
    def add_payee():
        payee_acc_no = payee_acc_entry.get()
        payee_name = payee_name_entry.get()

        if not payee_acc_no or not payee_name:
            messagebox.showerror("Error", "Both Payee Account No. and Name are required!")
            return

        # Check if the payee's account number exists
        if not account_exists(payee_acc_no):
            messagebox.showerror("Error", "The payee's account number does not exist!")
            return

        # Check if the payee already exists
        if payee_exists(account_no, payee_acc_no):
            messagebox.showerror("Error", "This payee is already added!")
            return

        # Insert the new payee into the database
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO payees (account_no, payee_account_no, payee_name) VALUES (%s, %s, %s)", 
                           (account_no, payee_acc_no, payee_name))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Payee added successfully!")
            fetch_and_display_payees()  # Refresh the listbox after adding payee

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    # Add Payee Button
    add_payee_button = Button(rootpay, text="Add Payee", font=("Times New Roman", 10), bd=10, bg="white", width=20, command=add_payee)
    add_payee_button.place(x=180, y=400)

    # Delete Payee Button
    def delete_payee():
        selected = payees_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No payee selected!")
            return

        payee_info = payees_listbox.get(selected[0])
        payee_acc_no = payee_info.split(' - ')[0]  # Extract the payee account number

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="bank")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM payees WHERE account_no = %s AND payee_account_no = %s", (account_no, payee_acc_no))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Payee deleted successfully!")
            fetch_and_display_payees()  # Refresh the listbox after deletion

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    delete_payee_button = Button(rootpay, text="Delete Selected Payee", font=("Times New Roman", 10), bd=10, bg="white", width=20, command=delete_payee)
    delete_payee_button.place(x=180, y=240)

    rootpay.mainloop()

    
   
us=StringVar()
us1=StringVar()

lb=Label(lwin, text="BANK MANAGEMENT", bg="white", relief="raised",bd=10,width=27,font=("Times New Roman",33))
lb.place(x=10, y=10)
lb=Label(lwin, text="---ACCOUNT LOGIN---", bg="#53b5a1", font=("Times New Roman",33),width=25)
lb.place(x=50, y=100)

lb1=Label(lwin, text="Enter email:", font=("Times New Roman",15), bg="#53b5a1")
lb1.place(x=130, y=200)

lb2=Label(lwin, text="Enter password:", bg="#53b5a1", font=("Times New Roman",15))
lb2.place(x=130, y=270)

bt=Button(lwin,text="Login", font=("Times New Roman",13), bd=10, bg="white",width=20, command=login)
bt.place(x=250, y=330)

bt=Button(lwin,text="Don't have an account? Register here", font=("Times New Roman",10), fg="blue", bg="white", command=registration)
bt.place(x=100, y=410)

show_hide_btn = Button(lwin, text="Hide password", command=toggle_pin)
show_hide_btn.place(x=530, y=270)

tb11= Entry(lwin, textvariable=us,width=25)
tb11.place(x=370, y=200)

tb22= Entry(lwin, textvariable=us1,width=25)
tb22.place(x=370, y=270)
