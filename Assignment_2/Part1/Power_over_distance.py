"""
Code for assignment 1 and 2
"""

import pandas as pd
import os as os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import scienceplots
plt.style.use(['science','ieee'])

f = 8.2e9

dir_path = os.path.dirname(os.path.realpath(__file__))

def getAssignment(assignment_number = 3):
    input_file = os.path.join(dir_path, f"assignment{assignment_number}.csv")
    data = pd.read_csv(input_file, sep = "\t")
    distances_cm = np.array(data["Distance"])
    amplitudes_dB = np.array(data["Amplitude (dB)"])

    return distances_cm, amplitudes_dB

def PowerOverDistance(x, A, b):
    """
    Function Signal Power = const / x^b
    """
    return A / x**b

distances_cm, amplitudes_dB = getAssignment(3)
amplitudes = 10**(amplitudes_dB/20)
distances = 0.01 * distances_cm

fig, ax = plt.subplots()
ax.plot(distances, amplitudes, label="Measurements")

(popt, pcov) = curve_fit(PowerOverDistance, distances, amplitudes, [amplitudes[0], 2])
A = popt[0]
b = popt[1]
perr = np.sqrt(np.diag(pcov))
print(perr, popt)
Astd = perr[0]
bstd = perr[1]

ax.plot(distances, A / distances**b, label = rf"$\frac{{A}}{{R^{{b}}}}=\frac{{{np.round(A, 2)}\pm {np.round(Astd,3)}}}{{R^{{{np.round(b, 2)} \pm {np.round(bstd,2)}}}}}$")
ax.set_title("Power over distance")
ax.set_ylabel("Power (W)")
ax.set_xlabel("Distance (m)")

plt.legend()
fig_out = os.path.join(dir_path, "Out", f"PowerOverDistance_ass3.svg")
plt.savefig(fig_out, transparent=True)
# plt.show()