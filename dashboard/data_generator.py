import pandas as pd
import random
import time
from datetime import datetime
import os

CSV_FILE = "../data/energy_log.csv"

energy = 0

while True:

    voltage = 230

    current = round(random.uniform(0,10),2)

    power = round(voltage * current,2)

    energy += power / 1000 / 3600

    cost = round(energy * 8,2)

    if power < 700:
        status = "LOW"
    elif power < 1500:
        status = "NORMAL"
    elif power < 2200:
        status = "HIGH"
    else:
        status = "CRITICAL"

    row = {
        "Timestamp": datetime.now(),
        "Voltage": voltage,
        "Current": current,
        "Power": power,
        "Energy": round(energy,4),
        "Cost": cost,
        "Status": status
    }

    df = pd.DataFrame([row])

    if not os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE,index=False)
    else:
        df.to_csv(
            CSV_FILE,
            mode="a",
            header=False,
            index=False
        )

    print(row)

    time.sleep(5)