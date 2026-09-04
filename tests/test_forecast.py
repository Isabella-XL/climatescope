from unittest.mock import MagicMock, patch

from app.services.forecasting.predictor import predict_temperature


def test_predict_temperature():
    features = {
        "TG_lag_1": 10.0,
        "TN_lag_1": 8.0,
        "TX_lag_1": 12.0,
        "TG_lag_7": 11.0,
        "TG_rolling_7": 10.5,
        "TG_rolling_14": 10.8,
        "day_of_year_sin": 0.5,
        "day_of_year_cos": 0.8,
    }

    fake_model = MagicMock()
    fake_model.predict.return_value = [12.5]

    with patch(
        "app.services.forecasting.predictor.load_model",
        return_value=fake_model,
    ):
        result = predict_temperature(features)

    assert result == 12.5
    fake_model.predict.assert_called_once()
