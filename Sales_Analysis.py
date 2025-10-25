from gettext import install
from pydoc import describe

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df = pd.read_csv('AusApparalSales4thQrt2020.csv', parse_dates=['Date'], dtype={'Time': str, 'State': str, 'Group': str})

print (df)

print (df.isna().sum())

print (df.notna().sum())

df_dataonly = df[['Unit', 'Sales']]

normalize = MinMaxScaler()
normalize_data = normalize.fit_transform(df_dataonly)

normalize_data[:, [0]]

normalize_data[:, [1]]

print (normalize_data[:, [0]])
print (normalize_data[:, [1]])

print(normalize_data[:, [0]].min(), normalize_data[:, [0]].max())

print(normalize_data[:, [1]].min(), normalize_data[:, [1]].max())

dates = df['Date']
df_unit_and_sales = df.groupby(by='Date'). sum()

print(df_unit_and_sales)

df_oct = df_unit_and_sales.loc['2020-10-01':'2020-10-30']
df_nov = df_unit_and_sales.loc['2020-11-01':'2020-11-30']
df_dec = df_unit_and_sales.loc['2020-12-01':'2020-12-31']

df_oct.index
sns.barplot(x = df_oct.index, y = 'Unit', data=df_oct)

#plt.show()
#df_nov.index
#sns.lineplot(x = df_nov.index, y='Unit', data=df_nov)

#plt.show()
#df_dec.index
#sns.barplot(x = df_dec.index, y = 'Unit', data=df_dec)

#plt.show()

print(df_oct.describe())
print(df_nov.describe())
print(df_dec.describe())

#Unit Analysis
sns.set(rc={'figure.figsize':(20,8)})
fig, axes = plt.subplots(1, 3)
bp_oct = sns.boxplot(x='Unit', data=df_oct, ax=axes[0])
bp_nov = sns.boxplot(x='Unit', data=df_nov, ax=axes[1])
bp_dec = sns.boxplot(x='Unit', data=df_dec, ax=axes[2])
bp_oct.set(title='October Units')
bp_nov.set(title='November Units')
bp_dec.set(title='December Units')

#Sales Analysis
sns.set(rc={'figure.figsize':(20,8)})
fig, axes = plt.subplots(1, 3)
bp_oct = sns.boxplot(x='Sales', data=df_oct, ax=axes[0])
bp_nov = sns.boxplot(x='Sales', data=df_nov, ax=axes[1])
bp_dec = sns.boxplot(x='Sales', data=df_dec, ax=axes[2])
bp_oct.set(title='October Sales')
bp_nov.set(title='November Sales')
bp_dec.set(title='December Sales')

#Overall Unit and Sales figures
oct_days = df_oct.index.day
oct_days.astype('str')
nov_days = df_nov.index.day
nov_days.astype('str')
dec_days = df_dec.index.day
dec_days.astype('str')


#Units sold in October, November and December

sns.set(rc={'figure.figsize':(20,8)})
fig, axes = plt.subplots(1, 3)
bp_oct = sns.barplot(x = df_oct.index, y='Unit', data=df_oct, ax=axes[0])
bp_nov = sns.barplot(x = df_nov.index, y='Unit', data=df_nov, ax=axes[1])
bp_dec = sns.barplot(x = df_dec.index, y='Unit', data=df_dec, ax=axes[2])
bp_oct.set(xlabel='Oct 2020', title='October Units')
bp_nov.set(xlabel='Nov 2020', title='November Units')
bp_dec.set(xlabel='Dev 2020', title='December Units')
bp_oct.set(ylim=(1000, 2000))
bp_nov.set(ylim=(1000, 2000))
bp_dec.set(ylim=(1000, 2000))
#o = bp_oct.set_xticklabels(oct_days)
#n = bp_nov.set_xticklabels(nov_days)
#d = bp_dec.set_xticklabels(dec_days)

#plt.show()

#Sales numbers for October, November and December

import matplotlib
# sns.lineplot(x = 'Date', y = 'Unit', data = df)
sns.set(rc={'figure.figsize':(20,8)})
fig, axes = plt.subplots(1, 3)
lp_oct = sns.lineplot(x = df_oct.index, y = 'Sales', data=df_oct, ax=axes[0])
lp_nov = sns.lineplot(x = df_nov.index, y = 'Sales', data=df_nov, ax = axes[1])
lp_dec = sns.lineplot(x = df_nov.index, y = 'Sales', data=df_dec, ax = axes[2])
lp_oct.set(ylim=(2.5e6, 5.0e6))
lp_nov.set(ylim=(2.5e6, 5.0e6))
lp_dec.set(ylim=(2.5e6, 5.0e6))
lp_oct.set(xlabel='Oct 2020', title='October Sales')
lp_nov.set(xlabel='Nov 2020', title='November Sales')
lp_dec.set(xlabel='Dev 2020', title='December Sales')

loc = matplotlib.dates.DayLocator(bymonthday=range(1, 30, 7))

lp_oct.xaxis.set_major_locator(loc)

#Consolidated 3 month Sales plot

sns.set(rc={'figure.figsize':(20,8)})
sns.lineplot(x = 'Date', y = 'Sales', data = df)

#Comprehensive Snapshot

fig, axes = plt.subplots(2, 3)

bp_oct = sns.barplot(x = df_oct.index, y='Unit', data=df_oct, ax=axes[0,0])
bp_nov = sns.barplot(x = df_nov.index, y='Unit', data=df_nov, ax=axes[0,1])
bp_dec = sns.barplot(x = df_dec.index, y='Unit', data=df_dec, ax=axes[0,2])

bp_oct.set(xlabel='Oct 2020', title='October Units')
bp_nov.set(xlabel='Nov 2020', title='November Units')
bp_dec.set(xlabel='Dev 2020', title='December Units')

bp_oct.set(ylim=(1000, 2000))
bp_nov.set(ylim=(1000, 2000))
bp_dec.set(ylim=(1000, 2000))

#o = bp_oct.set_xticklabels(oct_days)
#n = bp_nov.set_xticklabels(nov_days)
#d = bp_dec.set_xticklabels(dec_days)

lp_oct = sns.lineplot(x = df_oct.index, y='Sales', data=df_oct, ax=axes[1,0])
lp_nov = sns.lineplot(x = df_nov.index, y='Sales', data=df_nov, ax=axes[1,1])
lp_dec = sns.lineplot(x = df_dec.index, y='Sales', data=df_dec, ax=axes[1,2])

lp_oct.set(ylim=(2.5e6, 5.0e6))
lp_nov.set(ylim=(2.5e6, 5.0e6))
lp_dec.set(ylim=(2.5e6, 5.0e6))

#Analysis of Statewise sales in Australia

state_pivot = pd.pivot_table(df, index='State', aggfunc= ['sum', 'mean'])

labels = state_pivot['mean']['Sales'].index.to_list()
# print(labels)
colors = sns.color_palette('pastel')[0:5]
plt.pie(state_pivot['mean']['Sales'], labels=labels, colors=colors, autopct='%.0f%%')
plt.show()

group_pivot = pd.pivot_table(df, index='Group', aggfunc=['sum', 'mean'])
group_pivot


labels = group_pivot['mean']['Sales'].index.to_list()
# print(labels)
colors = sns.color_palette('pastel')[0:5]
plt.pie(group_pivot['mean']['Sales'], labels=labels, colors=colors, autopct='%.0f%%')
plt.show()

time_pivot = pd.pivot_table(df, index='Time', aggfunc=['sum', 'mean'])
time_pivot

labels = time_pivot['mean']['Sales'].index.to_list()
# print(labels)
colors = sns.color_palette('pastel')[0:5]
plt.pie(time_pivot['mean']['Sales'], labels=labels, colors=colors, autopct='%.0f%%')
plt.show()
#print (state_pivot)

