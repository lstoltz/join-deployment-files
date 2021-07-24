# join-deployment-files
Processing geospatial data by consuming text file and CSV data to output a combined CSV file for a more readily consumable format. Script also querys nearest GPS location against a bathymetry file to find approximate depths for crab pot deployments

## Use
In the python script, specify the absolute ``` PATH ``` to where the data are stored. This script will research all subdriectories if present, no folder assumed folder structure.
 
To run:
    first run ``` pip install requirements.txt ```
    second create ``` .env ``` file at the root directory and create four variables:
     ``` SRC = file_path_to_data
    BATHY_PATH = file_path_to_bathymetry_file
    DEST = file_path_to_data_destination
    FLAG = file_path_for_flagged_data ``` 

### Disclaimer
If no GPS file is found matching the CSV file, no coordinates will be appended.

```latitude_start``` and ```longitude_start``` coincide with the logger being interacted with by the DDH, i.e. before going back in the water (rws on GPS file)

```latitude_stop``` and ```longitude_stop``` coincide with the logger coming aboard after a deployment (sws on GPS file)