# **Tic-Tac-Toe AI with GUI (Prompt Engineering Project) 🎮🤖**

## **📌 Overview**  
This is an **AI-powered Tic-Tac-Toe game with a graphical user interface (GUI)**, created through **prompt engineering** with ChatGPT. The AI can play at **Easy, Medium, and Hard** difficulty levels, and the game features a **restart button** for continuous play.  

## **🛠️ Technologies Used**
- **Python**
- **Tkinter (for GUI)**
- **Minimax Algorithm (for AI)**
- **Randomized AI (for difficulty levels)**  

---

## **🎯 Goal of the Project**  
This project was created as a **learning exercise in prompt engineering**, where I explored how to:  
✅ **Guide AI-generated development** through structured prompts.  
✅ **Iteratively improve AI-generated code** with targeted refinements.  
✅ **Balance AI automation with manual decision-making** in development.  

Rather than writing the code myself, I used **carefully crafted prompts** to get ChatGPT to generate and refine the code **step by step**. This allowed me to learn how to leverage **AI as a development assistant** effectively.

---

## **🚀 Features**  
✅ **Playable Tic-Tac-Toe game** (Player vs. AI).  
✅ **Graphical interface with interactive buttons**.  
✅ **Three AI difficulty levels**:  
   - **Easy** → AI makes **many mistakes**.  
   - **Medium** → AI plays well but is **beatable**.  
   - **Hard** → AI is **unbeatable** (Minimax Algorithm).  
✅ **AI moves automatically** after the player.  
✅ **"Restart Game" button** to play multiple rounds.  

---

## **🎨 How It Works**  
1️⃣ **Player clicks a button** to place `"X"`.  
2️⃣ **AI makes a move** (based on difficulty level).  
3️⃣ **Game detects a win, draw, or continues**.  
4️⃣ **Player can restart the game anytime** with a button.  

---
 

ChatGPT created a very simple interface with tkinter:  

![Tic-Tac-Toe Screenshot](https://raw.githubusercontent.com/l-white/prompt-game/main/images/game-with-tkinter.png)


---

## **💡 Prompt Engineering Section**  
Below are some of the key prompts I used to develop this project step by step:

### **1️⃣ Building the Basic Game Logic**  
```plaintext
What are the steps to creating a tic-tac-toe game with Python?
```
✅ This generated a **basic text-based Tic-Tac-Toe game**.

### **2️⃣ Adding an AI Opponent**  
```plaintext
What would be the steps to create this game except the computer is the opponent?
```
✅ This added **basic AI that played randomly**.

### **3️⃣ Making the AI Smarter**  
```plaintext
What are the steps to making the computer smarter?
```
✅ AI now **blocks winning moves and tries to win when possible**.

### **4️⃣ Implementing an Unbeatable AI**  
```plaintext
Could you please detail the steps to create a perfect unbeatable AI opponent using the Minimax Algorithm?
```
✅ AI now **uses Minimax** to always win or force a draw.

### **5️⃣ Making the AI More Human-Like**  
```plaintext
Could you please outline the steps to create an AI opponent that sometimes makes mistakes?
```
✅ Introduced **Easy, Medium, and Hard** difficulty levels.

### **6️⃣ Creating a GUI**  
```plaintext
For the easy, medium, and hard game, it is a really interesting idea to add a GUI version. Could you please outline the steps you'd take to accomplish this?
```
✅ **Built a GUI with Tkinter** to replace text-based input.

### **7️⃣ Adding a Restart Button**  
```plaintext
What are the steps for adding a Restart button?
```
✅ Players can now **restart the game without restarting the app**.

This structured approach to **prompt engineering** allowed me to build the game **iteratively**, improving and refining it based on AI-generated responses.

To show the iterations, I have kept all versions of the game. choose-evel-with-gui.py is the current final version of the game.

---

## **💻 Installation & Running the Game**  
### **1️⃣ Install Python (if not installed)**  
You need Python installed on your machine. Download it from:  
🔗 [Python Official Site](https://www.python.org/downloads/)

### **2️⃣ Run the game**  
Clone the repository and run the script:  
```bash
git clone https://github.com/l-white/prompt-game.git
cd prompt-game
python3 choose-level-with-gui.py
```

---

## **🔮 Possible Future Improvements**  
Here are some potential next steps for enhancement:  
🔥 **Scoreboard** – Track wins/losses.  
🎶 **Sound Effects** – Add clicks and win/loss sounds.  
🌍 **Multiplayer Mode** – Play against another human.  
✨ **Animations** – Make the UI more dynamic.  

---

## **📖 Lessons Learned**  
### **🔹 Prompt Engineering**  
- **Breaking down the project** into step-by-step prompts improved AI output.  
- **Refining AI-generated code** through structured requests led to high-quality results.  
- **Iterative development** with AI required critical thinking and debugging.  

### **🔹 AI-Assisted Coding**  
- AI is great at generating **boilerplate code** quickly.  
- However, **manual debugging & optimization** were still necessary.  
- AI **doesn’t always get things right on the first try**, but **good prompts** help refine results.  
- AI does a much better job when it is asked to outline the steps prior to execution.

---

## **📝 Acknowledgments**  
This project was built **entirely using prompt engineering** with **ChatGPT**.  
I guided the AI through structured prompts, testing, debugging, and iterating **to improve the code step by step**.  

💡 **This project was an experiment in leveraging AI as a coding assistant rather than writing the code manually.**  

---

## **🎯 Final Thoughts**  
This project was an **amazing learning experience in prompt engineering** and **AI-assisted coding**.  
It demonstrated how **AI can be used effectively as a development tool** while still requiring human oversight and refinement.

---

