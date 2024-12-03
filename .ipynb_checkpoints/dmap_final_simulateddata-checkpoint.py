# -*- coding: utf-8 -*-
"""DMAP_Final_SimulatedData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N_GLJ3fZJwCI3t42w2rhbtbn1Qpcb3ft
"""

import random
import datetime
import csv

fake_names = [
    "John Smith", "Jane Doe", "Alex Johnson", "Emily Davis", "Michael Brown",
    "Sarah Wilson", "David Clark", "Laura Lewis", "Chris Walker", "Anna Hall",
    "Matthew Allen", "Lisa Young", "Daniel King", "Sophia Wright", "James Scott",
    "Olivia Green", "Anthony Baker", "Emma Adams", "William Nelson", "Grace Hill",
    "Andrew Carter", "Ava Turner", "Joshua Phillips", "Mia Campbell", "Robert Parker",
    "Ella Evans", "Charles Edwards", "Chloe Collins", "Benjamin Stewart", "Lily Sanders",
    "Jacob Rogers", "Zoe Morris", "Ryan Perry", "Nora Powell", "Nathan Russell",
    "Megan Foster", "Jonathan Brooks", "Victoria Howard", "Samuel Ward", "Isabella Torres",
    "Thomas Peterson", "Charlotte Gray", "Joseph Ramirez", "Amelia Butler", "Brandon Murphy",
    "Scarlett Cox", "Steven Bailey", "Ruby Hayes", "Justin Price", "Luna Reed",
    "Paul Wood", "Sadie Richardson", "Adam Bryant", "Madison Bennett", "Kyle James",
    "Ellie Griffin", "Mark Henderson", "Leah Flores", "Tyler West", "Ariana Simmons",
    "Scott Coleman", "Alyssa Foster", "Dylan Morgan", "Hailey Russell", "Aaron Patterson",
    "Natalie Ward", "Jason Alexander", "Brooklyn Perry", "Kevin Hayes", "Samantha Hughes",
    "Eric Moore", "Penelope Collins", "Sean Kelly", "Mila Ramirez", "Austin Cooper",
    "Jasmine Lopez", "Ethan Carter", "Layla Watson", "Brendan Perry", "Aurora Bryant",
    "Brian Sullivan", "Bella Griffin", "Ian Simmons", "Claire Powell", "Jordan Rivera",
    "Vivian Peterson", "Carlos Morgan", "Skylar Roberts", "Luis Price", "Paisley Coleman",
    "Shawn Russell", "Naomi Brooks", "Zachary Simmons", "Harper Hayes", "Sean Moriarty",
    "Cora Richardson", "Logan Morris", "Ivy Long", "Mason Reed", "Josephine Watson",
    "Cameron Anderson", "Lydia Hughes", "Patrick Mitchell", "Sophie Butler", "Trevor Barnes"
]



fake_boston_bars = [
    "Harbor & Hops",
    "Beacon Brews",
    "Fenway Tavern",
    "The Green Line Pub",
    "Back Bay Barrel",
    "Southie Spirits",
    "The Freedom Taproom",
    "Charles River Brew House",
    "Cobblestone & Co.",
    "The Bostonian Barrel"
]

people = {}

i = 0
for name in fake_names:
    i = i + 1
    people[name] = { "user_id": i }
print(people)


bars = {}
for name in fake_boston_bars:
    bars[name] = { "flow_rate": random.randint(5,40) }
print(bars)

def random_timestamp():

  today = datetime.date.today()
  three_months_ago = today - datetime.timedelta(days=30)
  random_date = three_months_ago + datetime.timedelta(days=random.randint(0, 90))


  random_hour = random.randint(20, 31)  # 20 (8 PM) to 31 (2 AM) using 24-hour format
  random_minute = random.randint(0, 59)
  random_second = random.randint(0, 59)


  random_datetime = datetime.datetime.combine(random_date, datetime.time(random_hour % 24, random_minute, random_second))

  return random_datetime

def get_bouncer_variance(guest_estimate, variance):
    while True:

        deviation_calc = random.uniform(.5, 2) #getting standard deviation
        deviation = deviation_calc * variance #feel like this is confusing, might come back to if I have time
        bouncer_estimate = guest_estimate + random.choice([-1, 1]) * deviation
        if 0.5 <= abs(bouncer_estimate - guest_estimate) <= 2 * variance:
          return round(abs(bouncer_estimate))



def simulated_data():

  people_keys = list(people.keys())
  name = random.choice(people_keys)
  user_id = people[name]['user_id']
  time = random_timestamp()


  bar_keys = list(bars.keys())
  bar = random.choice(bar_keys)
  flow_rate = bars[bar]['flow_rate']
  guest_estimate = random.randint(0,100)
  variance = 1.4 # can be changed as we see fit, assuming constant across each bar.
  bouncer_estimate = get_bouncer_variance(guest_estimate, variance)
  return time, name, user_id, bar,flow_rate , guest_estimate, bouncer_estimate


all_data = []


with open('simulated_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'name', 'user_id', 'bar', 'flow_rate', 'guest_estimate', 'bouncer_estimate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(10800): #10800 comes from needing at least 1 review every 10 minutes for 10 bars over a 30 day period.
    #so the math is 6 reviews per hour, for 6 hours (can change if needed) for 10 bars for 30 days.
      # 6*6 = 36, then 36*10 = 360 per day then 360*30 (~30 days in month) = 10,800 reviews!!
        time, name, user_id, bar, flow_rate, guest_estimate, bouncer_estimate = simulated_data()
        all_data.append([time, name, user_id, bar, flow_rate, guest_estimate, bouncer_estimate])

all_data.sort(key=lambda x: x[0], reverse=True) #wanted to get the most recent review first

with open('simulated_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_data:
        time, name, user_id, bar, flow_rate, guest_estimate, bouncer_estimate = row
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow({
            'timestamp': formatted_time,
            'name': name,
            'user_id': user_id,
            'bar': bar,
            'flow_rate': flow_rate,
            'guest_estimate': guest_estimate,
            'bouncer_estimate': bouncer_estimate
        })