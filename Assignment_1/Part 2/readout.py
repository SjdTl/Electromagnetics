import os as os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots

from scipy.fft import fft, fftfreq, fftshift

plt.style.use(['science','ieee'])


"""
__________________________________________________________________________________________________
I WILL CLEAN UP THIS CODE SINCE IT IS KIND OF A MESS AT THE MOMENT
__________________________________________________________________________________________________
"""


def optimize_svg(path):
    import shutil
    import subprocess
    # Run the SVGO command if SVGO is installed
    if shutil.which("svgo") is not None:
        subprocess.run([shutil.which("svgo"), path])

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

def plot_all_measurements(measurements, prefix_name=None, which_measurement = 'all', processing = None):
    for i, (key, measurement) in enumerate(measurements.items()):
        if i in list(which_measurement) or which_measurement == 'all':
            print(measurement)
            fig, ax = plt.subplots()
            ax.plot(measurement["t"] * 10e9, smooth_signal(measurement["CH1"], processing), label="CH1")
            if "CH2" in measurement.columns:
                ax.plot(measurement["t"] * 10e9, smooth_signal(measurement["CH2"], processing), label="CH2")

            ax.set_xlabel("ns")
            ax.set_ylabel("V")

            ax.set_title("Waveforms with different loads")
            plt.legend()

            if prefix_name != None:
                savepath = os.path.join(dir_path, "Out", rf"{prefix_name}_{key}")
            else:
                savepath = os.path.join(dir_path, "Out", rf"{key}")

            fig.savefig(f"{savepath}.svg", transparent=True)
            optimize_svg(f"{savepath}.svg")

def freq_domain(measurement, prefix_name = None, which_measurement = 'all', processing = None):
    for i, (key, measurement) in enumerate(measurement.items()):
        if i in list(which_measurement) or which_measurement == 'all':
            fs = 1/np.diff(measurement["t"])
            print(rf"Variance in sampling frequency: {np.var(fs)} Hz")
            fs = np.mean(fs)
            print(rf"Sampling frequency: {fs} Hz")

            fig, ax = plt.subplots()
            

            ch1f = fft(smooth_signal(measurement["CH1"], processing))
            xf = fftshift(fftfreq(len(ch1f), 1/fs))

            plt.plot(xf / 10e9, 20 * np.log(np.abs(fftshift(ch1f))), label = "CH1")
            if "CH2" in measurement.columns:
                ch2f = fft(smooth_signal(measurement["CH2"], processing))
                plt.plot(xf / 10e9, 20 * np.log(np.abs(fftshift(ch2f))), label="CH2")

            ax.set_xlabel("f (GHz)")
            ax.set_ylabel("Magnitude (dB)")

            if prefix_name != None:
                savepath = os.path.join(dir_path, "Out", "Freqdomain", rf"{prefix_name}_{key}")
            else: 
                savepath = os.path.join(dir_path, "Out", "Freqdomain", rf"{key}")
            fig.savefig(f"{savepath}.svg", transparent=True)
            optimize_svg(f"{savepath}.svg")


def smooth_signal(signal, type_smoothing = "SMA", smoothing_coef = 30):
    signal = np.array(signal)
    if type_smoothing == "SMA": # Simple moving average
        N = smoothing_coef
        signal = np.pad(signal, (int(np.ceil(N/2)-1),int(np.floor(N/2))), mode='edge')
        return np.convolve(signal, np.ones(N)/N, mode='valid')
    else:
        return signal


measurements = read_measurements(dir_path)
freq_domain(measurements, which_measurement='all')
freq_domain(measurements,prefix_name = "post_processing", which_measurement='all', processing = "SMA")
plot_all_measurements(measurements, "processed", processing = "SMA")
plot_all_measurements(measurements)