# 🌍 Building-EPC

Tools and resources for analyzing **Building Energy Performance Certificates (EPCs)** — with a focus on the Barcelona dataset. The repo contains Python scripts, Jupyter notebooks, data files, and figures to let you explore, model, and visualise EPC data end-to-end.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/Dumo1999/Building-EPC)](https://github.com/Dumo1999/Building-EPC/issues)

---

## 📑 Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [First-time Git quick-start](#first-time-git-quick-start)
  - [Cloning the repository](#1-clone-the-repository)
  - [Opening in VS Code](#2-open-the-project-in-vs-code-recommended)
  - [Installing dependencies](#3-install-required-packages)
- [Usage](#usage)
- [Typical Git Workflow](#typical-git-workflow)
- [Contributing](#contributing)
- [License](#license)

---

## 🗂️ Project Structure
\`\`\`
Barcelona_ANN_new.py            # Main Python script for ANN modelling
Barcelona_ANN.ipynb             # Jupyter notebook for ANN analysis
Masters_Code2.ipynb             # Additional notebook experiments
CE3X_details.md                 # Notes on the CE3X EPC tool
energy_efficiency_certificates.csv   # Main dataset
dataset_schema.csv              # Column descriptions
figs/                           # Pre-generated plots and charts
README.md                       # You are here
\`\`\`

---

## 🛠️ Prerequisites
- **Python 3.9+**  
- **Git** (any recent version)  
- **VS Code** (optional but recommended) with  
  - *Python* extension  
  - *Jupyter* extension  
  - *GitHub Copilot* or *ChatGPT Code Editor* for AI coding assistance  

> **Why VS Code?**  
> It bundles Git integration, a first-class Jupyter experience, and lets you use Copilot/LLM extensions that autocomplete or explain code as you type.

---

## 🚀 Getting Started

### First-time Git quick-start
1. **Install Git**: download from <https://git-scm.com> and follow the defaults.  
2. **Set your name & email** (one-off):  
   \`\`\`bash
   git config --global user.name  "Your Name"
   git config --global user.email "you@example.com"
   \`\`\`
3. **Generate an SSH key** (optional but nicer than HTTPS passwords):  
   \`\`\`bash
   ssh-keygen -t ed25519 -C "you@example.com"
   \`\`\`
   Add the public key (\`~/.ssh/id_ed25519.pub\`) to *GitHub → Settings → SSH keys*.

After that, every repo follows the same three-step loop: **clone → edit → commit & push**.

---

### 1. Clone the repository
```bash
git clone https://github.com/Dumo1999/Building-EPC.git
cd Building-EPC
```

### 2. Open the project in VS Code (recommended)
```bash
code .
```
- VS Code will detect the Python env and suggest installing extensions.  
- If you’ve enabled GitHub Copilot or another LLM helper, you’ll get smart autocompletion and inline explanations as you work.

### 3. Install required packages
If a \`requirements.txt\` is present:
```bash
pip install -r requirements.txt
```
Otherwise, install the common stack manually:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn tensorflow shap
```

*(Tip: use a virtual environment — \`python -m venv .venv\` then \`source .venv/bin/activate\`)*

---

## 🎛️ Usage

| Task                          | Command / Action                                   |
|-------------------------------|----------------------------------------------------|
| Run main script               | \`python Barcelona_ANN_new.py\`                      |
| Open notebooks                | \`jupyter lab\` **or** VS Code Jupyter view          |
| View figures                  | Browse \`figs/\` or load them in any image viewer    |

---

## 🔄 Typical Git Workflow
> Repeat this loop each time you make edits.

```bash
# See what changed
git status

# Stage only the files you want
git add path/to/file.py AnotherFile.ipynb

# Commit with a clear message
git commit -m "Fix: cleaner plotting function for ANN results"

# Push to GitHub
git push origin main   # or your feature branch
```

Need a refresher? GitHub has a great beginner guide:  
<https://docs.github.com/en/get-started/quickstart>

---

## 🤝 Contributing
Pull requests are welcome! For larger ideas, open an issue first so we can discuss direction and avoid duplicate work.

---

## 📜 License
Distributed under the **MIT License**. See [\`LICENSE\`](LICENSE) for details.

---

