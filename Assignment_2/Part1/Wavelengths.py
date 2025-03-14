"""
Code for assignment 1 and 2
"""

import pandas as pd
import os as os
import numpy as np
import matplotlib.pyplot as plt

f = 8.2e9

dir_path = os.path.dirname(os.path.realpath(__file__))

def getAssignment(assignment_number = 1):
    input_file = os.path.join(dir_path, f"assignment{assignment_number}.csv")
    data = pd.read_csv(input_file, sep = "\t")
    distances = data["Distance"]
    if assignment_number == 1:
        wavelengths = 4 * np.abs(np.diff(distances))
    if assignment_number == 2:
        wavelengths = 2 * np.abs(np.diff(distances))
    wavelengths = wavelengths[~np.isnan(wavelengths)]

    return wavelengths

wavelengths = []
wavelengths.append(getAssignment(1))
wavelengths.append(getAssignment(2))

# c = f * lambda
names = ["obstr", "phase"] 
txt = ""
for i in range(0,2):
    txt = txt + (f"$v_{{{names[i]}}}={(np.round(np.mean(wavelengths[i] * f * 1e-10), 2))} \\pm {np.round(np.std(wavelengths[i] * f * 1e-10),2)} \\cdot 10^{8} \\;[\\text{{m/s}}]$ with $n={wavelengths[i].size}$ measurements \n")
print(txt)

fig, ax = plt.subplots()
ax.boxplot(wavelengths, showmeans = True, meanline=True)
ax.set_xticklabels([rf"$v_{{\text{{obstr}}}} = {np.round(np.mean(wavelengths[0]),2)}\;[\text{{cm}}], n = {wavelengths[0].size}$",
                    rf"$v_{{\text{{phase}}}} = {np.round(np.mean(wavelengths[1]),2)}\;[\text{{cm}}], n = {wavelengths[1].size}$"])

f = open(file=os.path.join(dir_path, "Out", f"Velocities_ass1n2.md"), mode='w')
f.write(txt)
f.close()

fig_out = os.path.join(dir_path, "Out", f"Wavelengths_ass1n2.svg")
ax.set_title("Wavelengths using obstruction and phase measurements")
ax.set_ylabel("Lenght [cm]")
plt.savefig(fig_out, transparent=True)
# plt.show()