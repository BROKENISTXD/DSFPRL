import numpy as np
from dfsprl import DFSprl

def main():
    train_data = np.random.rand(100, 5)
    
    detector = DFSprl(contamination=0.1)

    detector.fit(train_data)
    
    new_data = np.random.rand(10, 5)  
    
    anomalies = detector.process(new_data)
    
    for idx, anomaly in enumerate(anomalies):
        print(f"Data point {idx + 1}: Anomaly {'Yes' if anomaly == -1 else 'No'}")

if __name__ == "__main__":
    main()
