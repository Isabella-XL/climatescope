import type { ClimateSummary as ClimateSummaryData } from "../services/climateApi";

interface ClimateSummaryProps {
  summary: ClimateSummaryData;
}

function ClimateSummary({ summary }: ClimateSummaryProps) {
  return (
    <section className="summary-section">
      <h2>
        Climate Summary
        {summary.location ? ` — ${summary.location}` : ""}
      </h2>

      <div className="summary-grid">
        <article className="summary-card">
          <h3>Average</h3>
          <p>{summary.average_temperature_c !== null
  ? `${summary.average_temperature_c.toFixed(1)}°C`
  : "N/A"}</p>
        </article>

        <article className="summary-card">
          <h3>Minimum</h3>
          <p>{summary.minimum_temperature_c !== null
    ? `${summary.minimum_temperature_c.toFixed(1)}°C`
    : "N/A"}</p>
        </article>

        <article className="summary-card">
          <h3>Maximum</h3>
          <p>{summary.maximum_temperature_c !== null
    ? `${summary.maximum_temperature_c.toFixed(1)}°C`
    : "N/A"}</p>
        </article>

        <article className="summary-card">
          <h3>Measurements</h3>
          <p>{summary.measurement_count}</p>
        </article>
      </div>
    </section>
  );
}

export default ClimateSummary;