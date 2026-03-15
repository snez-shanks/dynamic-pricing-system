import pandas as pd
from prophet import Prophet

data = pd.read_csv("dataset/pricing_data.csv")

forecast_data = data[['date','demand']]

forecast_data.columns = ['ds','y']

model = Prophet()

model.fit(forecast_data)

future = model.make_future_dataframe(periods=7)

forecast = model.predict(future)

print(forecast[['ds','yhat']].tail())