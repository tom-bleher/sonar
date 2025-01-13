import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_excel_columns(file_path, sheet_name, col1, col2):
    """Read two columns from an Excel file."""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    x_data = df.iloc[:, col1]
    y_data = df.iloc[:, col2]
    return x_data, y_data

def calculate_derivatives(time, position):
    """Calculate first and second derivatives of position data."""
    dt = np.diff(time)
    velocity = np.diff(position) / dt
    acceleration = np.diff(velocity) / dt[:-1]
    
    # Adjust arrays to match lengths
    time_v = time[1:]
    time_a = time[2:]
    
    return time_v, velocity, time_a, acceleration

def create_multi_plot(time, position, time_v, velocity, time_a, acceleration, sheet_name):
    """Create a plot showing position, velocity, and acceleration."""
    # Normalize data
    norm_pos = position / np.max(np.abs(position))
    norm_vel = velocity / np.max(np.abs(velocity))
    norm_acc = acceleration / np.max(np.abs(acceleration))
    
    # Find minimum values of normalized data
    datasets = [(norm_pos, position, time), (norm_vel, velocity, time_v), (norm_acc, acceleration, time_a)]
    min_values = [np.min(norm_data) for norm_data, _, _ in datasets]
    
    # Find which normalized dataset has the most significant minimum
    most_sig_idx = np.argmin(min_values)
    _, original_data, time_data = datasets[most_sig_idx]
    
    # Find the actual minimum time in the most significant dataset
    critical_time = time_data[np.argmin(original_data)]
    
    plt.figure(figsize=(12, 8))
    plt.suptitle(f'Data from {sheet_name}', y=0.995)
    
    plt.subplot(311)
    plt.plot(time, position, 'b-', label='x (m)')
    plt.axvline(x=critical_time, color='r', linestyle='--', alpha=0.5)
    plt.text(critical_time, plt.ylim()[1], f' t={critical_time:.3f}s', rotation=90, va='bottom')
    plt.ylabel('x')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(312)
    plt.plot(time_v, velocity, 'g-', label='v (m/s)')
    plt.axvline(x=critical_time, color='r', linestyle='--', alpha=0.5)
    plt.ylabel('v')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(313)
    plt.plot(time_a, acceleration, 'r-', label='a (m/s^2)')
    plt.axvline(x=critical_time, color='r', linestyle='--', alpha=0.5)
    plt.xlabel('t')
    plt.ylabel('a')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f"{sheet_name}.svg", format="svg")
    plt.show()

if __name__ == "__main__":
    # Example usage
    file_path = "sonar.xlsx"
    sheet_name = "run 7#"
    time_col = 0
    pos_col = 1
    
    try:
        time, position = read_excel_columns(file_path, sheet_name, time_col, pos_col)
        time_v, velocity, time_a, acceleration = calculate_derivatives(time.values, position.values)
        create_multi_plot(time, position, time_v, velocity, time_a, acceleration, sheet_name)
    except Exception as e:
        print(f"Error: {e}")