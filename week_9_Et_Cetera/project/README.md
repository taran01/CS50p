# WEATHER EXPLORER
### Video Demo:
#### https://youtu.be/ommqV27cK4M
<br/>

### Source Code:
#### https://github.com/taran01/CS50p/tree/main/project
<br/>

#### Description:
FInal Project for Harvard's CS50's Introduction to python. Weather program made using python. Used openweathermap.org's api to get current weather details. Required modules are in requirements.txt.

 Implemented get_city function to validate city name. This function raises ValueError if input is empty. Else it check the input for given regex pattern and returns it. If the pattern does not match, the function raises ValueError.

 Implemented get_unit function to validate unit of measure. This function raises ValueError if input is empty, or if input is not "c" nor "c". If input is "c" the function returns "matric". If input is "f" the function returns "imperial".

 Used while loops to use abovementioned functions to get city and unit until ctrl + d is pressed.

 User must have to provide either "c" or "f" on unit promt.
 User must have to provide one or more city names. Program supports for multiple weather enquiries.

 After getting city(s) used check_error function (which takes as argument the return json data from api) which validates if api recoginised the city name.

 If valid city name then use tabulate module to print a pretty table that shows current weather and some other details in terminal.
 Tabulate uses get_table function (argumets: response from api in json, unit of measure) which returns a list of lists where each list is weather detail each for "metric" or "imperial" unit.
 
 Else print the message from api (if city is not found) or any other error.
<br/>
#### Follow the below instructions:
    1. Type "python project.py" at command-line
    2. Type "C" for Celcius or "F" for Fahrenheit
    3. Type one or more valid city name
    4. Press "ctrl + d" to end city prompt

<br/>

#### Your provided city's current weather should be shown
<br/>

### Concepts Used:
#### functions, loops, exceptions, regular expressions, libraries, unit testing etc.