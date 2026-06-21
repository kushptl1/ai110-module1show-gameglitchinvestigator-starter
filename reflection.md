# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? Game opened by and I was able to enter numbers to try to guess it. Played around with the diffulty and settings. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hint system was inverted: it told me to go higher when the secret number was actually lower, and vice versa.
  2. The attempt counter stopped early; the game ended even though I still had one guess remaining.
  3. The score calculation was incorrect, and I couldn't tell how the game was tracking points.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  guess of 4  | go higher        |    go lower       📉 Go LOWER!
| attempts/wrong score |  Attempts left: 1.  | Didnt allow attempt | Out of attempts! The secret was 48. Score: -25 
|New Game| restart       |     Didnt restart   |  Game over. Start a new game to try again.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
1. ChatGPT

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
1. AI was able to fix the check_guess function easily and tested with pytest and passed all test cases. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
1. AI had created mutiple test files for pytest and ran the wrong ones since I had worked on it different days. Once i relized there was mutiple files I figured it out and deleted the old test and ran the correct pytest file. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Ran the pytest and lauched the streamlit again to see it live. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  1. The check_guess function showed me the logic was wrong and needed to be fixed. It was orginally giving inverse hints but was able to fix it with few test cases. 

- Did AI help you design or understand any tests? How?
1. Yes, it created the test cases on ask and able to run them without any issues to show if code worked. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
 1. Any user interaction in Streamlit triggers a complete rerun of your entire Python script from top to bottom. Because the script completely restarts, it loses its memory and forgets previous variable values (like a running game score). Session State acts as a built-in notepad, saving key details across reruns so your app always remembers where it left off.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  1. A strategy from this project I want to reuse is breaking down my prompts into specific, isolated tasks for individual chat sessions rather than feeding the AI an entire codebase at once. Combining this focused prompting with immediate pytest generation allowed me to quickly verify logic fixes in my terminal before moving on to the next bug

- What is one thing you would do differently next time you work with AI on a coding task?
1. When using a virtual environment, instead of having the AI try to run test cases to see if they worked, I have to run them in my own session. This is because the repositories and environment state might not all be loaded into the AI's session.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
1. This project showed me that while AI is incredibly fast at generating test cases and pinpointing complex logic bugs, it can't operate in a vacuum. It changed the way I look at AI-generated code by proving that an LLM is a powerful drafting tool, but a human engineer is still entirely responsible for managing the actual environment and verifying the fixes. 
