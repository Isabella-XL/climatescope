const API_BASE_URL =import.meta.env.VITE_API_BASE_URL;

export interface ClimateMeasurement {
  id: number;
  date: string;
  location: string;
  latitude: number;
  longitude: number;
  temperature_c: number;
}

export interface ClimateSummary {
  location: string | null;
  measurement_count: number;
  average_temperature_c: number;
  minimum_temperature_c: number;
  maximum_temperature_c: number;
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