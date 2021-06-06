#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We get the parameter list from the line
    params_list = line.strip().split(",")

    #(00) start_time => A String representing the time the trip started at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:05:00”
    #(01) stop_time => A String representing the time the trip finished at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:10:00”
    #(02) trip_duration => An Integer representing the duration of the trip. Example: 300
    #(03) start_station_id => An Integer representing the ID of the CityBike station the trip started from. Example: 150
    #(04) start_station_name => A String representing the name of the CitiBike station the trip started from. Example: “E 2 St &; Avenue C”.
    #(05) start_station_latitude => A Float representing the latitude of the CitiBike station the trip started from. Example: 40.7208736
    #(06) start_station_longitude => A Float representing the longitude of the CitiBike station the trip started from. Example:  -73.98085795
    #(07) stop_station_id => An Integer representing the ID of the CityBike station the trip stopped at. Example: 150
    #(08) stop_station_name => A String representing the name of the CitiBike station the trip stopped at. Example: “E 2 St &; Avenue C”.
    #(09) stop_station_latitude => A Float representing the latitude of the CitiBike station the trip stopped at. Example: 40.7208736
    #(10) stop_station_longitude => A Float representing the longitude of the CitiBike station the trip stopped at. Example:  -73.98085795
    #(11) bike_id => An Integer representing the id of the bike used in the trip. Example:  33882
    #(12) user_type => A String representing the type of user using the bike (it can be either “Subscriber” or “Customer”). Example: “Subscriber”.
    #(13) birth_year => An Integer representing the birth year of the user using the bike. Example:  1990
    #(14) gender => An Integer representing the gender of the user using the bike (it can be either 0 => Unknown; 1 => male; 2 => female). Example:  2.
    #(15) trip_id => An Integer representing the id of the trip. Example:  190

    # 3. If the list contains the right amount of parameters
    if (len(params_list) == 16):
        # 3.1. We set the right type for the parameters
        params_list[2] = int(params_list[2])
        params_list[3] = int(params_list[3])
        params_list[5] = float(params_list[5])
        params_list[6] = float(params_list[6])
        params_list[7] = int(params_list[7])
        params_list[9] = float(params_list[9])
        params_list[10] = float(params_list[10])
        params_list[11] = int(params_list[11])
        params_list[13] = int(params_list[13])
        params_list[14] = int(params_list[14])
        params_list[15] = int(params_list[15])

        # 3.2. We assign res
        res = tuple(params_list)

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    
    #Empty list to hold all bike IDs mentioned in the files
    bikeIdList = []
    
    #Set to hold all unique bike IDs
    bikeIdListUnique = set()
    
    #List to hold all tuples from each csv file together
    combined_data = []
    
    # Iterate over each row in the csv and use the process function and add result to list
    for row in my_input_stream:
        combined_data.append(process_line(row))
                      
    #Add bike ID in each row to above list
    for cd in combined_data:
        bikeIdList.append(cd[11])
        
    #Loop over all bike IDs mentioned and add to set, removing duplicates
    for x in bikeIdList:
        bikeIdListUnique.add(x)

    #Empty list to hold Id for each bike and its duration cycled and number of trips
    bike_tuple_list = list()
    
    #Loops over each unique bike ID, loops over each tuple from csv row
    for x in bikeIdListUnique:
     
        #Initializing trip duration and trip number to zero
        totalTripDuration = 0
        totalTripNumber = 0
        
        #Loop over list of all rows combined from all datasets
        for d in combined_data:
            
            #If the bike ID is in a row, add the trip duration and increment the trip number
            if (d[11] == x):
                totalTripDuration = totalTripDuration + d[2]
                totalTripNumber = totalTripNumber + 1
        
        #Loop is exited for that bike ID, its ID, trip duration and trip number are recorded into a tuple   
        bike_tuple = (x, totalTripDuration, totalTripNumber)
        
        #That tuple is then added to a list of tuples, and initialized to empty for the next bike ID
        bike_tuple_list.append(bike_tuple)
        bike_tuple = ()                       
    
    #Loop over the list of tuples and write each to the file as a line of text
    for x in bike_tuple_list:
        my_output_stream.write("universal" + "\t (" + str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ")\n")

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    file_name = "2019_05_10.csv"

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        file_name = sys.argv[1]

    # 2. Local or Hadoop
    local_False_hadoop_True = False

    # 3. We set the path to my_dataset and my_result
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout

    if (local_False_hadoop_True == False):
        my_input_stream = "../../my_dataset/" + file_name
        my_output_stream = "../../my_results/A01_Part5/1_my_map_simulation/" + file_name[:-4] + ".txt"

    # 4. my_mapper.py input parameters
    my_mapper_input_parameters = []

    # 5. We call to my_main
    my_map(my_input_stream, my_output_stream, my_mapper_input_parameters)
