from flask import Flask, request
import pandas as pd
import requests
import sqlite3
import tqdm 

app = Flask(__name__) 

# Define a function to create connection for reusability purpose
def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

# Make a connection
conn = make_connection()

def get_station_id(station_id, conn):
    query = f"""SELECT * FROM stations WHERE station_id = {station_id}"""
    result = pd.read_sql_query(query, conn)
    print(station_id)
    print(query)
    print(result)
    return result 

def get_all_stations(conn):
    query = f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

# Your code here
def get_trip_id(trip_id, conn):
    query = f"""SELECT * FROM trips WHERE trip_id = {trip_id}"""
    result = pd.read_sql_query(query, conn)
    return result 
    
def get_all_trips(conn):
    query = f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result

def get_bike_id(bikeid, conn):
    query = f"""SELECT * FROM trips WHERE bikeid = {bikeid}"""
    result = pd.read_sql_query(query, conn)
    return result 

def insert_into_stations(data, conn):
    query = f"""INSERT INTO stations values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

def insert_into_trips(data, conn):
    query = f"""INSERT INTO trips values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

@app.route('/')
def home():
    return '<head> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"> <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:300,400,700"> <!-- <link rel="stylesheet" href="https://kit.fontawesome.com/2046858601.css" crossorigin="anonymous"> --> <script src="https://kit.fontawesome.com/2046858601.js" crossorigin="anonymous"></script> <script src="assets/scripts/sweetalert.min.js"></script> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script> <script src="https://code.jquery.com/jquery-3.6.3.js" integrity="sha256-nQLuAZGRRcILA+6dMBOvcRh5Pe310sBpanc6+QBmyVM=" crossorigin="anonymous"></script> </head> <body data-bs-theme="dark" id="body"> <div class="container"> <div id="bike-sharing-api" class="section level2 tab-pane tabbed-pane active" number="3.2" role="tabpanel"> <div align="center"> <iframe width="728" height="410" src="https://www.youtube.com/embed/HNidIZd_-eo" data-external="1" allowfullscreen=""></iframe> <p> <a href="https://bit.ly/capstone_api" target="_blank">📁 <strong>GitLab Repository</strong>: Bike Sharing API </a> </p> </div> <div align="center"> <div id="rubrics-bike-sharing-api" class="section level3" number="3.2.1"> <div name="321_Rubrics:_Bike_Sharing_API" data-unique="321_Rubrics:_Bike_Sharing_API"></div> <h3> <span class="header-section-number">3.2.1</span> Rubrics: Bike Sharing API </h3> <ol style="list-style-type: decimal"> <li class="list-group-item"> <p>[ <strong>1 point</strong>] Created Flask App </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create app.py file to make flask app</p> </li> <li class="list-group-item"> <p>create Flask app to execute all of the endpoint you have made</p> </li> </ul> </li> <br><br> <li class="list-group-item"> <p>[ <strong>2 points</strong>] Created functionality to read or get specific data from the database </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create query to read data from database</p> </li> <li class="list-group-item"> <p>create function to execute read specific information into table from database</p> </li> </ul> </li> <br><br> <li class="list-group-item"> <p>[ <strong>4 points</strong>] Created functionality to input new data into each table for the databases </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create query to insert new data into stations and trips table</p> </li class="list-group-item"> <li class="list-group-item"> <p>create function to execute input data into stations and trips table</p> </li class="list-group-item"> </ul> </li> <br><br> <li class="list-group-item"> <p>[ <strong>3 points</strong>] Created static endpoints which return analytical result (must be different from point 2,3) <a href="/trips/average_duration/">[Link]</a> </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create query to make analytical result from the data</p> </li> <li class="list-group-item"> <p>create static endpoint to analyze the data from database, for example average trip durations</p> </li> </ul> </li> <br><br> <li class="list-group-item"> <p>[ <strong>3 points</strong>] Created dynamic endpoints which return analytical result (must be different from point 2,3,4)  <a href="/trips/average_duration/19456/">[Link (example: 19456)]</a> </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create query to make analytical result from the data</p> </li> <li class="list-group-item"> <p>create dinamic endpoint to analyze the data from database, for example average trip durations for each bike_id</p> </li> </ul> </li> <br><br> <li class="list-group-item"> <p>[ <strong>3 points</strong>] Created POST endpoint which receive input data, then utilize it to get analytical result (must be different from point 2,3,4,5) </p> <ul class="list-group mx-auto justify-content-center"> <li class="list-group-item"> <p>create input data for refering into query for post endpoint</p> </li> <li class="list-group-item"> <p>make query and aggregation function to implement the input</p> </li> </ul> </li> <br><br> </ol> <hr> <p> <br><br> </p> </div> </div> </div> </div> </body>'

@app.route('/stations/')
def route_all_stations():
    conn = make_connection()
    stations = get_all_stations(conn)
    return stations.to_json()
    
def get_all_stations(conn):
    query = f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

@app.route('/trips/')
def route_all_trips():
    conn = make_connection()
    trips = get_all_trips(conn)
    return trips.to_json()
    
def get_all_trips(conn):
    query = f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result



@app.route('/stations/<station_id>/')
def route_stations_id(station_id):
    conn = make_connection()
    station = get_station_id(station_id, conn)
    return station.to_json()


@app.route('/json', methods=['GET', 'POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    name = req['name']
    age = req['age']
    address = req['address']
    
    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')

@app.route('/stations/add', methods=['POST']) 
def route_add_station():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_stations(data, conn)
    return result

@app.route('/trips/average_duration/')
def avg_all_bike():
    conn = make_connection()
    avgs = get_avg_all_bike(conn)
    return avgs.to_json()
    
def get_avg_all_bike(conn):
    query = f"""SELECT bikeid, AVG(duration_minutes) AS AVG_MIN FROM trips GROUP BY bikeid ORDER BY AVG_MIN DESC"""
    result = pd.read_sql_query(query, conn, index_col='bikeid')
    return result

#WHERE bikeid = {bikeid} 
# Your Code Here
@app.route('/trips/average_duration/<bikeid>/')
def avg_bike_id(bikeid):
    conn = make_connection()
    query = f"""SELECT bikeid, AVG(duration_minutes) AS AVG_MIN FROM trips WHERE bikeid = "{bikeid}" GROUP BY bikeid ORDER BY AVG_MIN DESC"""
    avg = pd.read_sql_query(query, conn, index_col='bikeid')
    return avg.to_json()

@app.route('/dictionary/', methods=['GET', 'POST'])
# Your Code Here
def dictionary():
    input_data = request.get_json(force=True) # Get the input as dictionary
    specified_date = input_data['period'] # Select specific items (period) from the dictionary (the value will be "2015-08")
    # Subset the data with query 
    conn = make_connection()
    query = f"SELECT * FROM trips WHERE start_time LIKE '{specified_date}%'"
    selected_data = pd.read_sql_query(query, conn)

    # Make the aggregate
    result = selected_data.groupby('start_station_id').agg({
        'bikeid' : 'count', 
        'duration_minutes' : 'mean'
    })


    # Return the result
    return result.to_json()


if __name__ == '__main__':
    app.run(debug=True, port=5000)




