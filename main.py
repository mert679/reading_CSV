import csv

DATE_FILE = "grades.csv"

fileHandle = open(DATE_FILE,"r")
csvParsed =csv.reader(fileHandle)

def getLetterGrade(score):
  letter= ""
  if score>=90 :
    letter = "A"
  elif score >=80:
    letter = "B"
  elif score >=70:
    letter = "C"
  elif score >=60:
    letter = "D"

  else:
    letter = "F"
  return letter



count = 0
readingHeader = True



for row in csvParsed:
  if readingHeader:
    readingHeader = False
    continue
  # if count ==0:
  #   count = 1
  #   continue
  name = row[0]
  #print(name)

  total = 0

  for index in range(1,8):
    thisGrade = row[index]
    if thisGrade == "":
      thisGrade = 0.0
    else:
      thisGrade=float(thisGrade)
    
    total += thisGrade
  
  percent = total/2
  letterGrade = getLetterGrade(percent) 
  print(name,"percent",percent, "letterGrade: ", letterGrade)
