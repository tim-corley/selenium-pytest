# Automated UI Testing with Selenium & PyTest

---
### Prerequisites

 - Python3
 - pipenv

### Installation

```bash
git clone
cd project_dir
pipenv shell
pipenv install
```

### Run Tests
 - **Run All Tests**

``pipenv run python -m pytest``

 - **Run Single Test Suite/File**

``pipenv run python -m pytest tests/test_home.py``

 - **Run Single Test Case**

``pipenv run python -m pytest tests/test_home.py::test_LogoDisplayed``

 - **Run Tests in Parallel**

``pipenv run python -m pytest -n 3``