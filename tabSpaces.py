import csv
csvFile= open('example.tsv','w',newline='')
csvWriter= csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
csvWriter.writerow(['apples','orange','grapes'])
csvFile.close()
