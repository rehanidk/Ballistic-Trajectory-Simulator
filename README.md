# Ballistic Trajectory Simulator
Simulates and plots the 2D trajectory of a projectile accounting for gravity and aerodynamic drag.

## Installation
```bash
pip install matplotlib numpy
```

## Usage
Run from the CLI:
```bash
py project.py --velocity 50 --angle 45 --mass 0.145 --drag 0.47 --area 0.00426
```
| Argument | Description |
|----------|-------------|
| `--velocity` | Launch velocity (m/s) |
| `--angle` | Launch angle (degrees) |
| `--mass` | Mass of projectile (kg) |
| `--drag` | Drag coefficient |
| `--area` | Cross-sectional area (m²) |

Results are saved as `trajectory.png`, `trajectory.gif`, and `coordinates.csv`.

## How It Works
- **Custom classes** — `Vector2D` handles 2D math; `Projectile` tracks position, velocity, and mass
- **Euler integration** — Updates position and velocity every 10ms to simulate motion step by step
- **Aerodynamic drag** — Uses the standard drag equation (Fd = ½ρv²CdA), so a baseball and ping-pong ball launched identically will follow different paths

## Features
- Landing position and max height printed to terminal
- Trajectory data exported to `coordinates.csv` for further analysis

## Examples
<img width="640" height="480" alt="trajectory" src="https://github.com/user-attachments/assets/4fd0e69e-efc8-490a-b11d-445b2b87d901" />
<img width="640" height="480" alt="trajectory" src="https://github.com/user-attachments/assets/cce3d623-fedc-43c7-a4e5-ab1abfe653e7" />
