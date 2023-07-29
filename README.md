# summer_research_ChatGPT
This is a summer research project for 2023, regarding application with ChatGPT

To run the application locally:
- Install streamlit and streamlit_extras
```
pip install streamlit
pip install streamlit_extras
```
- Install redis
```
brew install redis
```
- Start redis server
```
redis-server
```
- In terminal go to the directory where you have the Login.py file.
- Run the streamlit app
```
streamlit run Login.py
```

To run the application on docker:
- [Install docker](https://docs.docker.com/engine/install/)

- In terminal go to the directory where you have the Login.py file.
- Run docker image using following command
``` 
docker-compose up
```
- Check out the app on http://0.0.0.0:8501 or http://localhost:8501
- Signup and login to the account for more details
