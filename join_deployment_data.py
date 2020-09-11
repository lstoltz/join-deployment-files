import os
from glob import glob
import pandas as pd
import fnmatch as fn
PATH = r"C:\Users\lstol\Documents\repositories\process-data\Data"
BATHY_PATH = r"C:\Users\lstol\Documents\repositories\join-deployment-files\Bathymetry_Oregon_300m_all_NA.txt"

''' Linus Stoltz 9/9/20 ~ Oregon State University
    This script will read all csv and gps files in a specified directory and append the GPS information
    to the excel file.
'''

def findCSV(PATH):
    csvFiles = [file
                    for path, subdir, files in os.walk(PATH) # find all csv files in a directory
                    for file in glob(os.path.join(path, '*.csv'))]
    return csvFiles

def findGPS(PATH):
    gpsFiles = [file
                    for path, subdir, files in os.walk(PATH) # find all csv files in a directory
                    for file in glob(os.path.join(path, '*.gps'))]
    return gpsFiles

def appendMiscData():
    bathy_data = pd.read_csv(BATHY_PATH)
    for file in findCSV(PATH):
        currentCSV = os.path.basename(file)[:-20]
        gpsFilePath = fn.filter(findGPS(PATH), str('*'+currentCSV+'*'))
        if gpsFilePath == []:
            pass
        else:
            coordinates = determineLatLong(gpsFilePath)
            df = pd.read_csv(file)
            df =  df.assign(latitude_stop =coordinates[0],
            longitude_stop =coordinates[1],
            latitude_start =coordinates[2],
            longitude_start =coordinates[3])
            
    
            stop_lat_idx = df.iloc(df['latitude_stop'].unique().sub(bathy_data.iloc[:,2])).abs().idxmin()
            stop_lon_idx = df.iloc(df['longitude_stop'].sub(bathy_data.iloc[:,1])).abs().idxmin()
            print(stop_lat_idx, stop_lon_idx)
   # df.to_csv(file, index = False)    
 

def determineLatLong(gpsFilePath):
    sws = None
    rws = None
    latitude_RWS = None
    longitude_RWS = None
    latitude_SWS = None
    longitude_SWS = None

    with open(gpsFilePath[0]) as fp:
        for cnt, line in enumerate(fp):
            if ("RWS" in line):
                rws = line.replace("RWS: ", "")
            elif ("SWS" in line):
                sws = line.replace("SWS: ", "")

        # Use appropriate value (default to SWS) and then split up lat/long
        if (sws and "N/A" not in sws):
            endOfLatIndex = sws.find(".") + 7
            latitude_SWS = sws[0:endOfLatIndex]
            longitude_SWS = sws[endOfLatIndex:]
        else:
            latitude_SWS = "N/A"
            longitude_SWS = "N/A"
        if (rws and "N/A" not in rws):
            endOfLatIndex = rws.find(".") + 7
            latitude_RWS = rws[0:endOfLatIndex]
            longitude_RWS = rws[endOfLatIndex:]
        else:
            latitude_RWS = "N/A"
            longitude_RWS = "N/A"


    return latitude_SWS.strip(), longitude_SWS.strip(), latitude_RWS.strip(), longitude_RWS.strip()
    
def main():
    appendMiscData()
    

main()