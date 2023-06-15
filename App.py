import tkinter as tk
from Servers import Servers

OpenServer = Servers()
Cost = OpenServer.getStock("RBLX")
print(f"Cost of RBLX: ${round(Cost,2)}")

root = tk.Tk()
root.geometry("1200x600")
root.title("Trading bot")

label = tk.Label(root, text = "New Text")
label.pack()
root.mainloop()