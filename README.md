# Sonar Data Analysis
This program reads sonar data from an Excel file, calculates the first and second derivatives (velocity and acceleration), and generates a multi-plot showing the position, velocity, and acceleration of a cart using the sonar data.

## Features
- Reads data (time and position) from an Excel file.
- Calculates the first and second discrete time derivatives (velocity, acceleration) of the position data from the sensor.
- Creates a multi-plot showing position, velocity, and acceleration.
- Finds critical points of the time of maximum velocity and the time when the cart stops.

## How It Works
### Finding Maximum Velocity
The program calculates the first derivative of the position data to obtain the velocity. It then identifies the time at which the velocity reaches its maximum value. This is done using the `np.argmax` function on the velocity array.

### Finding Stopping Time
To determine when the cart stops, the program looks for a period where the position data remains nearly constant and the velocity is close to zero (acceleration is not checked since it is very noisy). This is done by checking if the change in position between consecutive time points is below a small threshold and if the velocity is below a certain threshold. The search for the stopping time starts after the time of maximum velocity.

## Requirements
- Python 3.x
- pandas
- matplotlib
- numpy
- openpyxl

## Installation
1. Clone the repository or download the `sonar.py` file.
2. Install the required Python packages using pip:

```sh
pip install pandas matplotlib numpy openpyxl
```
