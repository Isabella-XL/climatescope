from app.services.forecasting.predictor import predict_temperature

features = {
    "TG_lag_1": 10.5,
    "TN_lag_1": 7.2,
    "TX_lag_1": 13.1,
    "TG_lag_7": 9.8,
    "TG_rolling_7": 10.2,
    "TG_rolling_14": 9.7,
    "day_of_year_sin": 0.45,
    "day_of_year_cos": 0.89,
}

prediction = predict_temperature(features)

print(f"Predicted temperature: {prediction:.2f} °C")
