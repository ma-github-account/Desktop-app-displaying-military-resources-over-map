The application displays strategic military resources positions on the map of the Ukraine.
User chooses map region, map type and map settings. After clicking Reload map is displayed.
The coordinates of the resources are stored in the database and uploaded from it before displaying map.

Prerequisites: 
- Python 3.9.7,
- mathplotlib,
- tkinter, 
- pyodbc.

The database:

CREATE TABLE [dbo].[Strategic_resources]( 
[Resource_type] varchar (50) NOT NULL, 
[Lon] [float] NOT NULL, 
[Lat] [float] NOT NULL, 
)

How to run: python strategic_resources_displayer.py






![1](https://user-images.githubusercontent.com/89083426/170118462-d906c098-4380-4fef-bfea-d3b6b4197c43.png)



![2](https://user-images.githubusercontent.com/89083426/170118481-5d6ebe8d-8299-41f0-aee9-864a45e71e5c.png)




![3](https://user-images.githubusercontent.com/89083426/170118494-623b85dd-5c10-464b-abe5-03cab1ba4707.png)




![4](https://user-images.githubusercontent.com/89083426/170118502-b50506b8-4ce7-4106-a5a9-ef4e5db2fcc8.png)











