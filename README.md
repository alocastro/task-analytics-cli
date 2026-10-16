# 📋 CLI Task Manager & Workload Analytics

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-clean-orange.svg)

A modular, robust Command-Line Interface (CLI) application built in Python designed to register, categorize, and analyze daily tasks. This project demonstrates core software development principles, including **defensive programming**, **modular architecture**, and **structured data processing**.

---

## ✨ Key Features

- **Dynamic Task Registration**: Interactively registers tasks with custom titles, priorities, and estimated completion times.
- **Robust Input Validation**: Employs defensive helper functions to handle edge cases and prevent runtime errors caused by invalid user input.
- **Priority Categorization**: Groups tasks logically by priority levels (`HIGH`, `MEDIUM`, `LOW`).
- **Workload Analytics**: Automatically calculates metrics such as total estimated workload duration and average task duration.
- **Clean Architecture**: Decouples execution orchestration from utility modules for improved maintainability and scalability.

---

## 📁 Repository Structure

```text
.
├── main.py              # Application entry point and reporting logic
├── utils/               # Custom utility package
│   ├── __init__.py      # Package initialization marker
│   └── functions.py     # Custom helper functions & input validation logic
└── README.md            # Project documentation
```

---

## 🛠️ Architecture & Technical Highlights

1. **Separation of Concerns (SoC)**:
   - `main.py`: Handles workflow execution, task list construction, dynamic output generation, and statistical calculations.
   - `utils/functions.py`: Encapsulates reusable utility logic, keeping the primary workflow clean and readable.

2. **Defensive Input Handling**:
   - Uses strict validation primitives (`get_valid_number`, `get_choice`, `get_valid_name`) to guarantee data integrity before dictionary construction.

3. **Safe Data Aggregation**:
   - Implements safe mathematical operations (e.g., zero-division checks) when computing workload metrics.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## 📊 Sample Output

```text
--- Entering Task 1 ---
Enter task title: Refactor API Endpoints
Enter priority (high, medium, low): high
Enter estimated time in minutes (>0): 45

================ TASK REPORT ================

HIGH priority tasks:
	- Refactor API Endpoints (45 min)

MEDIUM priority tasks:
	No tasks

LOW priority tasks:
	No tasks
------------------------------------------------

Total estimated time: 45 min
Average estimated time per task: 45.00 min

================================================
```

---

## 🎯 Future Improvements

- [ ] Add persistent storage (JSON / SQLite export).
- [ ] Implement task status updates (marking tasks as `Completed`).
- [ ] Build a search and filtering utility.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
