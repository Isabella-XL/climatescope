import { describe, expect, it } from "vitest";
import {
  buildForecastFeatures,
  type ClimateMeasurement,
} from "./climateApi";

describe("buildForecastFeatures", () => {
  it("builds forecast features from measurements", () => {
    const measurements: ClimateMeasurement[] = [
      {
        id: 1,
        date: "2025-12-01",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 8,
        min_temperature_c: 4,
        max_temperature_c: 12,
      },
      {
        id: 2,
        date: "2025-12-02",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 10,
        min_temperature_c: 6,
        max_temperature_c: 14,
      },
      {
        id: 3,
        date: "2025-12-03",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 12,
        min_temperature_c: 8,
        max_temperature_c: 16,
      },
      {
        id: 4,
        date: "2025-12-04",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 14,
        min_temperature_c: 10,
        max_temperature_c: 18,
      },
      {
        id: 5,
        date: "2025-12-05",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 16,
        min_temperature_c: 12,
        max_temperature_c: 20,
      },
      {
        id: 6,
        date: "2025-12-06",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 18,
        min_temperature_c: 14,
        max_temperature_c: 22,
      },
      {
        id: 7,
        date: "2025-12-07",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 20,
        min_temperature_c: 16,
        max_temperature_c: 24,
      },
      {
        id: 8,
        date: "2025-12-08",
        location: "Berlin-Tempelhof",
        latitude: 52.47,
        longitude: 13.4,
        mean_temperature_c: 22,
        min_temperature_c: 18,
        max_temperature_c: 26,
      },
    ];

    const result = buildForecastFeatures(measurements);

    expect(result.TG_lag_1).toBe(22);
    expect(result.TN_lag_1).toBe(18);
    expect(result.TX_lag_1).toBe(26);
    expect(result.TG_lag_7).toBe(8);

    expect(result.TG_rolling_7).toBeGreaterThan(0);
    expect(result.TG_rolling_14).toBeGreaterThan(0);

    expect(result.day_of_year_sin).toBeDefined();
    expect(result.day_of_year_cos).toBeDefined();
  });
});