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
    "John Smith", "Jane Doe", "Alex Johnson", "Emily Davis", "Michael Brown", "Sarah Wilson", "David Clark",
    "Laura Lewis", "Chris Walker", "Anna Hall", "Matthew Allen", "Lisa Young", "Daniel King", "Sophia Wright",
    "James Scott", "Olivia Green", "Anthony Baker", "Emma Adams", "William Nelson", "Grace Hill", "Andrew Carter",
    "Ava Turner", "Joshua Phillips", "Mia Campbell", "Robert Parker", "Ella Evans", "Charles Edwards", "Chloe Collins",
    "Benjamin Stewart", "Lily Sanders", "Jacob Rogers", "Zoe Morris", "Ryan Perry", "Nora Powell", "Nathan Russell",
    "Megan Foster", "Jonathan Brooks", "Victoria Howard", "Samuel Ward", "Isabella Torres", "Thomas Peterson",
    "Charlotte Gray", "Joseph Ramirez", "Amelia Butler", "Brandon Murphy", "Scarlett Cox", "Steven Bailey", "Ruby Hayes",
    "Justin Price", "Luna Reed", "Paul Wood", "Sadie Richardson", "Adam Bryant", "Madison Bennett", "Kyle James",
    "Ellie Griffin", "Mark Henderson", "Leah Flores", "Tyler West", "Ariana Simmons", "Scott Coleman", "Alyssa Foster",
    "Dylan Morgan", "Hailey Russell", "Aaron Patterson", "Natalie Ward", "Jason Alexander", "Brooklyn Perry", "Kevin Hayes",
    "Samantha Hughes", "Eric Moore", "Penelope Collins", "Sean Kelly", "Mila Ramirez", "Austin Cooper", "Jasmine Lopez",
    "Ethan Carter", "Layla Watson", "Brendan Perry", "Aurora Bryant", "Brian Sullivan", "Bella Griffin", "Ian Simmons",
    "Claire Powell", "Jordan Rivera", "Vivian Peterson", "Carlos Morgan", "Skylar Roberts", "Luis Price", "Paisley Coleman",
    "Shawn Russell", "Naomi Brooks", "Zachary Simmons", "Harper Hayes", "Sean Moriarty", "Cora Richardson", "Logan Morris",
    "Ivy Long", "Mason Reed", "Josephine Watson", "Cameron Anderson", "Lydia Hughes", "Patrick Mitchell", "Sophie Butler",
    "Trevor Barnes", "Lucas Cooper", "Ella Moore", "Jack Harris", "Charlotte Moore", "Benjamin Fisher", "Maya Clarke",
    "Oliver Allen", "Liam Thomas", "Amelia Scott", "Jacob Hall", "Isabella Adams", "Michael Lee", "Harper Carter",
    "Alexander Garcia", "Ella Kim", "Zoe Evans", "James Davis", "Lily Turner", "Ethan Harris", "Grace Green",
    "Henry Williams", "Sophie Clark", "Mason Mitchell", "Charlotte Ross", "Madison Foster", "Nathaniel Garcia", "Zoe Lopez",
    "Emma Rivera", "Ryan King", "Olivia Perez", "Sophia Evans", "Isaiah Brown", "Mila Cooper", "Zachary Adams", "Nina Morgan",
    "Eli Davis", "Mason Walker", "Liam White", "Sophia Green", "Jacob Carter", "Ella Mitchell", "James Foster", "Isabelle Brown",
    "Caleb Johnson", "Amelia Robinson", "Liam Walker", "Grace Clark", "Benjamin Phillips", "Megan Smith", "Olivia Lewis",
    "Oliver Moore", "Ryan Adams", "Lily Davis", "Madison Harris", "Ethan Scott", "Charlotte Evans", "Sophie Wright",
    "Lucas Taylor", "Grace Wilson", "Olivia Mitchell", "James Cooper", "Sophia Reed", "Ava Phillips", "Ryan Peterson",
    "Michael Brown", "Mia Foster", "James Anderson", "Benjamin Ward", "Ella Mitchell", "Tyler Green", "Nora Hall",
    "Oliver Wright", "Sadie Clark", "Sophia Cooper", "Aiden Brooks", "Zoe Brown", "Caleb Carter", "James Miller", "Emma Ross",
    "Jack Hughes", "Jacob Price", "Amelia Evans", "William Phillips", "Nora Anderson", "Sophie Carter", "Megan Taylor",
    "Isabella Morgan", "Mia Powell", "Liam Walker", "Emma Hall", "Benjamin Wright", "Sarah White", "Olivia Scott",
    "Lucas Harris", "Sophia Reed", "Charlotte Hughes", "James White", "Lucas Bennett", "Grace Lopez", "Mason Moore",
    "Caleb Taylor", "Sophie Brown", "Harper Anderson", "Benjamin Carter", "Olivia Harris", "Zachary Bennett", "Ethan Carter",
    "Sophie Powell", "Amelia Morgan", "Mason Davis", "Lucas Foster", "Sophie Clark", "Ella White", "James Davis", "Ava Harris",
    "Megan Walker", "Tyler Reed", "Isabella Foster", "Mia Wright", "Sophie White", "Madison Clark", "Nora Bennett", "Zoe Wilson",
    "Olivia White", "James Miller", "Isabella Carter", "Ethan Brown", "Ryan Clark", "Sophie Mitchell", "Lucas Powell", "Lily Foster",
    "Caleb Mitchell", "Tyler Taylor", "Isabella Ross", "James Walker", "Zoe Taylor", "Ethan Scott", "Amelia Ward", "Megan Ward",
    "Grace Walker", "Ryan Davis", "Harper Scott", "Ava Ross", "Mia Ward", "Madison Cooper", "Sophie Walker", "Zachary White",
    "Lucas Davis", "Benjamin Ross", "Zoe Harris", "Liam Harris", "Megan Cooper", "Nora Ross", "Sophie Green", "Ava Davis",
    "Lucas Green", "Megan Scott", "Sophie Ross", "Isabella Taylor", "James Harris", "Ava Green", "Madison Reed", "Sophie Ward",
    "Lily Cooper", "Zoe Cooper", "Lucas Scott", "James Green", "Ethan Walker", "Zachary Harris", "Ryan White", "Olivia Green",
    "John Alexander", "Victoria Parker", "Evan Butler", "Grace Ward", "Matthew Morgan", "Natalie Torres", "Dylan Price",
    "Riley Reed", "Alyssa Walker", "Brian Sanders", "Rachel Flores", "Justin Davis", "Patrick Rivera", "Christina Moore",
    "Eric Baker", "Jasmine Howard", "Nathan Gray", "Ashley King", "Kevin Hughes", "Aaron Adams", "Samantha Peterson",
    "Gabriel Young", "Hannah Lewis", "Adam Scott", "Charlotte Roberts", "Kayla Perry", "Logan Bennett", "Ella Ward",
    "Zachary Nelson", "Madeline Brooks", "Connor Foster", "Aiden Mitchell", "Lucas Turner", "Megan Johnson", "Hailey Moore",
    "Daniel Martinez", "Sophie Johnson", "Evelyn White", "Cameron Adams", "Isaac Hall", "Alexandra Scott", "Christopher Lee",
    "Rebecca Carter", "Gabriella Brown", "Hunter Harris", "Alexis Thompson", "Anna Ramirez", "Tyler Jones", "Jessica Price",
    "Andrew Smith", "Natalie Clark", "Samuel Foster", "Rachel Green", "Ava Morris", "Sean Lewis", "Lily Brooks", "Benjamin Clark",
    "Hunter Brown", "Sophia Russell", "Grace Murphy", "Ella Bennett", "Emma Wilson", "Henry Martin", "Mason Johnson",
    "Liam Evans", "Olivia Cooper", "Avery Kelly", "Samuel Torres", "Nathan Parker", "Madeline Peterson", "Leah Hughes",
    "Michael Brown", "Sophia Hall", "Ryan Anderson", "Abigail Lopez", "Joshua White", "Chloe Hill", "William Martin",
    "Eleanor Foster", "Jacob Green", "Grace Murphy", "Lucas Perez", "Aiden Mitchell", "Charlotte Brooks", "Ella Davis",
    "David Lee", "Jessica Clark", "Daniel Robinson", "Mia Allen", "Megan Wright", "Jack Hill", "Sophia Reed", "Alexander Brown",
    "Emily Adams", "Liam Foster", "Amelia Green", "Jacob Lopez", "Grace Moore", "Zachary Collins", "James Johnson",
    "Sophie Thomas", "Ethan Brooks", "Alexander Price", "Grace Brown", "Mia Scott", "Nathan Robinson", "Charlotte Mitchell",
    "Lucas Moore", "Megan Carter", "Zoe Johnson", "Ethan Green", "Aiden Parker", "Olivia Hill", "Isabella Lewis",
    "Ryan Thompson", "Ella Walker", "Alexander Peterson", "Grace Ward", "James White", "Samantha Green", "Michael Lopez",
    "Megan Lewis", "Ryan Cooper", "Olivia Harris", "Sophia Clark", "Mason Martin", "Lucas Davis", "Ethan Bennett",
    "Liam Brown", "Amelia Russell", "Madison White", "James Peterson", "Ella Martin", "Charlotte Parker", "Olivia Adams",
    "Grace Lewis", "Alexander Thomas", "Sophie Bennett", "Ava Foster", "Madison Lopez", "Liam Johnson", "Jacob Green",
    "Olivia Scott", "Ethan Moore", "Charlotte Lewis", "Zoe Brown", "Ryan Hall", "Madeline Harris", "Ella Clark", "Jacob White",
    "James Evans", "Amelia Ward", "Megan Ward",
    "Grace Walker", "Ryan Davis", "Harper Scott", "Ava Ross", "Mia Ward", "Madison Cooper", "Sophie Walker", "Zachary White",
    "Lucas Davis", "Benjamin Ross", "Zoe Harris", "Liam Harris", "Megan Cooper", "Nora Ross", "Sophie Green", "Ava Davis",
    "Lucas Green", "Megan Scott", "Sophie Ross", "Isabella Taylor", "James Harris", "Ava Green", "Madison Reed", "Sophie Ward",
    "Lily Cooper", "Zoe Cooper", "Lucas Scott", "James Green", "Ethan Walker", "Zachary Harris", "Ryan White", "Olivia Green",     "Daniel Cooper", "Mia Morgan", "Sophia Kelly", "Oliver Walker", "Isabella Foster", "Noah Carter", "Charlotte Rivera",
    "Jackson Phillips", "Amelia Harris", "Emma White", "James Lewis", "Sophie Ramirez", "Henry Baker", "Liam Torres",
    "Natalie Young", "Caleb Moore", "Grace Russell", "Lucas Mitchell", "Hannah Evans", "Benjamin Thomas", "Ava Johnson",
    "Ethan Clark", "Megan Robinson", "Jacob Martin", "Lily Allen", "William Brown", "Madeline Walker", "Samantha Murphy",
    "Ryan Young", "Alyssa Baker", "Charlotte Green", "Jack Nelson", "Emma Parker", "David Lee", "Sophie Campbell",
    "Tyler Hill", "Nora Roberts", "Oliver Scott", "Samantha King", "Michael Bennett", "Ella Adams", "Joshua Brooks",
    "Grace Flores", "Natalie Harris", "Liam Fisher", "Mason Brown", "Olivia Hughes", "Lucas Gray", "Chloe Peterson",
    "Daniel Foster", "Victoria Perez", "Ethan Taylor", "Sophie Martinez", "Jacob Sanders", "Madison Hall", "Alexander Carter",
    "Emily Brooks", "Charlotte Collins", "Matthew Stewart", "Olivia Powell", "Mia Bryant", "Benjamin Evans", "Isabella Hughes",
    "James Ross", "Harper Murphy", "Daniel King", "Zachary Long", "Grace Howard", "Samantha Price", "Ryan Adams",
    "Sarah Thomas", "Noah Walker", "Charlotte Harris", "Ella Gray", "William Phillips", "Avery Thompson", "Grace Davis",
    "Mason White", "Zoe Kelly", "Isaac Parker", "Chloe Lewis", "Olivia Robinson", "Alexander Hall", "Sophia Ward",
    "Matthew Anderson", "Emma Thompson", "Benjamin Russell", "Madeline Carter", "Sophie Adams", "Ryan Lee", "Victoria Foster",
    "Caleb Green", "Liam White", "Amelia Brooks", "James Mitchell", "Ava Hall", "Daniel Garcia", "Mia Moore", "Emily Nelson",
    "Michael King", "Sophie Fisher"
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

# prompt: add an age to each person between 21 and 90

import random
import datetime
import csv

people = {}

zip_codes = ['02115', '03126', '02129', '02103', '02228', '02127']
genders = ['0', '1', '2'] #male, #female, #na


i = 0
for name in fake_names:
    i = i + 1
    gender = random.choices(genders, weights=[48, 48, 4])[0]
    zip = random.choice(zip_codes)
    people[name] = { "user_id": i ,"age": random.randint(21, 60), "zip_code": zip, "gender": gender}
print(people)

fieldnames = ['Name', 'User ID', 'Age', 'Gender', 'Zip Code']
with open('consumer_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row,data in people.items():
        name, age, gender, zip_code = row, data['age'], data['gender'], data['zip_code']
        writer.writerow({
            'Name':name,
            "User ID": data['user_id'],
            'Age': data['age'],
            'Gender': data['gender'],
            'Zip Code': data['zip_code'],
        })



bars = {}

for name in fake_boston_bars:
    i = i + 1
    bars[name] = { "bar_id": i, "flow_rate": random.randint(5,40) , "bar_zipcode" :'02127'}
print(bars)

bar_fieldnames = ['Name', 'Bar ID', 'Flow Rate', 'Zip Code']
with open('bar_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=bar_fieldnames)
    writer.writeheader()
    for row,data in bars.items():
        name, bar_id, flow_rate, zip_code = row, data['bar_id'], data['flow_rate'], data['bar_zipcode']
        writer.writerow({
            'Name':name,
            'Bar ID': data['bar_id'],
            'Flow Rate': data['flow_rate'],
            'Zip Code': data['bar_zipcode'],
        })

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
  bar_id = bars[bar]['bar_id']
  flow_rate = bars[bar]['flow_rate']
  guest_estimate = random.randint(0,100)
  variance = 1.4 # can be changed as we see fit, assuming constant across each bar.
  bouncer_estimate = get_bouncer_variance(guest_estimate, variance)
  return time, name, user_id, bar, bar_id, flow_rate , guest_estimate


all_data = []


with open('simulated_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'name', 'user_id', 'bar', 'bar_id','flow_rate', 'guest_estimate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(10800): #10800 comes from needing at least 1 review every 10 minutes for 10 bars over a 30 day period.
    #so the math is 6 reviews per hour, for 6 hours (can change if needed) for 10 bars for 30 days.
      # 6*6 = 36, then 36*10 = 360 per day then 360*30 (~30 days in month) = 10,800 reviews!!
        time, name, user_id, bar, bar_id, flow_rate, guest_estimate= simulated_data()
        all_data.append([time, name, user_id, bar, bar_id, flow_rate, guest_estimate])

all_data.sort(key=lambda x: x[0], reverse=True) #wanted to get the most recent review first

with open('simulated_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_data:
        time, name, user_id, bar, bar_id, flow_rate, guest_estimate = row
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow({
            'timestamp': formatted_time,
            'name': name,
            'user_id': user_id,
            'bar': bar,
            'bar_id': bar_id,
            'flow_rate': flow_rate,
            'guest_estimate': guest_estimate
        })