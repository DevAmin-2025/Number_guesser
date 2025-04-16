# Number Guesser Game
Welcome to the Number Guesser Game.

## Introduction
The game generates a random number between 1 and 100, and the user is prompted to guess this number. For each incorrect guess, the user receives a hint and their score is reduced.
The initial score is 100 and every time that the user inputs a wrong guess 10 score will be reduced. The game will continue until the user guesses the correct number or the user's score hit ZERO.

## Game Rules
1. The game selects a random number within the range of 0 to 100.
2. The player has a limited number of attempts to guess the correct number.
3. After each guess, the game provides feedback:
    - "Too High" if the guess is higher than the number.
    - "Too Low" if the guess is lower than the number.
4. The game continues until the player guesses the number or runs out of score.

## How to Run
To run the game locally, follow these steps:

1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

1. Navigate to the main project directory.
```bash
cd Number_guesser
```

2. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
3. Install any necessary dependencies:
```bash
pip install -r requirements.txt
```
Follow the on-screen prompts to play the game.
