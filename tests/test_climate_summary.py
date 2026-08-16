from app.services.climate_data.analysis import calculate_temperature_summary


def test_calculate_temperature_summary():
    temperatures = [10.0, 20.0, 30.0]

    result = calculate_temperature_summary(temperatures)

    assert result["count"] == 3
    assert result["average"] == 20.0
    assert result["minimum"] == 10.0
    assert result["maximum"] == 30.0
