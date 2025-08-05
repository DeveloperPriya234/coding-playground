import tkinter as tk
import math
import random
import time

class BirthdayAnimation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Happy Birthday Animation!")
        self.root.geometry("800x600")
        self.root.configure(bg='lightblue')
        
        # Create canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='lightblue')
        self.canvas.pack()
        
        # Animation variables
        self.frame = 0
        self.balloons = []
        self.confetti = []
        self.stars = []
        
        # Colors
        self.balloon_colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'pink']
        self.confetti_colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'pink', 'cyan', 'magenta']
        
        # Initialize objects
        self.init_balloons()
        self.init_confetti()
        self.init_stars()
        
        # Start animation
        self.animate()
        
    def init_balloons(self):
        """Initialize floating balloons"""
        for i in range(8):
            balloon = {
                'x': random.randint(50, 750),
                'y': random.randint(200, 500),
                'color': random.choice(self.balloon_colors),
                'size': random.randint(25, 40),
                'speed': random.uniform(0.5, 1.5),
                'wobble': random.uniform(0.02, 0.05),
                'phase': random.uniform(0, 2 * math.pi)
            }
            self.balloons.append(balloon)
    
    def init_confetti(self):
        """Initialize confetti particles"""
        for i in range(30):
            particle = {
                'x': random.randint(100, 700),
                'y': random.randint(50, 200),
                'color': random.choice(self.confetti_colors),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(1, 3),
                'size': random.randint(3, 8)
            }
            self.confetti.append(particle)
    
    def init_stars(self):
        """Initialize twinkling stars"""
        star_positions = [(100, 80), (200, 60), (300, 90), (500, 70), (600, 85), (700, 65)]
        for x, y in star_positions:
            star = {
                'x': x,
                'y': y,
                'phase': random.uniform(0, 2 * math.pi)
            }
            self.stars.append(star)
    
    def draw_ground(self):
        """Draw the ground"""
        self.canvas.create_rectangle(0, 500, 800, 600, fill='lightgreen', outline='green')
    
    def draw_cake(self):
        """Draw birthday cake with candles"""
        cake_x, cake_y = 400, 450
        
        # Cake base
        self.canvas.create_rectangle(cake_x - 80, cake_y - 40, cake_x + 80, cake_y + 40, 
                                   fill='chocolate', outline='black', width=2)
        
        # Cake frosting
        self.canvas.create_rectangle(cake_x - 70, cake_y - 20, cake_x + 70, cake_y - 40, 
                                   fill='white', outline='pink', width=2)
        
        # Candles
        candle_positions = [-40, -20, 0, 20, 40]
        for pos in candle_positions:
            # Candle stick
            self.canvas.create_rectangle(cake_x + pos - 3, cake_y - 60, cake_x + pos + 3, cake_y - 40, 
                                       fill='yellow', outline='black')
            
            # Flickering flame
            flicker = 3 * math.sin(self.frame * 0.3 + pos * 0.1)
            self.canvas.create_oval(cake_x + pos - 5, cake_y - 75 + flicker, 
                                  cake_x + pos + 5, cake_y - 65 + flicker, 
                                  fill='orange', outline='red')
    
    def draw_balloons(self):
        """Draw and animate balloons"""
        for balloon in self.balloons:
            # Update balloon position
            balloon['y'] -= balloon['speed']
            balloon['x'] += balloon['wobble'] * math.sin(self.frame * 0.1 + balloon['phase']) * 10
            
            # Reset if balloon goes off screen
            if balloon['y'] < -50:
                balloon['y'] = 650
                balloon['x'] = random.randint(50, 750)
            
            # Keep balloons on screen horizontally
            if balloon['x'] < 50:
                balloon['x'] = 50
            elif balloon['x'] > 750:
                balloon['x'] = 750
            
            # Draw balloon string
            self.canvas.create_line(balloon['x'], balloon['y'] + balloon['size'], 
                                  balloon['x'], balloon['y'] + balloon['size'] + 60, 
                                  fill='black', width=2)
            
            # Draw balloon
            self.canvas.create_oval(balloon['x'] - balloon['size'], balloon['y'] - balloon['size'],
                                  balloon['x'] + balloon['size'], balloon['y'] + balloon['size'],
                                  fill=balloon['color'], outline='black', width=2)
            
            # Draw balloon highlight
            self.canvas.create_oval(balloon['x'] - balloon['size']//2, balloon['y'] - balloon['size']//2,
                                  balloon['x'] - balloon['size']//4, balloon['y'] - balloon['size']//4,
                                  fill='white', outline='')
    
    def draw_confetti(self):
        """Draw and animate confetti"""
        for particle in self.confetti:
            # Update confetti position
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vy'] += 0.1  # gravity
            
            # Reset if confetti goes off screen
            if particle['y'] > 600 or particle['x'] < 0 or particle['x'] > 800:
                particle['x'] = random.randint(100, 700)
                particle['y'] = random.randint(-50, 0)
                particle['vx'] = random.uniform(-2, 2)
                particle['vy'] = random.uniform(1, 3)
            
            # Draw confetti
            self.canvas.create_rectangle(particle['x'] - particle['size']//2, 
                                       particle['y'] - particle['size']//2,
                                       particle['x'] + particle['size']//2, 
                                       particle['y'] + particle['size']//2,
                                       fill=particle['color'], outline='')
    
    def draw_stars(self):
        """Draw twinkling stars"""
        for star in self.stars:
            # Calculate twinkling effect
            alpha = 0.5 + 0.5 * math.sin(self.frame * 0.1 + star['phase'])
            
            # Create star points
            size = 8 + 4 * alpha
            points = []
            for i in range(10):
                angle = i * math.pi / 5
                if i % 2 == 0:
                    radius = size
                else:
                    radius = size / 2
                x = star['x'] + radius * math.cos(angle - math.pi / 2)
                y = star['y'] + radius * math.sin(angle - math.pi / 2)
                points.extend([x, y])
            
            # Draw star
            color_intensity = int(255 * alpha)
            color = f"#{color_intensity:02x}{color_intensity:02x}00"  # Yellow with varying intensity
            self.canvas.create_polygon(points, fill=color, outline='gold')
    
    def draw_message(self):
        """Draw animated birthday message"""
        # Pulsing effect
        scale = 1 + 0.2 * math.sin(self.frame * 0.15)
        font_size = int(36 * scale)
        
        # Create text with shadow effect
        self.canvas.create_text(402, 152, text="HAPPY BIRTHDAY!", 
                              font=("Arial", font_size, "bold"), 
                              fill='black')  # Shadow
        self.canvas.create_text(400, 150, text="HAPPY BIRTHDAY!", 
                              font=("Arial", font_size, "bold"), 
                              fill='red')
        
        # Draw decorative box around text
        box_width = 300 * scale
        box_height = 60 * scale
        self.canvas.create_rectangle(400 - box_width//2, 150 - box_height//2,
                                   400 + box_width//2, 150 + box_height//2,
                                   fill='', outline='gold', width=3)
    
    def draw_party_hats(self):
        """Draw party hats in corners"""
        hat_positions = [(100, 100), (700, 100), (100, 500), (700, 500)]
        hat_colors = ['red', 'blue', 'green', 'purple']
        
        for i, (x, y) in enumerate(hat_positions):
            # Hat triangle
            points = [x, y - 30, x - 20, y + 10, x + 20, y + 10]
            self.canvas.create_polygon(points, fill=hat_colors[i], outline='black', width=2)
            
            # Hat pom-pom
            self.canvas.create_oval(x - 5, y - 35, x + 5, y - 25, fill='white', outline='black')
    
    def draw_presents(self):
        """Draw present boxes"""
        present_positions = [(150, 520), (650, 520)]
        present_colors = [('red', 'gold'), ('blue', 'silver')]
        
        for i, (x, y) in enumerate(present_positions):
            box_color, ribbon_color = present_colors[i]
            
            # Present box
            self.canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, 
                                       fill=box_color, outline='black', width=2)
            
            # Ribbon
            self.canvas.create_rectangle(x - 25, y - 3, x + 25, y + 3, 
                                       fill=ribbon_color, outline='')
            self.canvas.create_rectangle(x - 3, y - 25, x + 3, y + 25, 
                                       fill=ribbon_color, outline='')
            
            # Bow
            self.canvas.create_oval(x - 8, y - 30, x + 8, y - 20, 
                                  fill=ribbon_color, outline='black')
    
    def animate(self):
        """Main animation loop"""
        # Clear canvas
        self.canvas.delete("all")
        
        # Draw all elements
        self.draw_ground()
        self.draw_cake()
        self.draw_balloons()
        self.draw_confetti()
        self.draw_stars()
        self.draw_message()
        self.draw_party_hats()
        self.draw_presents()
        
        # Update frame counter
        self.frame += 1
        
        # Schedule next frame
        self.root.after(50, self.animate)  # 20 FPS
    
    def run(self):
        """Start the animation"""
        self.root.mainloop()

# Create and run the animation
if __name__ == "__main__":
    print("Starting Birthday Animation...")
    print("Close the window to stop the animation.")
    
    animation = BirthdayAnimation()
    animation.run()