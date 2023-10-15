from predition import Predict
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pandas as pd

class GUI:
    def __init__(self, root):
        self.root = root
        self.login_window = None  # Initialize the login window
        self.root.title("House Price Prediction")

        self.image = Image.open("house_price_pic.jpg")
        self.image = self.image.resize((400, 300))
        self.image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Add input fields for sqft_living, sqft_above, and sqft_basement 
        self.sqft_living_label = tk.Label(root, text="Sqft Living:")
        self.sqft_living_label.grid(row=1, column=0, sticky='e')
        self.sqft_living_entry = ttk.Entry(root)
        self.sqft_living_entry.grid(row=1, column=1)
        self.sqft_living_entry['style'] = 'Rounded.TEntry'

        self.sqft_above_label = tk.Label(root, text="Sqft Above:")
        self.sqft_above_label.grid(row=2, column=0, sticky='e')
        self.sqft_above_entry = ttk.Entry(root)
        self.sqft_above_entry.grid(row=2, column=1)
        self.sqft_above_entry['style'] = 'Rounded.TEntry'

        self.sqft_basement_label = tk.Label(root, text="Sqft Basement:")
        self.sqft_basement_label.grid(row=3, column=0, sticky='e')
        self.sqft_basement_entry = ttk.Entry(root)
        self.sqft_basement_entry.grid(row=3, column=1)
        self.sqft_basement_entry['style'] = 'Rounded.TEntry'

        # Defining buttons Predict Price, View Decision Tree and View Linear Decision Regression 
        self.predict_button = tk.Button(root, text="Predict Price", command=self.predict_price)
        self.predict_button.grid(row=4, column=1, pady=(10, 0))

        self.view_button = tk.Button(root, text="View Decision Tree", command=self.show_decision_tree)
        self.view_button.grid(row=5, column=0, padx=10, pady=10)
        self.view_button = tk.Button(root, text="View Linear Regression", command=self.show_linear_regression)
        self.view_button.grid(row=6, column=0, padx=10, pady=10)

        # Style for rounded corners
        style = ttk.Style()
        style.configure('Rounded.TEntry', borderwidth=1, relief='solid', padding=5, bordercolor='black')

    def show_decision_tree(self):
        predict = Predict('model')
        dataset = predict.read_data()
        predict.predict_decision_tree(dataset)

    def show_linear_regression(self):
        predict = Predict('model')
        dataset = predict.read_data()
        predict.predict_linear_regression(dataset)

    def predict_price(self):
        # Getting and storing data from fields
        sqft_living = float(self.sqft_living_entry.get())
        sqft_above = float(self.sqft_above_entry.get())
        sqft_basement = float(self.sqft_basement_entry.get())

        # Create an instance of the Predict class
        predict = Predict('model')

        # Prepare user data as a dictionary
        user_data = {
            'sqft_living': sqft_living,
            'sqft_above': sqft_above,
            'sqft_basement': sqft_basement
        }

        # Predict the price
        predicted_price = predict.my_predict_price(user_data)
        
        # Display the predicted price in a message box
        messagebox.showinfo("Predicted Price", f"Predicted Price: ${predicted_price[0]:.2f}")

    def create_login_page(self):
        # Create a new window for the login page
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login")

        # Add labels and entry fields for username and password
        username_label = tk.Label(self.login_window, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        username_entry = ttk.Entry(self.login_window)
        username_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(self.login_window, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        password_entry = ttk.Entry(self.login_window, show="*")  # Show asterisks for password
        password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Add a login button
        login_button = tk.Button(self.login_window, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.grid(row=2, columnspan=2, pady=10)

    def login(self, username, password):
        # Implement your login logic here
        if username == "admin" and password == "admin":
            # Close the login window if login is successful
            self.login_window.destroy()
            # Enable or show your main GUI here
            self.root.deiconify()
        else:
            # Display an error message or handle invalid login
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.withdraw()  # Start with the main window hidden
    app.create_login_page()
    root.mainloop()
