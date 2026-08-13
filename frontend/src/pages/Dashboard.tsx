import { useEffect, useState } from "react";
import ClimateMeasurementCard from "../components/ClimateMeasurementCard";
import TemperatureChart from "../components/TemperatureChart";


import ClimateSummary from "../components/ClimateSummary";
import {
  getClimateSummary,
  getMeasurements,
  type ClimateMeasurement,
  type ClimateSummary as ClimateSummaryData,
} from "../services/climateApi";




function Dashboard() {
  const [summary, setSummary] = useState<ClimateSummaryData | null>(null);
  const [measurements, setMeasurements] = useState<ClimateMeasurement[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadMeasurements() {
      try {
        const data = await getMeasurements();
        setMeasurements(data);

          const summaryData = await getClimateSummary("Berlin");
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

        <TemperatureChart measurements={measurements} />

      <section className="measurements-section">
        <div className="section-header">
          <h2>Climate Measurements</h2>
          <span>{measurements.length} records</span>
        </div>

        <div className="measurement-grid">
          {measurements.map((measurement) => (
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