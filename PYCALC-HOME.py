from datetime import datetime, timedelta
## Parser to get boat data from the boat database "PYLIST.txt"
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
                #rint(BoatList)
                tempNum = ""
            else:
                tempNum = tempNum + BoatData[i]

    return BoatList


## Define the GetAdjustedTime function.
## This is used to get corrected time on PY, Time Elased in seconds * 1000 / the boat's Py num
def GetAdjustedTime(py, Elasted_time):
    return Elasted_time * 1000 / py

def BoatPrinter(BoatList):
    for i in range(0, len(BoatList) - 1, 2):
        print(f"Adjusted time for the {0} is approximately {1:.2f} seconds", BoatList[i], BoatList[i + 1])



## Get the current time
startime = datetime.now() # 20


## Get today's date
today = datetime.today()

input("Enter a character to get results ")

## Calculate the time difference
time_difference = datetime.now() - startime 

## Print the time difference in seconds
print(f"The race has been going on for approximately {time_difference.total_seconds():.2f} seconds")


with open("PYLIST.txt", "r") as MyFile:
    BoatFile = MyFile.read()
BoatList = BoatParser(BoatFile)
#Hours wasted debugging plz update 2
## Boats
NewBoatList = []
#for i in range(1, len(BoatList) - 1, 2):
#    NewBoatList.append(GetAdjustedTime(BoatList[i], time_difference).total_seconds())
NewBoatList.append(GetAdjustedTime(BoatList[1], time_difference).total_seconds())
NewBoatList.append(GetAdjustedTime(BoatList[3], time_difference).total_seconds())
"""Need to work on how to print the boat names and where
they need to be on the race track to win. This is done by boat class and."""
## Calculate the adjusted times for boats (ILCA 6 and ILCA 7)

"""adjus_time = GetAdjustedTime(py_table["ILCA 6"], time_difference)
adjus_time1 = GetAdjustedTime(py_table["ILCA 7"], time_difference)"""

## Convert the timedelta objects to seconds

#adjus_time_seconds = adjus_time.total_seconds()
#adjus_time1_seconds = adjus_time1.total_seconds()

## Print the adjusted times in seconds
## Calculate the difference needed for the ILCA 7 to beat the ILCA 6

time_difference_seconds = NewBoatList[1] - NewBoatList[0]
print(time_difference_seconds, NewBoatList)

## Print the difference needed for the ILCA 7 to beat the ILCA 6

if time_difference_seconds > 0:
    print(f"The boat needs to finish ahead by approximately {time_difference_seconds:.0f} seconds to win.")
