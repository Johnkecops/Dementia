#!/usr/bin/env python3
"""
Module: Math Is Easy — Streamlit Web Frontend
Purpose: Browser-based interactive mathematical quiz for dementia prevention.
         Replicates the four-panel layout described in Ivan et al. (2019) Fig 2–4.
Author: Jeremias Ivan, Rizky Nurdiansyah, Arli A. Parikesit
        Department of Bioinformatics, i3L University, Jakarta, Indonesia
Date: 2019 (original study); Streamlit port 2026
License: GNU General Public License v3.0
Usage:
    streamlit run app.py
References:
    Ivan J, Nurdiansyah R, Parikesit AA. Mathematical Problem Solving: One Way to
    Prevent Dementia. Iran J Med Inform. 2019; 8(1): e10.
    https://doi.org/10.30699/IJMI.V8I1.179
"""

import streamlit as st
from math_quiz_engine import QuizSession, DIFFICULTY_RANGES

# ── Page config ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="Math Is Easy — Dementia Prevention Quiz",
    page_icon="🧠",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Global font */
html, body, [class*="css"] { font-family: "Segoe UI", sans-serif; }

/* Equation display */
.equation-box {
    background: #111;
    color: #fff;
    font-size: 3rem;
    font-weight: 900;
    text-align: center;
    padding: 1.2rem 0.5rem;
    border-radius: 10px;
    letter-spacing: 0.05em;
    min-height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Answer entry display */
.entry-box {
    background: #fff;
    color: #111;
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
    padding: 0.7rem 0.5rem;
    border-radius: 8px;
    border: 2px solid #809dff;
    min-height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Score chips */
.score-chip {
    display: inline-block;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-weight: 700;
    font-size: 1.1rem;
    margin: 0.2rem;
}
.score-right { background: #2ecc71; color: white; }
.score-wrong { background: #e74c3c; color: white; }

/* Status bar */
.status-bar {
    background: #809dff;
    color: #fff;
    text-align: center;
    padding: 1rem;
    border-radius: 10px;
    font-size: 1.2rem;
    min-height: 70px;
}
.status-bar h2 { margin: 0; font-size: 1.8rem; }

/* Intro panel */
.intro-panel {
    background: #ccd8ff;
    padding: 1.2rem;
    border-radius: 10px;
    min-height: 200px;
}
.intro-panel h2 { color: #2c3e9e; margin-top: 0; }

/* Numpad buttons — override streamlit default */
div[data-testid="column"] button {
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    background-color: #809dff !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    width: 100% !important;
    height: 3rem !important;
    cursor: pointer;
}
div[data-testid="column"] button:hover {
    background-color: #5a7de0 !important;
}
/* Difficulty selected highlight */
.diff-active button { background-color: #2c3e9e !important; }

/* Feedback flash */
.feedback-correct {
    background: #d4edda; color: #155724;
    padding: 0.5rem 1rem; border-radius: 8px;
    text-align: center; font-weight: 700;
}
.feedback-wrong {
    background: #f8d7da; color: #721c24;
    padding: 0.5rem 1rem; border-radius: 8px;
    text-align: center; font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ── Session state initialisation ──────────────────────────────────────

def _init_state() -> None:
    defaults = {
        "game_state":  "idle",      # idle | playing | finished
        "difficulty":  "",
        "session":     None,
        "user_input":  "",
        "feedback":    "",          # "" | "correct" | "wrong"
        "status_msg":  "",
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

_init_state()

# ── Convenience aliases ───────────────────────────────────────────────
ss = st.session_state

# ── Callback helpers ──────────────────────────────────────────────────

def cb_set_difficulty(diff: str) -> None:
    ss.difficulty = diff
    ss.game_state = "idle"
    ss.user_input = ""
    ss.feedback   = ""
    ss.session    = None
    ss.status_msg = f"Difficulty set to **{diff.capitalize()}**. Press START."


def cb_start() -> None:
    if ss.difficulty not in DIFFICULTY_RANGES:
        ss.status_msg = "⚠️ Choose a difficulty first, then press START."
        return
    ss.session    = QuizSession(ss.difficulty)
    ss.game_state = "playing"
    ss.user_input = ""
    ss.feedback   = ""
    ss.status_msg = ss.difficulty.capitalize()


def cb_press(value: str) -> None:
    if ss.game_state != "playing":
        return
    if value == "-":
        if ss.user_input == "":
            ss.user_input = "-"
    else:
        ss.user_input += value
    ss.feedback = ""


def cb_delete() -> None:
    ss.user_input = ss.user_input[:-1]
    ss.feedback   = ""


def cb_submit() -> None:
    if ss.game_state != "playing" or ss.session is None:
        return
    if ss.user_input in ("", "-"):
        return
    try:
        answer = int(ss.user_input)
    except ValueError:
        ss.user_input = ""
        return

    correct = ss.session.submit_answer(answer)
    ss.user_input = ""

    if correct:
        ss.feedback = "correct"
        if ss.session.finished:
            ss.game_state = "finished"
            ss.status_msg = (
                f"🎉 Good Job!  Your calculation time: **{ss.session.elapsed} seconds**  "
                f"— Keep practicing!"
            )
        else:
            ss.status_msg = ss.difficulty.capitalize()
    else:
        ss.feedback = "wrong"


def cb_reset() -> None:
    for key in ("game_state", "difficulty", "session", "user_input", "feedback", "status_msg"):
        del st.session_state[key]
    _init_state()


# ══════════════════════════════════════════════════════════════════════
# Layout
# ══════════════════════════════════════════════════════════════════════

st.title("🧠 Math Is Easy")
st.caption(
    "A mathematical quiz for cognitive training — helping reduce the risk of dementia. "
    "Based on: Ivan J, Nurdiansyah R, Parikesit AA. *Iran J Med Inform.* 2019; 8(1): e10."
)
st.divider()

# ── Three-column upper panel ──────────────────────────────────────────
col_left, col_mid, col_right = st.columns([2, 2, 2], gap="medium")

# ────────────────────────────────────────────────
# UPPER-LEFT: intro + difficulty selection
# ────────────────────────────────────────────────
with col_left:
    st.markdown("""
<div class="intro-panel">
<h2>Welcome!</h2>
<p>Each round has <strong>5 problems</strong> — addition, subtraction, or multiplication
between two numbers. No time limit, so go at your own pace.</p>
<p>Choose a difficulty, press <strong>START</strong>, and use the numpad to type your answer.</p>
<hr/>
<p><em>Easy</em> &nbsp;— numbers 0 to 10<br/>
<em>Medium</em> — numbers 11 to 20<br/>
<em>Hard</em> &nbsp;— numbers 21 to 30</p>
</div>
""", unsafe_allow_html=True)

    st.write("")
    st.markdown("**Select difficulty:**")
    d1, d2, d3 = st.columns(3)
    with d1:
        if st.button("Easy",   use_container_width=True, key="btn_easy"):
            cb_set_difficulty("easy")
            st.rerun()
    with d2:
        if st.button("Medium", use_container_width=True, key="btn_medium"):
            cb_set_difficulty("medium")
            st.rerun()
    with d3:
        if st.button("Hard",   use_container_width=True, key="btn_hard"):
            cb_set_difficulty("hard")
            st.rerun()

    if ss.difficulty:
        st.info(f"Selected: **{ss.difficulty.capitalize()}**")

# ────────────────────────────────────────────────
# UPPER-MIDDLE: equation + score + controls
# ────────────────────────────────────────────────
with col_mid:
    # Equation display
    if ss.game_state == "playing" and ss.session:
        eq_text = ss.session.equation_str
    elif ss.game_state == "finished":
        eq_text = "✓ Done!"
    else:
        eq_text = ""

    st.markdown(f'<div class="equation-box">{eq_text}</div>', unsafe_allow_html=True)
    st.write("")

    # Score display
    right_n = ss.session.right if ss.session else 0
    wrong_n = ss.session.wrong if ss.session else 0
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown(
            f'<div class="score-chip score-right">✔ Right: {right_n}</div>',
            unsafe_allow_html=True,
        )
    with sc2:
        st.markdown(
            f'<div class="score-chip score-wrong">✘ Wrong: {wrong_n}</div>',
            unsafe_allow_html=True,
        )

    st.write("")

    # Progress bar
    if ss.session:
        progress = ss.session.iteration / 5
        st.progress(progress, text=f"Question {min(ss.session.iteration + 1, 5)} of 5")

    st.write("")

    # START / RESET buttons
    ctrl1, ctrl2 = st.columns(2)
    with ctrl1:
        if st.button("▶ START", use_container_width=True, key="btn_start"):
            cb_start()
            st.rerun()
    with ctrl2:
        if st.button("↺ RESET", use_container_width=True, key="btn_reset"):
            cb_reset()
            st.rerun()

# ────────────────────────────────────────────────
# UPPER-RIGHT: answer entry + numpad
# ────────────────────────────────────────────────
with col_right:
    # Answer display box
    entry_display = ss.user_input if ss.user_input else "—"
    st.markdown(
        f'<div class="entry-box">{entry_display}</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    # Feedback flash
    if ss.feedback == "correct":
        st.markdown('<div class="feedback-correct">✔ Correct! Next question...</div>',
                    unsafe_allow_html=True)
    elif ss.feedback == "wrong":
        st.markdown('<div class="feedback-wrong">✘ Wrong answer — try again.</div>',
                    unsafe_allow_html=True)

    st.write("")
    st.markdown("**Numpad:**")

    # Row 1: 1 2 3  |  −
    r1a, r1b, r1c, r1d = st.columns([1, 1, 1, 1])
    with r1a:
        if st.button("1", use_container_width=True, key="n1"): cb_press("1"); st.rerun()
    with r1b:
        if st.button("2", use_container_width=True, key="n2"): cb_press("2"); st.rerun()
    with r1c:
        if st.button("3", use_container_width=True, key="n3"): cb_press("3"); st.rerun()
    with r1d:
        if st.button("−", use_container_width=True, key="nminus"): cb_press("-"); st.rerun()

    # Row 2: 4 5 6  |  Del
    r2a, r2b, r2c, r2d = st.columns([1, 1, 1, 1])
    with r2a:
        if st.button("4", use_container_width=True, key="n4"): cb_press("4"); st.rerun()
    with r2b:
        if st.button("5", use_container_width=True, key="n5"): cb_press("5"); st.rerun()
    with r2c:
        if st.button("6", use_container_width=True, key="n6"): cb_press("6"); st.rerun()
    with r2d:
        if st.button("⌫ Del", use_container_width=True, key="ndel"): cb_delete(); st.rerun()

    # Row 3: 7 8 9  |  Enter
    r3a, r3b, r3c, r3d = st.columns([1, 1, 1, 1])
    with r3a:
        if st.button("7", use_container_width=True, key="n7"): cb_press("7"); st.rerun()
    with r3b:
        if st.button("8", use_container_width=True, key="n8"): cb_press("8"); st.rerun()
    with r3c:
        if st.button("9", use_container_width=True, key="n9"): cb_press("9"); st.rerun()
    with r3d:
        if st.button("✔ Enter", use_container_width=True, key="nenter"): cb_submit(); st.rerun()

    # Row 4: 0 (wide)
    r4a, r4b = st.columns([3, 1])
    with r4a:
        if st.button("0", use_container_width=True, key="n0"): cb_press("0"); st.rerun()
    # r4b intentionally empty to keep layout proportional

# ── Bottom status bar ─────────────────────────────────────────────────
st.divider()
if ss.status_msg:
    st.markdown(
        f'<div class="status-bar">{ss.status_msg}</div>',
        unsafe_allow_html=True,
    )
elif ss.game_state == "idle" and not ss.difficulty:
    st.markdown(
        '<div class="status-bar">Select a difficulty level and press START to begin.</div>',
        unsafe_allow_html=True,
    )

# ── Keyboard input support (text box shortcut) ────────────────────────
st.divider()
with st.expander("⌨️ Keyboard input (alternative to numpad)", expanded=False):
    st.write("Type your answer here and press Enter:")
    kb_val = st.text_input("Answer", key="keyboard_input", label_visibility="collapsed")
    if st.button("Submit via keyboard", key="kb_submit"):
        if kb_val.strip():
            ss.user_input = kb_val.strip()
            cb_submit()
            st.rerun()

# ── Citation footer ───────────────────────────────────────────────────
st.write("")
st.caption(
    "**Citation:** Ivan J, Nurdiansyah R, Parikesit AA. Mathematical Problem Solving: "
    "One Way to Prevent Dementia. *Iran J Med Inform.* 2019; 8(1): e10. "
    "https://doi.org/10.30699/IJMI.V8I1.179  |  "
    "Department of Bioinformatics, i3L University, Jakarta, Indonesia"
)
