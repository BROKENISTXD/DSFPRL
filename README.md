# DFS-PRL - Anomaly Detection Library

![PyPI](https://img.shields.io/pypi/v/dfsprl)
![License](https://img.shields.io/badge/License-MIT-blue)

DFS-PRL is a Python library designed for efficient anomaly detection in time-series data. Identify outliers and unusual patterns in your datasets with simple integration and real-time capabilities.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [The `detect()` Function](#the-detect-function)
  - [Data Format Requirements](#data-format-requirements)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

Install the package from PyPI using pip:

```bash
pip install dfsprl
```

## Quick Start
Get started with anomaly detection in 3 simple steps:
```python
import dfsprl

# Sample dataset
data = [0.0, 0.1, 0.3, 0.5, 0.7, 1.0, 1.2, 1.4, 2.0]

# Detect anomalies
anomalies = dfsprl.detect(data)

# Display results
print("Detected Anomalies:")
for index, (value, is_anomaly) in enumerate(zip(data, anomalies)):
    status = "ANOMALY" if is_anomaly else "Normal"
    print(f"Point {index}: {value:.1f} → {status}")
```
## Usage
The detect() Function
The core functionality is provided through the detect() method:

def detect(data: list[float], threshold: float = 0.2) -> list[bool]:
    """
    Identifies anomalies in numerical data
    
    Parameters:
    data (list[float]): Input data points
    threshold (float): Sensitivity parameter (default: 0.2)
    
    Returns:
    list[bool]: Boolean mask indicating anomalies (True = anomaly)
    """
## Data Format Requirements
Input data should meet these specifications:

Numerical values (int or float)

Ordered sequentially (time-series preferred)

Minimum 10 data points for reliable detection

Example valid input: 
temperature_readings = [22.1, 22.3, 22.4, 22.5, 23.8, 22.2, 22.3, 45.6, 22.3]

## Examples
import dfsprl

sales_data = [120, 125, 130, 118, 115, 122, 350, 116, 121]
anomalies = dfsprl.detect(sales_data)

print(f"Anomaly positions: {[i for i, val in enumerate(anomalies) if val]}")
# Output: Anomaly positions: [6]
# Increase sensitivity with lower threshold
sensitive_anomalies = dfsprl.detect(data, threshold=0.1)

# Decrease sensitivity with higher threshold
relaxed_anomalies = dfsprl.detect(data, threshold=0.3)

## Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Ensure all code follows PEP-8 guidelines and includes appropriate tests.
