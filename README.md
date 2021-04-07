<!-- PROJECT HEADER -->
<br />
<div>
<p align="center">
  <a href="https://www.selenium.dev/">
    <img src="/img/selenium.svg" alt="Selenium Logo" width="100" height="100">
  </a>
  <a href="https://docs.pytest.org/en/stable/">
    <img src="/img/pytest.svg" alt="PyTest Logo" width="100" height="100">
  </a>
</p>
<h2 align="center">Automated UI Testing with Selenium & PyTest</h2>
<p align="center">
Easy & Effective Browser Test Automation
    <br />
    <br />
    <a href="https://github.com/tim-corley/selenium-pytest/issues">Report Issue</a>
</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-tests">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
### About

**This repo contains boilerplate code to get up-and-running with Automated UI Testing using Selenium & PyTest. It is intended to be used as a foundation for writing / adding your own tests.**

### Built With

* [Selenium](https://www.selenium.dev/) - a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user’s interaction with the browser
* [PyTest](https://docs.pytest.org/en/stable/) - a framework that makes building simple and scalable tests easy

<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to get a local development instance up & running.

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

### Test Data

Navigate to Automated Practice's [create an account page](http://automationpractice.com/index.php?controller=authentication&back=my-account) and manually create a new test account. Then add the email address, password, and user name to a `.env` in project root.

```
EMAIL=tester@email.com
PASSWORD=yourpassword
USERNAME=Your Name
```


### Running Tests

 - **Run All Tests**

``pipenv run python -m pytest``

 - **Run Single Test Suite/File**

``pipenv run python -m pytest tests/test_home.py``

 - **Run Single Test Case**

``pipenv run python -m pytest tests/test_home.py::test_LogoDisplayed``

 - **Run Tests in Parallel**

``pipenv run python -m pytest -n 3``



<!-- CONTACT -->
## Contact

Tim Corley | [@tcor215](https://twitter.com/tcor215) | contact@tim-corley.dev

[selenium-logo]: img/selenium.svg
[pytest-logo]: img/pytest.svg