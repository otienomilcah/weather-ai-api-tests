# WeatherAI API Test Automation Framework

Automated API testing framework for the WeatherAI developer API using Python, Pytest, and Requests.

The framework covers functional validation, authentication, authorization, error handling, performance checks, and maintainable test organization.

## Technology Stack

- Python
- Pytest
- Requests
- python-dotenv
- pytest-html
- GitHub Actions

## Project Structure

```text
weather-ai-api-tests/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_authentication.py
│   ├── test_authorization.py
│   ├── test_error_handling.py
│   ├── test_performance.py
│   ├── test_rate_limit.py
│   ├── test_validation.py
│   └── test_weather.py
│
├── utils/
│   ├── __init__.py
│   └── api_client.py
│
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md