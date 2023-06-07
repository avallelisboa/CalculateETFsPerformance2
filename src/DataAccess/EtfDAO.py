import pandas as pd
import xlrd

def SaveFiles(dataframes):
    spy = dataframes["spy"]
    vss =  dataframes["vss"]
    scz =  dataframes["scz"]
    osmax = dataframes["osmax"]
    tlt =  dataframes["tlt"]
    
    spy.to_excel("spy.xlsx", sheet_name="SPY_Year_Price")
    vss.to_excel("vss.xlsx", sheet_name="VSS_Year_Price")
    scz.to_excel("scz.xlsx", sheet_name="SCZ_Year_Price")
    osmax.to_excel("osmax.xlsx", sheet_name="OSMAX_Year_Price")
    tlt.to_excel("tlt.xlsx", sheet_name="TLT_Year_Price")

def ReadFiles():
    spy = pd.read_excel("spy.xlsx")
    vss = pd.read_excel("vss.xlsx")
    scz = pd.read_excel("scz.xlsx")
    osmax = pd.read_excel("osmax.xlsx")
    tlt = pd.read_excel("tlt.xlsx")

    data = {
        "spy": spy,
        "vss": vss,
        "scz": scz,
        "osmax": osmax,
        "tlt": tlt
    }
    return data

def ReadTripleMomentum():
    etfstrmom = pd.read_excel("triplemomentumetfs.xlsx")
    return etfstrmom