from app.db.session import get_db
from app.services.climate_data.analysis import analyze_measurements

db = next(get_db())

try:
    result = analyze_measurements(db, location="Berlin")
    print(result)
finally:
    db.close()
