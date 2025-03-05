# Project Name

## Description

Provide a brief description of what your project does. 

---

## Local Setup

Follow these steps to set up the project on your local machine:

### Prerequisites

Before starting, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- (Optional) Virtual Environment for isolated dependencies

## step 1:Clone the repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/Jackdrakes/Gdg-event.git
cd Gdg-event
```

## Step 2: Set up a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment for your project to avoid dependency conflicts.

#### Create a virtual environment:

```bash
python -m venv .venv
```

### Activate Virtual Environment

- On Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

- On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

## Step 3: Install Dependencies
Once your virtual environment is activated (or if you skipped the virtual environment), install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Step 4: Set up Environment Variables 
Some projects may require environment variables. Check for a `.env.example` or documentation for the specific variables needed.

You can create a `.env` file in the root of the project and add the variables:

Get `GROQ_API_KEY` from [Groq Console](https://console.groq.com/keys) 
Get `AGENTOPS_API_KEY` from [AgentOps App](https://app.agentops.ai/settings/projects)
you can get api key from [Agno App](https://app.agno.com/)
```env
GROQ_API_KEY=value
AGNO_API_KEY=value
AGENTOPS_API_KEY=value
```
