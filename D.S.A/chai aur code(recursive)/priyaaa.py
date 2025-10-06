import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import math
import time
import threading

class BirthdayVideo:
    def __init__(self, master):
        self.master = master
        self.master.title("🎉 Birthday Video Creator 🎂")
        self.master.geometry("900x700")
        self.master.configure(bg='#2C3E50')
        self.master.resizable(False, False)
        
        # Animation variables
        self.is_playing = False
        self.animation_thread = None
        self.frame_count = 0
        self.balloons = []
        self.confetti = []
        self.stars = []
        self.cake_candles = []
        
        # Birthday person's name
        self.birthday_name = "Friend"
        
        # Colors
        self.colors = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', 
            '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F',
            '#BB8FCE', '#85C1E9', '#F8C471', '#82E0AA'
        ]
        
        self.setup_ui()
        self.create_initial_elements()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.master, text="🎉 Birthday Video Creator 🎂", 
                              font=('Arial', 20, 'bold'), 
                              bg='#2C3E50', fg='#ECF0F1')
        title_label.pack(pady=10)
        
        # Control frame
        control_frame = tk.Frame(self.master, bg='#2C3E50')
        control_frame.pack(pady=10)
        
        # Name entry
        name_frame = tk.Frame(control_frame, bg='#2C3E50')
        name_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(name_frame, text="Birthday Person:", 
                font=('Arial', 10), bg='#2C3E50', fg='#ECF0F1').pack()
        
        self.name_entry = tk.Entry(name_frame, font=('Arial', 12), width=15)
        self.name_entry.pack()
        self.name_entry.insert(0, "Friend")
        
        # Control buttons
        button_frame = tk.Frame(control_frame, bg='#2C3E50')
        button_frame.pack(side=tk.LEFT, padx=20)
        
        self.play_btn = tk.Button(button_frame, text="🎬 Play Video", 
                                 command=self.start_video,
                                 font=('Arial', 12, 'bold'),
                                 bg='#27AE60', fg='white',
                                 width=12, height=2)
        self.play_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(button_frame, text="⏹️ Stop", 
                                 command=self.stop_video,
                                 font=('Arial', 12, 'bold'),
                                 bg='#E74C3C', fg='white',
                                 width=12, height=2)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Canvas for animation
        self.canvas = tk.Canvas(self.master, width=850, height=550, 
                               bg='#87CEEB', highlightthickness=2,
                               highlightbackground='#34495E')
        self.canvas.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(self.master, text="Ready to create birthday magic! ✨", 
                                   font=('Arial', 10), bg='#2C3E50', fg='#ECF0F1')
        self.status_label.pack()
        
    def create_initial_elements(self):
        """Create static birthday elements"""
        # Ground
        self.canvas.create_rectangle(0, 450, 850, 550, fill='#2ECC71', outline='')
        
        # Sun
        self.sun = self.canvas.create_oval(700, 50, 750, 100, fill='#F1C40F', outline='#F39C12', width=3)
        
        # Sun rays
        for i in range(8):
            angle = i * 45 * math.pi / 180
            x1 = 725 + 40 * math.cos(angle)
            y1 = 75 + 40 * math.sin(angle)
            x2 = 725 + 50 * math.cos(angle)
            y2 = 75 + 50 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill='#F1C40F', width=3)
        
        # Clouds
        self.create_cloud(150, 80)
        self.create_cloud(350, 120)
        self.create_cloud(550, 90)
        
        # Birthday cake
        self.create_birthday_cake()
        
        # Initial balloons
        self.create_balloons()
        
        # Welcome message
        self.canvas.create_text(425, 200, text="🎊 Get Ready for Birthday Fun! 🎊", 
                               font=('Arial', 16, 'bold'), fill='#2C3E50')
        
    def create_cloud(self, x, y):
        """Create a fluffy cloud"""
        cloud_color = '#FFFFFF'
        # Main cloud body
        self.canvas.create_oval(x, y, x+60, y+30, fill=cloud_color, outline='')
        self.canvas.create_oval(x+20, y-10, x+70, y+20, fill=cloud_color, outline='')
        self.canvas.create_oval(x+40, y, x+90, y+30, fill=cloud_color, outline='')
        self.canvas.create_oval(x+10, y+10, x+50, y+35, fill=cloud_color, outline='')
        
    def create_birthday_cake(self):
        """Create an animated birthday cake"""
        cake_x, cake_y = 350, 350
        
        # Cake base
        self.canvas.create_rectangle(cake_x, cake_y, cake_x+150, cake_y+80, 
                                   fill='#D2691E', outline='#8B4513', width=2)
        
        # Cake layers
        self.canvas.create_rectangle(cake_x+10, cake_y+10, cake_x+140, cake_y+35, 
                                   fill='#FFB6C1', outline='#FF69B4', width=1)
        self.canvas.create_rectangle(cake_x+10, cake_y+45, cake_x+140, cake_y+70, 
                                   fill='#98FB98', outline='#32CD32', width=1)
        
        # Cake decorations
        for i in range(7):
            x = cake_x + 20 + i * 18
            self.canvas.create_oval(x, cake_y+20, x+8, cake_y+28, fill='#FF1493', outline='')
            self.canvas.create_oval(x, cake_y+55, x+8, cake_y+63, fill='#1E90FF', outline='')
        
        # Candles
        self.cake_candles = []
        candle_positions = [375, 395, 415, 435, 455, 475]
        for x in candle_positions:
            # Candle
            candle = self.canvas.create_rectangle(x, cake_y-15, x+6, cake_y+5, 
                                                fill='#FFFF00', outline='#FFD700')
            # Flame (will be animated)
            flame = self.canvas.create_oval(x+1, cake_y-25, x+5, cake_y-15, 
                                          fill='#FF4500', outline='#FF6347')
            self.cake_candles.append((candle, flame))
    
    def create_balloons(self):
        """Create floating balloons"""
        self.balloons = []
        balloon_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
        
        for i in range(5):
            x = 100 + i * 150
            y = 300 + random.randint(-50, 50)
            color = balloon_colors[i]
            
            # Balloon
            balloon = self.canvas.create_oval(x, y, x+40, y+60, fill=color, outline='#2C3E50', width=2)
            # String
            string = self.canvas.create_line(x+20, y+60, x+20, y+120, fill='#2C3E50', width=2)
            # Highlight
            highlight = self.canvas.create_oval(x+10, y+10, x+20, y+20, fill='white', outline='')
            
            self.balloons.append({
                'balloon': balloon,
                'string': string,
                'highlight': highlight,
                'x': x,
                'y': y,
                'float_offset': 0,
                'color': color
            })
    
    def start_video(self):
        """Start the birthday video animation"""
        if self.is_playing:
            return
            
        self.birthday_name = self.name_entry.get().strip()
        if not self.birthday_name:
            self.birthday_name = "Friend"
            
        self.is_playing = True
        self.frame_count = 0
        self.play_btn.config(state='disabled')
        self.status_label.config(text=f"🎬 Playing birthday video for {self.birthday_name}! 🎉")
        
        # Start animation in separate thread
        self.animation_thread = threading.Thread(target=self.animation_loop)
        self.animation_thread.daemon = True
        self.animation_thread.start()
    
    def stop_video(self):
        """Stop the birthday video"""
        self.is_playing = False
        self.play_btn.config(state='normal')
        self.status_label.config(text="Video stopped. Ready for another celebration! 🎊")
        
        # Clear temporary animations
        self.clear_effects()
    
    def animation_loop(self):
        """Main animation loop"""
        scene_duration = 300  # frames per scene
        
        while self.is_playing:
            try:
                scene = (self.frame_count // scene_duration) % 4
                
                if scene == 0:
                    self.scene_welcome()
                elif scene == 1:
                    self.scene_balloons_party()
                elif scene == 2:
                    self.scene_confetti_rain()
                elif scene == 3:
                    self.scene_happy_birthday()
                
                self.animate_candles()
                self.animate_balloons()
                
                self.frame_count += 1
                time.sleep(0.05)  # ~20 FPS
                
            except tk.TclError:
                # Window was closed
                break
                
        self.is_playing = False
    
    def scene_welcome(self):
        """Scene 1: Welcome message"""
        if self.frame_count % 300 == 0:
            self.canvas.delete("welcome_text")
            self.canvas.create_text(425, 200, text=f"🎊 Welcome to {self.birthday_name}'s Birthday! 🎊", 
                                   font=('Arial', 18, 'bold'), fill='#2C3E50', tags="welcome_text")
        
        # Animate sun rotation
        if self.frame_count % 10 == 0:
            self.canvas.delete("sun_rays")
            for i in range(8):
                angle = (i * 45 + self.frame_count * 2) * math.pi / 180
                x1 = 725 + 40 * math.cos(angle)
                y1 = 75 + 40 * math.sin(angle)
                x2 = 725 + 50 * math.cos(angle)
                y2 = 75 + 50 * math.sin(angle)
                self.canvas.create_line(x1, y1, x2, y2, fill='#F1C40F', width=3, tags="sun_rays")
    
    def scene_balloons_party(self):
        """Scene 2: Dancing balloons"""
        if self.frame_count % 300 == 0:
            self.canvas.delete("welcome_text")
            self.canvas.create_text(425, 200, text=f"🎈 Let's Celebrate {self.birthday_name}! 🎈", 
                                   font=('Arial', 18, 'bold'), fill='#E74C3C', tags="welcome_text")
        
        # Make balloons dance more vigorously
        for balloon in self.balloons:
            dance_x = math.sin(self.frame_count * 0.1) * 10
            dance_y = math.cos(self.frame_count * 0.15) * 15
            
            self.canvas.coords(balloon['balloon'], 
                             balloon['x'] + dance_x, balloon['y'] + dance_y,
                             balloon['x'] + dance_x + 40, balloon['y'] + dance_y + 60)
    
    def scene_confetti_rain(self):
        """Scene 3: Confetti celebration"""
        if self.frame_count % 300 == 0:
            self.canvas.delete("welcome_text")
            self.canvas.create_text(425, 200, text=f"🎊 Confetti Time for {self.birthday_name}! 🎊", 
                                   font=('Arial', 18, 'bold'), fill='#8E44AD', tags="welcome_text")
            self.create_confetti()
        
        self.animate_confetti()
    
    def scene_happy_birthday(self):
        """Scene 4: Final birthday wishes"""
        if self.frame_count % 300 == 0:
            self.canvas.delete("welcome_text")
            self.canvas.delete("confetti")
            
            # Multi-line birthday message
            messages = [
                f"🎂 Happy Birthday",
                f"{self.birthday_name}! 🎂",
                "🌟 May all your wishes",
                "come true! 🌟"
            ]
            
            for i, msg in enumerate(messages):
                y_pos = 180 + i * 30
                color = self.colors[i % len(self.colors)]
                self.canvas.create_text(425, y_pos, text=msg, 
                                       font=('Arial', 16, 'bold'), 
                                       fill=color, tags="welcome_text")
        
        # Create birthday stars
        if self.frame_count % 20 == 0:
            self.create_birthday_stars()
    
    def create_confetti(self):
        """Create falling confetti pieces"""
        self.confetti = []
        for _ in range(50):
            x = random.randint(0, 850)
            y = random.randint(-100, -10)
            color = random.choice(self.colors)
            size = random.randint(3, 8)
            
            if random.choice([True, False]):
                # Rectangle confetti
                confetti = self.canvas.create_rectangle(x, y, x+size, y+size, 
                                                      fill=color, outline='', tags="confetti")
            else:
                # Oval confetti
                confetti = self.canvas.create_oval(x, y, x+size, y+size, 
                                                 fill=color, outline='', tags="confetti")
            
            self.confetti.append({
                'item': confetti,
                'x': x,
                'y': y,
                'speed': random.randint(2, 6),
                'rotation': random.randint(0, 360)
            })
    
    def animate_confetti(self):
        """Animate falling confetti"""
        for piece in self.confetti[:]:
            piece['y'] += piece['speed']
            piece['rotation'] += 5
            
            # Move confetti
            coords = self.canvas.coords(piece['item'])
            if coords:
                size = coords[2] - coords[0]
                self.canvas.coords(piece['item'], 
                                 piece['x'], piece['y'],
                                 piece['x'] + size, piece['y'] + size)
                
                # Remove if off screen
                if piece['y'] > 600:
                    self.canvas.delete(piece['item'])
                    self.confetti.remove(piece)
    
    def create_birthday_stars(self):
        """Create twinkling birthday stars"""
        self.canvas.delete("birthday_stars")
        
        for _ in range(10):
            x = random.randint(50, 800)
            y = random.randint(50, 400)
            color = random.choice(self.colors)
            
            # Create star shape
            size = random.randint(8, 15)
            points = []
            for i in range(10):
                angle = i * math.pi / 5
                if i % 2 == 0:
                    r = size
                else:
                    r = size * 0.5
                px = x + r * math.cos(angle - math.pi / 2)
                py = y + r * math.sin(angle - math.pi / 2)
                points.extend([px, py])
            
            self.canvas.create_polygon(points, fill=color, outline='white', 
                                     width=1, tags="birthday_stars")
    
    def animate_candles(self):
        """Animate candle flames"""
        if self.frame_count % 3 == 0:  # Flicker effect
            for candle, flame in self.cake_candles:
                coords = self.canvas.coords(flame)
                if coords:
                    # Make flame flicker
                    flicker = random.randint(-2, 2)
                    self.canvas.coords(flame, 
                                     coords[0] + flicker, coords[1], 
                                     coords[2] + flicker, coords[3])
                    
                    # Change flame color occasionally
                    if random.random() < 0.1:
                        flame_colors = ['#FF4500', '#FF6347', '#FF0000', '#FFA500']
                        self.canvas.itemconfig(flame, fill=random.choice(flame_colors))
    
    def animate_balloons(self):
        """Animate floating balloons"""
        for balloon in self.balloons:
            # Gentle floating motion
            balloon['float_offset'] += 0.1
            float_y = math.sin(balloon['float_offset']) * 5
            
            # Update positions
            self.canvas.coords(balloon['balloon'], 
                             balloon['x'], balloon['y'] + float_y,
                             balloon['x'] + 40, balloon['y'] + float_y + 60)
            
            self.canvas.coords(balloon['string'], 
                             balloon['x'] + 20, balloon['y'] + float_y + 60,
                             balloon['x'] + 20, balloon['y'] + float_y + 120)
            
            self.canvas.coords(balloon['highlight'], 
                             balloon['x'] + 10, balloon['y'] + float_y + 10,
                             balloon['x'] + 20, balloon['y'] + float_y + 20)
    
    def clear_effects(self):
        """Clear temporary animation effects"""
        self.canvas.delete("confetti")
        self.canvas.delete("birthday_stars")
        self.canvas.delete("welcome_text")
        
        # Reset balloons to original positions
        for balloon in self.balloons:
            self.canvas.coords(balloon['balloon'], 
                             balloon['x'], balloon['y'],
                             balloon['x'] + 40, balloon['y'] + 60)

def main():
    root = tk.Tk()
    
    # Center window on screen
    root.update_idletasks()
    width = 900
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = BirthdayVideo(root)
    
    # Show welcome message
    messagebox.showinfo("🎉 Birthday Video Creator", 
                       "Welcome to the Birthday Video Creator!\n\n"
                       "✨ Enter the birthday person's name\n"
                       "🎬 Click 'Play Video' to start the celebration\n"
                       "🎊 Enjoy the animated birthday party!\n\n"
                       "Made with ❤️ using pure Python!")
    
    root.mainloop()

if __name__ == "__main__":
    main()