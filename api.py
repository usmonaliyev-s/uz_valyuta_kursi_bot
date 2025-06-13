import requests
import sqlite3
from datetime import datetime, timedelta
import time

# Create or connect to SQLite DB
conn = sqlite3.connect('currency_rates.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    code TEXT,
    name_en TEXT,
    nominal INTEGER,
    rate REAL,
    diff REAL
)
''')
conn.commit()

# Date range
start_date = datetime(2000, 1, 1)
end_date = datetime(2025, 6, 13)

def safe_float(value):
    try:
        value = value.replace(',', '').strip()
        return float(value) if value else None
    except:
        return None

current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    url = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{date_str}/'
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            if not data:
                print(f"No data for {date_str}, skipping.")
            else:
                usd_data = next((item for item in data if item.get('Ccy') == 'USD'), None)
                
                if usd_data:
                    cursor.execute('''
                    INSERT INTO rates (date, code, name_en, nominal, rate, diff)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        usd_data.get('Date'),
                        usd_data.get('Ccy'),
                        usd_data.get('CcyNm_EN'),
                        int(usd_data.get('Nominal', 1)),
                        safe_float(usd_data.get('Rate', '')),
                        safe_float(usd_data.get('Diff', ''))
                    ))
                    conn.commit()
                    print(f"Saved USD data for {date_str}")
                else:
                    print(f"USD not found for {date_str}")
        else:
            print(f"Failed to fetch {date_str}: Status {response.status_code}")
            
    except Exception as e:
        print(f"Error on {date_str}: {e}")
    
    # Move to next day
    current_date += timedelta(days=1)
    
    # Respect API rate limits
    time.sleep(0.5)

# Close DB connection
conn.close()
print("✅ All done!")
