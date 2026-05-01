#!/usr/bin/env python3
"""
Module: Math Is Easy — Tkinter GUI
Purpose: Interactive mathematical quiz for dementia prevention cognitive training.
         GUI frontend for math_quiz_engine.QuizSession.
Author: Jeremias Ivan, Rizky Nurdiansyah, Arli A. Parikesit
        Department of Bioinformatics, i3L University, Jakarta, Indonesia
Date: 2019 (original); refactored 2026
License: GNU General Public License v3.0
References:
    Ivan J, Nurdiansyah R, Parikesit AA. Mathematical Problem Solving: One Way to
    Prevent Dementia. Iran J Med Inform. 2019; 8(1): e10.
    https://doi.org/10.30699/IJMI.V8I1.179
"""

from tkinter import Tk, Label, Button, IntVar, StringVar, W, E, N, S
from math_quiz_engine import QuizSession, DIFFICULTY_RANGES

# ── Colour palette ────────────────────────────────────────────────────
BG_INTRO  = "#ccd8ff"
BG_PANEL  = "#809dff"
BG_DARK   = "black"
FG_LIGHT  = "white"

FONT_TITLE  = ("Comic Sans MS", 20, "bold")
FONT_BODY   = ("Comic Sans MS", 12)
FONT_SCORE  = ("Comic Sans MS", 10)
FONT_EQ     = ("Cambria Math", 30, "bold")
FONT_ENTRY  = ("Arial", 20, "bold")
FONT_BTN    = ("Arial", 18, "bold")
FONT_SMBTN  = ("Arial", 13, "bold")
FONT_LVLBTN = ("Arial", 11, "bold")

DIFFICULTY_HINT = (
    "Easy:   numbers 0 – 10\n"
    "Medium: numbers 11 – 20\n"
    "Hard:   numbers 21 – 30"
)


class MathApp:
    """Tkinter GUI for the Math Is Easy quiz."""

    def __init__(self, master: Tk) -> None:
        self.master = master
        master.title("Math Is Easy")
        master.resizable(False, False)

        # ── Internal state ────────────────────────────────────────────
        self._session: QuizSession | None = None
        self._difficulty: str = ""
        self._nentry: str = ""       # current typed digits

        # ── StringVar / IntVar for reactive labels ────────────────────
        self._equation_var  = StringVar(value="")
        self._entry_var     = StringVar(value="")
        self._right_var     = IntVar(value=0)
        self._wrong_var     = IntVar(value=0)
        self._status1_var   = StringVar(value="")
        self._status2_var   = StringVar(value="")

        self._build_ui()

    # ══════════════════════════════════════════════════════════════════
    # UI construction
    # ══════════════════════════════════════════════════════════════════

    def _build_ui(self) -> None:
        m = self.master

        # ── Spacer rows / columns ─────────────────────────────────────
        for col in (0, 5, 10, 15):
            Label(m, text="", width=2, bg=BG_INTRO).grid(row=0, column=col, rowspan=6, sticky=W+E+N+S)
        Label(m, text="", bg=BG_INTRO).grid(row=0, column=0, columnspan=16, sticky=W+E+N+S)
        Label(m, text="", bg=BG_INTRO).grid(row=6, column=0, columnspan=16, sticky=W+E+N+S)
        Label(m, text="", bg=BG_PANEL).grid(row=7, column=0, columnspan=16, sticky=W+E+N+S)

        # ── Upper-left: intro ─────────────────────────────────────────
        Label(m, text="\nMath Is Easy",
              font=FONT_TITLE, justify="center", bg=BG_INTRO
              ).grid(row=1, column=1, columnspan=4, sticky=W+E+N+S)

        Label(m, text=(
                "In this quiz, there will be 5 problems\n"
                "per round — addition, subtraction,\n"
                "or multiplication between two numbers.\n\n"
                "Happy calculating!"
              ), justify="center", font=FONT_BODY, bg=BG_INTRO
              ).grid(row=2, column=1, columnspan=4, rowspan=3, sticky=W+E+N+S)

        # ── Upper-middle: equation + scoreboard ───────────────────────
        Label(m, textvariable=self._equation_var,
              width=13, justify="center", font=FONT_EQ, bg=BG_DARK, fg=FG_LIGHT
              ).grid(row=1, column=6, columnspan=4, rowspan=3, sticky=W+E+N+S)

        Label(m, text="Right:", font=FONT_SCORE, bg=BG_DARK, fg=FG_LIGHT
              ).grid(row=4, column=6, sticky=W+E+N+S)
        Label(m, textvariable=self._right_var, font=FONT_SCORE, bg=BG_DARK, fg=FG_LIGHT
              ).grid(row=4, column=7, sticky=W+E+N+S)
        Label(m, text="Wrong:", font=FONT_SCORE, bg=BG_DARK, fg=FG_LIGHT
              ).grid(row=4, column=8, sticky=W+E+N+S)
        Label(m, textvariable=self._wrong_var, font=FONT_SCORE, bg=BG_DARK, fg=FG_LIGHT
              ).grid(row=4, column=9, sticky=W+E+N+S)

        # ── Upper-right: answer entry display + numpad ────────────────
        Label(m, textvariable=self._entry_var,
              font=FONT_ENTRY, justify="center", bg="white"
              ).grid(row=1, column=11, columnspan=4, sticky=W+E+N+S)

        self._minus_btn = Button(m, text="-", font=FONT_BTN, width=4,
                                  bg=BG_PANEL, command=lambda: self._press("-"))
        self._minus_btn.grid(row=2, column=14, sticky=W+E+N+S)

        numpad = [(1,2,11),(2,2,12),(3,2,13),
                  (4,3,11),(5,3,12),(6,3,13),
                  (7,4,11),(8,4,12),(9,4,13)]
        for val, row, col in numpad:
            Button(m, text=str(val), font=FONT_BTN, width=3, bg=BG_PANEL,
                   command=lambda v=val: self._press(v)
                   ).grid(row=row, column=col, sticky=W+E+N+S)

        Button(m, text="0", font=FONT_BTN, bg=BG_PANEL,
               command=lambda: self._press(0)
               ).grid(row=5, column=11, columnspan=3, sticky=W+E+N+S)

        Button(m, text="Del", font=FONT_SMBTN, bg=BG_PANEL,
               command=lambda: self._action("delete")
               ).grid(row=3, column=14, sticky=W+E+N+S)

        Button(m, text="Enter", font=FONT_SMBTN, bg=BG_PANEL,
               command=lambda: self._action("submit")
               ).grid(row=4, column=14, rowspan=2, sticky=W+E+N+S)

        # ── Middle controls: START / RESET ────────────────────────────
        Button(m, text="START", font=FONT_SMBTN, bg=BG_PANEL,
               command=self._start
               ).grid(row=5, column=6, columnspan=2, sticky=W+E+N+S)

        Button(m, text="RESET", font=FONT_SMBTN, bg=BG_PANEL,
               command=self._reset
               ).grid(row=5, column=8, columnspan=2, sticky=W+E+N+S)

        # ── Difficulty buttons ────────────────────────────────────────
        for label, col in (("Easy", 1), ("Medium", 2), ("Hard", 3), ("?", 4)):
            Button(m, text=label, font=FONT_LVLBTN, width=4, bg=BG_PANEL,
                   command=lambda l=label: self._set_difficulty(l)
                   ).grid(row=5, column=col, sticky=W+E+N+S)

        # ── Bottom status row ─────────────────────────────────────────
        Label(m, textvariable=self._status1_var,
              font=("Comic Sans MS", 20), justify="center", bg=BG_PANEL
              ).grid(row=8, column=0, columnspan=16, sticky=W+E+N+S)
        Label(m, textvariable=self._status2_var,
              font=FONT_BODY, justify="center", bg=BG_PANEL
              ).grid(row=9, column=0, columnspan=16, sticky=W+E+N+S)

    # ══════════════════════════════════════════════════════════════════
    # Event handlers
    # ══════════════════════════════════════════════════════════════════

    def _set_difficulty(self, label: str) -> None:
        if label == "?":
            self._status1_var.set("Description")
            self._status2_var.set(DIFFICULTY_HINT)
            return

        self._difficulty = label.lower()
        self._status1_var.set(label)
        self._status2_var.set("")
        self._clear_scores()
        self._equation_var.set("")
        self._clear_entry()

    def _start(self) -> None:
        if self._difficulty not in DIFFICULTY_RANGES:
            self._status1_var.set("Choose difficulty first!")
            return
        self._session = QuizSession(self._difficulty)
        self._equation_var.set(self._session.equation_str)
        self._clear_entry()
        self._clear_scores()
        self._status1_var.set(self._difficulty.capitalize())
        self._status2_var.set("")

    def _press(self, value: int | str) -> None:
        if value == "-":
            if self._nentry == "":       # only allow leading minus
                self._nentry = "-"
        else:
            self._nentry += str(value)
        self._entry_var.set(self._nentry)

    def _action(self, method: str) -> None:
        if method == "delete":
            self._nentry = self._nentry[:-1]
            self._entry_var.set(self._nentry)

        elif method == "submit":
            if self._session is None or self._session.finished:
                return
            if self._nentry in ("", "-"):
                return
            try:
                answer = int(self._nentry)
            except ValueError:
                self._clear_entry()
                return

            correct = self._session.submit_answer(answer)
            self._right_var.set(self._session.right)
            self._wrong_var.set(self._session.wrong)
            self._clear_entry()

            if self._session.finished:
                self._equation_var.set("")
                self._status1_var.set("Good Job!")
                self._status2_var.set(
                    f"Your calculation time: {self._session.elapsed} seconds\n"
                    "Keep practicing!"
                )
            elif correct:
                self._equation_var.set(self._session.equation_str)
            # wrong answer: keep same equation, user tries again

        elif method == "reset":
            self._session = None
            self._difficulty = ""
            self._equation_var.set("")
            self._status1_var.set("")
            self._status2_var.set("")
            self._clear_scores()
            self._clear_entry()

    def _reset(self) -> None:
        self._action("reset")

    # ── Helpers ───────────────────────────────────────────────────────

    def _clear_entry(self) -> None:
        self._nentry = ""
        self._entry_var.set("")

    def _clear_scores(self) -> None:
        self._right_var.set(0)
        self._wrong_var.set(0)


# ── Entry point ───────────────────────────────────────────────────────

if __name__ == "__main__":
    root = Tk()
    MathApp(root)
    root.mainloop()
