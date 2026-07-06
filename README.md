# done-cli

A clean, zero-dependency Python CLI tool built for managing daily tasks directly inside the terminal. It sidesteps heavy frameworks and databases, using a raw state-machine loop paired with atomic JSON reads and writes to keep your to-do tracking instant and localized.

## Key Features
* **Zero Dependencies:** Runs on plain Python 3.x using native standard libraries.
* **Local State Machine:** Operates on an isolated main-loop structure with defensive error handling for user inputs.
* **Atomic Storage:** Saves data immediately upon mutation to a local JSON file, preventing runtime state drift.
* **Corrupted State Graceful Recovery:** Detects warped or malformed save files dynamically and restarts cleanly instead of crashing out.

## Tech Stack Breakdown
* **Language:** Python 3.x
* **Persistence:** Native `json` module for serialization
* **Environment Interactivity:** Native `os` standard library

## Web-Based Quick Start

You do not need to pull code down to your machine to run or modify this project. 

### Launching in GitHub Codespaces
1. Click the green **Code** button at the top right of this repository.
2. Switch to the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Once the browser container spins up, open the terminal pane and execute:
   ```bash
   python main.py

### Quick Local Execution (Alternative)
If you prefer running it locally without git, download main.py and run:
  python main.py

## Project Structure
```bash
done-cli/
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions sanity compilation runner
├── .gitignore          # Keeps build caches and local state tracking out of source control
├── README.md           # Documentation
└── main.py             # Main interactive application loop and state logic
```
## Project Roadmap
[ ] Implement query filters to view completed vs. pending tasks separately.

[ ] Add explicit flags or positional args (main.py --add "Task description") to skip the interactive loop for quick terminal pipelines.

[ ] Introduce soft-deletion logic or timestamp tracking for finished items.
