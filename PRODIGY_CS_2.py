import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def encrypt_image(image, key):
    encrypted_image = image.copy()
    pixels = encrypted_image.load()

    for i in range(encrypted_image.size[0]):
        for j in range(encrypted_image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    
    return encrypted_image

def decrypt_image(image, key):
    return encrypt_image(image, key)

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")
        self.root.configure(bg='black')
        
        self.key = tk.IntVar()
        self.image_path = ""
        self.encrypted_image = None
        self.decrypted_image = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.pack(padx=10, pady=10)
        
        button_style = {
            'bg': 'black', 'fg': 'green', 'font': ('Courier', 12),
            'activebackground': 'green', 'activeforeground': 'black'
        }
        
        label_style = {
            'bg': 'black', 'fg': 'green', 'font': ('Courier', 12)
        }
        
        self.load_button = tk.Button(self.frame, text="Load Image", command=self.load_image, **button_style)
        self.load_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.encrypt_button = tk.Button(self.frame, text="Encrypt Image", command=self.encrypt_image, **button_style)
        self.encrypt_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.decrypt_button = tk.Button(self.frame, text="Decrypt Image", command=self.decrypt_image, **button_style)
        self.decrypt_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.save_encrypted_button = tk.Button(self.frame, text="Save Encrypted Image", command=self.save_encrypted_image, **button_style)
        self.save_encrypted_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.save_decrypted_button = tk.Button(self.frame, text="Save Decrypted Image", command=self.save_decrypted_image, **button_style)
        self.save_decrypted_button.grid(row=4, column=0, padx=5, pady=5)
        
        self.key_label = tk.Label(self.frame, text="Encryption Key (0-255):", **label_style)
        self.key_label.grid(row=5, column=0, padx=5, pady=5)
        
        self.key_entry = tk.Entry(self.frame, textvariable=self.key, bg='black', fg='green', font=('Courier', 12), insertbackground='green')
        self.key_entry.grid(row=6, column=0, padx=5, pady=5)
        
        self.image_label = tk.Label(self.frame, bg='black')
        self.image_label.grid(row=7, column=0, padx=5, pady=5)
        
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            self.display_image(self.image_path)
    
    def display_image(self, path):
        image = Image.open(path)
        image.thumbnail((300, 300))
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo
    
    def encrypt_image(self):
        if self.image_path:
            key = self.key.get()
            image = Image.open(self.image_path)
            self.encrypted_image = encrypt_image(image, key)
            self.display_image_from_image(self.encrypted_image)
    
    def decrypt_image(self):
        if self.image_path:
            key = self.key.get()
            image = Image.open(self.image_path)
            self.decrypted_image = decrypt_image(image, key)
            self.display_image_from_image(self.decrypted_image)
    
    def display_image_from_image(self, image):
        image.thumbnail((300, 300))
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo
    
    def save_encrypted_image(self):
        if self.encrypted_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.encrypted_image.save(save_path)
    
    def save_decrypted_image(self):
        if self.decrypted_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.decrypted_image.save(save_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
