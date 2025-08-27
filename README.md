
# 📘 GIT Exam Result Checker

This is a Python script that automatically checks **General Information Technology (G.I.T.) exam results** from the official exam website.  
It scans through a range of index numbers, extracts the details, and saves them into a text file (`results.txt`).

---

## 🛠️ Prerequisites

Before running the script, make sure you have:

1. **Python 3.x** installed  
   - Check if Python is installed:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
   - If you don’t have it, download from 👉 [Python.org](https://www.python.org/downloads/)

2. **Pip** (Python package manager) installed  
   - Check with:
     ```bash
     pip --version
     ```
   - Pip usually comes with Python, but if missing, install it separately.

3. Required libraries:  
   Install using pip:
   ```bash
   pip install requests beautifulsoup4

---

## 🚀 How to Use

### Step 1: Download or Clone this Repository

Option 1 – Download as ZIP:

* Click **Code → Download ZIP** on this GitHub repo.
* Extract the ZIP file.

Option 2 – Clone with Git:

```bash
git clone https://github.com/VihangaNethmaka/GIT-exam-result-checker.git
cd GIT-exam-result-checker
```

---

### Step 2: Run the Script

Open a terminal/command prompt inside the folder and run:

```bash
python main.py --start <START_INDEX> --end <END_INDEX>
```

👉 Example:

```bash
python main.py --start 1000000 --end 1000100
```

This will check results for all index numbers from **1000000** to **1000100**.

---

### Step 3: View Results

* If valid results are found, they will be saved into a file named **`results.txt`** in the same folder.
* Open it with Notepad, VS Code, or any text editor.

Example result in `results.txt`:

```
==================== Result Found ====================
Index Number: 1000001
Examination: General Information Technology Examination
Year: 2024
Name: John Doe
School/ Address: Example College
Medium: English
Due Year: 2024
Subject: GIT
Grade: A
======================================================
```

---

## ⚠️ Notes & Tips

* Run with smaller index ranges first to test (e.g., 5–10 index numbers).
* Add a short delay is already built into the script (`time.sleep(0.5)`) to avoid server overload.
* Use responsibly ⚠️ This is only for **educational and personal purposes**.
* If you get **ModuleNotFoundError**, it means you forgot to install required libraries (see Prerequisites).

---

## ✅ Quick Example (Windows)

1. Open **Command Prompt**.
2. Navigate to the folder:

   ```bash
   cd Desktop\GIT-exam-result-checker
   ```
3. Run:

   ```bash
   python main.py --start 2000000 --end 2000010
   ```
4. Open `results.txt` to see results.

---

## 🖥️ Quick Example (Linux/Mac)

```bash
cd ~/Downloads/GIT-exam-result-checker
python3 main.py --start 2000000 --end 2000010
```

---

## 📜 License

This project is for **educational purposes only**. Please don’t misuse the script or overload the official exam results server.



