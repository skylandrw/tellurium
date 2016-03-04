"""
    tellurium 1.3.1

    auto-generated code (2016-03-04T18:08:27)
    sedmlDoc: L1V2  
    workingDir: /home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml
    inputType: SEDML_FILE
"""
from __future__ import print_function, division
import tellurium as te
from tellurium.sedml.mathml import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import libsedml
import pandas
import os.path

workingDir = '/home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
# Model <model1>
import tellurium.temiriam as temiriam
__model1_sbml = temiriam.getSBMLFromBiomodelsURN('urn:miriam:biomodels.db:BIOMD0000000140')
model1 = te.loadSBMLModel(__model1_sbml)

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
# Task <task1>
# Task: <task1>
task1 = [None]
model1.setIntegrator('cvode')
model1.timeCourseSelections = ['Total_IkBeps', 'Total_NFkBn', 'Total_IkBalpha', 'Total_IkBbeta', 'time']
task1[0] = model1.simulate(start=0.0, end=2500.0, steps=1000)

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
# DataGenerator <time>
__var__time1 = np.transpose(np.array([sim['time'] for sim in task1]))
if len(__var__time1.shape) == 1:
     __var__time1.shape += (1,)
time = __var__time1

# DataGenerator <Total_NFkBn>
__var__Total_NFkBn1 = np.transpose(np.array([sim['Total_NFkBn'] for sim in task1]))
if len(__var__Total_NFkBn1.shape) == 1:
     __var__Total_NFkBn1.shape += (1,)
Total_NFkBn = __var__Total_NFkBn1

# DataGenerator <Total_IkBbeta>
__var__Total_IkBbeta1 = np.transpose(np.array([sim['Total_IkBbeta'] for sim in task1]))
if len(__var__Total_IkBbeta1.shape) == 1:
     __var__Total_IkBbeta1.shape += (1,)
Total_IkBbeta = __var__Total_IkBbeta1

# DataGenerator <Total_IkBeps>
__var__Total_IkBeps1 = np.transpose(np.array([sim['Total_IkBeps'] for sim in task1]))
if len(__var__Total_IkBeps1.shape) == 1:
     __var__Total_IkBeps1.shape += (1,)
Total_IkBeps = __var__Total_IkBeps1

# DataGenerator <Total_IkBalpha>
__var__Total_IkBalpha1 = np.transpose(np.array([sim['Total_IkBalpha'] for sim in task1]))
if len(__var__Total_IkBalpha1.shape) == 1:
     __var__Total_IkBalpha1.shape += (1,)
Total_IkBalpha = __var__Total_IkBalpha1

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
# Output <plot1>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Total_NFkBn[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='Total_NFkBn')
    else:
        plt.plot(time[:,k], Total_NFkBn[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('BM140 Total_NFkBn', fontweight='bold')
plt.xlabel('time', fontweight='bold')
plt.ylabel('Total_NFkBn', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.show()

# Output <plot2>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Total_IkBbeta[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='Total_IkBbeta')
    else:
        plt.plot(time[:,k], Total_IkBbeta[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('BM140 Total_IkBbeta', fontweight='bold')
plt.xlabel('time', fontweight='bold')
plt.ylabel('Total_IkBbeta', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.show()

# Output <plot3>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Total_IkBeps[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='Total_IkBeps')
    else:
        plt.plot(time[:,k], Total_IkBeps[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('BM140 Total_IkBeps', fontweight='bold')
plt.xlabel('time', fontweight='bold')
plt.ylabel('Total_IkBeps', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.show()

# Output <plot4>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(time.shape[1]):
    if k == 0:
        plt.plot(time[:,k], Total_IkBalpha[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='Total_IkBalpha')
    else:
        plt.plot(time[:,k], Total_IkBalpha[:,k], '-o', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('BM140 Total_IkBalpha', fontweight='bold')
plt.xlabel('time', fontweight='bold')
plt.ylabel('Total_IkBalpha', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.show()

