from predition import Predict
import tkinter as tk
from PIL import Image, ImageTk  

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Decision Tree Visualization")
        
        self.image = Image.open("house_price_pic.jpg")
        self.image = self.image.resize((400, 300))
        self.image = ImageTk.PhotoImage(self.image)


        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(padx=10, pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        self.view_button = tk.Button(root, text="View Decision Tree", command=self.show_decision_tree)
        self.view_button.pack(pady=10)
        self.view_button = tk.Button(root, text="View Linear Regression", command=self.show_linear_regression)
        self.view_button.pack(pady=10)

    def show_decision_tree(self):
        predict = Predict('model')
        dataset = predict.read_data()
        predict.predict_decision_tree(dataset)

    def show_linear_regression(self):
        predict = Predict('model')
        dataset = predict.read_data()
        predict.predict_linear_regression(dataset)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()