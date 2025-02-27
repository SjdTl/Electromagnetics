## Assignment 1


1. Determine the phase velocity $v_{p}(f)=\lambda_{w}f$, $\lambda_{w}=\dfrac{\lambda_{0}}{\sqrt{ 1-\left( \cfrac{\lambda_{0}}{2a} \right)^{2} }}$,  $\lambda_{0}=c /f$  of the EM wave in the given waveguide within the frequency band from 8GHz till 12GHz theoretically (using provided equations) and on one fixed frequency at this band experimentally, using the measurements of standing wave. Make measurements a few times to improve the accuracy of your estimation and to estimate the measurement error. Analyse the frequency dependence of the EM waves propagation velocity in waveguide and compare experimental result with theoretical prediction, estimate the accuracy of your measurements.

Combining equations to obtain $v_{p}(f)=\dfrac{c}{\sqrt{ 1-\left( \cfrac{c}{2af} \right)^{2} }}$ 
Which gives $v_{p}(10G)=3.97 \cdot 10^{8}\;m/s$ (see ```calculations.py```)

3. Compare the measured velocities with that in free space and explain your observations.
4. Determine the absolute value of the reflection coefficients for different loads (see below) and the fraction of power, which is delivered into this load from the transmission line (waveguide). To this end, measure the voltage-standing-wave ratio ($VSWR=\dfrac{E_{\text{max}}}{E_{\text{min}}}=\dfrac{1+\lvert \Gamma \rvert}{1-\lvert \Gamma \rvert}$) for: 
	1. Movable short circuit – the piece of the waveguide that has a variable depth that changes using a metal piston with contacting fingers riding against the sides of the waveguide. Check the reflection coefficients for a few positions of the piston. Combine these measurements with measurements for the task 4 (below).
	2. Matched load
	3. Open waveguide
	4. Horn antenna (Antenna is a device that have not only a function to direct electromagnetic waves in free space in specific direction but also to match impedances of the transmission line and free space, preventing wave reflections and energy losses) 
5. Compare patterns of standing waves (nodes-antinodes location) for a few positions of the piston of the movable short circuit (see task 3a, the standing wave patterns looks like in Fig.1.6). Use the first position as a reference, measure all other relatively to it. Use the normalization of the depth of the short to the wavelength of the EMW in the waveguide. Explain the shift of standing waves antinodes.

Additional tasks for the report:
- What other parameters of waveguide and loads can be estimated from your measurements?
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