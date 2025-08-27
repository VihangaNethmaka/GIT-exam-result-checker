# GIT Exam Result Checker

This Python script allows you to check **General Information Technology (G.I.T.) exam results** from the official results website for a range of index numbers.  
It will automatically extract the details and save them into a `results.txt` file.

---

## 📌 Requirements

- Python 3.x  
- Required libraries:

  
  ```bash
  pip install requests beautifulsoup4


---

## 📌 Usage

1. Clone this repository or download the script:

   ```bash
   git clone https://github.com/VihangaNethmaka/GIT-exam-result-checker.git
   cd GIT-exam-result-checker
   ```

2. Run the script with a **range of index numbers**:

   ```bash
   python main.py --start <START_INDEX> --end <END_INDEX>
   ```

   Example:

   ```bash
   python main.py --start 1000000 --end 1000100
   ```

   This will check all index numbers from **1000000** to **1000100**.

---

## 📌 Output

* If valid results are found, they will be saved into `results.txt` in the same folder.
* Example saved result:

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

## ⚠️ Disclaimer

* This script is for **educational purposes only**.
* Please use responsibly and do not overload the exam results server.

