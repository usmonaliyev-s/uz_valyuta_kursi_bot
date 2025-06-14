import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

conn = sqlite3.connect('currency_rates.db')
df = pd.read_sql_query("SELECT * FROM rates", conn)

sns.set_style('whitegrid')

df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(18, 7), dpi=500)
sns.lineplot(data=df, x="date", y="rate", color='blue', linewidth=3)

plt.title("Currency Rates")
plt.xlabel("Date")
plt.ylabel("Currency Rates")

ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=8))
plt.xticks(rotation=45)

plt.gca().set_facecolor("#ffffff")
plt.grid(True, color='#ffffff')


plt.tight_layout()
plt.show()

conn.close()
