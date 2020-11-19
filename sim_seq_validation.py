import os
from pulseq_jemris_simulator import simulate_pulseq_jemris, recon_jemris
from scipy.io import savemat, loadmat


# IRSE
n = 32
phantom_info = {'fov': 0.25, 'N': n, 'type': 'cylindrical', 'dim': 2, 'dir': 'z', 'loc': 0}
sps = 'sim/seq_validation/irse_32/irse32.seq'
sim_name = 'seq_validation\\irse_32'

#Simulate
simulate_pulseq_jemris(seq_path=sps, phantom_info=phantom_info, sim_name=sim_name, coil_fov=0.25)
kk, im, images = recon_jemris(file='sim/' + sim_name + '/signals.h5', dims=[n, n])
savemat('sim/' + sim_name + '/utest_pulseq_sim_output.mat', {'images': images, 'kspace': kk, 'imspace': im})


# #
# # TSE
# n = 32
# phantom_info = {'fov': 0.25, 'N': n, 'type': 'cylindrical', 'dim': 2, 'dir': 'z', 'loc': -0.08}
# sps = 'sim/seq_validation/tse_32/tse32.seq'
# sim_name = 'seq_validation\\tse_32'
# # Make sequence
# simulate_pulseq_jemris(seq_path=sps, phantom_info=phantom_info, sim_name=sim_name, coil_fov=0.25)
# kk, im, images = recon_jemris(file='sim/' + sim_name + '/signals.h5', dims=[n, n])
# savemat('sim/' + sim_name + '/TSE-T2PLANE-utest_pulseq_sim_output.mat', {'images': images, 'kspace': kk, 'imspace': im})
#

# ## DWI
# n = 32
# phantom_info = {'fov':0.25, 'N':n, 'type': 'cylindrical', 'dim': 2, 'dir': 'z', 'loc': -0.08}
# sps = 'sim/seq_validation/dwi_32/dwi32.seq'
# sim_name = 'seq_validation\\tse_32'
#
# simulate_pulseq_jemris(seq_path=sps, phantom_info=phantom_info, sim_name=sim_name, coil_fov=0.25)
# kk, im, images = recon_jemris(file='sim/'+sim_name+'/signals.h5',dims=[n,n])
# savemat('sim/'+ sim_name + '/dwi_pulseq_sim_output.mat',{'images':images, 'kspace':kk, 'imspace':im})