"""
Code for assignment 1 and 2
"""

import pandas as pd
import os as os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

import scienceplots
plt.style.use(['science','ieee'])

f = 8.2e9

dir_path = os.path.dirname(os.path.realpath(__file__))

def getAssignment(assignment_number = 1):
    input_file = os.path.join(dir_path, f"assignment{assignment_number}.csv")
    data = pd.read_csv(input_file, sep = "\t")
    print(data)
    distances = data["Distance"]
    if assignment_number == 1:
        wavelengths = 4 * np.abs(np.diff(distances))
    if assignment_number == 2:
        wavelengths = 2 * np.abs(np.diff(distances))
    wavelengths = wavelengths[~np.isnan(wavelengths)]

    return wavelengths

def obstructedPower():
    input_file = os.path.join(dir_path, f"assignment1.csv")
    df = pd.read_csv(input_file, sep = "\t")
    values = {}
    values["Min"] = df[df["Min or max"] == "Min"].reset_index(drop=True)
    values["Max"] = df[df["Min or max"] == "Max"].reset_index(drop=True)

    fig, ax = plt.subplots()
    for key, value in values.items():
        ax.plot(value["Distance"], 10**(3) * 10 ** ((np.array(value["Amplitude (dB)"]))/20), label=ke ,)
    
    ax.set_xlabel("Distance (cm)")
    ax.set_ylabel("Amplitude (mW)")
    ax.set_title("Received maximum and minimum power at different distances")
    plt.legend()
    fig.savefig(os.path.join(dir_path, "Out", "obstructedPower.svg"), transparent = True)

def assignment5():
    input_file = os.path.join(dir_path, f"assignment5.csv")
    df = pd.read_csv(input_file, sep = "\t")
    print(df)
    fig, ax = plt.subplots()
    ax.plot(df["degree"], ((np.array(df["Unnamed: 0"]))), marker= 'o', ls="")
    ax.set_xlabel("Rotation (degrees)")
    ax.set_ylabel("Power (dB)")
    ax.set_title("Received power at a select few rotations")
    plt.legend()
    fig.savefig(os.path.join(dir_path, "Out", "rotationPower.svg"), transparent = True)

def assignments():
    wavelengths = []
    wavelengths.append(getAssignment(1))
    wavelengths.append(getAssignment(2))

    # c = f * lambda
    names = ["obstr", "phase"] 
    txt = ""
    for i in range(0,2):
        v = wavelengths[i] * f * 1e-10
        mean_v = (np.round(np.mean(v), 2))
        std_v = np.std(v, ddof=1)
        confidence = 0.95 # 95% confidence interval
        tstar = t.ppf((1 + confidence) / 2, v.size-1)
        print(tstar)
        ME =  np.round(tstar * (std_v / np.sqrt(v.size)), 2)
        
        txt = txt + (f"$v_{{{names[i]}}}={mean_v} \\pm {ME} \\cdot 10^{8} \\;[\\text{{m/s}}]$\n")
    print(txt)

    fig, ax = plt.subplots()
    ax.boxplot(wavelengths, showmeans = True, meanline=True, widths = 0.5)
    ax.set_xticklabels([rf"$\lambda_{{\text{{obstr}}}} = {np.round(np.mean(wavelengths[0]),2)}\;[\text{{cm}}], n = {wavelengths[0].size}$",
                        rf"$\lambda_{{\text{{phase}}}} = {np.round(np.mean(wavelengths[1]),2)}\;[\text{{cm}}], n = {wavelengths[1].size}$"])

    fi = open(file=os.path.join(dir_path, "Out", f"Velocities_ass1n2.md"), mode='w')
    fi.write(txt)
    fi.write(rf"\n Is the 95% confidence interval assuming a normal distribution")
    fi.close()

    fig_out = os.path.join(dir_path, "Out", f"Wavelengths_ass1n2.svg")
    ax.set_title("Wavelengths using obstruction and phase measurements")
    ax.set_ylabel("Lenght [cm]")
    plt.tight_layout()
    plt.savefig(fig_out, transparent=True)
    # plt.show()

# obstructedPower()
# assignments()
assignment5()