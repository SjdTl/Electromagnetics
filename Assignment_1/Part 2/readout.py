import os as os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots
plt.style.use(['science','ieee'])


dir_path = os.path.dirname(os.path.realpath(__file__))


def read_measurements(dir_path):
    """
    Measurements are in measurements dictionary as pd.Dataframes of the following form
    measurement["ALL0001"] = | t      | CH1     | CH2
                            --------------------------
                            | 0       | 0.02    | 0.03

    """
    data_info = pd.read_csv(os.path.join(dir_path, "Data", f"data_info.csv"))

    measurements = {}

    for datanum in data_info["Measurement_name"]:
        ch1 = pd.read_csv(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH1.CSV"), names=["a","b", "c", "t","CH1","d"]).iloc[:, [3,4]]
        if os.path.exists(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH2.CSV")):
            ch2 = pd.read_csv(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH2.CSV"), names=["a","b", "c", "t","CH2","d"]).iloc[:, [4]]
        else:
            ch2 = pd.DataFrame()
        measurements[datanum] = pd.concat([ch1, ch2], axis=1)

    return measurements

def plot_all_measurements(measurements):
    for key, measurement in measurements.items():
        print(measurement)
        fig, ax = plt.subplots()
        ax.plot(measurement["t"] * 10e9, measurement["CH1"], label="CH1")
        if "CH2" in measurement.columns:
            ax.plot(measurement["t"] * 10e9, measurement["CH2"], label="CH2")

        ax.set_xlabel("ns")
        ax.set_ylabel("V")

        ax.set_title("Waveforms with different loads")
        plt.legend()

        savepath = os.path.join(dir_path, "Out", key)
        fig.savefig(f"{savepath}.svg", transparent=True)

measurements = read_measurements(dir_path)
plot_all_measurements(measurements)
