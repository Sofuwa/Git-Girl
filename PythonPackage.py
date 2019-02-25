import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
np_revenue = np.array(revenue)
np_expenses = np.array(expenses)
profit = np_revenue - np_expenses
print ("Profit = %s" % (profit))
Fin_status = dict(zip(months,profit))
print (Fin_status)
Fin_status = pd.Series(Fin_status)
print (Fin_status)
plt.plot(Fin_status)
plt.xlabel("Months")
plt.ylabel("Profit or loss")
plt.title("Monthly Profit for ABD Company")
plt.show()
