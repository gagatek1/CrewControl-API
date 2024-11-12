<h1>CrewControl API</h1>
<h2>Overview</h2>
The API provides a system to control users, teams, tasks, and departments
<h2>Quick Start</h2>
<ol>
  <li>Install Docker and Docker Compose (if not already installed).</li>
  <li>Navigate to the project directory where docker-compose.yml is located using CMD</li>
  <li>Create .env file in app directory
  <br>
  Example:
  

    DATABASE_URL='postgresql://crewcontrol:crewcontrol@crewcontrol_postgres:5432/crewcontrol_db'
    SECRET_KEY='41aa124df73c4eb6ce690120a1959640bc1e9ccab78dcd292355060778a89d4d'
    
    TEST_DATABASE_URL='postgresql://crewcontrol:crewcontrol@crewcontrol_postgres:5432/test_crewcontrol_db'
  </li>
  <li>Start the application 
 

    docker-compose up
  </li>
</ol>
<h2>Tests</h2>
To run the tests use pytest command in the docker container.
