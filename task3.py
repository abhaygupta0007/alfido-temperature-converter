import tkinter as tk
from tkinter import ttk, messagebox

# Conversion function
def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == 'Celsius':
            result = temp if to_unit == 'Celsius' else (temp * 9/5 + 32) if to_unit == 'Fahrenheit' else (temp + 273.15)
        elif from_unit == 'Fahrenheit':
            result = temp if to_unit == 'Fahrenheit' else (temp - 32) * 5/9 if to_unit == 'Celsius' else ((temp - 32) * 5/9 + 273.15)
        elif from_unit == 'Kelvin':
            result = temp if to_unit == 'Kelvin' else (temp - 273.15) if to_unit == 'Celsius' else ((temp - 273.15) * 9/5 + 32)

        output_var.set(f"{result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter - Alfido Tech")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Heading
tk.Label(root, text="🌡 Temperature Converter", font=("Arial", 16, 'bold'), bg="#f0f0f0").pack(pady=10)

# Entry for temperature
entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack(pady=10)

# Dropdowns for units
from_var = tk.StringVar(value="Celsius")
to_var = tk.StringVar(value="Fahrenheit")

unit_options = ['Celsius', 'Fahrenheit', 'Kelvin']

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack()

tk.Label(frame, text="From:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
from_menu = ttk.Combobox(frame, textvariable=from_var, values=unit_options, state='readonly')
from_menu.grid(row=0, column=1)

tk.Label(frame, text="To:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10)
to_menu = ttk.Combobox(frame, textvariable=to_var, values=unit_options, state='readonly')
to_menu.grid(row=1, column=1)

# Convert button
tk.Button(root, text="Convert", font=("Arial", 12), bg="#4caf50", fg="white", command=convert_temperature).pack(pady=15)

# Output label
output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, font=("Arial", 14, 'bold'), bg="#f0f0f0", fg="blue").pack()

# Start GUI loop
root.mainloop()
