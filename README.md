# Python Radar Simulator

A simple radar simulation project built for educational purposes using Python.  
This project generates, moves, and visualizes radar targets in 3D, mimicking a basic radar system workflow. Ideal for students exploring data simulation and visualization.

---

## Features

- Generate random radar targets with **X, Y, Z coordinates** and **speed**
- Simulate **target movement** over time
- Save radar data to **CSV file**
- Display data in a **clean console table**
- Visualize radar targets in **3D using matplotlib**
- Fully **student-friendly**, clean, and readable code

---

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>

Install required dependencies:
pip install matplotlib
----
Usage

Run the simulator with Python:
python main.py
----

You will see:
Console output with the radar data table
CSV file radar_data.csv saved in the project folder
3D visualization showing target positions and speeds
----
Example Output
       X        Y      Z    Speed
----------------------------------
   23.45    78.12  12.34   150.67
   56.12    45.23  25.67   230.45
   ...
----
The 3D plot color-codes targets based on speed for easy visualization.

Project Structure
RadarSignalSimulator/
├─ main.py           # Main program
├─ radar_data.csv    # Sample output file
└─ README.md         # Project documentation
---
Why This Project?

This project demonstrates a complete workflow of a radar system simulation:
Data generation
Movement simulation
Tabular representation
3D visualization
CSV export for further analysis
It’s a student-level but professional-looking project, perfect for demonstrating skills in Python, data simulation, and visualization.
Great for portfolio projects or educational exercises.