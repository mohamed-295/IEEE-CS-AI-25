
# Employee Database – Excel Project

## Overview

This Excel-based project is designed to manage and analyze employee records with:
- Structured data entry and validation  
- Automated calculations and lookups  
- Conditional formatting  
- PivotTable reports for insights and trends  

---

## Dataset Structure

### Employee Fields

| Column             | Description                                  |
|--------------------|----------------------------------------------|
| Employee ID        | Unique identifier                            |
| Name               | Full name of employee                        |
| Department         | Department name (HR, IT, etc.)               |
| Job Title          | Role/title appropriate to the department     |
| Date of Joining    | Must not be in the future                    |
| Salary             | Numeric, must be greater than 0              |
| Email              | Must follow a valid format                   |
| Phone Number       | Egyptian format: +20XXXXXXXXXXX              |
| Status             | Active / Inactive                            |
| Max Salary         | Lookup from Department Rules                 |
| Min Salary         | Lookup from Department Rules                 |
| OFF Days           | Lookup from Department Rules                 |

---

## Data Validation

- **Department & Job Title**: Drop-down lists (sourced from `Lists` sheet)  
- **Status**: Only "Active" or "Inactive"  
- **Email**: Custom formula to validate standard format  
- **Salary**: Must be numeric and > 0  
- **Date of Joining**: Cannot be a future date  
- **Phone Number**: Must follow the +20 Egyptian format and be 12 digits  

---

## Conditional Formatting

- Employees earning **below $3,000** are highlighted in **Red**  
- Employees who joined within the **last 6 months** are highlighted in **Green**

---

## Functions & Lookups

### Seniority Classification

`=IF([@[Salary]] > 5000, "Senior", "Junior")`

### Department-Specific Rules (VLOOKUP from Department_Rules sheet)

`=IFERROR(VLOOKUP([@[Department]], Department_Rules!$A$2:$D$100, 2, FALSE), "")`

- Column 2: Max Salary  
- Column 3: Min Salary  
- Column 4: OFF Days

---

## Reports (PivotTables)

All PivotTables are created in separate sheets for clarity:

1. **Employees Per Department** – Count of employees by department  
2. **Average Salary Per Department** – Average salary by department  
3. **Employee Status Report** – Active vs. Inactive count  
4. **Hiring Trends by Year** – Grouped by year from `Date of Joining`

> **To group by year**:  
> Right-click any date in PivotTable → `Group...` → select `Years` (and optionally `Months`)

---

## Dynamic Filter by Joining Date

Use the fields `N9` (Year), `P9` (Month), and `R9` (Day) to filter employees by joining date:

```
=IF(N9="", 
    "Enter Year At N9 to Filter", 
    FILTER(Dataset, Dataset[Date of Joining] >= DATE(N9, IF(P9="",1,P9), IF(R9="",1,R9)), "No Employees joined")
)
```

- If any of the date inputs are blank, it defaults to `1`

---

## Additional Notes

- All dropdowns are managed in the `Lists` sheet  
- `Department_Rules` sheet controls salary/leave policy for each department  
- Table format is used for dynamic referencing  
- PivotCharts can be added for visual analysis  
- **Always Refresh PivotTables** after updating dataset  

---

## Folder Structure

```
Task_11/
├── Employee_Database.xlsx
├── README.md
```
---
