# Building-EPC

This repository provides tools and resources for analyzing and predicting building energy performance certificates (EPCs), with a focus on the Barcelona dataset. It includes Python scripts, Jupyter notebooks, datasets, and figures to help users explore, model, and visualize EPC data.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Updating and Uploading Changes](#updating-and-uploading-changes)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```
Barcelona_ANN_new.py           # Main Python script for ANN modeling
Barcelona_ANN.ipynb            # Jupyter notebook for ANN analysis
Masters_Code2.ipynb            # Additional Jupyter notebook
CE3X_details.md                # Documentation on CE3X tool
energy_efficiency_certificates.csv # Main dataset
figs/                          # Folder with figures (e.g., pie charts)
dataset_schema.csv             # Dataset schema/description
README.md                      # Project documentation
```

## Getting Started

### 1. Clone the Repository
To get the files on your computer, open a terminal (PowerShell on Windows) and run:

```powershell
git clone https://https://github.com/Dumo1999/Building-EPC
```

### 2. Navigate to the Project Directory
```powershell
cd Building-EPC
```

### 3. Install Required Packages
If there is a `requirements.txt` file, install dependencies with:

```powershell
pip install -r requirements.txt
```
If not, install common packages manually (e.g., numpy, pandas, scikit-learn, matplotlib, tensorflow, etc.):

```powershell
pip install numpy pandas scikit-learn matplotlib tensorflow
```

## Usage
- Open the Jupyter notebooks (`.ipynb`) in VS Code or JupyterLab to explore and run analyses.
- Run the Python scripts (e.g., `Barcelona_ANN_new.py`) from the terminal:

```powershell
python Barcelona_ANN_new.py
```

- Review the figures in the `figs/` directory for visualizations.

## Updating and Uploading Changes

### 1. Save Your Changes
Make sure all your changes are saved locally.

### 2. Check the Status
```powershell
git status
```

### 3. Stage the Changes
```powershell
git add .
```

### 4. Commit the Changes
```powershell
git commit -m "Describe your changes here"
```

### 5. Upload (Push) the Changes to GitHub
```powershell
git push origin main
```
Replace `main` with your branch name if different.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
Specify your license here (e.g., MIT, GPL, etc.).
