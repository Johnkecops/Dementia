# Math Is Easy — Mathematical Quiz for Dementia Prevention

A cognitive-training application derived from the peer-reviewed study:

> Ivan J, Nurdiansyah R, Parikesit AA. **Mathematical Problem Solving: One Way to Prevent Dementia.**  
> *Iranian Journal of Medical Informatics.* 2019; 8(1): e10.  
> https://doi.org/10.30699/IJMI.V8I1.179

Department of Bioinformatics, School of Life Sciences,  
Indonesia International Institute for Life Sciences (i3L), Jakarta, Indonesia.

---

## Background

Dementia is a progressive syndrome affecting millions worldwide, with no effective cure. Previous studies show that cognitive activities — including mathematical problem solving — can slow cognitive decline. This application provides a simple, interactive arithmetic quiz to serve as a regular mental exercise, particularly for older adults.

---

## Repository Structure

```
Dementia-main/
├── math_quiz_engine.py   # Core logic: NUMBER, EQUATION, MAIN procedures (pseudocode → Python)
├── Trial_2.py            # Tkinter desktop GUI (updated to use engine)
├── app.py                # Streamlit web frontend
├── requirements.txt      # Python dependencies
├── LICENSE               # GNU General Public License v3.0
└── README.md             # This file
```

---

## How It Works

The program implements three procedures described in the original pseudocode:

| Procedure | Role |
|-----------|------|
| **NUMBER** | Randomly generates two operands and an operator (+, −, ×) within difficulty-specific ranges |
| **EQUATION** | Calculates the correct answer for the generated equation |
| **MAIN** | Manages a round of 5 questions, tracks right/wrong answers, measures calculation time |

### Difficulty Levels

| Level  | Number Range |
|--------|-------------|
| Easy   | 0 – 10      |
| Medium | 11 – 20     |
| Hard   | 21 – 30     |

Each round consists of exactly **5 questions**. The user must answer correctly to advance; wrong answers keep the same question active. Calculation time is recorded at round end.

---

## Installation

Python ≥ 3.10 required.

```bash
pip install streamlit
```

Tkinter ships with standard Python distributions (no extra install on most systems). If missing:

```bash
# Debian/Ubuntu
sudo apt install python3-tk
# macOS (Homebrew)
brew install python-tk
```

---

## Usage

### Streamlit Web App (recommended)

```bash
streamlit run app.py
```

Opens in your default browser at `http://localhost:8501`.

### Tkinter Desktop App

```bash
python Trial_2.py
```

### Engine (programmatic use)

```python
from math_quiz_engine import QuizSession

session = QuizSession("easy")
while not session.finished:
    print(session.equation_str)
    answer = int(input("Your answer: "))
    correct = session.submit_answer(answer)
    print("Correct!" if correct else "Wrong, try again.")

print(f"Right: {session.right}  Wrong: {session.wrong}  Time: {session.elapsed}s")
```

---

## Application Layout

The UI mirrors the four-panel layout described in Ivan et al. (2019) Fig 2:

| Panel | Content |
|-------|---------|
| Upper-left | Introduction text + difficulty selection buttons |
| Upper-middle | Current equation, Right/Wrong score, START/RESET controls |
| Upper-right | Numpad (digits 0–9, minus, Del, Enter) + answer display |
| Bottom | Status messages — difficulty label, "Good Job!", calculation time |

---

## Citation

If you use this code in your research or project, please cite:

```
Ivan J, Nurdiansyah R, Parikesit AA. Mathematical Problem Solving: One Way to Prevent
Dementia. Iran J Med Inform. 2019; 8(1): e10. https://doi.org/10.30699/IJMI.V8I1.179
```

---

## License

This project is released under the **GNU General Public License v3.0**.  
See [LICENSE](LICENSE) for full terms.

Copyright © 2019 Jeremias Ivan, Rizky Nurdiansyah, Arli A. Parikesit.  
Streamlit port and engine refactor © 2026 Arli A. Parikesit, i3L University.
