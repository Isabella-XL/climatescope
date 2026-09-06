# ClimateScope 🌍

**AI-powered climate data analysis and temperature forecasting platform**

ClimateScope is a full-stack climate analytics application that combines historical temperature data, statistical analysis, and machine learning to provide climate insights and short-term temperature forecasts for **Berlin-Tempelhof, Germany**.

The project demonstrates an end-to-end data and machine-learning workflow: climate data ingestion → PostgreSQL storage → FastAPI API → machine-learning prediction → React dashboard.

## 🖥️ Dashboard Preview

![ClimateScope Dashboard1](docs/images/Screenshot1.png)

![ClimateScope Dashboard2](docs/images/Screenshot2.png)


## 🚀 Live Demo

**Frontend:**
https://climatescope-1.onrender.com

**Backend API:**
https://climatescope-o2lu.onrender.com

**API Health Check:**
https://climatescope-o2lu.onrender.com/health

---

## ✨ Features

* 📊 Historical climate measurement visualization
* 🌡️ Mean, minimum, and maximum temperature analysis
* 📈 Climate summary statistics
* 🤖 Machine-learning temperature forecasting
* 🗄️ PostgreSQL database powered by Supabase
* ⚡ REST API built with FastAPI
* 💻 Interactive React + TypeScript dashboard
* 🐳 Dockerized backend
* 🧪 Automated backend and frontend tests
* ☁️ Production deployment using Render and Supabase
* 🔐 Environment-based configuration for production secrets

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      User / Web      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ React + TypeScript  │
                         │      Dashboard      │
                         └──────────┬──────────┘
                                    │ REST API
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │      Backend        │
                         └──────┬─────────┬────┘
                                │         │
                         SQLAlchemy       │
                                │         │
                                ▼         ▼
                    ┌────────────────┐  ┌───────────────┐
                    │    Supabase    │  │ Scikit-learn  │
                    │   PostgreSQL   │  │ Random Forest │
                    └────────────────┘  │     Model     │
                                        └───────────────┘
```

### Production stack

| Layer               | Technology              |
| ------------------- | ----------------------- |
| Frontend            | React, TypeScript, Vite |
| Backend             | FastAPI, Python         |
| ORM                 | SQLAlchemy              |
| Database            | PostgreSQL / Supabase   |
| Machine Learning    | Scikit-learn            |
| Data Processing     | Pandas                  |
| Model Serialization | Joblib                  |
| Database Migrations | Alembic                 |
| Containerization    | Docker                  |
| Frontend Hosting    | Render                  |
| Backend Hosting     | Render                  |
| Database Hosting    | Supabase                |
| Testing             | Pytest, Vitest          |

---

## 📁 Project Structure

```text
ClimateScope/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── climate.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── climate_measurement.py
│   │
│   ├── schemas/
│   │   └── climate.py
│   │
│   └── services/
│       ├── climate_data/
│       │   ├── analysis.py
│       │   ├── database_loader.py
│       │   └── ecad_loader.py
│       │
│       └── forecasting/
│           └── predictor.py
│
├── data/
│   └── processed/
│       └── berlin_temperature_model.joblib
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   │
│   ├── package.json
│   └── Dockerfile
│
├── scripts/
│   └── import_climate_data.py
│
├── tests/
│   ├── test_climate_api.py
│   ├── test_climate_summary.py
│   └── test_forecast.py
│
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── requirements/
└── README.md
```

---

## 🌡️ Data

ClimateScope uses daily temperature measurements from the **ECA&D (European Climate Assessment & Dataset)** project.

The current dataset contains **4,018 measurements** for:

**Berlin-Tempelhof**

The application processes:

* Mean temperature
* Minimum temperature
* Maximum temperature
* Measurement date
* Geographic coordinates
* Station/location information

Temperatures are converted from the source representation into degrees Celsius during data ingestion.

---

## 🤖 Machine Learning

ClimateScope includes a **Random Forest regression model** for temperature forecasting.

The trained model is stored as:

```text
data/processed/berlin_temperature_model.joblib
```

### Model features

The forecasting pipeline uses:

```text
TG_lag_1
TN_lag_1
TX_lag_1
TG_lag_7
TG_rolling_7
TG_rolling_14
day_of_year_sin
day_of_year_cos
```

These features represent historical temperature information, rolling temperature statistics, and seasonal information.

### Forecasting workflow

```text
Historical Measurements
          │
          ▼
    Feature Creation
          │
          ▼
   Random Forest Model
          │
          ▼
 Predicted Temperature
          │
          ▼
      React Dashboard
```

The trained model is loaded by the backend using Joblib and used by the `/forecast` API endpoint.

---

## 🔌 API

The FastAPI backend exposes versioned REST endpoints under:

```text
/api/v1
```

### Health

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Get measurements

```http
GET /api/v1/climate/measurements
```

Optional location filtering:

```http
GET /api/v1/climate/measurements?location=Berlin-Tempelhof
```

### Get climate summary

```http
GET /api/v1/climate/summary?location=Berlin-Tempelhof
```

The summary includes:

* Measurement count
* Average temperature
* Minimum temperature
* Maximum temperature

### Generate forecast

```http
POST /api/v1/climate/forecast
```

The forecast endpoint accepts the model features and returns a predicted temperature.

---

## 🗄️ Database

ClimateScope uses **PostgreSQL** hosted through **Supabase** in production.

SQLAlchemy provides database access from the FastAPI application.

The main table is:

```text
climate_measurements
```

Database schema changes are managed using **Alembic migrations**.

Migration history includes:

```text
create climate datasets table
add climate measurements
add min max mean temperatures
```

---

## 🐳 Docker

The backend can be run in a Docker container.

Build the image:

```bash
docker build -t climatescope-api .
```

Run the container:

```bash
docker run -p 8000:8000 climatescope-api
```

The API will then be available at:

```text
http://localhost:8000
```

Docker is also used as part of the production backend deployment.

---

## ⚙️ Environment Variables

Create a `.env` file for local development.

Example:

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/postgres
OPENAI_API_KEY=
SECRET_KEY=your-secret-key
ENVIRONMENT=development
```

For the frontend:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### Production

Production environment variables are configured through the hosting platform rather than committed to Git.

**Never commit:**

```text
.env
```

or real database passwords, API keys, or secret keys.

A safe `.env.example` file can be committed to the repository.

---

## 🛠️ Local Development

### 1. Clone the repository

```bash
git clone https://github.com/Isabella-XL/ClimateScope.git
cd ClimateScope
```

### 2. Configure environment variables

Create the backend `.env` file and add the required database configuration.

Create:

```text
frontend/.env
```

with:

```env
VITE_API_BASE_URL=http://localhost:8000
```

### 3. Start the backend

Using Docker:

```bash
docker compose up -d --build
```

The API will be available at:

```text
http://localhost:8000
```

### 4. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

## 📥 Import Climate Data

After configuring the database and running the migrations:

```bash
docker compose exec api python -m scripts.import_climate_data
```

The current dataset imports approximately:

```text
4018 measurements
```

You can verify the database count with:

```bash
docker compose exec api python -c "from app.db.database import SessionLocal; from app.models.climate_measurement import ClimateMeasurement; db=SessionLocal(); print(db.query(ClimateMeasurement).count()); db.close()"
```

---

## 🧪 Testing

### Backend

Run the backend tests with:

```bash
pytest
```

The backend test suite covers:

* Health endpoint
* Root endpoint
* Climate measurements
* Location filtering
* Climate summaries
* Date filtering
* Validation errors
* Forecast requests
* Forecast validation
* Forecast prediction logic

### Frontend

From the `frontend` directory:

```bash
npm test
```

### Production build

```bash
npm run build
```

---

## ☁️ Deployment

ClimateScope uses a production architecture consisting of:

```text
React Frontend
      │
      ▼
    Render
      │
      ▼
FastAPI Backend
      │
      ├──────────────► Supabase PostgreSQL
      │
      └──────────────► Random Forest Model
```

### Frontend

The React application is deployed as a Render Static Site.

Production API configuration:

```env
VITE_API_BASE_URL=https://YOUR-BACKEND-URL
```

### Backend

The FastAPI application is deployed as a Docker-based Render Web Service.

Production CORS configuration allows requests from the deployed frontend.

### Database

Production data is stored in Supabase PostgreSQL.

---

## 🔐 Security

Secrets are provided through environment variables rather than committed to source control.

The project uses:

* Environment-based configuration
* `.gitignore` protection for `.env`
* Production CORS configuration
* Supabase PostgreSQL
* Separate development and production environments

No database credentials or API keys should be stored in the repository.

---

## 📊 Current Capabilities

ClimateScope currently provides:

* **4,018** historical climate measurements
* Berlin-Tempelhof climate analysis
* Historical temperature statistics
* RESTful climate API
* Machine-learning temperature forecasting
* PostgreSQL persistence
* Production Docker deployment
* Automated testing
* Cloud-hosted frontend and backend

---

## 🔮 Future Improvements

Potential next steps include:

* 🌍 Support for multiple weather stations and cities
* 📅 Longer-range forecasting
* 📈 Interactive historical temperature charts
* 🗺️ Geographic climate visualization
* 🌡️ Climate anomaly detection
* 📊 Year-over-year climate comparisons
* 🤖 Model performance monitoring
* 🔄 Automated data ingestion
* 📉 Forecast confidence intervals
* 🌐 Additional climate datasets
* 🔐 More granular authentication and authorization

---

## 🎯 Project Goals

ClimateScope was built to demonstrate practical skills across the full machine-learning application lifecycle:

```text
Data Engineering
       ↓
Data Storage
       ↓
Statistical Analysis
       ↓
Machine Learning
       ↓
Backend API
       ↓
Frontend Application
       ↓
Docker
       ↓
Cloud Deployment
```

The project focuses on turning raw climate data into an accessible, production-ready analytical application rather than building a standalone machine-learning model.

---

## 👨‍💻 Technologies Demonstrated

This project demonstrates practical experience with:

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Supabase
* Alembic
* Pandas
* Scikit-learn
* Joblib
* React
* TypeScript
* Vite
* REST APIs
* Docker
* Pytest
* Vitest
* Git/GitHub
* Cloud deployment
* Environment-based configuration
* CORS
* Machine-learning inference

---
## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

### Data

ClimateScope uses climate data from the **European Climate Assessment & Dataset (ECA&D)**. The dataset remains subject to its original terms of use and attribution requirements.
