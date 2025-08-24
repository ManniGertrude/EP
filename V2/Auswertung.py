import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def Data(Diode):
    if Diode == 'D1F':
        U = [0.01, 0.45, 0.53, 0.6, 0.64, 0.67, 0.68, 0.695, 0.7, 0.716]
        I = [0, 0, 0.5, 2, 5, 7, 10, 13, 16, 20] 
    elif Diode == 'D2F':
        U = [0.012, 0.061, 0.075, 0.081, 0.117, 0.133, 0.142, 0.151, 0.169, 0.181]
        I = [0, 0.1, 0.2, 0.5, 2, 3.5, 5, 7, 13, 20]
    elif Diode == "D2R":
        U = [-0.0144, -0.0213, -0.0333, -0.0574, -0.093, -0.2898, -1.0066, -3.009, -8.75, -15]
        I = [1.4, 2, 3, 5, 8, 24, 30, 42, 80, 134]
    else:
        raise ValueError("Diode must be 'D1', 'D2', or 'ZD'")
    I = np.array(I).astype(float)
    U = np.array(U).astype(float)
    return U, I


for Diode in ['D1F', 'D2F']:
    U, I = Data(Diode=Diode)
    fig, ax = plt.subplots(layout='constrained')
    ax.errorbar(U, I, xerr=0.001+0.02*U, yerr=0.1+0.02*I, fmt='.', label='Messwerte', linestyle='None', color = 'black', capsize=3, capthick=1.5)
    ax.set_xlabel('U in V', ha='right', x=1, fontsize=32)
    ax.set_ylabel('I in mA', ha='right', y=1, fontsize=32)
    ax.set_title(f'Diode {Diode[:2]}', fontsize=32, x=0.85)
    ax.grid()
    plt.legend(loc='best', fontsize=24)
    ax.tick_params(axis='both', which='major', labelsize=24)
    plt.minorticks_on()
    plt.savefig(f'V2/{Diode}.pdf')
    plt.close()
    
    
for Diode in ['D2R']:
    U, I = Data(Diode=Diode)
    fig, ax = plt.subplots(1, 2, layout='constrained', figsize=(12, 6))
    for a in ax:
        a.tick_params(axis='both', which='major', labelsize=24)
        a.errorbar(-U, I, xerr=0.001-0.02*U, yerr=0.1+0.02*I, fmt='.', label='Messwerte', linestyle='None', color = 'black', capsize=3, capthick=1.5)
        a.grid()
        a.set_xlabel('U in V', ha='right', x=1)
    ax[0].set_title(f'Linear IV-curve for {Diode[:2]}', fontsize=32, ha='right', x=1)
    ax[1].set_title(f'Double-log IV-curve for {Diode[:2]}', fontsize=32, ha='right', x=1)
    ax[0].set_ylabel('I in µA', ha='right', y=1)
    ax[1].set_xscale('log')
    ax[1].set_yscale('log')
    plt.legend(loc='best')
    plt.minorticks_on()
    plt.savefig(f'V2/{Diode}.pdf')
    plt.close()