# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:10:15 2024

Script illustrating the polarization pattern shown in the EE2P1
lab seesion 2

@author: PJA
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio
import pandas as pd
import scienceplots
plt.style.use(['science','ieee'])

#------------------------------------------------------------------------------
#                                FUNCTIONS
#------------------------------------------------------------------------------

def PolarPhasor(phi, tau):
    '''
    1.1 - Polarization Phasor (eq. 2)
    Parameters
    ----------
    phi : angle of orientation in radians [-pi, pi]
    tau : angle of ellipticity in radians [-pi/4, pi/4]

    Returns
    -------
    p : complex polarization ratio (polarization phasor)

    '''
    p = (np.tan(phi)+1j*np.tan(tau))/(1-1j*np.tan(phi)*np.tan(tau))
    return p


def FresnelCoeff(Er_1, Er_2, th_i):
    '''
    1.2 Complex Fresnel reflection coefficient (eq. 14)
    Parameters
    ----------
    Er_1 : relative dielectric permittivity of medium 1
    Er_2 : Er_2 relative dielectric permittivity of medium 2
    th_i : angle of incidence [radians]

    Returns
    -------
    Gamma_h : Fresnel reflection coefficient for horizontal polarization
    Gamma_v : Fresnel reflection coefficient for vertical polarization
    
    '''
    Gamma_h = (np.cos(th_i)-np.sqrt(Er_2/Er_1-np.square(np.sin(th_i))))/ \
        (np.cos(th_i)+np.sqrt(Er_2/Er_1-np.square(np.sin(th_i))))              
    Gamma_v = -(Er_2*np.cos(th_i)-Er_1*np.sqrt(Er_2/Er_1-np.square(np.sin(th_i))))/ \
        (Er_2*np.cos(th_i)+Er_1*np.sqrt(Er_2/Er_1-np.square(np.sin(th_i))))
    return Gamma_h, Gamma_v


def MultipathRxPolarState(pt, f, R, H, Er, free_space = False):
    '''
    1.3 Polarization state of the received wave in multipath propagation  (eq. 13)
    Parameters
    ----------
    pt : transmit wave polarization phasor
    f : frequency [Hz]
    R: distance between antennas [m]
    H: reflector height [m]
    Er: reflector material relative permittivity
    
    Returns
    -------
    pr: received wave polarization phasor
    
    '''
    k = 2*np.pi*f/3e8;         # wave number 
    th_i = np.arctan(R/2/H);     # angle of incidence
    print(f"Incident angle: {th_i }")
    deltaR = 2*np.sqrt(R**2/4+H**2)-R
    if free_space == True:
        [G_h, G_v] = [0,0]
    else: 
        [G_h, G_v]=FresnelCoeff(1, Er, th_i)
    print(f"[G_h, G_v] = {[G_h, G_v]}")

    pr = pt*(1+G_v*np.exp(1j*k*deltaR))/(1+G_h*np.exp(1j*k*deltaR))
    print(f"[pr, pt] = {pr, pt}")
    return pr


def PolarPattern(p):
    '''
    Parameters
    ----------
    p : polarization phasor

    Returns
    -------
    x : angles [0 2pi]
    V : polarization pattern

    '''
    x = np.linspace(0, 2*np.pi, 361)
    Et_h = np.exp(1j*x)
    Et_v = Et_h*p
    V = Et_h*np.cos(x)+Et_v*np.sin(x)
    return x, V

def saveplot(name, folder = None):
    import os as os
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if folder == None:
        file_path = os.path.join(dir_path, "Out", f"{name}.svg")
    else:
        file_path = os.path.join(dir_path, "Out", f"{folder}", f"{name}.svg")

    plt.savefig(file_path, transparent=True)

def angular_patterns(phi,tau,f, R, H, Er, plot = False, name_plot = "angular_patterns", folder_name = None, free_space = False):
    pt = PolarPhasor(phi, tau)#np.pi/4)    # transmit vertical pol
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for h in H:
        pr = MultipathRxPolarState(pt, f, R, h, Er, free_space=free_space)
        th, rho = PolarPattern(pr)
        ax.plot(th, np.abs(rho)/np.max(np.abs(rho)),label=round(h,2))

    
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title(f"Polarization Pattern {name_plot}", va='bottom')
    plt.legend(title="H",loc='best', fontsize=6, fancybox=True)
    saveplot(f"{name_plot}", folder=folder_name)
    plt.tight_layout()
    if plot:
        plt.show()
#-------------------------  END OF FUNCTIONS ----------------------------------

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import mat73

grData = mat73.loadmat(os.path.join(dir_path, "group-02.02.mat"))
grDataDF = pd.DataFrame(grData['session2'])
grDataDF=grDataDF.drop("group", axis=1)
pd.set_option("display.width", 400)  # Increase the display width
pd.set_option("display.max_colwidth", None)  # Allow full column width
print(grDataDF)
# ------------------------------------------------

f = grData['session2']['task2']['frequency']
R = grData['session2']['task2']['antennas_distance']
Er = grData['session2']['task2']['dielectric_prermittivity']
H = grData['session2']['task2']['reflection_height']

def do_assignments(orientation = "horizontal"):
    if orientation == "horizontal":
        phi = 0 #angle of orientation [-pi, pi]
        tau = 0 #angle of ellipticity [-pi/4. +pi/4]
    if orientation == "vertical":
        phi = np.pi/2
        tau = 0
    if orientation == "circular":
        phi = 0
        tau = np.pi/4

    print("Dielectric")
    print("-------------------------------")
    angular_patterns(phi,tau,f, R, H, Er, plot=False, name_plot =   f"dielectric_reflection_{orientation}", folder_name=f"{orientation}")
    print("Metallic")
    print("-------------------------------")
    angular_patterns(phi,tau,f, R, H, 1e9, plot=False, name_plot = f"metallic_reflection_{orientation}", folder_name=f"{orientation}")
    print("Free space")
    print("-------------------------------")
    angular_patterns(phi,tau,f, R, H, 1, plot=False, name_plot =    f"free_space_{orientation}", folder_name=f"{orientation}", free_space=True)
    if orientation == "circular":
        brewster = 1.21 #rad
        Hb = R/(2*np.tan(brewster))
        angular_patterns(phi,tau,f, R, [Hb], Er, plot=False, name_plot =    f"Brewster_{orientation}", folder_name=f"{orientation}", free_space=False)


# do_assignments("horizontal")
# do_assignments("vertical")
do_assignments("circular")


## Fresnel / Brewster
## glass example (n2 = 1.5)

# plt.figure()
# plt.axes()
# coefficients = np.arange(1.5,6,1)
# th_i = np.linspace(0, np.pi/2, 500)
# # for i in coefficients:
# Gh, Gv = FresnelCoeff(1, (2.6342 - 0.0195j)**2, th_i)

# #find the Brewster angle
# th_i_min = th_i[np.argmin(np.abs(Gv))]
# print(f"The Brewster angle is {th_i_min*180/np.pi} degrees")

# plt.figure()
# plt.plot(180*th_i/np.pi,np.abs(Gh),color='b')
# plt.plot(180*th_i/np.pi,np.abs(Gv),color='r')
# # plt.text(180 * th_i[0] / np.pi, np.abs(Gh[0]), f'{i:.2f}', color='b', fontsize=9, verticalalignment='bottom')
# # plt.text(180 * th_i[0] / np.pi, np.abs(Gv[0]), f'$\\epsilon_r$= {i:.2f}', color='black', fontsize=9, verticalalignment='bottom')

# plt.title('Fresnel reflection coefficients')
# plt.xlabel('Incident angle [deg]')
# plt.ylabel('Reflection coefficient')
# plt.legend(['$\\Gamma_H$','$\\Gamma_V$'])
# saveplot("Brewster")
# plt.show()
