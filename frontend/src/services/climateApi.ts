const API_BASE_URL =import.meta.env.VITE_API_BASE_URL;

export interface ClimateMeasurement {
  id: number;
  date: string;
  location: string;
  latitude: number;
  longitude: number;
   mean_temperature_c: number;
  min_temperature_c: number;
  max_temperature_c: number;
}

export interface ClimateSummary {
  location: string | null;
  measurement_count: number;
  average_temperature_c: number;
  minimum_temperature_c: number;
  maximum_temperature_c: number;
}


export interface ClimateForecastRequest {
  forecast_date: string;
  TG_lag_1: number;
  TN_lag_1: number;
  TX_lag_1: number;
  TG_lag_7: number;
  TG_rolling_7: number;
  TG_rolling_14: number;
  day_of_year_sin: number;
  day_of_year_cos: number;
}

export interface ClimateForecast {
  location: string;
  forecast_date: string;
  predicted_temperature_c: number;
}


export async function getMeasurements(): Promise<ClimateMeasurement[]> {
  const response = await fetch(
    `${API_BASE_URL}/climate/measurements`,
  );

  if (!response.ok) {
    throw new Error("Failed to fetch climate measurements");
  }

  return response.json();
}


export async function getClimateSummary(
  location?: string,
): Promise<ClimateSummary> {
  const url = new URL(
    `${API_BASE_URL}/climate/summary`,
  );

  if (location) {
    url.searchParams.set("location", location);
  }

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Failed to fetch climate summary");
  }

  return response.json();
}

export async function getClimateForecast(
  features: ClimateForecastRequest,
): Promise<ClimateForecast> {
  const response = await fetch(
    `${API_BASE_URL}/climate/forecast`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(features),
    },
  );

  if (!response.ok) {
    throw new Error("Failed to fetch climate forecast");
  }

  return response.json();
}


export function buildForecastFeatures(
  measurements: ClimateMeasurement[],
): ClimateForecastRequest {
  const sorted = [...measurements].sort(
    (a, b) =>
      new Date(a.date).getTime() -
      new Date(b.date).getTime(),
  );

  const latest = sorted[sorted.length - 1];

  const forecastDate = new Date(latest.date);
forecastDate.setDate(forecastDate.getDate() + 1);

  const last7 = sorted.slice(-7);
  const last14 = sorted.slice(-14);

  const TG_rolling_7 =
    last7.reduce(
      (sum, measurement) => sum + measurement.mean_temperature_c,
      0,
    ) / last7.length;

  const TG_rolling_14 =
    last14.reduce(
      (sum, measurement) => sum + measurement.mean_temperature_c,
      0,
    ) / last14.length;

  const previous7 = sorted[sorted.length - 8];

  const dayOfYear =
    Math.floor(
      (
        new Date(latest.date).getTime() -
        new Date(
          new Date(latest.date).getFullYear(),
          0,
          0,
        ).getTime()
      ) /
        (1000 * 60 * 60 * 24),
    );

  return {
    forecast_date: forecastDate.toISOString().split("T")[0],
    TG_lag_1: latest.mean_temperature_c,
TN_lag_1: latest.min_temperature_c,
TX_lag_1: latest.max_temperature_c,
TG_lag_7: previous7.mean_temperature_c,
    TG_rolling_7,
    TG_rolling_14,
    day_of_year_sin:
      Math.sin(
        (2 * Math.PI * dayOfYear) / 365.25,
      ),
    day_of_year_cos:
      Math.cos(
        (2 * Math.PI * dayOfYear) / 365.25,
      ),
  };
}