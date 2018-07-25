import Tkinter as tk

window = tk.Tk()
window.title('User Simulator')
window.geometry('640x480')

text = tk.Text(window)
text.pack()
text.insert(1.0, "ABCD")

"""
labelframe = tk.LabelFrame(window, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = tk.Label(labelframe, text="Inside the LabelFrame")
left.pack()
"""

window.mainloop()
