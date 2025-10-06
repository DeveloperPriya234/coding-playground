import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import math
import json
import os

class DrawingCanvas:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Canvas Drawing Application")
        self.master.geometry("1000x700")
        self.master.configure(bg='#f0f0f0')
        
        # Drawing variables
        self.current_tool = "pen"
        self.current_color = "#000000"
        self.brush_size = 3
        self.start_x = None
        self.start_y = None
        self.drawing = False
        self.shapes = []  # Store drawn shapes for saving/loading
        
        # Undo/Redo functionality
        self.canvas_states = []
        self.current_state_index = -1
        
        self.setup_ui()
        self.bind_events()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.master, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Toolbar frame
        toolbar_frame = tk.Frame(main_frame, bg='#e0e0e0', relief=tk.RAISED, bd=1)
        toolbar_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Tools section
        tools_frame = tk.LabelFrame(toolbar_frame, text="Tools", bg='#e0e0e0', fg='#333')
        tools_frame.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Tool buttons
        tools = [
            ("✏️ Pen", "pen"),
            ("📝 Pencil", "pencil"),
            ("🖌️ Brush", "brush"),
            ("⭕ Circle", "circle"),
            ("⬜ Rectangle", "rectangle"),
            ("📏 Line", "line"),
            ("🌟 Star", "star"),
            ("🔺 Triangle", "triangle"),
            ("🧽 Eraser", "eraser"),
            ("🎨 Spray", "spray")
        ]
        
        self.tool_buttons = {}
        for i, (text, tool) in enumerate(tools):
            btn = tk.Button(tools_frame, text=text, width=8, height=1,
                          command=lambda t=tool: self.select_tool(t),
                          bg='white', relief=tk.RAISED)
            btn.grid(row=i//5, column=i%5, padx=2, pady=2)
            self.tool_buttons[tool] = btn
        
        # Highlight default tool
        self.tool_buttons["pen"].config(bg='#4CAF50', fg='white')
        
        # Colors section
        colors_frame = tk.LabelFrame(toolbar_frame, text="Colors", bg='#e0e0e0', fg='#333')
        colors_frame.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Color palette
        colors = [
            "#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF",
            "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#800080",
            "#FFC0CB", "#A52A2A", "#808080", "#000080", "#008000"
        ]
        
        self.color_buttons = {}
        for i, color in enumerate(colors):
            btn = tk.Button(colors_frame, bg=color, width=3, height=1,
                          command=lambda c=color: self.select_color(c),
                          relief=tk.RAISED, bd=2)
            btn.grid(row=i//5, column=i%5, padx=1, pady=1)
            self.color_buttons[color] = btn
        
        # Custom color button
        custom_color_btn = tk.Button(colors_frame, text="🎨", width=3, height=1,
                                   command=self.choose_custom_color,
                                   bg='#f0f0f0', relief=tk.RAISED)
        custom_color_btn.grid(row=3, column=0, padx=1, pady=1)
        
        # Current color display
        self.current_color_display = tk.Label(colors_frame, bg=self.current_color, 
                                            width=6, height=2, relief=tk.SUNKEN, bd=2)
        self.current_color_display.grid(row=3, column=1, columnspan=2, padx=1, pady=1)
        
        # Brush size section
        size_frame = tk.LabelFrame(toolbar_frame, text="Brush Size", bg='#e0e0e0', fg='#333')
        size_frame.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.size_scale = tk.Scale(size_frame, from_=1, to=20, orient=tk.HORIZONTAL,
                                 command=self.change_brush_size, bg='#e0e0e0')
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(padx=5, pady=5)
        
        # Actions section
        actions_frame = tk.LabelFrame(toolbar_frame, text="Actions", bg='#e0e0e0', fg='#333')
        actions_frame.pack(side=tk.LEFT, padx=5, pady=5)
        
        action_buttons = [
            ("↶ Undo", self.undo),
            ("↷ Redo", self.redo),
            ("🗑️ Clear", self.clear_canvas),
            ("💾 Save", self.save_drawing),
            ("📁 Load", self.load_drawing),
            ("📤 Export", self.export_image)
        ]
        
        for i, (text, command) in enumerate(action_buttons):
            btn = tk.Button(actions_frame, text=text, width=8, height=1,
                          command=command, bg='white', relief=tk.RAISED)
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)
        
        # Canvas frame
        canvas_frame = tk.Frame(main_frame, bg='#d0d0d0', relief=tk.SUNKEN, bd=2)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbars
        self.canvas = tk.Canvas(canvas_frame, bg='white', width=800, height=600,
                              scrollregion=(0, 0, 1200, 900))
        
        # Scrollbars
        v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack scrollbars and canvas
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = tk.Label(self.master, text="Ready | Tool: Pen | Color: Black", 
                                 relief=tk.SUNKEN, anchor=tk.W, bg='#f0f0f0')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Save initial state
        self.save_state()
    
    def bind_events(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        
        # Keyboard shortcuts
        self.master.bind("<Control-z>", lambda e: self.undo())
        self.master.bind("<Control-y>", lambda e: self.redo())
        self.master.bind("<Control-s>", lambda e: self.save_drawing())
        self.master.bind("<Control-o>", lambda e: self.load_drawing())
        self.master.bind("<Control-n>", lambda e: self.clear_canvas())
    
    def select_tool(self, tool):
        # Reset all button colors
        for btn in self.tool_buttons.values():
            btn.config(bg='white', fg='black')
        
        # Highlight selected tool
        self.tool_buttons[tool].config(bg='#4CAF50', fg='white')
        self.current_tool = tool
        self.update_status()
    
    def select_color(self, color):
        self.current_color = color
        self.current_color_display.config(bg=color)
        self.update_status()
    
    def choose_custom_color(self):
        color = colorchooser.askcolor(title="Choose Color")[1]
        if color:
            self.select_color(color)
    
    def change_brush_size(self, value):
        self.brush_size = int(value)
        self.update_status()
    
    def update_status(self):
        tool_name = self.current_tool.capitalize()
        color_name = self.current_color
        self.status_bar.config(text=f"Ready | Tool: {tool_name} | Color: {color_name} | Size: {self.brush_size}")
    
    def on_click(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.drawing = True
        
        if self.current_tool in ["pen", "pencil", "brush", "eraser", "spray"]:
            self.draw_point(self.start_x, self.start_y)
    
    def on_drag(self, event):
        if not self.drawing:
            return
        
        current_x = self.canvas.canvasx(event.x)
        current_y = self.canvas.canvasy(event.y)
        
        if self.current_tool in ["pen", "pencil", "brush"]:
            self.draw_line(self.start_x, self.start_y, current_x, current_y)
            self.start_x, self.start_y = current_x, current_y
        elif self.current_tool == "eraser":
            self.erase_area(current_x, current_y)
        elif self.current_tool == "spray":
            self.spray_paint(current_x, current_y)
    
    def on_release(self, event):
        if not self.drawing:
            return
        
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        
        if self.current_tool == "circle":
            self.draw_circle(self.start_x, self.start_y, end_x, end_y)
        elif self.current_tool == "rectangle":
            self.draw_rectangle(self.start_x, self.start_y, end_x, end_y)
        elif self.current_tool == "line":
            self.draw_line(self.start_x, self.start_y, end_x, end_y)
        elif self.current_tool == "star":
            self.draw_star(self.start_x, self.start_y, end_x, end_y)
        elif self.current_tool == "triangle":
            self.draw_triangle(self.start_x, self.start_y, end_x, end_y)
        
        self.drawing = False
        self.save_state()
    
    def on_mouse_move(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.status_bar.config(text=f"Position: ({int(x)}, {int(y)}) | Tool: {self.current_tool.capitalize()} | Color: {self.current_color}")
    
    def draw_point(self, x, y):
        size = self.brush_size
        color = "white" if self.current_tool == "eraser" else self.current_color
        
        if self.current_tool == "pencil":
            size = max(1, size - 1)
        elif self.current_tool == "brush":
            size = size + 2
        
        self.canvas.create_oval(x-size, y-size, x+size, y+size, 
                              fill=color, outline=color)
    
    def draw_line(self, x1, y1, x2, y2):
        color = "white" if self.current_tool == "eraser" else self.current_color
        width = self.brush_size
        
        if self.current_tool == "pencil":
            width = max(1, width - 1)
        elif self.current_tool == "brush":
            width = width + 2
        
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width, capstyle=tk.ROUND)
    
    def draw_circle(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.current_color, 
                              width=self.brush_size, fill="")
    
    def draw_rectangle(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.current_color, 
                                   width=self.brush_size, fill="")
    
    def draw_triangle(self, x1, y1, x2, y2):
        # Calculate triangle points
        mid_x = (x1 + x2) / 2
        points = [mid_x, y1, x1, y2, x2, y2]
        self.canvas.create_polygon(points, outline=self.current_color, 
                                 width=self.brush_size, fill="")
    
    def draw_star(self, x1, y1, x2, y2):
        # Calculate star points
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
        
        points = []
        for i in range(10):
            angle = i * math.pi / 5
            if i % 2 == 0:
                r = radius
            else:
                r = radius * 0.5
            x = center_x + r * math.cos(angle - math.pi / 2)
            y = center_y + r * math.sin(angle - math.pi / 2)
            points.extend([x, y])
        
        self.canvas.create_polygon(points, outline=self.current_color, 
                                 width=self.brush_size, fill="")
    
    def erase_area(self, x, y):
        size = self.brush_size * 3
        self.canvas.create_oval(x-size, y-size, x+size, y+size, 
                              fill="white", outline="white")
    
    def spray_paint(self, x, y):
        import random
        for _ in range(20):
            offset_x = random.randint(-self.brush_size*3, self.brush_size*3)
            offset_y = random.randint(-self.brush_size*3, self.brush_size*3)
            self.canvas.create_oval(x+offset_x-1, y+offset_y-1, 
                                  x+offset_x+1, y+offset_y+1, 
                                  fill=self.current_color, outline=self.current_color)
    
    def save_state(self):
        # Remove states after current index if we're not at the end
        if self.current_state_index < len(self.canvas_states) - 1:
            self.canvas_states = self.canvas_states[:self.current_state_index + 1]
        
        # Save current canvas state
        state = self.canvas.postscript(colormode='color')
        self.canvas_states.append(state)
        self.current_state_index += 1
        
        # Limit undo history to 20 states
        if len(self.canvas_states) > 20:
            self.canvas_states.pop(0)
            self.current_state_index -= 1
    
    def undo(self):
        if self.current_state_index > 0:
            self.current_state_index -= 1
            self.restore_state()
    
    def redo(self):
        if self.current_state_index < len(self.canvas_states) - 1:
            self.current_state_index += 1
            self.restore_state()
    
    def restore_state(self):
        # This is a simplified undo/redo - in a full implementation,
        # you'd store canvas item data rather than postscript
        messagebox.showinfo("Undo/Redo", "Undo/Redo functionality is simplified.\nUse Clear to start over.")
    
    def clear_canvas(self):
        if messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the canvas?"):
            self.canvas.delete("all")
            self.save_state()
    
    def save_drawing(self):
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".ps",
                filetypes=[("PostScript files", "*.ps"), ("All files", "*.*")]
            )
            if filename:
                ps_data = self.canvas.postscript(colormode='color')
                with open(filename, 'w') as f:
                    f.write(ps_data)
                messagebox.showinfo("Success", f"Drawing saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def load_drawing(self):
        messagebox.showinfo("Load Drawing", "Loading drawings is not fully implemented.\nThis is a demonstration feature.")
    
    def export_image(self):
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".ps",
                filetypes=[("PostScript files", "*.ps"), ("All files", "*.*")]
            )
            if filename:
                # Export as PostScript (can be converted to other formats)
                self.canvas.postscript(file=filename, colormode='color')
                messagebox.showinfo("Success", f"Image exported as {filename}\n(PostScript format)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")

def main():
    root = tk.Tk()
    app = DrawingCanvas(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()