# import csv
# import requests

# access_key = 'f3c20c646e0b053e9927c2c15c9f346f'
# BASE_URL = 'https://api.aviationstack.com/v1/flights'
# params = {'access_key': access_key}  # Adjust limit as needed

# response = requests.get(BASE_URL, params=params)
# data = response.json()
# print(data)

# flights = data.get('data', [])

# with open('flights_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#    writer = csv.writer(csvfile)
#    # Write header
#    writer.writerow([
#        'Flight Number', 'Airline', 'Departure Airport', 'Arrival Airport',
#        'Departure Scheduled', 'Departure Actual',
#        'Arrival Scheduled', 'Arrival Actual', 'Status'
#    ])
#    # Write flight data
#    for flight in flights:
#        writer.writerow([
#            flight.get('flight', {}).get('iata', ''),
#            flight.get('airline', {}).get('name', ''),
#            flight.get('departure', {}).get('airport', ''),
#            flight.get('arrival', {}).get('airport', ''),
#            flight.get('departure', {}).get('scheduled', ''),
#            flight.get('departure', {}).get('actual', ''),
#            flight.get('arrival', {}).get('scheduled', ''),
#            flight.get('arrival', {}).get('actual', ''),
#            flight.get('flight_status', '')
#        ])
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pymysql
import pandas as pd

# Replace with your actual credentials and host
engine = create_engine('mysql+pymysql://admin_remote:879dhJVBNwT)@3.252.97.149:3306/classicmodels')
Session = sessionmaker(bind=engine)
session = Session()

query = text("""
   SELECT
       DATE_FORMAT(orderDate, '%Y-%m') AS yearmonth,
       SUM(quantityOrdered * priceEach) AS current_month
   FROM orders
   JOIN orderdetails USING (orderNumber)
   GROUP BY yearmonth
   ORDER BY yearmonth
""")
print(query)
result = session.execute(query).fetchall()

# Convert result to DataFrame
df = pd.DataFrame(result, columns=['yearmonth', 'current_month'])
df['previous_month'] = df['current_month'].shift(1).fillna(0)

for _, row in df.iterrows():
   insert_query = text("""
       INSERT INTO python_demo (yearmonth, current_month, previous_month)
       VALUES (:yearmonth, :current_month, :previous_month)
   """)
   session.execute(insert_query, {
       'yearmonth': row['yearmonth'],
       'current_month': row['current_month'],
       'previous_month': row['previous_month']
   })
session.commit()
