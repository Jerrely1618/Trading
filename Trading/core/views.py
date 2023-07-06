from django.shortcuts import render
from utils import APIconnection

financeData = APIconnection()

def guest(request):
    script,div = financeData.getStockGraph("VOO","Max")
    context = {
        "VOO": financeData.getStockPrice("VOO"),
        "AAPL":financeData.getStockPrice("AAPL"),
        "GOOGL":financeData.getStockPrice("GOOGL"),
        "TSLA":financeData.getStockPrice("TSLA"),
        "AMZN":financeData.getStockPrice("AMZN"),
        "script":script,
        "div": div,
    }
    return render(request,'guest/GuestHome.html',context)

def login(request):
    return render(request,'guest/Login.html')

def signup(request):
    return render(request,'guest/SignUp.html')
