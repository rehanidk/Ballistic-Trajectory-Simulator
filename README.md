# Ballistic Trajectory Simulator

Simulates and plots the 2D trajectory of a projectile accounting for gravity and aerodynamic drag.

## Installation
pip install matplotlib csv sys argparse

## Usage
1) Go to project.py
2) Enter into the CLI : py project.py --velocity 50 --angle 45 --mass 0.145 --drag 0.47 --area 0.00426
3) Modify the values after each argument to your needs
4) Open trajectory.gif / trajectory.png to see results

## Features
1) Data is saved in a CSV file "coordinates.csv", can be used for further checking or simulation
2) Landing position and max height is found and printed to the terminal

