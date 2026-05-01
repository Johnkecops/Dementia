#!/usr/bin/env python3
"""
Module: Math Quiz Engine for Dementia Prevention
Purpose: Core game logic — number generation (NUMBER), equation calculation (EQUATION),
         and session management (MAIN) as described in the pseudocode of Ivan et al. (2019).
Author: Jeremias Ivan, Rizky Nurdiansyah, Arli A. Parikesit
        Department of Bioinformatics, i3L University, Jakarta, Indonesia
Date: 2019 (original); updated 2026
References:
    Ivan J, Nurdiansyah R, Parikesit AA. Mathematical Problem Solving: One Way to
    Prevent Dementia. Iran J Med Inform. 2019; 8(1): e10.
    https://doi.org/10.30699/IJMI.V8I1.179
"""

import random
import time

DIFFICULTY_RANGES: dict[str, tuple[int, int]] = {
    "easy":   (0,  10),
    "medium": (11, 20),
    "hard":   (21, 30),
}

OPERATORS = ["+", "-", "*"]
MAX_QUESTIONS = 5


def generate_numbers(difficulty: str) -> tuple[int, str, int]:
    """NUMBER procedure: randomize two operands and an operator for the given difficulty."""
    if difficulty not in DIFFICULTY_RANGES:
        raise ValueError(f"difficulty must be one of {list(DIFFICULTY_RANGES)}")
    lo, hi = DIFFICULTY_RANGES[difficulty]
    n1 = random.randint(lo, hi)
    n2 = random.randint(lo, hi)
    symbol = random.choice(OPERATORS)
    return n1, symbol, n2


def calculate_equation(n1: int, symbol: str, n2: int) -> int:
    """EQUATION procedure: compute the correct answer for (n1 symbol n2)."""
    if symbol == "+":
        return n1 + n2
    elif symbol == "-":
        return n1 - n2
    elif symbol == "*":
        return n1 * n2
    raise ValueError(f"Unknown operator: {symbol}")


class QuizSession:
    """
    MAIN procedure encapsulated as a stateful session.

    Lifecycle:
        session = QuizSession("easy")
        while not session.finished:
            correct = session.submit_answer(user_int)
        print(session.right, session.wrong, session.elapsed)
    """

    def __init__(self, difficulty: str) -> None:
        if difficulty not in DIFFICULTY_RANGES:
            raise ValueError(f"difficulty must be one of {list(DIFFICULTY_RANGES)}")
        self.difficulty = difficulty
        self.right = 0
        self.wrong = 0
        self.iteration = 0        # x in pseudocode — counts correct answers
        self.start_time = time.time()
        self.elapsed = 0.0
        self.finished = False
        self._new_question()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _new_question(self) -> None:
        self.n1, self.symbol, self.n2 = generate_numbers(self.difficulty)
        self.correct_answer = calculate_equation(self.n1, self.symbol, self.n2)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def equation_str(self) -> str:
        """Human-readable equation, e.g. '7 × 6'."""
        display = {"*": "×", "+": "+", "-": "-"}
        return f"{self.n1} {display[self.symbol]} {self.n2}"

    def submit_answer(self, user_answer: int) -> bool:
        """
        Submit the user's answer.
        Returns True if correct, False if wrong.
        When iteration reaches MAX_QUESTIONS after a correct answer, sets finished=True.
        """
        if self.finished:
            return False

        if user_answer == self.correct_answer:
            self.right += 1
            self.iteration += 1
            if self.iteration >= MAX_QUESTIONS:
                self.elapsed = round(time.time() - self.start_time, 2)
                self.finished = True
            else:
                self._new_question()
            return True
        else:
            self.wrong += 1
            return False
