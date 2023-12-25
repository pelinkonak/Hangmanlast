import pygame
import random

class HangmanButton:
    def __init__(self, position, image, letter):
        self.position = position
        self.letter = letter
        self.image = image
        self.imageRect = pygame.Rect(self.position[0] - 5, self.position[1], 30, 30)
        self.active = True

    def mouseHighlight(self, window):
        pygame.draw.rect(window, (255, 0, 0), [self.imageRect[0], self.imageRect[1], self.imageRect[2], self.imageRect[3]])
        window.blit(self.image, self.position)
        pygame.draw.rect(window, WHITE, [self.imageRect[0], self.imageRect[1], self.imageRect[2], self.imageRect[3]], 1)

    def draw(self, window):
        if self.active:
            window.blit(self.image, self.position)
            pygame.draw.rect(window, WHITE, [self.imageRect[0], self.imageRect[1], self.imageRect[2], self.imageRect[3]], 1)
        else:
            self.mouseHighlight(window)

def openFile(difficulty):
    """Open and load words from the text file into a simple list based on difficulty"""
    filename = f'{difficulty}WordList.txt'
    with open(filename, 'r') as file:
        content = file.readlines()
        newList = []
        for itemList in content:
            newList.append(itemList.split(','))

        for wordList in newList:
            for word in wordList:
                if len(word.strip()) >= 3 and len(word.strip()) <= 10:
                    WORDLIST.append(word.strip())

def selectDifficulty():
    """Allow the player to choose difficulty level"""
    print("Select difficulty level:")
    print("1. Easy Level")
    print("2. Medium Level")
    print("3. Hard Level")

    while True:
        choice = input("Which level would you like to choose?: ")
        if choice in ['1', '2', '3']:
            return {'1': 'easy', '2': 'medium', '3': 'hard'}[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def selectRandomWord():
    """Select a random word from the Word List Generated"""
    return random.choice(WORDLIST)

def drawLetters(letter):
    """Creates the font object for text on the screen."""
    text = pygame.font.SysFont('Comic sans', 22)
    printText = text.render(letter, 1, WHITE)
    return printText

def drawLetterLines(word):
    """Draw lines for each letter in the chosen word"""
    wordLengthX = len(word) * (25 + 15)

    startXY = [SCREENWIDTH - 50 - wordLengthX, 350]
    lengthXY = [25, 0]
    spacing = [15, 0]

    for ind, letter in enumerate(word):
        pygame.draw.line(GAMESCREEN, WHITE, (startXY[0], startXY[1]), (startXY[0] + lengthXY[0], startXY[1] + lengthXY[1]), 3)
        GAMESCREEN.blit(drawLetters(guessWord[ind]), (startXY[0]+10, 320))
        startXY[0] = startXY[0] + lengthXY[0] + spacing[0]
        startXY[1] = startXY[1] + lengthXY[1] + spacing[1]

def createAlphabet():
    """Creates the alphabet objects for the screen"""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    xPos = 100
    yPos = 500
    letNum = 0
    for num in [9, 9, 8]:
        for _ in range(num):
            ALPHABETBUTTONS.append(HangmanButton((xPos, yPos), drawLetters(alphabet[letNum]), alphabet[letNum]))
            letNum += 1
            xPos += 50
        xPos = 100
        yPos += 40

def drawAlphabet(itemList):
    """Draws the alphabet to the screen."""
    for item in itemList:
        item.draw(GAMESCREEN)

    GAMESCREEN.blit(drawLetters(f'Winning Series : {str(winStreak)}'), (SCREENWIDTH - 300, 100))

def endGame():
    """Handles the end of a round"""
    global chosenWord
    global guessWord
    global numberOfGuesses
    global gameOver
    global winStreak

    if ''.join(guessWord) == chosenWord:
        winStreak += 1

    while gameOver:
        ALPHABETBUTTONS.clear()
        GAMESCREEN.fill((0, 0, 0))
        message = drawLetters('Click to play again')
        GAMESCREEN.blit(message, (SCREENWIDTH // 2 - message.get_width() // 2, SCREENHEIGHT // 2 + 30))

        if ''.join(guessWord) == chosenWord:
            message = drawLetters(f'Congratulations! You guessed {chosenWord}!')
            GAMESCREEN.blit(message, (SCREENWIDTH//2 - message.get_width()//2, SCREENHEIGHT//2))
        elif numberOfGuesses == 6:
            message = drawLetters(f'Sorry, you lost! The word was {chosenWord}!')
            GAMESCREEN.blit(message, (SCREENWIDTH//2 - message.get_width()//2, SCREENHEIGHT//2))
            winStreak = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                numberOfGuesses = 0
                chosenWord = selectRandomWord().upper()
                guessWord = [' ' for letter in chosenWord]
                createAlphabet()
                drawAlphabet(ALPHABETBUTTONS)
                gameOver = False
            if event.type == pygame.QUIT:
                pygame.quit()

def drawGallows(window):
    """Draw the Gallows"""
    pygame.draw.line(window, (255, 255, 0), (100, 400), (275, 400), 3)
    pygame.draw.line(window, (255, 255, 0), (125, 400), (125, 50), 3)
    pygame.draw.line(window, (255, 255, 0), (125, 50), (275, 50), 3)
    pygame.draw.line(window, (255, 255, 0), (125, 100), (175, 50), 3)
    pygame.draw.line(window, (255, 255, 0), (275, 50), (275, 125), 3)

def drawHead(window):
    """Draws the Hanged man's Head"""
    pygame.draw.circle(window, (255, 255, 0), (275, 150), (25), 3)

def drawBody(window):
    """Draws the Hanged Man's Body"""
    pygame.draw.line(window, (255, 255, 0), (275, 175), (275, 225), 3)

def drawLeftArm(window):
    """Draws the Hanged Man's Left Arm"""
    pygame.draw.line(window, (255, 255, 0), (275, 185), (245, 215), 3)

def drawRightArm(window):
    """Draws the Hanged Man's Right Arm"""
    pygame.draw.line(window, (255, 255, 0), (275, 185), (305, 215), 3)

def drawLeftLeg(window):
    """Draws the Hanged Man's Left Leg"""
    pygame.draw.line(window, (255, 255, 0), (275, 225), (250, 250), 3)
    pygame.draw.line(window, (255, 255, 0), (250, 250), (250, 275), 3)
    pygame.draw.line(window, (255, 255, 0), (250, 275), (240, 275), 3)

def drawRightLeg(window):
    """Draws the Hanged Man's Left Leg"""
    pygame.draw.line(window, (255, 255, 0), (275, 225), (300, 250), 3)
    pygame.draw.line(window, (255, 255, 0), (300, 250), (300, 275), 3)
    pygame.draw.line(window, (255, 255, 0), (300, 275), (310, 275), 3)

def drawHangman(window, numberGuesses):
    """Draws the various stages of the Hanged Man"""
    if numberGuesses >= 0:
        drawGallows(window)
    if numberGuesses >= 1:
        drawHead(window)
    if numberGuesses >= 2:
        drawBody(window)
    if numberGuesses >= 3:
        drawLeftArm(window)
    if numberGuesses >= 4:
        drawRightArm(window)
    if numberGuesses >= 5:
        drawLeftLeg(window)
    if numberGuesses >= 6:
        drawRightLeg(window)

def useHint(chosen_word, guessed_word):
    """Uses the hint to reveal a random letter in the chosen word."""
    available_hints = [index for index, letter in enumerate(chosen_word) if guessed_word[index] == ' ']
    if available_hints:
        hint_index = random.choice(available_hints)
        guessed_word[hint_index] = chosen_word[hint_index]

# Hangman Words list
pygame.init()
pygame.font.init()
difficulty = selectDifficulty()
WORDLIST = []
ALPHABETBUTTONS = []

openFile(difficulty)  # Assuming 'difficulty' is already defined

# Game settings
SCREENWIDTH = 800
SCREENHEIGHT = 640
WHITE = (255, 255, 255)

# Display Initialization
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Hang Man')

# Game Variables and load functions
numberOfGuesses = 0
chosenWord = selectRandomWord().upper()
guessWord = [' ' for letter in chosenWord]
createAlphabet()
print(chosenWord)
print(guessWord)
mouseClicked = False
gameOver = False
winStreak = 0

# Define hint button rectangle
hintButtonRect = pygame.Rect(SCREENWIDTH - 100, 10, 80, 30)

# Main game loop.
RUN = True
while RUN:
    GAMESCREEN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True

            for item in ALPHABETBUTTONS:
                if item.imageRect.collidepoint(event.pos):
                    if item.letter in chosenWord:
                        for ind, let in enumerate(chosenWord):
                            if item.letter == let:
                                guessWord[ind] = item.letter
                    elif item.letter not in chosenWord and item.active:
                        numberOfGuesses += 1
                    item.active = False

            # Check if the hint button is pressed
            if hintButtonRect.collidepoint(event.pos):
                useHint(chosenWord, guessWord)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseClicked = False

    drawLetterLines(chosenWord)
    drawAlphabet(ALPHABETBUTTONS)
    drawHangman(GAMESCREEN, numberOfGuesses)

    # Draw the hint button
    pygame.draw.rect(GAMESCREEN, (255, 0, 0), hintButtonRect)
    pygame.draw.rect(GAMESCREEN, WHITE, hintButtonRect, 1)
    hint_text = drawLetters('ASK ME!')
    GAMESCREEN.blit(hint_text, (hintButtonRect.x + hintButtonRect.width // 2 - hint_text.get_width() // 2,
                                hintButtonRect.y + hintButtonRect.height // 2 - hint_text.get_height() // 2))

    pygame.display.update()

    if ''.join(guessWord) == chosenWord or numberOfGuesses == 6:
        gameOver = True
        endGame()

pygame.quit()
