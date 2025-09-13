# Import required libraries
from tkinter import *  # GUI library for creating the interface
import pandas as pd    # Data manipulation library for handling CSV files
import random as r     # Random library for selecting random words

class FlashCard:
    # Class constants for color scheme
    BACKGROUND_COLOR = "#8AF1BC"  # Light green background
    FLASHCARD_COLOR = "#236336"   # Dark green for contrast
    
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        
        # Load French-English word pairs from CSV file into a list of dictionaries
        try:
            self.data = pd.read_csv('./data/practice_words.csv').to_dict(orient='records')
        except FileNotFoundError:
            self.data = pd.read_csv('./data/french_words.csv').to_dict(orient='records')
        # List to store words that user got wrong for practice later
        self.practice_words = []
        
        # Current word being displayed
        self.random_word = None
        
        # Set up the GUI components
        self.init()

    def init(self):
        # Configure main window appearance
        self.root.config(padx=50, pady=50, bg=FlashCard.BACKGROUND_COLOR)

        # Create main canvas for flashcard display (800x526 pixels)
        self.canvas = Canvas(self.root, width=800, height=526, 
                           bg=FlashCard.BACKGROUND_COLOR, highlightthickness=0)
        
        # Load and display card front image
        self.card_front_photo = PhotoImage(file='./images/card_front.png')
        self.canvas_img = self.canvas.create_image(400, 263, image=self.card_front_photo)
        
        # Create text elements on the card
        self.canvas_word = self.canvas.create_text(400, 263, text='', 
                                                 font=('Arial', 60, 'bold'))
        self.canvas_language = self.canvas.create_text(400, 150, text='', 
                                                     font=('Arial', 40, 'italic'))
        
        # Position canvas in the grid layout
        # Position canvas in the grid layout
        self.canvas.grid(row=0, column=0)

        # Create frame to hold the buttons below the flashcard
        self.button_frame = Frame(self.root, bg=FlashCard.BACKGROUND_COLOR, 
                                width=800, highlightthickness=0)
        
        # Configure grid layout for button frame - make columns expandable
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)  # Left column (wrong button)
        self.button_frame.grid_columnconfigure(1, weight=1)  # Right column (correct button)
        self.button_frame.grid(row=1, column=0, sticky='ew')

        # Create "Wrong" button (X mark) - keeps word for practice
        self.wrong_photo = PhotoImage(file='./images/wrong.png')
        self.wrong_button = Button(self.button_frame, image=self.wrong_photo,
                                 highlightthickness=0, width=100, command=self.keep_word)
        self.wrong_button.grid(row=0, column=0)

        # Create "Correct" button (checkmark) - removes word from deck
        self.correct_photo = PhotoImage(file='./images/right.png')
        self.correct_button = Button(self.button_frame, image=self.correct_photo,
                                   highlightthickness=0, width=100, command=self.remove_word)
        self.correct_button.grid(row=0, column=1)
    
    def keep_word(self):
        """
        Called when user clicks the "Wrong" button (X mark).
        Saves the word for practice later and moves to next card.
        """
        # Cancel the automatic card flip timer
        self.root.after_cancel(self.flip_card_id)
        
        # Add current word to practice list
        self.practice_words.append(self.random_word)
        
        # Save practice words to CSV file for future sessions
        df = pd.DataFrame(self.practice_words)
        df.to_csv('./data/practice_words.csv', index=False)
        
        # Show next card
        self.new_card()
        

    def remove_word(self):
        """
        Called when user clicks the "Correct" button (checkmark).
        Removes the word from the deck and moves to next card.
        """
        # Cancel the automatic card flip timer
        self.root.after_cancel(self.flip_card_id)
        
        # Remove current word from the main deck (user knows this word)
        self.data.remove(self.random_word)
        
        # Show next card
        self.new_card()

    def flip_card(self):
        """
        Flips the card to show the English translation.
        Called automatically 3 seconds after a new card is shown.
        """
        # Load and display card back image
        self.card_back_photo = PhotoImage(file='./images/card_back.png')
        self.canvas.itemconfig(self.canvas_img, image=self.card_back_photo)
        
        # Update text to show English translation
        self.canvas.itemconfig(self.canvas_language, text='English')
        self.canvas.itemconfig(self.canvas_word, text=self.random_word.get('English'))
        
        # Cancel any pending flip timer (safety measure)
        self.root.after_cancel(self.flip_card_id)


    def new_card(self):
        """
        Prepares and displays a new flashcard with a French word.
        Sets up automatic flip to English after 3 seconds.
        """
        # Reset card to front side
        self.canvas.itemconfig(self.canvas_img, image=self.card_front_photo)
        self.canvas.itemconfig(self.canvas_language, text='')
        self.canvas.itemconfig(self.canvas_word, text='')
        
        
        # Schedule automatic flip to English after 3 seconds (3000ms)
        if self.get_new_word():
            self.flip_card_id = self.root.after(3000, self.flip_card)

    def get_new_word(self):
        """
        Selects a random word from the remaining deck and displays the French side.
        """
        # Choose random word from available words
        if len(self.data):
            self.random_word: dict = r.choice(self.data)
            
            # Get index of selected word (for potential future use)
            self.random_word_idx = self.data.index(self.random_word)
            
            # Display French word on the front of the card
            self.canvas.itemconfig(self.canvas_language, text='French')
            self.canvas.itemconfig(self.canvas_word, text=self.random_word.get('French'))
            return True
        else:
            self.canvas.itemconfig(self.canvas_language, text='')
            self.canvas.itemconfig(self.canvas_word, text='Good Job! Now bake your French wife\'s croissants'
                                   ,font=('Arial', 20, 'bold'))
            return False

    def start(self):
        """
        Starts the flashcard application by showing the first card
        and beginning the GUI event loop.
        """
        # Show the first card
        self.new_card()
        
        # Start the tkinter main loop (keeps window open and responsive)
        self.root.mainloop()


def main():
    """
    Main function to create and start the FlashCard application.
    """
    # Create FlashCard instance
    game = FlashCard()
    
    # Start the game
    game.start()


# Entry point - run main function if this file is executed directly
if __name__ == "__main__":
    main()