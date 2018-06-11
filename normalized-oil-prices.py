#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Normalized oil prices in BiH and World.

@author: Kenan Klisura
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def normalize(values):
    max = np.max(values.where(np.isfinite))
    return values / max

years = mdates.YearLocator();
months = mdates.MonthLocator();
yearsFmt = mdates.DateFormatter('%Y');

oil_prices = pd.read_csv('data.csv');

time_domain = oil_prices.loc[:,'date'].map(np.datetime64).map(mdates.date2num).values;

oil_usd_price = oil_prices.loc[:,'oil_USD']
diesel_bam_price = oil_prices.loc[:,'diesel_BAM']
a98_bam_price = oil_prices.loc[:,'a98_BAM']
a95_bam_price = oil_prices.loc[:,'a95_BAM']

normalized_oil_price = normalize(oil_usd_price)
normalized_diesel_bam_price = normalize(diesel_bam_price)
normalized_a98_bam_price = normalize(a98_bam_price)
normalized_a95_bam_price = normalize(a95_bam_price)

fig, ax = plt.subplots()

ax.plot_date(time_domain, normalized_oil_price, label = 'Oil WTI (world)', linestyle = '-', marker = None)
ax.plot_date(time_domain, normalized_diesel_bam_price, label = 'Diesel (local)', linestyle = '-', marker = None)
ax.plot_date(time_domain, normalized_a98_bam_price, label = '98 BMB (local)', linestyle = '-', marker = None)
ax.plot_date(time_domain, normalized_a95_bam_price, label = '95 BMB (local)', linestyle = '-', marker = None)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

plt.ylabel('Normalized price')
plt.legend()
plt.grid(True)

fig.autofmt_xdate()

plt.show()