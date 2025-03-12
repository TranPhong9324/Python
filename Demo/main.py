import tkinter as tk
from tkinter import ttk, colorchooser
from PIL import Image, ImageTk

class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x600")

        self.current_color = "black"
        self.brush_size = 3
        self.last_x = None
        self.last_y = None
        self.draw_mode = "pencil"
        self.shape_id = None

        # Tạo khung chính
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Tạo bảng điều khiển
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill="x", padx=5, pady=5)

        # Tạo bảng vẽ
        self.canvas = tk.Canvas(self.main_frame, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.load_images()
        self.setup_controls()

        # Gắn sự kiện chuột
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def load_images(self):
        try:
            self.img_pencil = ImageTk.PhotoImage(Image.open("ic_pencil.png").resize((30, 30)))
            self.img_color = ImageTk.PhotoImage(Image.open("ic_color.png").resize((30, 30)))  
            self.img_rubber = ImageTk.PhotoImage(Image.open("ic_rubber.png").resize((30, 30)))
            self.img_rectangle = ImageTk.PhotoImage(Image.open("ic_rectangle.png").resize((30, 30)))
            self.img_circle = ImageTk.PhotoImage(Image.open("ic_circle.png").resize((30, 30)))
            self.img_line = ImageTk.PhotoImage(Image.open("ic_line.png").resize((30, 30)))
        except FileNotFoundError:
            print("Không tìm thấy file ảnh. Vui lòng đảm bảo các file ảnh tồn tại trong thư mục.")

    def setup_controls(self):
        ttk.Button(self.control_frame, image=self.img_pencil, command=self.use_pencil).pack(side="left", padx=5)
        ttk.Button(self.control_frame, image=self.img_color, command=self.choose_color).pack(side="left", padx=5)
        ttk.Button(self.control_frame, image=self.img_rubber, command=self.use_rubber).pack(side="left", padx=5)
        ttk.Button(self.control_frame, image=self.img_rectangle, command=self.use_rectangle).pack(side="left", padx=5)
        ttk.Button(self.control_frame, image=self.img_circle, command=self.use_circle).pack(side="left", padx=5)
        ttk.Button(self.control_frame, image=self.img_line, command=self.use_line).pack(side="left", padx=5)

        # Thanh trượt kích thước bút
        ttk.Label(self.control_frame, text="Brush Size:").pack(side="left", padx=5)
        self.size_slider = ttk.Scale(self.control_frame, from_=1, to=20,
                                   orient="horizontal", command=self.update_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side="left", padx=5)

        ttk.Button(self.control_frame, text="CLEAR", command=self.clear_canvas).pack(side="right", padx=5)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Color")[1]
        if color:
            self.current_color = color

    def update_brush_size(self, value):
        self.brush_size = int(float(value))

    def use_pencil(self):
        self.draw_mode = "pencil"

    def use_rubber(self):
        self.current_color = "white"
        self.draw_mode = "pencil"

    def use_rectangle(self):
        self.draw_mode = "rectangle"

    def use_circle(self):
        self.draw_mode = "circle"

    def use_line(self):
        self.draw_mode = "line"

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
        if self.draw_mode in ("rectangle", "circle", "line"):
            self.shape_id = None

    def draw(self, event):
        if self.draw_mode == "pencil":
            if self.last_x and self.last_y:
                self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                      width=self.brush_size, fill=self.current_color,
                                      capstyle="round", smooth=True)
            self.last_x = event.x
            self.last_y = event.y

        elif self.draw_mode in ("rectangle", "circle", "line") and self.last_x and self.last_y:
            if self.shape_id:
                self.canvas.delete(self.shape_id)

            if self.draw_mode == "rectangle":
                self.shape_id = self.canvas.create_rectangle(self.last_x, self.last_y, event.x, event.y,
                                                           outline=self.current_color, width=self.brush_size)
            elif self.draw_mode == "circle":
                self.shape_id = self.canvas.create_oval(self.last_x, self.last_y, event.x, event.y,
                                                      outline=self.current_color, width=self.brush_size)
            elif self.draw_mode == "line":
                self.shape_id = self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                                      fill=self.current_color, width=self.brush_size)

    def end_draw(self, event):
        self.last_x = None
        self.last_y = None
        self.shape_id = None

    def clear_canvas(self):
        self.canvas.delete("all")

def main():
    root = tk.Tk()
    app = Paint(root)
    root.mainloop()

if __name__ == "__main__":
    main()