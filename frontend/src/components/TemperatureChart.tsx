import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import type { ClimateMeasurement } from "../services/climateApi";

interface TemperatureChartProps {
  measurements: ClimateMeasurement[];
}

function TemperatureChart({
  measurements,
}: TemperatureChartProps) {
  const chartData = measurements.map((measurement) => ({
    date: measurement.date,
    temperature: measurement.temperature_c,
  }));

  return (
    <section className="temperature-chart-section">
      <div className="section-header">
        <div>
          <h2>Temperature Trend</h2>
          <p>Temperature measurements over time</p>
        </div>
      </div>

      <div className="temperature-chart">
        <ResponsiveContainer width="100%" height={350}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="date"
              tick={{ fontSize: 12 }}
            />

            <YAxis
              unit="°C"
              tick={{ fontSize: 12 }}
            />

            <Tooltip
              formatter={(value) => [`${value}°C`, "Temperature"]}
            />

            <Line
              type="monotone"
              dataKey="temperature"
              strokeWidth={2}
              dot={{ r: 4 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}

export default TemperatureChart;