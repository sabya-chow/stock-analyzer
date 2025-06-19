import yfinance as yf
import pandas as pd
import os

def get_stock_data(ticker="TCS.NS", period="6mo", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

def save_stock_data(df: pd.DataFrame, ticker="TCS", out_dir="data/processed"):
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, f"{ticker}_ohlc.csv")
    df.to_csv(file_path)
    print(f"Saved OHLC data to: {file_path}")
