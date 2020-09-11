# py2jemris
Python library for interfacing with the [JEMRIS][JEMRIS_repo] MR simulator.
* Convert [Pulseq][Pulseq_repo]/[PyPulseq][PyPulseq_repo] sequence files (.seq) into JEMRIS format for simulation
* Construct custom Tx/Rx coil maps and numerical phantoms
* Perform JEMRIS simulation pipeline for rapid .seq file testing 

## Introduction
The JEMRIS project provides a fast and robust Bloch simulation core for Magentic Resonance Imaging (MRI) experiments, along with sequence design functions. The sequence representation in JEMRIS is high level, consisting of nested loops and parameter dependencies across sequence components [[1]](#references). In contrast, the Pulseq MR sequence standard represents the sequence in unrolled, consecutive blocks, with no interdependencies between blocks [[2]](@references). 

Importantly, Pulseq is mainly intended for sequence development and can be interfaced to three main vendors for open-source acquisition. While JEMRIS can convert its sequences (typically, an .xml sequence construction file with a list of .h5 waveform data files) into the Pulseq format, it does not allow the reverse operation - converting any Pulseq sequence into a form ready for JEMRIS simulation. We developed py2jemris in order to incorporate simulations into our fully open-source sequence development cycle, as PyPulseq [[3]](#references) scripting allows flexible and rapid open-source sequence construction. 

## Usage
py2jemris is intended for rapid MR sequence development - it enables dual simulation/acquisition using the same sequence file. 

## Get Started
To get started, clone the repository and read the function docstrings. You will need to have JEMRIS installed on your system. A Wiki page and a Google Colab Notebook will be available soon.  

## References 
1. Stöcker, T., Vahedipour, K., Pflugfelder, D., & Shah, N. J. (2010). High‐performance computing MRI simulations. Magnetic resonance in medicine, 64(1), 186-193.
2. Layton, K. J., Kroboth, S., Jia, F., Littin, S., Yu, H., Leupold, J., ... & Zaitsev, M. (2017). Pulseq: a rapid and hardware‐independent pulse sequence prototyping framework. Magnetic resonance in medicine, 77(4), 1544-1552.
3. Ravi, K. S., Geethanath, S., & Vaughan, J. T. (2019). PyPulseq: A Python Package for MRI Pulse Sequence Design. Journal of Open Source Software, 4(42), 1725.



[Pulseq_repo]: https://github.com/pulseq/pulseq
[PyPulseq_repo]: https://github.com/imr-framework/pypulseq
[JEMRIS_repo]: https://github.com/JEMRIS/jemris
