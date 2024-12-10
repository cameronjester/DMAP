# DMAP

## Fall 2024 Final Project for Data Management and Processing 

### Where to find our Final Project submissions:
* Final Presentation: Saved in our repo named "DMAP Final Presentation.pdf"
* Final Technical Report: Saved in our repo named "FinalReport.pdf"
* Final Code: Saved in our repo in various important files.
    * "Aggregation.ipynb" is where we calculated 10 minute time intervals of our Line Estimates for analysis.
    * "BarVisuals.ipynb" and "User_Visuals.ipynb" is where the visualizations based off our simulated data exists. These visuals are what Bar Patrons would see.
    * "db-config.ipynb" is where we configured our MySQL database and loaded the data into the tables using SQL queries.
    * "dmap_final_simulateddata.py" is where we generated the simulated data using various python methods to create random data while conforming to our table structures.
    * "bar_data_cleaned.csv", "user_data_cleaned.csv", and "review_data_cleaned.csv" is where our data lives. These 3 files represent the 3 tables of data in our relational database.
    * "final-project-erd.png" is our ERD diagram for our final project data.

### Project Responsibilities and Timelines:

	- Steps 
		○ ONGOING (both) document workflow and process in a shared word document
		○ (matt) setup sql database server
		○ (matt) create tables and define schema
		○ (cameron) simulate data per our discussion
		○ (both) insert data into tables
		○ -
		○ (both) brainstorm/design dashboard for both user and bar
			§ Matt does user side, cameron does bar side
			§ Could be any output that a user wants to see: charts, tables, and visualization 
		○ (matt) write python connectors to get data out of sql server
		○ (cameron) preprocessing, calculations, aggregations
		○ (both) write python to implement dashboards and output charts 
		○ -
		○ (both) Slides
		○ (both) Presentation
		○ (both) Demo
			§ Show sql server and table schema
			§ Show how we simulated data and inserted it
			§ Show python connectors
			§ Show how we preprocessed
			§ Show how we output the visualizations
	- Timelines (Weeks)
		○ 1
			§ Setup sql server
			§ Create tables define schema
			§ Simulate data
			§ Insert data (stretch)
		○ 2
			§ Brainstorm dashboards and visualizations
			§ Write python connectors to access data
			§ Preprocessing, aggregation
		○ 3
			§ Write python to implement actual dashboards
				□ Maybe seeps into week 4
		○ 4
			§ Overleaf start
		○ 5
			§ Overleaf finish
			§ Slides, presentation, and demo
