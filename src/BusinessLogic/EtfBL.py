from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import yfinance as yf

def _calculatePerformance(initialPrice, finalPrice):
    difference = finalPrice - initialPrice
    performance = difference * 100 / initialPrice
    return performance

def _calculatePerformanceSum(currentPrice, priceOneMonthAgo, priceThreeMonthsAgo, priceSixMonthsAgo):

    oneMonthPerformance = round(_calculatePerformance(priceOneMonthAgo, currentPrice),2)
    threeMonthsPerformance = round(_calculatePerformance(priceThreeMonthsAgo,  currentPrice),2)
    sixMonthsPerformance = round(_calculatePerformance(priceSixMonthsAgo, currentPrice),2)

    performanceSum = oneMonthPerformance + threeMonthsPerformance + sixMonthsPerformance
    performance = {
        'performanceSum': performanceSum
    }

    return performance

def _getPrice(date, etf, columnsNumber):
    for i in range(0, columnsNumber):
        if etf['Date'][i] == date:
            return etf['Close'][i]
        

        return 0

def _getPriceDate(etf, columnsNumber, delta):
    pricedate = data['Date'][columnsNumber - 1] - relativedelta(months = delta)
    if pricedate.weekday() == 5:
        pricedate -= relativedelta(day = 1)
    elif pricedate.weekday() == 6:
        pricedate += relativedelta(day = 1)
   
    return pricedate

def CalculateETFPerformance(etf):
    columnsNumber = etf.columns[0].count()
    currentPrice = etf['Close'][columnsNumber - 1]

    oneMonthAgoDate = _getPriceDate(etf,columnsNumber,1)
    threeMonthsAgoDate = _getPriceDate(etf,columnsNumber,3)
    sixMonthsAgoDate = _getPrice(etf,columnsNumber,6)

    oneMonthAgoPrice = _getPrice(oneMonthAgoDate,etf,columnsNumber)
    threeMonthsAgoPrice = _getPrice(threeMonthsAgoDate,etf,columnsNumber)
    sixMonthsAgoPrice = _getPrice(sixMonthsAgoDate,etf,columnsNumber)

    performanceSum = _calculatePerformanceSum(currentPrice, oneMonthAgoPrice, threeMonthsAgoPrice, sixMonthsAgoPrice)
    etf ={
        'name': etf,
        'performancesum': performanceSum,

    }
    return etf

def DownloadData():
    finaldate = datetime.today()    
    yearbackdate = (finaldate - timedelta(days=365)).strftime('%Y-%m-%d')
    finaldate = finaldate.strftime('%Y-%m-%d')
    fds = str(finaldate)
    ids = str(yearbackdate)

    spy = yf.download('SPY', period='1y', interval='1d' , start=ids, end=fds)
    vss = yf.download('VSS', period='1y', interval='1d' , start=ids, end=fds)
    scz = yf.download('SCZ', period='1y', interval='1d' , start=ids, end=fds)
    osmax = yf.download('OSMAX', period='1y', interval='1d' , start=ids, end=fds)
    tlt = yf.download('TLT', period='1y', interval='1d' , start=ids, end=fds)

    data = {
        "spy": spy,
        "vss": vss,
        "scz": scz,
        "osmax": osmax,
        "tlt": tlt
    }
    return data
