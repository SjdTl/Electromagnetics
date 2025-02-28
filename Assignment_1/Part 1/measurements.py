import pandas as pd
import os 
from scipy.constants import speed_of_light as c
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, f"measurements.csv")
a = 22.86e-3  # 22.86 mm in meters

m = pd.read_csv(file_path)

m["lambda_0"] = c / (m["f (GHz)"] * 10e9)
m["lambda_w (theory)"] = m["lambda_0"] / (np.sqrt(1 - (m["lambda_0"]/ (2 * a))**2))
m["VSWR (measured)"] = m["Emax"] / m["Emin"]
m["|Γ| (measured)"] = (m["VSWR (measured)"] - 1) / (m["VSWR (measured)"] + 1) 
print(m)
m.to_csv(os.path.join(dir_path, f"measurements_calc.csv"))