# ATM Simulation

A simple CLI-based program that simulates a basic ATM. Manage a single account balance from the command line — no database or internet connection required.

## Table of Contents
- [Features Overview](#features-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Next Steps](#next-steps)

## Features Overview

| # | Feature | Description |
|---|---------|-------------|
| 1 | Check Balance | Display your current account balance. |
| 2 | Deposit | Add money to your account. The amount must be greater than 0. |
| 3 | Withdraw | Take money out of your account. Rejects amounts that are 0 or less, or greater than your balance. |
| 4 | Exit | Quit the program. |

## Installation
To install this program, use the commands below:
```bash
git clone https://github.com/fmax-dev/ATM-SIMULATION.git
cd ATM-SIMULATION
```
No external dependencies are required.

## Usage
To start using this program:
1. Clone this repo using the commands above
2. Run the program:
    - Windows: `python atm_controller.py`
    - Mac/Linux: `python3 atm_controller.py`
3. Select an option from the menu and follow the prompts

```
----- WELCOME TO YOUR ATM MACHINE -----

ATM MENU
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
```

## Project Structure
| File | Responsibility |
|------|----------------|
| `atm.py` | The `ATM` model — holds the balance and the deposit/withdraw logic. |
| `atm_controller.py` | The `ATMController` — runs the menu, validates input, and is the program's entry point. |

The dependency flows one way: the controller imports the model, never the reverse.

## Next Steps
- Persist the balance between sessions (e.g. save to a JSON file)
- Add PIN authentication and support for multiple accounts
- Add a transaction history log
- Add a transfer-between-accounts feature
