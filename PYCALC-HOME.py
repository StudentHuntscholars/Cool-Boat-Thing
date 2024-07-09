from datetime import datetime, timedelta

def BoatParser(BoatData):
    BoatList = []
    tempName = ""
    tempNum = ""
    readingName = True
    for i in range(0, len(BoatData)):
        if readingName == True:
            if BoatData[i] == " ":
                readingName = False
                BoatList.append(tempName)
                tempName = ""
            else:
                tempName = tempName + BoatData[i]
            
        else:
            if BoatData[i] == "\n":
                readingName = True
                BoatList.append(int(tempNum))
                print(BoatList)
                tempNum = ""
            else:
                tempNum = tempNum + BoatData[i]

    return BoatList


# Get the current time
startime = datetime.now() # 20


# Get today's date
today = datetime.today()

input()

# Calculate the time difference
time_difference = datetime.now() - startime 

# Print the time difference in seconds
print(f"The race has been going on for approximately {time_difference.total_seconds():.2f} seconds")

# Define the GetAdjustedTime function.
def GetAdjustedTime(py, Elasted_time):
    return Elasted_time * 1000 / py

# Boats
py_table = {"ILCA 6": 1154, "ILCA 7": 1102}


# Calculate the adjusted times for boats (ILCA 6 and ILCA 7)
adjus_time = GetAdjustedTime(py_table["ILCA 6"], time_difference)
adjus_time1 = GetAdjustedTime(py_table["ILCA 7"], time_difference)

# Convert the timedelta objects to seconds
adjus_time_seconds = adjus_time.total_seconds()
adjus_time1_seconds = adjus_time1.total_seconds()

# Print the adjusted times in seconds
print(f"Adjusted time for the ILCA 6 is approximately {adjus_time_seconds:.0f} seconds")
print(f"Adjusted time for the ILCA 7 is approximately {adjus_time1_seconds:.0f} seconds")

# Calculate the difference needed for the ILCA 7 to beat the ILCA 6
time_difference_seconds = adjus_time1.total_seconds() - adjus_time.total_seconds()

# Print the difference needed for the ILCA 7 to beat the ILCA 6
if time_difference_seconds > 0:
    print(f"The ILCA 7 needs to finish ahead by approximately {time_difference_seconds:.0f} seconds to win.")
