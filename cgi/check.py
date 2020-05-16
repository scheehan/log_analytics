from pandas import DataFrame

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

# Data = {'Tasks': [300,500,700]}
# df = DataFrame(Data,columns=['Tasks'],index = ['Tasks Pending','Tasks Ongoing','Tasks Completed'])

sevs = {}

df = pd.read_csv('../tmp/log.txt', names=['Time','Severity','Text'], engine='python')

print(df)

sd = df['Severity']

cf = pd.value_counts(df['Severity'].values)


print(cf)


df.Severity.value_counts().plot.pie(y='Severities', figsize=(5, 5),autopct='%1.1f%%', startangle=90)
plt.savefig('foo_1.png')

#print(sd)
# plt.title('severities dataset')
# plt.axis('severities')



# df.plot.pie(y='Severity') 

# plt.show()


#sd.plot.pie(y='Severity',figsize=(5, 5),autopct='%1.1f%%', startangle=90)

# # df.plot.pie(y='Tasks',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
# # #plt.show()
# plt.savefig('foo_1.png')