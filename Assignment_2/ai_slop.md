## Briefing Document: EE3P11 EM Practicum - Session 2: Free Space Propagation of EM Waves

**Date:** 2024-05-15 (Based on document dates) **Subject:** Review of Sources for EE3P11 EM Practicum - Session 2 **Prepared For:** Students of EE3P11 - EM Practicum **Prepared By:** AI Assistant

This briefing document summarises the main themes and important information from the provided sources for the EE3P11 EM Practicum, Session 2, focusing on the free space propagation of electromagnetic waves. The session aims to extend basic knowledge, provide physical insight into multipath propagation, offer practical knowledge on polarisation and antennas, and allow students to exercise theoretical knowledge on reflection.

### 1. Assignment Description ("Assignment_description.pdf")

This document outlines the goals, setup, and specific assignments for the second session of the EM Practicum, focusing on free space propagation.

**1.1. Goals of the Practicum Session:**

The primary goals are to:

1. "Extend the basic knowledge on electromagnetic wave propagation in free space including the propagation velocity and propagation loss;"
2. "get physical insight in multi-path propagation of electromagnetic waves;"
3. "get practical knowledge on the polarization of electromagnetic waves and antennas, different states of the polarization of the waves, and polarization control;"
4. "exercise the theoretical knowledge on electromagnetic waves' reflection from a flat boundary between different media."

**1.2. Experimental Setup:**

The experiment utilises a setup with:

- A rail supporting two horn antennas (transmit and receive).
- A Vector Network Analyser (VNA) connected to the antennas, capable of measuring amplitudes and phases of the received signal over a wide frequency band.
- One antenna mounted on a rotation table for studying directivity.
- A frequency in the X-band (8.0 – 10.0 GHz) specific to each group, provided in a Matlab MAT file.

The document acknowledges that the lab environment is not true free space due to reflections and obstacles, but argues that within the close area between antennas, free space propagation can be approximated, supported by the relative permittivity of air being close to unity.

**1.3. Assignment 1: Free Space Propagation (45 min)**

This assignment includes several sub-tasks:

- **1.1. Wavelength and propagation velocity in free space using obstructing object:**
- Uses horizontally polarised antennas and an array of horizontal wires placed between them.
- Moving the wire array along the line of sight will cause periodic changes in received signal amplitude due to standing waves.
- Students are expected to measure the period of this standing wave pattern to determine the wavelength and then calculate the phase velocity.
- "Use this modulation to measure the period of standing wave pattern and, as result, the wavelength of EM wave with a given frequency in free space (in air)."
- Students should also attempt to create a simple mathematical model of the observed amplitude dependency.
- **1.2. Wavelength and propagation velocity in free space using phase measurements:**
- Utilises the VNA's phase measurement capability.
- By changing the distance between antennas, the phase of the received wave changes ($\phi = 2\pi r / \lambda$).
- Students need to measure the distance over which the phase changes by 360 degrees to determine the wavelength and subsequently the propagation velocity.
- "For the wavelength measurement we will need to measure the distance between two points on the rail when the phase of the receive signal will change for 360 degrees..."
- **1.3. Measurement of the relation between the power of received signal and the propagation distance:**
- Involves measuring the received signal strength at various distances with horizontally polarised antennas.
- Students are expected to process the data assuming a power law relationship: "Signal Power = const / R x" and estimate the value of 'x', providing justification for their result (the expected inverse square law for free space propagation).
- **1.4. The influence of polarisation:**
- Investigates polarisation isolation by rotating the receiver antenna by 90 degrees relative to the horizontally polarised transmitter at a fixed distance.
- "Measure the polarization isolation (in dB scale) between orthogonally polarized antennas..."
- Examines the effect of the orientation of horizontal wires placed between orthogonally polarised antennas, relating the reradiated wave's polarisation to the wire orientation.
- "Make interpretation of the results assuming that the wires reradiate EM waves with linear polarization, which is parallel to wires."
- **1.5. Study of the antenna pattern (directivity) of the horizontally polarized horn antenna:**
- Uses the rotation table to estimate the antenna's spatial directivity, specifically the -3dB beamwidth.
- "estimate the spatial directivity of the horn antennas – the antenna beamwidth that can be defined as the angular difference between directions when the received power decreased to the level of - 3dB from the maximum value of received power."

**1.4. Assignment 2: Simulation of the measurements of the polarisation state of the EM Wave using the polarization pattern method:**

This assignment focuses on deepening understanding of EM wave polarisation and reflection effects.

- **Theoretical Overview:** Students are referred to selected chapters from Mott, H. "Polarization in Antennas and Radar" (available on Brightspace). The document introduces the representation of polarised waves using horizontal and vertical components and the complex polarisation ratio. It also discusses the polarisation sensitivity of receiving antennas and the concept of the polarisation pattern measurement using a rotating linearly polarised antenna.
- Equation (1) defines the electric field vector in terms of horizontal and vertical components.
- Equation (2) defines the complex polarisation ratio $\chi$.
- Equation (5) states that the received voltage is proportional to the scalar product of the incident field and the receiver antenna's effective length.
- The polarisation pattern allows estimation of the axis ratio (Eq. 6), ellipticity angle (Eq. 7), orientation angle ($\phi$), and amplitude of the received wave.
- **Multipath Propagation:** The document introduces the concept of multipath propagation, particularly reflection from the ground surface (floor). Fresnel reflection coefficients are mentioned as governing the reflection of horizontally and vertically polarised components.
- Equation (8) shows the received signal as a sum of direct and reflected waves.
- Equation (9) provides a more detailed form for the received wave considering the polarisation vector of the transmitted wave.
- Equations (10) give the received amplitudes for horizontally and vertically polarised transmitted waves in a specific multipath scenario.
- Equations (11), (12), and (13) extend this to cases with complex polarisation ratios for the transmitted wave and the resulting received wave.
- Equations (14) define the Fresnel reflection coefficients ($\Gamma_h$ and $\Gamma_v$) depending on the relative dielectric permittivity of the reflecting surface and the incident angle.
- **Practical Tasks:**
- **Implement Matlab functions:**Polarisation phasor of EMW (Eq. 2).
- Complex Fresnel reflection coefficients (Eq. 14).
- Polarisation state of the received wave in multipath propagation (Fig. 6, Eq. 13).
- Illustrate implementations with plots and analysis.
- Plot Fresnel reflection coefficients vs. incident angle and find the Brewster angle.
- **Develop Matlab script for simulation of polarisation pattern measurements:**Simulate polarisation patterns (similar to Fig. 3) for transmitted vertical, horizontal, and circular polarisations in:
- Free space (Fig. 5).
- Multipath case with metallic reflecting plate (different heights H).
- Multipath case with dielectric reflecting plate (different heights H).
- Analyse the case of transmitted circular polarisation when the incident angle equals the Brewster angle for the dielectric plate.
- Simulation parameters (frequency, dielectric permittivity, antenna distance, reflection heights) are provided in session2.task2 in the group's MAT file.
- **Short notes on demo hardware:** Briefly describes the horn antennas used for transmitting and receiving microwaves in the X-band, noting that the rectangular horn maintains linear polarisation from the waveguide, while the circular horn can generate arbitrary polarisations by controlling the amplitude and phase of signals fed to its two ports.

### 2. Example Matlab Script ("Example.txt")

This file provides an example Matlab script illustrating the generation of a polarisation pattern for a circularly polarised transmitted wave in a multipath scenario with a dielectric reflecting plate.

- It defines several functions:
- PolarPhasor(phi, tau): Calculates the complex polarisation ratio.
- FresnelCoeff(Er_1, Er_2, th_i): Calculates the Fresnel reflection coefficients.
- MultipathRxPolarState(pt, f, R, H, Er): Calculates the received wave's polarisation phasor in multipath.
- PolarPattern(p): Generates the polarisation pattern.
- The script loads data from a MAT file (group-02.02.mat).
- It sets parameters (frequency, distance, dielectric permittivity, reflection heights).
- It defines the transmitted polarisation as circular.
- It iterates through different reflection heights (H), calculates the received polarisation state using MultipathRxPolarState, generates the polarisation pattern using PolarPattern, and plots the results on a polar plot.
- There are commented-out sections for plotting Fresnel coefficients against incident angle.

**Key takeaway:** This script provides a starting point and example for Assignment 2, demonstrating how to implement the necessary functions and simulate polarisation patterns in a multipath environment. Students will need to adapt this script to the different scenarios and analyses required in the assignment.

### 3. Excerpts from "Polarization in antennas and radar.pdf" (Mott, H.)

These excerpts provide the theoretical background on wave polarisation, essential for understanding Assignment 2.

- **Chapter 2: Representation of Wave Polarization:**
- Introduces the concept of the polarisation ellipse and its parameters: axial ratio, tilt angle ($\tau$), and sense of rotation.
- Explains how a general, nonplanar harmonic wave can be represented by two orthogonal components.
- Discusses linear and circular polarisation as special cases of elliptical polarisation.
- Equation (2.1) represents a nonplanar harmonic wave.
- Figures 2.1, 2.2, and 2.3 visually depict the polarisation ellipse, tilted ellipse, and coordinate transformations.
- Explains the mathematical relationships between the electric field components and the polarisation ellipse parameters (e.g., Equations 2.11 onwards).
- Defines the axial ratio ($n/m$) and tilt angle ($\tau$) mathematically.
- Introduces the complex polarisation ratio $P = E_y / E_x = (n/m)e^{j\delta}$ (Equation 2.73 in the full text, related to the assignment's $\chi$).
- **Chapter 3: Polarization Matching of Antennas:**
- Discusses the importance of polarisation alignment between transmitting and receiving antennas for efficient power transfer.
- Introduces the concept of the effective length vector of an antenna, which characterises its polarisation sensitivity.
- Equation (3.15) (mentioned in the assignment description) likely relates the received voltage to the incident electric field and the effective length vector.
- Figure 3.3 illustrates transmit and receive antenna coordinate systems.
- Defines the polarisation match factor ($\rho$) which quantifies the power transfer efficiency based on polarisation alignment.
- **Chapter 8: Polarization Measurements (Section 8.4, "The Polarization Pattern"):**
- Explains how the polarisation state of an unknown wave can be determined by measuring the received power as a linearly polarised receiving antenna is rotated about the line of sight.
- The resulting plot of received power versus rotation angle is the "polarisation pattern".
- Figure 8.1 shows typical polarisation patterns for linear and elliptical polarisation.
- Relates the characteristics of the polarisation pattern (maximum and minimum received power, angle of maximum) to the parameters of the polarisation ellipse (axial ratio, orientation).
- Equations (8.4), (8.5), and (8.6) (likely corresponding to Assignment Eq. 6, 7, and the orientation angle) describe these relationships.

**Key takeaway:** These excerpts provide the fundamental theory behind electromagnetic wave polarisation and how it can be characterised and measured using the polarisation pattern method, which is the core of Assignment 2.

### 4. Excerpts from "t.pdf" (Likely supplementary material):

This document contains figures and descriptions related to some of the experiments in Assignment 1.

- **Slide 20:** Depicts the setup for measuring wavelength using an obstructing metallic grid. It shows a transmitter, transmit antenna, a movable vertical metallic grid, a receive antenna, a detector (voltmeter), and a rail. A graph shows the received voltage (proportional to power) varying periodically as the grid is moved.
- It poses questions about the distance between minima in the pattern and the explanation of the observed phenomena based on reflection and transmission by the grid leading to standing waves.
- This directly relates to Assignment 1.1.
- **Slide 21:** Illustrates the setup for measuring the relationship between received power and propagation distance. It shows a similar setup without the obstructing grid, and a graph showing a decaying received voltage as the distance between antennas (R) increases.
- It states that voltage (V) is proportional to power (P) and follows a power law: $V \sim P = C / R^x$.
- It suggests taking a logarithm to estimate the unknown power 'x' by fitting a linear regression to $\log_{10} V = \log_{10} C - x \cdot \log_{10} R$.
- This directly relates to Assignment 1.3.

**Key takeaway:** This supplementary material provides visual context and guidance for interpreting the results of the free space propagation experiments in Assignment 1.

### Conclusion

These sources collectively provide a comprehensive overview of the theoretical concepts, experimental procedures, and simulation tasks for Session 2 of the EE3P11 EM Practicum. Students should carefully review each document to understand the goals of each assignment, the experimental setup, the underlying theory of electromagnetic wave propagation and polarisation, and the specific requirements for the report and simulations. The example Matlab script offers a valuable starting point for the simulation task. The supplementary material clarifies some aspects of the first assignment related to measurements of wavelength and propagation loss.
