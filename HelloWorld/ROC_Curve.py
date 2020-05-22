import numpy as np
from sklearn.metrics import roc_curve, auc
#Model1
y = np.array([1, 1, 0, 0, 1, 1, 0, 0, 1, 0])
scores = np.array([0.73, 0.69, 0.44, 0.55,0.67,0.47,0.08,0.15,0.45,0.35])
fpr, tpr, threshold = roc_curve(y, scores)
roc_auc = auc(fpr, tpr)

#Model2
y = np.array([1, 1, 0, 0, 1, 0, 0, 1, 1, 0])
scores = np.array([0.99, 0.97, 0.96, 0.95,0.91,0.69,0.62,0.55,0.39,0.32])
fpr2, tpr2, threshold2 = roc_curve(y, scores)
roc_auc2 = auc(fpr2, tpr2)


import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange', lw=lw, label='Model 1 (area = %0.2f)' % roc_auc)
plt.plot(fpr2, tpr2, color='red', lw=lw, label='Model 2 (area = %0.2f)' % roc_auc2)

plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
#fig.savefig('/tmp/roc.png')
plt.show()