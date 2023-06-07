import os
import keyboard
import src

def Clear():  
   os.system('cls' if os.name == 'nt' else 'clear')

def ReadFiles():
    data = ReadFilesDA()
    return data

def SaveFiles(dataframes):
    try:
        SaveFilesDA(dataframes)
        return True
    except:
        return False


def DownloadData():
    data = DownloadDataBL()
    wasSaved = SaveFiles(dataframes)    

def etfSort(e):
        return e['performancesum']

def PerformanceList():
    data = ReadFiles();
    spy = CalculateETFPerformance(data['spy'])
    vss = CalculateETFPerformance(data['vss'])
    scs = CalculateETFPerformance(data['scz'])
    osmax = CalculateETFPerformance(data['osmax'])
    tlt = CalculateETFPerformance(data['tlt'])

    etfslist= list()
    etfslist.append(spy)
    etfslist.append(vss)
    etfslist.append(scs)
    etfslist.append(osmax)
    etfslist.append(tlt)

    etfslist.sort(reverse=True, key=etfSort)
    for etf in etfslist:
        print(etf['name'])
        print("Rendimiento semestral: " + str(etf['semiannualperformance']))
        print("Rendimiento trimestral: " + str(etf['threemonthsperformance']))
        print("Rendimiento mensual: " + str(etf['monthlyperformance']))
        print("Sumatoria: " + str(etf['performancesum']))
        print('\n')
    
    print("\n Presione una tecla para continuar")

    keyboard.read_key()

    Clear();
