 UAE 5% VAT Billing & Sales Logger

A Python command-line billing application designed for small retail stores and cafes in the UAE. It automates item selection, promotional discounts, **5% UAE VAT calculation**, and persistent daily sales logging.

#Key Features
 **Automated 5% UAE VAT:** Accurately calculates tax compliance on taxable totals.
 **Smart Discount Logic:** Automatically applies a 10% promotional discount on orders of 100 AED or above.
**Audit & Sales Logging:** Saves timestamped receipts to `daily_sales_log.txt` for end-of-day accounting.
 **Input Validation:** Handles invalid menu choices and non-numeric quantities smoothly.

#Technologies Used
 Python 3 (Core data structures, functions, file handling, `datetime` module)

#How to run
1. Clone this repository or download `billing_system.py`.
2. Open your terminal in the project folder and run:
   ```bash
   python billing_system.py
   ```
#sample output
========================================
         DUBAI RETAIL & CAFE            
       TRN: 100234567800003 (UAE)       
Date: 2026-11-18 13:55:13
Customer: aysha
----------------------------------------
Karak Chai (x2) : 10.00 AED
----------------------------------------
Subtotal       : 10.00 AED
Discount (10%) : -0.00 AED
UAE VAT (5%)   : +0.50 AED
GRAND TOTAL    : 10.50 AED
========================================
