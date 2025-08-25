import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6 * np.pi, 1000)
f = 50
A = 1

ac_signal = A * np.sin(t)

einweg = np.maximum(ac_signal, 0)

zweiweg = np.abs(ac_signal)

fig, ax = plt.subplots(1, 2, layout='constrained', figsize=(12, 6))

ax[0].plot(t, einweg, label='Einweg-Gleichrichter (Half-wave)', zorder = 5, color = 'navy')
ax[1].plot(t, zweiweg, label='Zweiweg-Gleichrichter (Full-wave)', zorder = 5, color = 'navy')
ax[0].set_title('Einweggleichrichter', fontsize=32)
ax[1].set_title('Zweiweggleichrichter', fontsize=32)
ax[0].set_ylabel('Voltage [V]', ha='right', y=1, fontsize=28)
for axis in ax:
    axis.plot(t, ac_signal, label='AC Input (sinusoidal)', color = 'crimson', zorder = 10, linestyle = '-.')
    axis.set_xlabel('Time [rad]', ha='right', x=1, fontsize=28)
    
    # axis.legend()
    axis.grid(True)
    axis.tick_params(axis='both', which='major', labelsize=24)
    axis.minorticks_on()
plt.savefig('V2/Gleichrichter.pdf')
