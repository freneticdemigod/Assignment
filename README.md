# CampaignData API
This project is a Django-based API for managing campaigns, agents, and campaign results. It is deployed on PythonAnywhere.

Project Structure
models.py: Defines the database models for Agents, Campaigns, and Campaign Results.
serializers.py: Serializes the models for use with Django REST framework.
views.py: Contains the viewsets for the API endpoints.
urls.py: Configures the URL routing for the API endpoints.
Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/freneticdemigod/Assignment.git
cd yourrepository

2. Create a Virtual Environment
Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate

3. Install Dependencies
Install the required dependencies:

pip install -r requirements.txt

4. Configure the Database
Apply the database migrations:

python manage.py migrate

5. Collect Static Files
Collect static files:

python manage.py collectstatic

6. Run the Development Server
Start the development server:

python manage.py runserver

API Endpoints
Agents API: /api/agents/
Campaigns API: /api/campaigns/
Campaign Results API: /api/campaign-results/

Note
## This project does not have a main page. It only provides API endpoints for managing campaigns, agents, and campaign results.
