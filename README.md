# Knights and Knaves Logic Solver

This project solves logic puzzles involving characters who are either **knights** (always tell the truth) or **knaves** (always lie). The program models these puzzles using **propositional logic** and applies **model checking** to deduce which characters are knights and which are knaves.

---

## Problem Description

In each puzzle, you're given statements made by characters. Each character is either a knight or a knave — never both.

For example:
> A says, “We are both knaves.”

Using logic, we determine what roles are possible for each character such that all statements are consistent with the rules of knights and knaves.

---

## Concepts Used

- Propositional Logic
- Logical Connectives (AND, OR, NOT, Implication, Biconditional)
- Knowledge Bases
- Model Checking
- Constraint Satisfaction

---

## File Structure

knights/
logic.py # Logic expression and model-checking framework
knights.py # Definitions of puzzles and their logical modeling
README.md # Project documentation


---

## How to Run with python3

```bash
python3 knights.py
```

## How to Run with python

```bash
python knights.py
```

Puzzle 0
    A is a Knight

Puzzle 1
    A is a Knave
    B is a Knight

Puzzle 2
    A is a Knight
    B is a Knave
    C is a Knave

Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight




