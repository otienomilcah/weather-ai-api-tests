# WeatherAI API Test Automation Framework

Automated API testing framework for the WeatherAI developer API using Python, Pytest, and Requests.

The framework covers functional validation, authentication, authorization, error handling, performance checks, rate-limit behavior, test reporting, and CI execution.

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
```

## Setup Instructions

### Prerequisites

Install:

- Python 3.10 or later
- Git
- A valid WeatherAI API key

### 1. Clone the repository

```bash
git clone https://github.com/otienomilcah/weather-ai-api-tests.git
cd weather-ai-api-tests
```

### 2. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Git Bash

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Use `.env.example` as the template:

```env
WEATHER_API_KEY=your_api_key_here
BASE_URL=https://api.weather-ai.co
```

Do not commit `.env` to Git. It contains the API key and is excluded through `.gitignore`.

## Running the Tests

### Run the complete test suite

```bash
pytest
```

### Run with verbose output

```bash
pytest -v
```

### Run individual test modules

```bash
pytest tests/test_weather.py -v
```

```bash
pytest tests/test_validation.py -v
```

```bash
pytest tests/test_authentication.py -v
```

```bash
pytest tests/test_authorization.py -v
```

```bash
pytest tests/test_error_handling.py -v
```

```bash
pytest tests/test_performance.py -v
```

```bash
pytest tests/test_rate_limit.py -v
```

## HTML Test Reporting

Generate an HTML test report with:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report will be generated at:

```text
reports/report.html
```

Open the report locally with a browser.

## Test Strategy

The framework uses a layered API testing strategy focused on functional correctness, negative testing, authentication, error handling, performance, and maintainability.

### 1. Happy Path Testing

`test_weather.py` validates successful weather requests using valid geographic coordinates from multiple locations.

The tests verify:

- HTTP 200 response
- JSON response
- Response data type
- Basic response-time expectations

Parameterized tests are used to execute the same test against multiple coordinate pairs without duplicating test logic.

### 2. Input Validation

`test_validation.py` validates documented request validation scenarios.

Examples include:

- Missing latitude
- Missing longitude
- Missing both coordinates
- Valid coordinate boundaries
- Invalid coordinate boundaries where supported by the API

The tests are based on documented API behavior rather than assuming undocumented validation rules.

### 3. Authentication

`test_authentication.py` validates API-key behavior.

The tests cover:

- Valid API key
- Invalid API key
- Missing API key
- Authorization header presence
- Authorization header absence when no API key is supplied

### 4. Authorization

`test_authorization.py` verifies access restrictions for protected API functionality, including documented plan-based access behavior.

### 5. Error Handling

`test_error_handling.py` verifies that the framework correctly handles server-side and service-level HTTP errors.

Examples include:

- `429 Too Many Requests`
- `500 Internal Server Error`
- `503 Service Unavailable`

Mocking is used where appropriate so that error-handling behavior can be tested without intentionally forcing the live API into an error state.

### 6. Performance

`test_performance.py` performs lightweight API performance checks.

The tests include:

- Individual response-time measurement
- Multiple consecutive requests
- Average response time
- Maximum response time
- Request success rate

These checks provide basic performance visibility. They are not intended to replace dedicated load or stress testing tools such as JMeter or k6.

### 7. Rate Limiting

Rate-limit behavior is covered through HTTP `429 Too Many Requests` handling in `test_error_handling.py`.

The test uses mocking to verify that the framework correctly handles a rate-limit response without intentionally exhausting the live API quota.

Rate-limit response headers such as `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` are not asserted because they were not returned by the live API during testing.

## Test Design Principles

The framework follows these principles:

- Reusable API client
- Pytest fixtures
- Parameterized tests
- Environment-based configuration
- Clear and meaningful assertions
- Separation of test concerns
- No hard-coded API secrets
- Maintainable project structure
- Lightweight performance checks
- CI execution through GitHub Actions

## Configuration and API Client

The API client is centralized in:

```text
utils/api_client.py
```

This prevents individual tests from duplicating HTTP request logic.

Configuration is centralized in:

```text
config/settings.py
```

Environment variables are loaded using `python-dotenv`.

This separation makes the framework easier to maintain and allows the API base URL and API key to be changed without modifying test code.

## CI/CD

GitHub Actions automatically executes the test suite when changes are pushed to the `main` branch or when a pull request targets `main`.

The CI workflow:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Configures the WeatherAI API key using GitHub Secrets
5. Runs the Pytest suite
6. Generates JUnit and HTML test reports
7. Uploads the reports as workflow artifacts

Workflow file:

```text
.github/workflows/api-tests.yml
```

## Live CI Test Results

View the live GitHub Actions workflow runs:

https://github.com/otienomilcah/weather-ai-api-tests/actions

Each workflow run provides the execution status and detailed test output.

The generated HTML and JUnit reports are also uploaded as workflow artifacts when the workflow is configured to do so.

## API Documentation

The WeatherAI API documentation used as the source of truth for the tests is:

https://weather-ai.co/docs

## Security

API credentials must not be committed to source control.

The local `.env` file is excluded through `.gitignore`.

For GitHub Actions, the API key should be stored as a repository secret:

```text
WEATHER_API_KEY
```

The workflow accesses it through:

```yaml
${{ secrets.WEATHER_API_KEY }}
```

Never commit API keys, passwords, access tokens, or other credentials to the repository.

## Assignment Coverage

This project addresses the key requirements of the API automation assignment:

| Requirement | Implementation |
|---|---|
| Clear test structure | Separate test modules by concern |
| Happy paths | `test_weather.py` |
| Edge cases | `test_validation.py` |
| Authentication | `test_authentication.py` |
| Authorization | `test_authorization.py` |
| Error handling | `test_error_handling.py` |
| Performance considerations | `test_performance.py` |
| Rate-limit considerations | HTTP 429 handling in `test_error_handling.py` |
| Readable and maintainable code | Reusable API client and Pytest fixtures |
| Test reporting | `pytest-html` |
| CI integration | GitHub Actions |
| Live test results | GitHub Actions workflow runs |
| Secure configuration | `.env` and GitHub Secrets |

## Test Execution Example

A successful local test run should look similar to:

```text
27 passed
```

The exact number of tests may change as the framework evolves.

## License

This project was created as an API test automation assessment project.
