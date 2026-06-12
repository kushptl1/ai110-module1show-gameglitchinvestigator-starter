# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? Game opened by and I was able to enter numbers to try to guess it. Played around with the diffulty and settings. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Inverse Hints it would say go higher when it was really lower and vice versa. 
  2. Attempts were wrong I got to 1 attempt left and the game was over. 
  3. Score was wrong, not understanding how the score if being kept. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  guess of 4  | go higher        |    go lower       📉 Go LOWER!
| attempts/wrong score |  Attempts left: 1.  | Didnt allow attempt | Out of attempts! The secret was 48. Score: -25 
|New Game| restart       |     Didnt restart   |  Game over. Start a new game to try again.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
