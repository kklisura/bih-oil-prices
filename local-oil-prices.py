#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oil prices in BiH.

@author: Kenan Klisura
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

years = mdates.YearLocator();
months = mdates.MonthLocator();
yearsFmt = mdates.DateFormatter('%Y');

oil_prices = pd.read_csv('data.csv');

time_domain = oil_prices.loc[:,'date'].map(np.datetime64).map(mdates.date2num).values;

diesel_bam_price = oil_prices.loc[:,'diesel_BAM']
a98_bam_price = oil_prices.loc[:,'a98_BAM']
a95_bam_price = oil_prices.loc[:,'a95_BAM']

fig, ax = plt.subplots()

ax.plot_date(time_domain, diesel_bam_price, label = 'Diesel (local)', linestyle = '-', marker = None)
ax.plot_date(time_domain, a98_bam_price, label = '98 BMB (local)', linestyle = '-', marker = None)
ax.plot_date(time_domain, a95_bam_price, label = '95 BMB (local)', linestyle = '-', marker = None)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

plt.ylabel('Price (BAM)')
plt.legend()
plt.grid(True)

fig.autofmt_xdate()

plt.show()