import tkinter as tk
from tkinter import messagebox
import math
import random
import time

class BirthdayPartyGames:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎉 Birthday Party Games! 🎉")
        self.root.geometry("900x700")
        self.root.configure(bg='lightblue')
        
        # Game state
        self.current_game = "menu"
        self.score = 0
        self.lives = 3
        self.level = 1
        self.frame = 0
        
        # Create main canvas
        self.canvas = tk.Canvas(self.root, width=900, height=600, bg='lightblue')
        self.canvas.pack()
        
        # Create control panel
        self.control_frame = tk.Frame(self.root, bg='lightgray', height=100)
        self.control_frame.pack(fill='x')
        
        # Game objects
        self.balloons = []
        self.confetti = []
        self.candles = []
        self.presents = []
        self.player = {'x': 450, 'y': 500, 'size': 20}
        
        # Colors
        self.colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'pink', 'cyan']
        
        # Bind events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()
        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.bind('<Motion>', self.mouse_move)
        
        # Initialize
        self.create_controls()
        self.show_menu()
        self.animate()
    
    def create_controls(self):
        """Create control buttons"""
        tk.Label(self.control_frame, text="🎮 Birthday Party Games 🎮", 
                font=("Arial", 16, "bold"), bg='lightgray').pack(side='left', padx=10)
        
        tk.Button(self.control_frame, text="🏠 Menu", command=self.show_menu,
                 bg='lightgreen', font=("Arial", 12)).pack(side='left', padx=5)
        
        tk.Button(self.control_frame, text="🎈 Balloon Pop", command=self.start_balloon_game,
                 bg='yellow', font=("Arial", 12)).pack(side='left', padx=5)
        
        tk.Button(self.control_frame, text="🕯️ Candle Blow", command=self.start_candle_game,
                 bg='orange', font=("Arial", 12)).pack(side='left', padx=5)
        
        tk.Button(self.control_frame, text="🎁 Present Hunt", command=self.start_present_game,
                 bg='pink', font=("Arial", 12)).pack(side='left', padx=5)
        
        tk.Button(self.control_frame, text="🎯 Party Catcher", command=self.start_catcher_game,
                 bg='lightcoral', font=("Arial", 12)).pack(side='left', padx=5)
        
        # Score display
        self.score_label = tk.Label(self.control_frame, text=f"Score: {self.score}", 
                                   font=("Arial", 12, "bold"), bg='lightgray')
        self.score_label.pack(side='right', padx=10)
    
    def show_menu(self):
        """Show main menu"""
        self.current_game = "menu"
        self.canvas.delete("all")
        
        # Title
        self.canvas.create_text(450, 100, text="🎉 BIRTHDAY PARTY GAMES 🎉",
                               font=("Arial", 32, "bold"), fill='red')
        
        # Instructions
        instructions = [
            "🎈 Balloon Pop - Click balloons to pop them!",
            "🕯️ Candle Blow - Move mouse to blow out candles!",
            "🎁 Present Hunt - Find hidden presents with arrow keys!",
            "🎯 Party Catcher - Catch falling party items!",
            "",
            "Use the buttons below to start any game!"
        ]
        
        for i, instruction in enumerate(instructions):
            self.canvas.create_text(450, 200 + i * 30, text=instruction,
                                   font=("Arial", 14), fill='black')
        
        # Decorations
        self.draw_party_decorations()
    
    def start_balloon_game(self):
        """Start balloon popping game"""
        self.current_game = "balloon"
        self.balloons = []
        self.lives = 3
        
        # Create balloons
        for i in range(8):
            balloon = {
                'x': random.randint(50, 850),
                'y': random.randint(100, 500),
                'size': random.randint(25, 45),
                'color': random.choice(self.colors),
                'speed': random.uniform(0.5, 2.0),
                'direction': random.uniform(0, 2 * math.pi),
                'alive': True
            }
            self.balloons.append(balloon)
    
    def start_candle_game(self):
        """Start candle blowing game"""
        self.current_game = "candle"
        self.candles = []
        
        # Create candles
        for i in range(6):
            candle = {
                'x': 150 + i * 120,
                'y': 300,
                'lit': True,
                'flame_size': random.uniform(8, 15)
            }
            self.candles.append(candle)
    
    def start_present_game(self):
        """Start present hunting game"""
        self.current_game = "present"
        self.presents = []
        self.player = {'x': 450, 'y': 300, 'size': 20}
        
        # Create hidden presents
        for i in range(5):
            present = {
                'x': random.randint(50, 850),
                'y': random.randint(50, 550),
                'color': random.choice(self.colors),
                'found': False,
                'pulse': random.uniform(0, 2 * math.pi)
            }
            self.presents.append(present)
    
    def start_catcher_game(self):
        """Start party catcher game"""
        self.current_game = "catcher"
        self.confetti = []
        self.player = {'x': 450, 'y': 550, 'size': 30}
        
        # Create falling items
        for i in range(3):
            self.spawn_falling_item()
    
    def spawn_falling_item(self):
        """Spawn a new falling item"""
        item = {
            'x': random.randint(50, 850),
            'y': 0,
            'type': random.choice(['balloon', 'present', 'confetti', 'star']),
            'color': random.choice(self.colors),
            'speed': random.uniform(2, 5),
            'size': random.randint(15, 30)
        }
        self.confetti.append(item)
    
    def key_press(self, event):
        """Handle key presses"""
        if self.current_game == "present":
            # Move player in present hunt
            if event.keysym == 'Left' and self.player['x'] > 25:
                self.player['x'] -= 20
            elif event.keysym == 'Right' and self.player['x'] < 875:
                self.player['x'] += 20
            elif event.keysym == 'Up' and self.player['y'] > 25:
                self.player['y'] -= 20
            elif event.keysym == 'Down' and self.player['y'] < 575:
                self.player['y'] += 20
                
        elif self.current_game == "catcher":
            # Move player in catcher game
            if event.keysym == 'Left' and self.player['x'] > 25:
                self.player['x'] -= 25
            elif event.keysym == 'Right' and self.player['x'] < 875:
                self.player['x'] += 25
    
    def mouse_click(self, event):
        """Handle mouse clicks"""
        if self.current_game == "balloon":
            # Check balloon clicks
            for balloon in self.balloons:
                if balloon['alive']:
                    distance = math.sqrt((event.x - balloon['x'])**2 + (event.y - balloon['y'])**2)
                    if distance < balloon['size']:
                        balloon['alive'] = False
                        self.score += 10
                        self.update_score()
                        
                        # Create pop effect
                        for i in range(6):
                            self.create_pop_effect(balloon['x'], balloon['y'])
    
    def mouse_move(self, event):
        """Handle mouse movement"""
        if self.current_game == "candle":
            # Blow out candles near mouse
            for candle in self.candles:
                distance = math.sqrt((event.x - candle['x'])**2 + (event.y - candle['y'])**2)
                if distance < 80 and candle['lit']:
                    candle['lit'] = False
                    self.score += 20
                    self.update_score()
    
    def create_pop_effect(self, x, y):
        """Create balloon pop effect"""
        # This would create a visual effect - simplified for this example
        pass
    
    def update_score(self):
        """Update score display"""
        self.score_label.config(text=f"Score: {self.score}")
    
    def draw_party_decorations(self):
        """Draw party decorations for menu"""
        # Draw balloons
        for i in range(4):
            x = 150 + i * 200
            y = 400 + 30 * math.sin(self.frame * 0.1 + i)
            self.canvas.create_oval(x - 25, y - 35, x + 25, y + 5, 
                                  fill=self.colors[i], outline='black', width=2)
            self.canvas.create_line(x, y + 5, x, y + 40, fill='black', width=2)
        
        # Draw confetti
        for i in range(20):
            x = random.randint(50, 850)
            y = random.randint(50, 150)
            size = random.randint(3, 8)
            color = random.choice(self.colors)
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline='')
    
    def draw_balloon_game(self):
        """Draw balloon popping game"""
        self.canvas.create_text(450, 30, text="🎈 POP THE BALLOONS! 🎈",
                               font=("Arial", 24, "bold"), fill='red')
        
        self.canvas.create_text(450, 60, text="Click on balloons to pop them!",
                               font=("Arial", 14), fill='black')
        
        # Update and draw balloons
        active_balloons = 0
        for balloon in self.balloons:
            if balloon['alive']:
                active_balloons += 1
                
                # Move balloon
                balloon['x'] += balloon['speed'] * math.cos(balloon['direction'])
                balloon['y'] += balloon['speed'] * math.sin(balloon['direction'])
                
                # Bounce off walls
                if balloon['x'] < balloon['size'] or balloon['x'] > 900 - balloon['size']:
                    balloon['direction'] = math.pi - balloon['direction']
                if balloon['y'] < balloon['size'] or balloon['y'] > 600 - balloon['size']:
                    balloon['direction'] = -balloon['direction']
                
                # Keep in bounds
                balloon['x'] = max(balloon['size'], min(900 - balloon['size'], balloon['x']))
                balloon['y'] = max(balloon['size'], min(600 - balloon['size'], balloon['y']))
                
                # Draw balloon
                self.canvas.create_oval(balloon['x'] - balloon['size'], balloon['y'] - balloon['size'],
                                      balloon['x'] + balloon['size'], balloon['y'] + balloon['size'],
                                      fill=balloon['color'], outline='black', width=2)
                
                # Draw highlight
                self.canvas.create_oval(balloon['x'] - balloon['size']//2, balloon['y'] - balloon['size']//2,
                                      balloon['x'] - balloon['size']//4, balloon['y'] - balloon['size']//4,
                                      fill='white', outline='')
        
        # Check win condition
        if active_balloons == 0:
            self.canvas.create_text(450, 300, text="🎉 ALL BALLOONS POPPED! 🎉",
                                   font=("Arial", 32, "bold"), fill='gold')
            # Add new balloons
            if self.frame % 120 == 0:  # Every 6 seconds
                self.start_balloon_game()
    
    def draw_candle_game(self):
        """Draw candle blowing game"""
        self.canvas.create_text(450, 30, text="🕯️ BLOW OUT THE CANDLES! 🕯️",
                               font=("Arial", 24, "bold"), fill='orange')
        
        self.canvas.create_text(450, 60, text="Move your mouse near candles to blow them out!",
                               font=("Arial", 14), fill='black')
        
        # Draw cake
        self.canvas.create_rectangle(300, 350, 600, 450, fill='chocolate', outline='black', width=2)
        self.canvas.create_rectangle(310, 330, 590, 350, fill='white', outline='pink', width=2)
        
        # Draw candles
        lit_candles = 0
        for candle in self.candles:
            # Candle stick
            self.canvas.create_rectangle(candle['x'] - 5, 250, candle['x'] + 5, 330,
                                       fill='yellow', outline='black', width=1)
            
            if candle['lit']:
                lit_candles += 1
                # Flickering flame
                flicker = candle['flame_size'] + 3 * math.sin(self.frame * 0.3 + candle['x'] * 0.01)
                self.canvas.create_oval(candle['x'] - 8, 240 - flicker, candle['x'] + 8, 250,
                                      fill='orange', outline='red', width=1)
        
        # Check win condition
        if lit_candles == 0:
            self.canvas.create_text(450, 500, text="🎂 HAPPY BIRTHDAY! ALL CANDLES OUT! 🎂",
                                   font=("Arial", 28, "bold"), fill='gold')
            # Reset candles
            if self.frame % 180 == 0:  # Every 9 seconds
                self.start_candle_game()
    
    def draw_present_game(self):
        """Draw present hunting game"""
        self.canvas.create_text(450, 30, text="🎁 FIND THE HIDDEN PRESENTS! 🎁",
                               font=("Arial", 24, "bold"), fill='purple')
        
        self.canvas.create_text(450, 60, text="Use arrow keys to move and find presents!",
                               font=("Arial", 14), fill='black')
        
        # Draw player
        self.canvas.create_oval(self.player['x'] - self.player['size'], 
                               self.player['y'] - self.player['size'],
                               self.player['x'] + self.player['size'], 
                               self.player['y'] + self.player['size'],
                               fill='blue', outline='darkblue', width=3)
        
        # Draw presents
        found_presents = 0
        for present in self.presents:
            if not present['found']:
                # Check collision with player
                distance = math.sqrt((self.player['x'] - present['x'])**2 + 
                                   (self.player['y'] - present['y'])**2)
                if distance < self.player['size'] + 20:
                    present['found'] = True
                    self.score += 50
                    self.update_score()
                
                # Draw present with pulsing effect
                pulse = 5 * math.sin(self.frame * 0.2 + present['pulse'])
                size = 20 + pulse
                
                self.canvas.create_rectangle(present['x'] - size, present['y'] - size,
                                           present['x'] + size, present['y'] + size,
                                           fill=present['color'], outline='black', width=2)
                
                # Draw ribbon
                self.canvas.create_line(present['x'] - size, present['y'],
                                      present['x'] + size, present['y'],
                                      fill='gold', width=4)
                self.canvas.create_line(present['x'], present['y'] - size,
                                      present['x'], present['y'] + size,
                                      fill='gold', width=4)
            else:
                found_presents += 1
        
        # Check win condition
        if found_presents == len(self.presents):
            self.canvas.create_text(450, 500, text="🏆 ALL PRESENTS FOUND! 🏆",
                                   font=("Arial", 32, "bold"), fill='gold')
            # Reset game
            if self.frame % 180 == 0:
                self.start_present_game()
    
    def draw_catcher_game(self):
        """Draw party catcher game"""
        self.canvas.create_text(450, 30, text="🎯 CATCH THE PARTY ITEMS! 🎯",
                               font=("Arial", 24, "bold"), fill='green')
        
        self.canvas.create_text(450, 60, text="Use left/right arrow keys to catch falling items!",
                               font=("Arial", 14), fill='black')
        
        # Draw player basket
        self.canvas.create_arc(self.player['x'] - self.player['size'], 
                              self.player['y'] - self.player['size']//2,
                              self.player['x'] + self.player['size'], 
                              self.player['y'] + self.player['size']//2,
                              start=0, extent=180, fill='brown', outline='black', width=2)
        
        # Update and draw falling items
        for item in self.confetti[:]:
            item['y'] += item['speed']
            
            # Check collision with player
            if (abs(item['x'] - self.player['x']) < self.player['size'] and 
                abs(item['y'] - self.player['y']) < self.player['size']):
                self.confetti.remove(item)
                self.score += 25
                self.update_score()
                self.spawn_falling_item()
                continue
            
            # Remove if off screen
            if item['y'] > 650:
                self.confetti.remove(item)
                self.spawn_falling_item()
                continue
            
            # Draw item based on type
            if item['type'] == 'balloon':
                self.canvas.create_oval(item['x'] - item['size']//2, item['y'] - item['size']//2,
                                      item['x'] + item['size']//2, item['y'] + item['size']//2,
                                      fill=item['color'], outline='black', width=1)
            elif item['type'] == 'present':
                self.canvas.create_rectangle(item['x'] - item['size']//2, item['y'] - item['size']//2,
                                           item['x'] + item['size']//2, item['y'] + item['size']//2,
                                           fill=item['color'], outline='black', width=1)
            elif item['type'] == 'confetti':
                self.canvas.create_rectangle(item['x'] - 3, item['y'] - 3,
                                           item['x'] + 3, item['y'] + 3,
                                           fill=item['color'], outline='')
            elif item['type'] == 'star':
                # Draw simple star
                self.canvas.create_text(item['x'], item['y'], text='⭐', font=("Arial", item['size']))
    
    def animate(self):
        """Main animation loop"""
        self.canvas.delete("all")
        
        # Draw current game
        if self.current_game == "menu":
            self.show_menu()
        elif self.current_game == "balloon":
            self.draw_balloon_game()
        elif self.current_game == "candle":
            self.draw_candle_game()
        elif self.current_game == "present":
            self.draw_present_game()
        elif self.current_game == "catcher":
            self.draw_catcher_game()
        
        self.frame += 1
        self.root.after(50, self.animate)  # 20 FPS
    
    def run(self):
        """Start the game"""
        self.root.mainloop()

# Create and run the birthday party games
if __name__ == "__main__":
    print("🎉 Starting Birthday Party Games! 🎉")
    print("Use buttons to switch between games:")
    print("🎈 Balloon Pop - Click to pop balloons")
    print("🕯️ Candle Blow - Move mouse to blow candles")
    print("🎁 Present Hunt - Arrow keys to find presents")
    print("🎯 Party Catcher - Arrow keys to catch items")
    
    game = BirthdayPartyGames()
    game.run()