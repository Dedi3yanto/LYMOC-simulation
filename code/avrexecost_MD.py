import matplotlib.pyplot as plt

# Given data
lea = [0.017631567896822, 0.0346408671308353, 0.0511942166935529, 0.0679772468490831, 0.084867318169341]
oa = [0.0124090162405831, 0.0241145963097977, 0.0362274949458864, 0.0475276949076497, 0.0607750697026911]
lymd = [0.0112155358923716, 0.0219603736001996, 0.03152897733423, 0.0424854722724445, 0.052005042788468]
lymc = [0.0106920480073503, 0.0188995217158881, 0.028783790205107, 0.0371731727379543, 0.0465338259976164]

md = [20, 40, 60, 80, 100]

# Create the plot
plt.plot(md, lea, 'g--d', label='LEA')
plt.plot(md, oa, 'b--o', label='OA')
plt.plot(md, lymd, 'y--s', label='LYMSD')
plt.plot(md, lymc, 'r--x', label='LYMOC')

# Add labels and title
plt.xlabel('The number of MDs')
plt.ylabel('Average execution cost (s)')
plt.legend()
plt.show()
