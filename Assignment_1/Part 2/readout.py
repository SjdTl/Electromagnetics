import os as os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots
from scipy.constants import speed_of_light

TESTING = False

if TESTING == False:
    plt.style.use(['science','ieee'])

from scipy.fft import fft, fftfreq, fftshift
from scipy.signal import savgol_filter


def save_plot(name, fig):
    import shutil
    import subprocess

    savepath = os.path.join(dir_path, "Out", rf"{name}.svg")

    fig.savefig(f"{savepath}", transparent=True)

    # Run the SVGO command if SVGO is installed
    if shutil.which("svgo") is not None:
        subprocess.run([shutil.which("svgo"), savepath])

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

    for datanum, datadesc in zip(data_info["Measurement_name"], data_info["Description"]):
        ch1 = pd.read_csv(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH1.CSV"), names=["a","b", "c", "t","CH1","d"]).iloc[:, [3,4]]
        if os.path.exists(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH2.CSV")):
            ch2 = pd.read_csv(os.path.join(dir_path, "Data", datanum, f"F{datanum[3:]}CH2.CSV"), names=["a","b", "c", "t","CH2","d"]).iloc[:, [4]]
        else:
            ch2 = pd.DataFrame()
        measurements[datadesc] = pd.concat([ch1, ch2], axis=1)

    return measurements

def freq_domain(t, signal):
        signal = np.array(signal)

        if signal.ndim == 1:
            signal = np.array([signal])
        
        fs = 1/np.diff(t)
        print(rf"Variance in sampling frequency: {np.var(fs)} Hz")
        fs = np.mean(fs)
        print(rf"Sampling frequency: {fs} Hz")

        out = []

        for sig in signal:
            out.append(20 * np.log(np.abs(fftshift(fft(sig)))))

        xf = fftshift(fftfreq(len(out[0]), 1/fs))

        if np.shape(out)[0] == 1:
            return xf, out[0]
        else:
            return xf, out

def smooth_signal(signal, type_smoothing = "SMA", smoothing_coef = 30):
    signal = np.array(signal)

    if signal.ndim == 1:
        signal = np.array([signal])

    N = smoothing_coef

    out = []
    for sig in signal:
        if type_smoothing == "SMA": # Simple moving average
            pad_sig = (np.pad(sig, (int(np.ceil(N/2)-1),int(np.floor(N/2))), mode='edge'))
            out.append(np.convolve(pad_sig, np.ones(N)/N, mode='valid'))
        elif type_smoothing == "savgol":
            out.append(savgol_filter(sig, window_length=N, polyorder=3))
        else:
            out.append(sig)
    out = np.array(out)
    if np.shape(out)[0] == 1:
        return out[0]
    else:
        return out
    
def test_smoothing(signal):
    """
    Test different smoothing methods on signal
    by plotting original and different smoothing
    methods in the time- and frequency domain
    """
    smoothing_methods = ["None", "SMA", "savgol"]

    fig, ax = plt.subplots(len(smoothing_methods),2, figsize=(5,5))

    for i, smoothing_method in enumerate(smoothing_methods):
        signals = [np.array(signal["CH1"])]
        if "CH2" in signal.columns:
            signals.append(np.array(signal["CH2"]))
        smoothed_signals = smooth_signal(signals, smoothing_method)

        if smoothed_signals.ndim == 1:
            smoothed_signals = np.array([smoothed_signals])
        
        for smoothed_signal in smoothed_signals:
            # Time domain
            ax[i][0].plot(signal["t"] * 1e9, smoothed_signal)
            ax[i][0].set_xlabel("$t\;[ns]$")
            ax[i][0].set_ylabel("Voltage$\;[V]$")
            ax[i][0].set_title(rf"Time domain ({smoothing_method})")

            # Frequency domain
            xf, out = freq_domain(signal["t"], smoothed_signal)
            ax[i][1].plot(xf * 1e-9, out)
            ax[i][1].set_xlabel(rf"$f\;[GHz]$")
            ax[i][1].set_ylabel(rf"Magnitude$\;[dB]$")
            ax[i][1].set_title(rf"Frequency domain ({smoothing_method})")

    fig.suptitle("Comparison of different smoothing techniques")
    fig.tight_layout()
    save_plot("comparison_smoothing", fig)

def long_cable(signal10m, reference):
    t = [signal10m["t"], reference["t"]]
    signals = [smooth_signal([signal10m["CH1"], signal10m["CH2"]]), smooth_signal([reference["CH1"], reference["CH2"]])]
    signal_names = [["Reference1 + 10m", "Reference2"], ["Reference1", "Reference2"]]
    titles = ["Delay between a reference and a 10m cable", "Delay between the two references"]
    delays = []

    fig, ax = plt.subplots(1,2, figsize=(6,3))
    for i, signal in enumerate(signals):
        for j, sig in enumerate(signal):
            ax[i].plot(t[i] * 1e9, sig, label=signal_names[i][j])
        ax[i].set_xlabel("$t\;[ns]$")
        ax[i].set_ylabel("Voltage$\;[V]$")
        ax[i].set_title(rf"{titles[i]}")
        ax[i].legend()


        dT = np.mean(np.diff(t[i]))
        argmax_derivative_CH1 = np.argmax(np.diff(signal[0]))
        argmax_derivative_CH2 = np.argmax(np.diff(signal[1]))

        tmax_derivative_CH1_ns = (argmax_derivative_CH1 * dT + np.min(t[i])) * 1e9
        tmax_derivative_CH2_ns = (argmax_derivative_CH2 * dT + np.min(t[i])) * 1e9
        delay = np.abs(tmax_derivative_CH2_ns - tmax_derivative_CH1_ns)
        delays.append(delay)
        ax[i].vlines([tmax_derivative_CH1_ns, tmax_derivative_CH2_ns], np.min(signal[0]), np.max(signal[0])*0.97, linestyles="dotted")

        average_length = np.average([tmax_derivative_CH1_ns, tmax_derivative_CH2_ns])
        ax[i].text(average_length, np.max(signal[0]), rf"$\tau={np.round(delay,2)}\;ns$", horizontalalignment='center')

    f = open(file=os.path.join(dir_path, "Out", f"long_cable.md"), mode='w')

    l=10
    total_delay = np.abs(delays[0]-delays[1])
    v=l/((total_delay) * 1e-9)

    f.write(rf"$v_p=\dfrac{{l}}{{t}} = \dfrac{{{l}}}{{{np.round(total_delay,2)}n}} \approx {np.round(v *1e-6,2)}\cdot 10^6 \;m/s = {np.round(v/speed_of_light,2)}c_0$")
    f.write("\n")
    f.write(rf"$v_p = \dfrac{{c}}{{\sqrt{{\epsilon_r}}}}\to \epsilon_r = \left(\dfrac{{c}}{{v_p}}\right)^2={np.round((speed_of_light/v)**2,2)}$")
    f.close()

    plt.suptitle("Delay due to an extra 10m cable")
    plt.tight_layout()
    save_plot("long_cable", fig)

def calibration(signal):
    fig, ax = plt.subplots()
    ax.plot(signal["t"] * 1e9, smooth_signal(signal["CH1"]))
    ax.set_xlabel("$t\;[ns]$")
    ax.set_ylabel("Voltage$\;[V]$")
    ax.set_title(rf"Maximum reflection")
    ax.legend()

    plt.tight_layout()
    save_plot("calibration", fig)

def reflections(signals, names):
    fig, ax = plt.subplots()
    E_i = []
    E_r = []

    for i, signal in enumerate(signals):
        smoothed_signal = smooth_signal(signal["CH1"], smoothing_coef=40)
        ax.plot(signal['t'] * 1e9, smoothed_signal, label=names[i])

        N = np.size(smoothed_signal)
        cE_i = np.mean(smoothed_signal[int(0.6 * N):int(0.7 * N)])
        E_i.append(cE_i)
        E_r.append(np.mean(smoothed_signal[int(N * 0.9):])- cE_i)
    
    E_i = np.array(E_i)
    E_r = np.array(E_r)
    Gamma = E_r / E_i
    Z0 = 50

    ax.set_xlabel("$t\;[ns]$")
    ax.set_ylabel("Voltage$\;[V]$")
    ax.set_title(rf"Reflection at different loads")
    ax.legend()

    f = open(file=os.path.join(dir_path, "Out", f"reflection.md"), mode='w')
    f.write(rf"\begin{{tabular}}{{|c|c|c|c|c|}}")
    f.write("\n \\hline \n")
    f.write(rf"Load & $E_i\;[V]$ & $E_r\;[V]$ & $\Gamma$ & $Z_L$")
    f.write("\\\\ \\hline \n")
    for i in range(len(names)):
        f.write(rf"{names[i]} & {np.round(E_i[i],2)} & {np.round(E_r[i],2)} & {np.round(Gamma[i],2)} & {np.round(Z0 * (1 + Gamma[i])/(1-Gamma[i]),2)}")
        if i != len(names) -1:
            f.write("\\\\ \n ")
        else:
            f.write("\\\\ \\hline \n ")

    f.write(rf"\end{{tabular}}")
    f.close()


    plt.tight_layout()
    save_plot("reflections", fig)


measurements = read_measurements(dir_path)
# test_smoothing(measurements["LongCable"])

# Assignment 1
# long_cable(measurements["LongCable"], measurements["NoCable"])

# Assignment 2
# calibration(measurements["OpenEnd"])
names = ["MatchedGreen", "ShortedGreen", "Black", "Grey"]
reflections([measurements[name] for name in names], names)