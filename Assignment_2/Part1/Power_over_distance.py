"""
Code for assignment 1 and 2
"""

import pandas as pd
import os as os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f = 8.2e9

dir_path = os.path.dirname(os.path.realpath(__file__))

def getAssignment(assignment_number = 3):
    input_file = os.path.join(dir_path, f"assignment{assignment_number}.csv")
    data = pd.read_csv(input_file, sep = "\t")
    distances = np.array(data["Distance"])
    amplitudes_dB = np.array(data["Amplitude (dB)"])

    return distances, amplitudes_dB

def PowerOverDistance(x, A, b):
    """
    Function Signal Power = const / x^b
    """
    return A / x**b

distances, amplitudes_dB = getAssignment(3)
amplitudes = 10**(amplitudes_dB/20)

fig, ax = plt.subplots()
ax.plot(distances, amplitudes, label="Measurements")

(popt, pcov) = curve_fit(PowerOverDistance, distances, amplitudes, [amplitudes[0], 2])
A = popt[0]
b = popt[1]

ax.plot(distances, A / distances**b, label = rf"$\frac{{A}}{{R^{{b}}}}=\frac{{{np.round(A, 2)}}}{{R^{{{np.round(b, 2)}}}}}$")

ax.set_title("Power over distance")
ax.set_ylabel("Power (W)")
ax.set_xlabel("Distance (cm)")

plt.legend()
fig_out = os.path.join(dir_path, "Out", f"PowerOverDistance_ass3.svg")
plt.savefig(fig_out, transparent=True)
# plt.show()