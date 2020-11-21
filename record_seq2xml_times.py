# Records how long seq2xml takes to convert SPGR sequences at N = 16, 32, 64, and 128

from seq2xml import seq2xml
import timeit
from pypulseq.Sequence.sequence import Sequence
from scipy.io import savemat, loadmat
import numpy as np
from datetime import datetime
from pulseq_jemris_simulator import simulate_pulseq_jemris, recon_jemris

def tbt_seq2xml(n):
    seq = Sequence()
    seq_path = f'sim/ismrm_abstract/spgr_var_N/spgr_gspoil_N{n}_Ns1_TE10ms_TR50ms_FA30deg_acq_112020.seq'
    seq.read(seq_path)
    seq2xml(seq, seq_name=f'spgr{n}',out_folder=f'sim/ismrm_abstract/spgr_var_N/spgr{n}')

def tbt_sim_pipeline(n):
    # SPGR
    phantom_info = {'fov': 0.25, 'N': n, 'type': 'cylindrical', 'dim': 2, 'dir': 'z', 'loc': 0}
    sps = f'sim/ismrm_abstract/spgr_var_N/spgr_gspoil_N{n}_Ns1_TE10ms_TR50ms_FA30deg_acq_112020.seq'
    sim_name = f'ismrm_abstract\\spgr_var_N\\spgr{n}'

    # Use cylindrical phantom to time
    # Simulate
    simulate_pulseq_jemris(seq_path=sps, phantom_info=phantom_info, sim_name=sim_name, coil_fov=0.25)
    kk, im, images = recon_jemris(file='sim/' + sim_name + '/signals.h5', dims=[n, n])
    savemat('sim/' + sim_name + '/utest_pulseq_sim_output.mat', {'images': images, 'kspace': kk, 'imspace': im})


if __name__ == '__main__':
    #for n in [8]:
    #    print(f'Timing seq2xml for n = {n}')
    #    ttken = timeit.timeit('tbt_seq2xml(N)', setup=f'N = {n}; from __main__ import tbt_seq2xml',number=10)
    #    print(f'Avg. time over 10 reps is {ttken}')



    #Time pipeline
    q = 1
    n = 8
    ttken = timeit.timeit('tbt_sim_pipeline(n)',setup=f'n={n}; from __main__ import tbt_sim_pipeline',number=q)
    print(f'Avg. sim pipeline time over {q} reps for n = {n} is {ttken} seconds.')