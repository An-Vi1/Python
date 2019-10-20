import tkinter as tk

root = tk.Tk()
root.title('Food price')
root.geometry('300x200')
root.resizable( width = False, height = False)
root.configure( bg = 'gray')                   # color of background

label = tk.Label(root, text = 'Choose An Item')
label.place(x = 100, y = 5)

# Radio buttons
r_btn = tk.Radiobutton(root, text = 'Banana')
r_btn.place(x = 5, y = 30)

r_btn_2 = tk.Radiobutton(root, text = 'Apple')
r_btn_2.place(x = 5, y = 60)

r_btn_3 = tk.Radiobutton(root, text = 'Orange')
r_btn_3.place(x = 5, y = 90)


entry = tk.Entry(root, width = 25)
entry.place(x = 80, y = 130)

label_res = tk.Label(root, text = 'Price')
label_res.place(x = 5, y = 130)

entry_2 = tk.Entry(root, width = 25)
entry_2.place(x = 80, y = 160)

btn = tk.Button(root, text = 'Cal')
btn.place(x = 5, y = 160)


root.mainloop()