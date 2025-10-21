# 🏓 Ping Pong Game

A classic **two-player Ping Pong (Pong) game** built in **Python** using the `turtle` graphics module.
Play against a friend and keep score as the ball bounces faster and faster with each hit!

---

## 🎮 Features

* **Two-player gameplay**

  * Right paddle: control with `Up` / `Down`
  * Left paddle: control with `W` / `S`
* **Ball physics** with realistic bouncing mechanics.
* **Scoreboard** automatically updates when a player scores.
* **Progressive difficulty** — the ball speeds up with every paddle hit.
* **Smooth gameplay** using `turtle.Screen.tracer()` and `update()` for efficient rendering.

---

## 🧩 Project Structure

```
📁 ping_pong_game
├── main.py           # Main game loop and screen setup
├── paddle.py         # Right paddle class (arrow keys)
├── otherPaddle.py    # Left paddle class (W/S keys)
├── ball.py           # Ball physics, bouncing logic, and speed control
├── scoreBoard.py     # Score display and update logic
└── README.md         # Documentation (this file)
```

---

## ⚙️ How to Run

1. **Install Python 3.7+**
   You can verify your installation:

   ```bash
   python --version
   ```

2. **Clone the repository**

   ```bash
   git clone https://github.com/YossiKaminsky/ping_pong_game.git
   cd ping_pong_game
   ```

3. **Run the game**

   ```bash
   python main.py
   ```

---

## 🕹️ Controls

| Player          |   Move Up   |   Move Down   |
| :-------------- | :---------: | :-----------: |
| 🧑 Right Paddle | ⬆️ Up Arrow | ⬇️ Down Arrow |
| 🧑 Left Paddle  |    **W**    |     **S**     |

---

## 🧠 How It Works

* The **`Paddle`** and **`OtherPaddle`** classes handle user-controlled paddles using keyboard events.
* The **`Ball`** class moves across the screen, bounces off walls and paddles, and accelerates after each hit.
* The **`ScoreBoard`** class displays and updates player scores on screen.
* The **`main.py`** file coordinates all components, runs the game loop, and checks for scoring events.

---

## 🏆 Future Enhancements

* Add AI for single-player mode.
* Introduce sound effects on paddle hits and scoring.
* Add a start menu and difficulty settings.
* Implement pause/resume functionality.

---

Would you like me to add a **preview GIF/image** section (so that the README looks visual on GitHub)? I can generate a placeholder image for the gameplay if you want.
