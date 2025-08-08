# 🚗 Vehicle Insurance ML Pipeline — End‑to‑End MLOps

A production‑grade Machine Learning pipeline for the **vehicle insurance** domain. It covers the full lifecycle: **data ingestion → validation → transformation → model training → evaluation → deployment**, with **MongoDB Atlas**, **AWS S3**, **Docker**, and **GitHub Actions (self‑hosted EC2 runner)**.

---

## ✨ About the Project

This project demonstrates how to build and ship an ML system like real teams do:

- **Modular pipeline** with clean separation of stages
- **Config‑driven** via constants and entities
- **MongoDB Atlas** as the source of truth for data
- **Reusable preprocessing** saved for inference parity
- **Model registry on S3** with simple promotion logic
- **Containerized app** deployed via CI/CD to **EC2**
- **FastAPI/Flask web UI** (your app file decides) for interactive predictions

Use it as a template to scale to other supervised learning problems.

---

### 📊 Dataset Description – Vehicle Insurance Customer Data

- **id**: Unique ID for the customer  
- **Gender**: Gender of the customer  
- **Age**: Age of the customer  
- **Driving_License**:  
  - `0`: Customer does **not** have a Driving License  
  - `1`: Customer **has** a Driving License  
- **Region_Code**: Unique code representing the customer’s region  
- **Previously_Insured**:  
  - `1`: Customer **already has** Vehicle Insurance  
  - `0`: Customer **does not have** Vehicle Insurance  
- **Vehicle_Age**: Age of the vehicle (e.g., `< 1 Year`, `1-2 Year`, `> 2 Years`)  
- **Vehicle_Damage**:  
  - `1`: Customer's vehicle was **damaged** in the past  
  - `0`: Customer's vehicle was **not damaged** in the past  
- **Annual_Premium**: Annual premium amount the customer needs to pay  
- **Policy_Sales_Channel**: Anonymized code representing the sales channel (e.g., Agent, Phone, Email, In-person)  
- **Vintage**: Number of days the customer has been associated with the company  
- **Response**:  
  - `1`: Customer is **interested** in vehicle insurance  
  - `0`: Customer is **not interested**
  


## 🔄 Workflow (Pipeline Stages)

1. **📥 Data Ingestion**
   - Connects to **MongoDB Atlas** using `MONGODB_URL`
   - Pulls raw documents, converts to a clean **DataFrame**
   - Persists raw/ingested splits (train/test) as artifacts

2. **✅ Data Validation**
   - Validates dataset against **`config/schema.yaml`**
   - Checks column presence, dtypes, allowed categories, missing values
   - Produces a **validation report** artifact

3. **⚙️ Data Transformation**
   - Feature engineering, encoding (e.g., `Vehicle_Age` dummies), scaling
   - Saves the fitted **preprocessing object** (to ensure train/inference parity)
   - Outputs transformed train/test sets

4. **🧠 Model Training**
   - Trains ML models (e.g., RandomForest / LogisticRegression)
   - Hyperparameters controlled via constants/config
   - Exports the **trained model artifact**

5. **📊 Model Evaluation**
   - Compares new model vs. previously deployed model
   - Uses a **minimum improvement threshold** (e.g., `0.02`) to decide promotion

6. **🚀 Model Pusher**
   - Pushes the promoted model to **AWS S3** (model registry)
   - Maintains a predictable **S3 key structure** for the latest model

7. **🌐 Serving (Prediction Pipeline)**
   - Web API (FastAPI/Flask) that:
     - Accepts user input (form/JSON)
     - Applies the **same preprocessing object**
     - Loads the **latest model** from S3/registry
     - Returns predictions in real time

8. **🐳 CI/CD & Deployment**
   - **Docker** image build → pushed to **ECR**
   - **EC2 self‑hosted runner** pulls and runs container
   - App exposed over the configured port/security group

---

## 🗂️ Project File Structure

    vehicle-insurance-ml/
    │
    ├── .github/workflows/         # CI/CD pipeline (GitHub Actions)
    ├── artifacts/                 # Pipeline artifacts (ignored in git)
    ├── notebook/                  # EDA & experiments
    ├── src/                       # Source (Python package)
    │   ├── components/            # Each pipeline stage (ingestion/validation/...)
    │   ├── configuration/         # MongoDB / AWS connections
    │   ├── constants/             # Global constants & keys
    │   ├── data_access/           # DB read/write utilities
    │   ├── entity/                # @dataclass configs & artifacts
    │   ├── pipeline/              # Orchestrators (training / prediction)
    │   ├── utils/                 # Helpers (logging, IO, etc.)
    │   └── __init__.py
    │
    ├── templates/                 # HTML templates for the web app
    ├── static/                    # CSS / static assets
    ├── config/                    # schema.yaml, model.yaml, etc.
    ├── app.py                     # App entry (FastAPI/Flask)
    ├── demo.py                    # Local pipeline trigger (optional)
    ├── requirements.txt           # Python dependencies
    ├── Dockerfile                 # Container build instructions
    ├── .dockerignore              # Exclude venv, artifacts, etc. from build context
    ├── pyproject.toml             # Modern packaging config (optional)
    ├── setup.py                   # Legacy packaging/editable installs (optional)
    └── README.md                  # This file

> Tip: Every folder in `src/` has an `__init__.py` so it behaves as a package and imports work cleanly across modules.

---

## ⚡ Quickstart — Run Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/<your-username>/vehicle-insurance-ml.git
    cd vehicle-insurance-ml
    ```

2. **Create & activate a virtual environment (Python 3.10)**
    ```bash
    python3 -m venv venv
    ```
    **macOS / Linux**
    ```bash
    source venv/bin/activate
    ```
    **Windows (PowerShell)**
    ```powershell
    venv\Scripts\Activate.ps1
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables** (use a `.env` file or export manually)  

    **`.env` file example:**
    ```env
    MONGODB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/<db>?retryWrites=true&w=majority
    AWS_ACCESS_KEY_ID=<your_access_key>
    AWS_SECRET_ACCESS_KEY=<your_secret_key>
    AWS_DEFAULT_REGION=us-east-1
    MODEL_BUCKET_NAME=my-model-mlopsproj
    ```

    **Or export (macOS/Linux)**
    ```bash
    export MONGODB_URL="..."
    export AWS_ACCESS_KEY_ID="..."
    export AWS_SECRET_ACCESS_KEY="..."
    export AWS_DEFAULT_REGION="us-east-1"
    export MODEL_BUCKET_NAME="my-model-mlopsproj"
    ```

5. **(Optional) Run the training pipeline**
    ```bash
    python demo.py
    ```
    **Or, if your training orchestrator is in `src/pipeline/training_pipeline.py`:**
    ```bash
    python -m src.pipeline.training_pipeline
    ```

6. **Start the web app**  

    **Using FastAPI with Uvicorn:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 5000 --reload
    ```

    **If `app.py` runs directly:**
    ```bash
    python app.py
    ```

    **Open in browser:**
    ```
    http://127.0.0.1:5000
    ```
    *(or the port you configured)*

---

### 🔧 Notes & Good Practices

- Keep secrets out of git; use **GitHub Secrets** for CI and `--env-file .env` for `docker run`.
- Add local dirs like `venv/`, `artifacts/`, `__pycache__/`, `*.pkl` to `.gitignore` and `.dockerignore`.
- Ensure preprocessing objects are versioned alongside the model to avoid train/inference drift.
- Prefer **`pyproject.toml`** for modern packaging; keep `setup.py` only if you need legacy tooling.

---

### 🧰 Tech Stack

- **Language & Frameworks:** Python 3.10, FastAPI/Flask
- **Data & Storage:** MongoDB Atlas, AWS S3
- **ML:** scikit‑learn, pandas, numpy
- **Ops:** Docker, AWS ECR/EC2, GitHub Actions (self‑hosted runner)
- **Config & Utils:** PyYAML, python‑dotenv, logging

---

### 🗣️ Author

**Atharva Chundurwar**  
GitHub: https://github.com/AtharvaBOT7  
LinkedIn: https://www.linkedin.com/in/atharva-chundurwar-7080a31b7/

---

