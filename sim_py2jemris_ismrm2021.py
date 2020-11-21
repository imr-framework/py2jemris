import os
from pulseq_jemris_simulator import simulate_pulseq_jemris, recon_jemris
from scipy.io import savemat, loadmat
import numpy as np
from datetime import datetime


# SPGR
# Create phantom
n = 16
#phantom_info = {'fov': 0.25, 'N': n, 'type': 'cylindrical', 'dim': 2, 'dir': 'z', 'loc': 0}



sps = 'sim/ismrm_abstract/spgr_16_pht/spgr_gspoil_N16_Ns1_TE10ms_TR50ms_FA30deg_acq_111920.seq'
sim_name = 'ismrm_abstract\\spgr_16_pht'
phtmaps = loadmat('sim/ismrm_abstract/spgr_16_pht/ph2bottles16.mat')
FOV = 0.25
N = 16
dr = FOV/N
t1map = np.zeros((N,N,1))
t1map[:,:,0] = 1e-3 * phtmaps['T1map16'] # Original is in ms; convert to seconds
t2map = np.zeros((N,N,1))
t2map[:,:,0] = 1e-3 * phtmaps['T2map16'] # Original is in ms; convert to seconds
pdmap = np.zeros((N,N,1))
pdmap[:,:,0] = phtmaps['PDmap16']

phantom_info = {'T1': t1map, 'T2': t2map, 'PD': pdmap,
                'dr': dr, 'fov': FOV, 'N': N, 'type': 'custom', 'dim': 2, 'dir': 'z', 'loc': 0}


# Simulate
print('Starting at: ', datetime.now())
simulate_pulseq_jemris(seq_path=sps, phantom_info=phantom_info, sim_name=sim_name, coil_fov=0.25)
kk, im, images = recon_jemris(file='sim/' + sim_name + '/signals.h5', dims=[n, n])
savemat('sim/' + sim_name + '/utest_pulseq_sim_output.mat', {'images': images, 'kspace': kk, 'imspace': im})
print('Ending at: ', datetime.now())