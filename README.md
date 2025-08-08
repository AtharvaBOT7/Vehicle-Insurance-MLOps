# Vehicle-Insurance-MLOps
This project will target the customers who are most likely to get an insurance from our Vehicle Insurance Company.

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
MLOps Project: Vehicle Data Regression
🌟 Project Overview
This project implements an end-to-end Machine Learning Operations (MLOps) pipeline for a vehicle data regression task. The solution automates the entire lifecycle, from data ingestion to model deployment, using a robust and scalable architecture.

The core components include:

Data Ingestion: Fetching data from a MongoDB Atlas cloud database.

ML Pipeline: A well-structured pipeline for data validation, transformation, and model training.

Model Management: Storing and retrieving trained models from AWS S3.

Deployment: A complete CI/CD pipeline using GitHub Actions, ECR, and EC2 to containerize and deploy the application.

🚀 Project Workflow
The project is built on a modular and scalable architecture, following a structured workflow to ensure smooth development and deployment.

1. Project Setup & Data Ingestion
Initialize the project structure with template.py and configure local packages via setup.py.

Establish a connection to MongoDB Atlas, a cloud-based NoSQL database, to ingest the raw dataset.

Data is fetched, transformed into a DataFrame, and stored for the next pipeline steps.

2. Core ML Pipeline
Data Validation: Utilizes a schema.yaml file to validate the incoming data, ensuring it meets the required format and quality standards.

Data Transformation: Cleans and prepares the data for modeling.

Model Training: Trains a regression model on the processed data.

3. Cloud Integration & Deployment
The trained model is pushed to an AWS S3 bucket for versioning and storage.

The project code is containerized using Docker.

GitHub Actions automates the build and deployment process.

The Docker image is pushed to AWS ECR (Elastic Container Registry).

The application is deployed on an AWS EC2 instance, running the latest containerized version of the model.

🛠️ Technology Stack
Category

Technology

Description

Language



The primary language for the entire pipeline and application logic.

Database



Used for storing and accessing the vehicle dataset in a flexible key-value format.

Cloud



A cloud storage service for storing and managing trained model artifacts.

Cloud



A private Docker registry for storing and managing our application's Docker images.

Cloud



A virtual server used for hosting the deployed application.

CI/CD



Automates the build, test, and deployment process on every push to the repository.

Containerization



Packages the application and its dependencies into a single, portable container.

⚙️ Local Setup
Prerequisites
Python 3.10 installed.

A MongoDB Atlas account with a cluster and user configured.

An AWS account with an IAM user having AdministratorAccess and an S3 bucket created.

A GitHub account with secrets configured for AWS and ECR.

Installation
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # For macOS/Linux
.\venv\Scripts\activate   # For Windows

Install the required packages:

pip install -r requirements.txt

Environment Variables
Set the following environment variables to connect to your cloud services.

MongoDB Connection URL
Bash (macOS/Linux):

export MONGODB_URL="mongodb+srv://<username>:<password>@<cluster_url>/<db_name>?retryWrites=true&w=majority"

PowerShell (Windows):

$env:MONGODB_URL = "mongodb+srv://<username>:<password>@<cluster_url>/<db_name>?retryWrites=true&w=majority"

AWS Credentials
Bash (macOS/Linux):

export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_access_key"

PowerShell (Windows):

$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_access_key"

🏃 Usage
Running the Application
To run the application locally, use the following command:

python app.py

The application will be accessible at http://localhost:5080.

Triggering the Training Pipeline
The training pipeline can be triggered by a GET request to the /training endpoint, which is useful for retraining the model on new data.

📂 Project Structure
.
├── .github/
│   └── workflows/
│       └── aws.yaml                 # GitHub Actions workflow for CI/CD
├── src/
│   ├── __init__.py
│   ├── components/                  # ML pipeline components (ingestion, validation, etc.)
│   ├── config/                      # Configuration files and connections
│   ├── constants/                   # Project constants and environment variables
│   ├── data_access/                 # MongoDB data access layer
│   ├── entity/                      # Data classes and object definitions
│   └── utils/                       # Helper functions
├── notebooks/                       # Exploratory Data Analysis and Feature Engineering
├── app.py                           # Main application file for API endpoints
├── Dockerfile                       # Docker configuration for containerization
├── requirements.txt                 # Python dependencies
├── setup.py                         # Local package setup file
└── README.md
  
