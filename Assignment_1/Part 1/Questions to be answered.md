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
