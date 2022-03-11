# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:44:38 2022

@author: N_Kundu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:51:58 2022

@author: N_Kundu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator,StrMethodFormatter)

#------------------------------------------------------------------------#
# Load the required data files
#------------------------------------------------------------------------#
Data = np.loadtxt("uv_vis_ply_exp_data.txt",dtype = float);
Data1 = np.loadtxt("uv_vis_vpp_pbe_data.txt",dtype = float);
energies = Data1[4:25,2] ; osc= Data1[4:25,3];
exp_x= Data[:,0]; exp_y1= Data[:,1]; 
exp_y=exp_y1/max(exp_y1)
######################################################
def spectrum(E,osc,sigma,x):
    gE=[]
    for Ei in x:
        tot=0
        for Ej,os in zip(E,osc):
            tot+=os*np.exp(-((((Ej-Ei)/sigma)**2)))
        gE.append(tot)
    return gE
########### plot figure ################
# fig,ax=plt.subplots(figsize=(6,4))
# for energy,osc_strength in zip(energies,osc):
#     ax.plot((energy,energy),(0,osc_strength),c="r")
# ax.set_xlabel("Energy (eV)",fontsize=16)
# ax.xaxis.set_tick_params(labelsize=14,width=1.5)
# ax.yaxis.set_tick_params(labelsize=14,width=1.5)
# for axis in ['top','bottom','left','right']:
#     ax.spines[axis].set_linewidth(1.5)
# ax.set_ylabel("Osc. Strength",fontsize=16)
# plt.tight_layout()
# #plt.show()
###########################
x=np.linspace(220,580, num=500, endpoint=True)
gE=spectrum(energies,osc,20,x)

########################################
fig,ax=plt.subplots(figsize=(7,5))
ax.plot(x,gE,"--k",label='PBE0/def2-TZVPP',linewidth=2.0)
for energy,osc_strength in zip(energies,osc):
    ax.plot((energy,energy),(0,osc_strength),c="r", )
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
ax.set_xlabel("Excitaion energy (nm)",fontsize=12)
ax.set_ylabel("Osc. Strength",fontsize=12)
ax.xaxis.set_tick_params(labelsize=12,width=1.5)
ax.yaxis.set_tick_params(labelsize=12,width=1.5)
plt.tight_layout()
plt.legend(loc=1, ncol=1, fancybox=True, edgecolor='k', title="Theoritical UV-VIS spectra of PLY",fontsize=12, title_fontsize=13,labelcolor='b')
plt.savefig('plot/uv_vis_spectra_ply.png', format='png')
plt.show()
##########################  Theoretical_tauc plot  ###########################
x=1240/x;
z=(2.303*x*gE)**2
########### experimental_tauc plot #####################################
x_e=1240/exp_x
z_e=(2.303*exp_x*exp_y)**2
#################################################################
fig=plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
plt.plot(x,z, 'ro-', ms=4, mfc='k',label='PBE0/def2-tzvpp')
plt.hlines(0, 2.0 , 6, color='b', linewidth=2.0,linestyle='--')
ax.annotate("453 nm ", xy =(2.75,1),xytext =(2.9,7), arrowprops = dict(facecolor ='c',shrink = 0.05),fontsize=12)
ax.annotate("497 nm ", xy =(2.5,1),xytext =(2.1,12), arrowprops = dict(facecolor ='c',shrink = 0.05),fontsize=12)
ax.annotate("340 nm ", xy =(3.7,25),xytext =(3.0, 23), arrowprops = dict(facecolor ='c',shrink = 0.05),fontsize=12)
#ax.annotate("270 nm ", xy =(5,4),xytext =(5,15), arrowprops = dict(facecolor ='c',shrink = 0.05),fontsize=12)
#############################
ax.annotate("2.4 eV", xy =(2.4,0.0),xytext =(2.1,-8), arrowprops = dict(facecolor ='y',shrink = 0.05),fontsize=12)
ax.annotate("2.65 eV", xy =(2.65,0.0),xytext =(2.7,-8), arrowprops = dict(facecolor ='y',shrink = 0.05),fontsize=12)
ax.annotate("3.4 eV ", xy =(3.4,0.0),xytext =(3.5, -8), arrowprops = dict(facecolor ='y',shrink = 0.05),fontsize=12)
#ax.annotate("4.1 eV ", xy =(4.1,0.0),xytext =(4.5, -8), arrowprops = dict(facecolor ='y',shrink = 0.05),fontsize=12)
plt.ylim(-10,26); plt.xlim(2,4.1)
#plt.plot(x_e,z_e, 'bo-', ms=4, mfc='k',label='Experimental Tauc plot')
plt.xlabel('Excitation energy (ev)'); plt.ylabel(r'($\alpha$h$\nu$)(eV cm$^{-1}$)'); #ax.set_yticklabels([])
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
plt.legend(loc='best', ncol=1, fancybox=True, edgecolor='k', title="Tauc plot ",fontsize=12, title_fontsize=14,labelcolor='b')
plt.tight_layout()
plt.savefig('plot/truc_plot_ply.png', format='png')
plt.show()

###################################################################################################
fig=plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
plt.plot(exp_x,exp_y, 'bo-', ms=4, mfc='k',label='Exp. data')
plt.xlabel('Excitation energy (nm)'); plt.ylabel('Normalised absorbance strength'); 
  
#ax.set_yticklabels([])
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
plt.legend(loc=1, ncol=1, fancybox=True, edgecolor='k', title="Exp. UV-VIS spectra of PLY",fontsize=12, title_fontsize=14,labelcolor='b')
plt.tight_layout()
plt.savefig('plot/UV-VIS spectra of PLY.png', format='png')
plt.show()
