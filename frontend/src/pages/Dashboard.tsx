import { useEffect, useState } from "react";
import ClimateMeasurementCard from "../components/ClimateMeasurementCard";
import TemperatureChart from "../components/TemperatureChart";


import ClimateSummary from "../components/ClimateSummary";
import {
   getClimateForecast,
  getClimateSummary,
  getMeasurements,
  buildForecastFeatures,
  type ClimateForecast,
  type ClimateMeasurement,
  type ClimateSummary as ClimateSummaryData,
} from "../services/climateApi";




function Dashboard() {
  const [summary, setSummary] = useState<ClimateSummaryData | null>(null);
  const [measurements, setMeasurements] = useState<ClimateMeasurement[]>([]);
  const [forecast, setForecast] =
  useState<ClimateForecast | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadMeasurements() {
      try {
        const data = await getMeasurements();
        setMeasurements(data);
        const features = buildForecastFeatures(data);

const forecastData = await getClimateForecast(features);
setForecast(forecastData);


console.log("Forecast features:", features);
console.log("Forecast:", forecastData);

          const summaryData = await getClimateSummary("Berlin-Tempelhof");
  setSummary(summaryData);

      } catch (error) {
  console.error("Climate data loading error:", error);
  setError(
    error instanceof Error
      ? error.message
      : "Unable to load climate data.",
  );
}finally {
        setLoading(false);
      }
    }

    loadMeasurements();
  }, []);

  if (loading) {
    return <main>Loading climate data...</main>;
  }

  if (error) {
    return <main>{error}</main>;
  }

return (
  <main className="dashboard">
    <header className="dashboard-header">
      <div>
        <h1>ClimateScope</h1>
        <p>Climate data analysis dashboard</p>
      </div>
    </header>

    <section className="dashboard-content">
      {summary && <ClimateSummary summary={summary} />}

{forecast && (
  <section>
    <h2>Temperature Forecast</h2>
    <p>
      Location: {forecast.location}
    </p>
    <p>
  Forecast date: {forecast.forecast_date}
</p>
    <p>
      Predicted temperature:{" "}
      {forecast.predicted_temperature_c.toFixed(1)}°C
    </p>
  </section>
)}

        <TemperatureChart measurements={measurements} />

      <section className="measurements-section">
        <div className="section-header">
          <h2>Climate Measurements</h2>
          <span>{measurements.length} records</span>
        </div>

        <div className="measurement-grid">
          {measurements.slice(-50).map((measurement) => (
            <ClimateMeasurementCard
              key={measurement.id}
              measurement={measurement}
            />
          ))}
        </div>
      </section>
    </section>
  </main>
);
}

export default Dashboard;