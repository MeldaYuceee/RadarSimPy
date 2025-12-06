# Python Radar Simulator – Basic 3D Radar Target Model

> **Domain:** Radar Simulation / Target Modelling / Signal Visualization  
> **Level:** Prototype (Student R&D)  
> **Purpose:** Demonstrate a simplified radar target model with position updates and 3D visualization for educational use

---

## 1. Background & Concept
Modern radar systems track objects in 3D space by estimating range, azimuth and elevation and updating these values over time.  
This project builds a **minimal radar target simulator** using Python, modelling random targets with basic kinematic updates and visualizing their positions.

The focus is on making radar fundamentals accessible rather than reproducing real radar signal processing.

---

## 2. Features
- Random 3D target generation (X, Y, Z)
- Basic kinematic movement over time
- Radar table output in terminal
- CSV export for later analysis
- 3D target visualization using `matplotlib`
- Lightweight, beginner-friendly implementation

---

## 3. Architecture
[Random Targets]
↓
[Movement Update]
↓
[Data Logging → CSV]
↓
[3D Visualization]

- Input: random initial positions and speeds  
- Processing: simple movement model  
- Output: console table + CSV + 3D plot  

---

## 4. Installation

```bash
git clone <your-repo-url>
cd PythonRadarSimulator

