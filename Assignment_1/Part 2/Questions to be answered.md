## Assignment 2
## Part 1. Dielectric in Coaxial Cable: the Estimation of the Propagation Speed and Relative Permittivity
The goal is to compute the relative permittivity of the coaxial cable’s dielectric filling based on the
measured propagation delay and the cable’s physical length.
Two waveforms are acquired, the “reference”, with the short “blue” cable connected to the scope
(Figure 2. 2), and the “delayed” waveform, with a 10 m “green” cable inserted between the “blue”
cable and the scope (Figure 2. 3). The length of "blue" signal and trigger cables are equal - that gives a
possibility to directly estimate the time delay for the propagation of signal through the additional
"green" cable comparing time delays of signal fronts for both cases recorded with different length of
"signal" cables.
Use the TDR_USB_SCOPE.m Matlab script located in the TDR folder on the desktop to save your data
for postprocessing. The variables t and y, are the time vector in seconds and the amplitude vector in
Volts, respectively.
You can also read the delays directly on the oscilloscope following the steps below.
- Measure the delay between the 2 channels (use softkeys 1 to 4 as shown in Figure 2. 5), this is
your time reference.
- Insert the green cable (10 m) between the tee and the blue cable using a female-female
adapter, as in the Figure 2. 3.
- Measure the new delay between the two channels (see Figure 2. 6).
Knowing the propagation time through the cable as well as its physical length, you can calculate the
propagation velocity inside the coaxial cable and deduce the relative permittivity of its dielectric filling.
## Part 2. Time Domain Reflectometry: estimate the load’s impedance
The goal of this assignment is to compute the impedance of the loads using the measured reflection
coefficients. Compared with frequency domain techniques, time domain reflectometry (TDR) provides
a more intuitive and direct look at the device under test (DUT) characteristics. A step pulse is
transmitted through the line under investigation and the incident and reflected voltage waves are
measured with an oscilloscope. Interpret the recorder time dependency of the signals when the
oscilloscope measures initially only the incident signal and then - the sum of incident and reflected
from the load signals. See Agilent’s TDR theory application note for more details about your
measurements interpretation.
- Using the measured signals, for each unknown load compute the reflection coefficient and determine the impedance $Z$ knowing that $Z =50Ω$ 
- Explain the difference between measurements of load’s impedance in time and frequency domains.


| Measurement |                               |
| ----------- | ----------------------------- |
| 000         | Long cable 10m (assignment 1) |
| 001         | Without cable                 |
| 002         | 10m open end (part 2)         |
| 003         | Green matched load            |
| 004         | Green shorted                 |
| 005         | Black wire                    |
