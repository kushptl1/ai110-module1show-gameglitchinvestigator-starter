# 🎮 Game Glitch Investigator: The Impossible Guesser

## Demo Walkthrough

1. **Initial State:** The game initializes with a secret number (e.g., `55`) and the score starts at `100`.
2. **First Guess:** The user enters a guess of `40`. 
   * *Result:* The game correctly displays a "Too Low" hint, and the score decreases.
3. **Second Guess:** The user enters a guess of `70`. 
   * *Result:* The game correctly returns a "Too High" hint, and the score updates again.
4. **State Persistence:** The user clicks a UI element, triggering a Streamlit rerun; the current score and previous guess state are successfully preserved via Session State.
5. **Correct Guess:** The user inputs the correct guess of `55`. 
   * *Result:* The game displays a success message, tracks the final score accurately, and ends the game loop.


## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - A simple number guessing game where the player tries to guess a secret number and the app gives higher/lower feedback while tracking score.
- [x] Detail which bugs you found.
  - The secret number was resetting on each submit because it was not stored in Streamlit session state.
  - The hint logic was reversed, showing wrong higher/lower feedback.
  - The score update logic could be inconsistent when the guess was evaluated.
- [x] Explain what fixes you applied.
  - Stored the secret number and score in session state to persist across reruns.
  - Corrected the comparison logic so hints match the guess relative to the secret number.
  - Ensured score changes only happen when a valid guess is submitted.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the Streamlit app and enter a guess in the input box.
2. Click the "Submit" button to check the guess against the secret number.
3. The app displays whether the guess is too low, too high, or correct.
4. The score updates only when a valid guess is submitted, and the secret number remains the same across reruns.
5. When the guess is correct, the game shows a success message and the final score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
 python3 -m pytest tests/ -q
.........                                                                                                                                                                [100%]
9 passed in 0.01s
```



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

