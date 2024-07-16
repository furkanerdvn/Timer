
import tkinter as tk
from tkinter import ttk
import threading
import time

class KronometreUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kronometre")

        self.is_running = False
        self.start_time = 0
        self.scale_factor = 1.0

        self.label_var = tk.StringVar()
        self.label_var.set("Geçen Süre: 0 saniye")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))
        style.configure("TLabel", font=("Helvetica", 18), padding=10)

        self.label = ttk.Label(root, textvariable=self.label_var, style="TLabel", anchor="center")
        self.label.pack(expand=True)

        self.start_button = ttk.Button(root, text="Başlat", command=self.toggle)
        self.start_button.pack(expand=True)

        self.thread = None
        self.update_interval = 100  # Güncelleme aralığı (ms)

    def toggle(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.thread = threading.Thread(target=self.update_time)
            self.thread.start()
            self.start_button.config(text="Durdur")
            self.update_label()
        else:
            self.is_running = False
            self.start_button.config(text="Başlat")

    def update_time(self):
        while self.is_running:
            elapsed_time = self.get_elapsed_scaled_time()
            self.label_var.set(f"Geçen Süre: {elapsed_time} saniye")
            time.sleep(0.1)

    def get_elapsed_scaled_time(self):
        current_time = time.time()
        elapsed = current_time - self.start_time
        return int(elapsed * self.scale_factor)

    def update_label(self):
        if self.is_running:
            self.root.after(self.update_interval, self.update_label)

def main():
    root = tk.Tk()
    app = KronometreUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()