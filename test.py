def averagesleep(n):
        import csv
        with open('sleepexport2.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                L = []
                for row in readCSV:
                        L.append(row[5])
                M = L[-n:]
                import statistics
                M = [float(x) for x in M]
                print (statistics.mean(M))

def heartrate(n):
        import csv
        with open('sleepexport2.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                L = []
                for row in readCSV:
                        L.append(row[11])
                M = L[-n:]
                import statistics
                M = [float(x) for x in M]
                print (statistics.mean(M))
        
    
