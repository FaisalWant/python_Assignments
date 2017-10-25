import csv
exampleFile= open('example.csv')
exampleReader=csv.reader(exampleFile)  #iterates over the lines of a file
#exampleData=list(exampleReader)
#print(exampleData)

for row in exampleReader:
      print('Row #' +str(exampleReader.line_num)+' '+str(row))

outputFile= open('output.csv','w',newline='')
outputWriter=csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
