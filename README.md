# Trade Reconciliation Automation (Python)

## Overview

This project simulates a **trade reconciliation process** commonly performed in financial operations and middle office roles.

It compares **internal trading records** with **external counterparty data**, identifies discrepancies, and produces a clear reconciliation output.

The goal is to demonstrate how **manual reconciliation processes can be automated using Python**, improving efficiency and reducing operational risk.

---

## Key Features

* Reconciles internal vs external trade data
* Identifies:

  * Matches
  * Mismatches (amount/currency)
  * Missing trades (internal/external)
* Generates a **summary report**
* Visualizes reconciliation results
* Exports outputs to Excel and CSV

---

## Technologies Used

* Python
* pandas
* matplotlib
* openpyxl (Excel export)

---

## Project Structure

* `reconcile.ipynb` → Main notebook with full workflow
* `requirements.txt` → Required Python libraries

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/reconciliation-automation.git
cd reconciliation-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

1. Open the notebook:

   * In VS Code (with Jupyter extension), or
   * Using Jupyter Notebook

2. Run all cells from top to bottom

3. The script will:

   * Perform reconciliation
   * Generate a summary
   * Export results automatically

---

## Output Files

Running the notebook generates:

* `reconciliation_results.xlsx` → Full reconciliation output
* `reconciliation_summary.xlsx` → Summary of results
* CSV versions of both files

---

## Example Logic

Each trade is classified as:

* **Match** → Amount and currency match
* **Mismatch** → Differences in amount or currency
* **Missing Internal** → Present only in external data
* **Missing External** → Present only in internal data

---

## Business Context

This project reflects real-world workflows in:

* Treasury Operations
* Trade Support / Middle Office
* Prime Brokerage
* Hedge Fund Operations

It demonstrates how **Python can be used to automate reconciliation**, a traditionally manual and time-sensitive process.

---

## Future Improvements

* Read data from real CSV/Excel files instead of hardcoded data
* Add tolerance thresholds for amount differences
* Integrate with SQL database
* Automate daily reconciliation runs

---

## Author

Ana Galfi
Operations Analyst | Treasury & Trade Lifecycle | Python & Data Analysis
