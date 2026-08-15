import app.services.climate_data.ecad_loader as ecad_loader

print("LOADER FILE:", ecad_loader.__file__)

dataset = ecad_loader.load_ecad_temperature(
    "data/raw/TG_STAID2759.txt",
    "TG",
)

print(dataset.head())
print(dataset.dtypes)
print(dataset.shape)
