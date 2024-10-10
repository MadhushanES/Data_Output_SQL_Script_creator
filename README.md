# Data_Output_SQL_Script_creator
Create Sql scripts for output Data related to given time period. This is to get data separately from a large data collection.

For this I used python language and user can input start date and end date of the data that want and then user can input number of days for separate data sets to separate csv files. Then the programm will generate single sql files for each data ranges and one master script for run all scripts. In this I used Arrival date for start date of data set and departure date for end date. And I used a table called TEST_TABLE_OF_OROJECT for data table. User can customized this according to requirement.

Libraries :
  datetime   - used for handling dates and times
  timedelta  - used for representing the difference between two dates

-By Madhushan Pilapitiya
