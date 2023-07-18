FROM python:3.8

# Install python packages
RUN mkdir /summer_research_ChatGPT
COPY requirements.txt /summer_research_ChatGPT
RUN pip install -r /summer_research_ChatGPT/requirements.txt

# Copy files into container
COPY . /summer_research_ChatGPT

# Set work directory and open the required port
WORKDIR /summer_research_ChatGPT

EXPOSE 8501

# Run our service script
CMD ["streamlit", "run","Login.py"]
