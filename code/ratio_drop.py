import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

chosen_mode_loc = pd.read_csv('loc_mode.csv').values
T, N = chosen_mode_loc.shape
mode_counts_loc = np.zeros((T, 2))  # asumsikan ada 3 mode
for t in range(T):
    for i in range(N):
        mode = chosen_mode_loc[t, i]
        if mode != 3:  # asumsikan mode 4 tidak dihitung
            mode_counts_loc[t, mode-1] += 1  # indeks di python dimulai dari 0
total_counts_loc = np.sum(mode_counts_loc, axis=1)
average_ratios_loc = mode_counts_loc / total_counts_loc[:, None]

chosen_mode_off = pd.read_csv('off_mode.csv').values
T, N = chosen_mode_off.shape
mode_counts_off = np.zeros((T, 2))  # asumsikan ada 3 mode
for t in range(T):
    for i in range(N):
        mode = chosen_mode_off[t, i]
        if mode != 3:  # asumsikan mode 4 tidak dihitung
            mode_counts_off[t, mode-1] += 1  # indeks di python dimulai dari 0
total_counts_off = np.sum(mode_counts_off, axis=1)
average_ratios_off = mode_counts_off / total_counts_off[:, None]

chosen_mode_dist = pd.read_csv('dist_mode.csv').values
T, N = chosen_mode_dist.shape
mode_counts_dist = np.zeros((T, 3))  # asumsikan ada 3 mode
for t in range(T):
    for i in range(N):
        mode = chosen_mode_dist[t, i]
        if mode != 4:  # asumsikan mode 4 tidak dihitung
            mode_counts_dist[t, mode-1] += 1  # indeks di python dimulai dari 0
total_counts_dist = np.sum(mode_counts_dist, axis=1)
average_ratios_dist = mode_counts_dist / total_counts_dist[:, None]

chosen_mode_dyn = pd.read_csv('dyn_mode.csv').values
T, N = chosen_mode_dyn.shape
mode_counts_dyn = np.zeros((T, 3))  # asumsikan ada 3 mode
for t in range(T):
    for i in range(N):
        mode = chosen_mode_dyn[t, i]
        if mode != 4:  # asumsikan mode 4 tidak dihitung
            mode_counts_dyn[t, mode-1] += 1  # indeks di python dimulai dari 0
total_counts_dyn = np.sum(mode_counts_dyn, axis=1)
average_ratios_dyn = mode_counts_dyn / total_counts_dyn[:, None]

# Ambil mode ke-2 dari average_ratios_loc dan average_ratios_off
selected_mode_loc = average_ratios_loc[:, 1]
selected_mode_off = average_ratios_off[:, 1]
# Ambil mode ke-3 dari average_ratios_dist dan average_ratios_dyn
selected_mode_dist = average_ratios_dist[:, 2]
selected_mode_dyn = average_ratios_dyn[:, 2]

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size), 'valid') / window_size

window_size = 500  # Atur ukuran window sesuai kebutuhan

# Hitung moving average
smoothed_mode_loc = moving_average(selected_mode_loc, window_size)
smoothed_mode_off = moving_average(selected_mode_off, window_size)
smoothed_mode_dist = moving_average(selected_mode_dist, window_size)
smoothed_mode_dyn = moving_average(selected_mode_dyn, window_size)

plt.plot(smoothed_mode_loc, 'g-d', label='LEA', markevery=50)
plt.plot(smoothed_mode_off, 'b-o', label='OA', markevery=50)
plt.plot(smoothed_mode_dist, 'y-s', label='LYMSD', markevery=50)
plt.plot(smoothed_mode_dyn, 'r-x', label='LYMOC', markevery=50)

plt.ylabel('Average ratio of the dropped tasks')
plt.xlabel('Time slot (s)')
plt.legend()

plt.xlim(left=0, right=500)
plt.ylim(bottom=-0.01, top=1.01)
plt.grid(True,linestyle='--')

plt.show()
