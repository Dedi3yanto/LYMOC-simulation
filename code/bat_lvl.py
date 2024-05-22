import matplotlib.pyplot as plt

data1 = pd.read_csv('loc_avr_bat.csv', header=None, names=['Data 1'])
data2 = pd.read_csv('off_avr_bat.csv', header=None, names=['Data 2'])
data3 = pd.read_csv('dist_avr_bat.csv', header=None, names=['Data 3'])
data4 = pd.read_csv('dyn_avr_bat.csv', header=None, names=['Data 4'])

merged_data = pd.concat([data1, data2, data3, data4], axis=1)
merged_data = merged_data * 1000

# Buat grafik plot
plt.plot(merged_data.index, merged_data['Data 1'], 'g-d', label='LEA', markevery=50)
plt.plot(merged_data.index, merged_data['Data 2'], 'b-o', label='OA', markevery=50)
plt.plot(merged_data.index, merged_data['Data 3'], 'y-s', label='LYMSD', markevery=50)
plt.plot(merged_data.index, merged_data['Data 4'], 'r-x', label='LYMOC', markevery=50)
plt.ylabel('Average battery energy level (mJ)')
plt.xlabel('Time slot (s)')
plt.legend()

plt.xlim(left=0, right=500)
plt.ylim(bottom=0, top=3)
plt.grid(True,linestyle='--')

plt.show()
