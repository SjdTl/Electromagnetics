%-----------------------------%
% EE2P1 practicum session 2.2 %
%-----------------------------%

% Example free space vertical polarization
pv = PolarPhasor(pi/2, 0);
figure; PlotPolarPattern(pv); title('Free space V-pol')

% Example dielectric plate, transmit circular polarization 
% load group specific data
grData = load('Group data\group-04.01.mat');
f = grData.session2.task2.frequency;
Er = grData.session2.task2.dielectric_prermittivity;
R = grData.session2.task2.antennas_distance;
H = grData.session2.task2.reflection_height;

pt = PolarPhasor(0, pi/4); % transmit C-pol
figure;
for i=1:3
    pr = MultipathRxPolarState(pt, f, R, H(i), Er);
    PlotPolarPattern(pr); hold on
end
title('Dielectric plate - C-pol')

%-------------------------------------------------------------------------
% FUNCTIONS
%
% 1.1 - Polarization Phasor (eq. 2)
% INPUT:
%   - phi angle of orientation in radians [-pi, pi]
%   - tau angle of ellipticity in radians [-pi/4, pi/4]
% OUTPUT:
%   - p complex polarization ratio (polarization phasor)
function p = PolarPhasor(phi, tau)
    p = (tan(phi)+1i*tan(tau))/(1-1i*tan(phi)*tan(tau));        
end

% 1.2 Complex Fresnel reflection coefficient (eq. 14)
% IN:
%   - Er_1 relative dielectric permittivity of medium 1
%   - Er_2 relative dielectric permittivity of medium 2
%   - th_i angle of incidence [radians]
% OUT:
%   - Gamma_h Fresnel reflection coefficient for horizontal polarization
%   - Gamma_v Fresnel reflection coefficient for vertical polarization
function [Gamma_h, Gamma_v] = FresnelCoeff(Er_1, Er_2, th_i)
    Gamma_h = (cos(th_i)-sqrt(Er_2/Er_1-sin(th_i).^2))./(cos(th_i)+sqrt(Er_2/Er_1-sin(th_i).^2));               
    Gamma_v = -(Er_2*cos(th_i)-Er_1*sqrt(Er_2/Er_1-sin(th_i).^2))./(Er_2*cos(th_i)+Er_1*sqrt(Er_2/Er_1-sin(th_i).^2));
end

% 1.3 Polarization state of the received wave in multipath propagation  (eq. 13)
% IN:
%   - pt: transmit wave polarization phasor
%   - f: frequency [Hz]
%   - R: distance between antennas [m]
%   - H: reflector height [m]
%   - Er: reflector material relative permittivity
% OUT:
%   - pr: received wave polarization phasor
function pr = MultipathRxPolarState(pt, f, R, H, Er)
    k = 2*pi*f/3e8;         % wave number 
    th_i = atan(R/2/H);     % angle of incidence
    deltaR = 2*sqrt(R^2/4+H^2)-R;
    [G_h, G_v]=FresnelCoeff(1, Er, th_i);

    pr = pt*(1+G_v*exp(1i*k*deltaR))/(1+G_h*exp(1i*k*deltaR));
end

function PlotPolarPattern(p)
    % IN:
    %   - p polarization phasor
    x = linspace(0,2*pi,1001);
    Et_h = exp(1i*x);
    Et_v = Et_h.*p;

    % polar pattern
    V = Et_h.*cos(x)+Et_v.*sin(x);
    [th,V0]=cart2pol(real(Et_h),real(Et_v));
    polarplot(x,abs(V)/norm(V),th,abs(V0)/norm(V0))
end

