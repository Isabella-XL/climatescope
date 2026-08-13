import type { ClimateMeasurement } from "../services/climateApi";

interface ClimateMeasurementCardProps {
  measurement: ClimateMeasurement;
}

function ClimateMeasurementCard({
  measurement,
}: ClimateMeasurementCardProps) {
  return (
    <article className="measurement-card">
      <h2>{measurement.location}</h2>

      <p>Date: {measurement.date}</p>

      <p>
        Temperature: {measurement.temperature_c}°C
      </p>

      <p>
        Coordinates: {measurement.latitude},{" "}
        {measurement.longitude}
      </p>
    </article>
  );
}

export default ClimateMeasurementCard;