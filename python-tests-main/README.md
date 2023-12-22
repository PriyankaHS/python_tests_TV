# UI Automation Framework using Pytest based on Page Object Model

This is a UI automation framework built using Python, Selenium, and Pytest, following the Page Object Model (POM) design
pattern.
It is designed for automated testing of web applications.

## Features

- **Page Object Model (POM):** Organize and maintain your tests efficiently.
- **Pytest:** Manage and execute test cases effectively.
- **Selenium WebDriver:** Interact with web elements easily.
- **Fixture-based Setup:** Simplify test setup and teardown.
- **Configuration and Test Data Management:** Easily configure and manage test data.
- **Multi-browser Support:** Currently supports Chrome.
- **Parallel execution support:** Reduce the execution time

## Installation

### Step 1: Clone the Repository

You can clone the repository using one of the following methods:

- HTTPS:
    ```bash
    https://github.com/testvagrant/python-tests.git
- SSH:
    ```bash
  git@github.com:testvagrant/python-tests.git
- GitHub CLI:
    ```bash
  gh repo clone testvagrant/python-tests

### Step 2: Set Up the Environment

Open the project in your preferred Python IDE (e.g., PyCharm, VS Code).

### Step 3: Install Dependencies

1. Open a terminal in your project's directory.
2. Run the following commands to install the required packages:
    - Pytest: Pytest is a testing framework that simplifies test case management and execution. It provides powerful
      features for test discovery, setup, and reporting.
      ```bash
      pip install pytest
    - Selenium: Selenium WebDriver is used to interact with web elements in your web application. It allows you to
      automate user actions like clicking buttons, filling forms, and more.
      ```bash
      pip install selenium
    - WebDriver Manager: WebDriver Manager is a utility that helps you manage WebDriver binaries for different browsers.
      It automatically downloads and configures WebDriver binaries, making it easy to use multiple browsers for testing.
      ```bash 
      pip install webdriver-manager
    - Allure-Pytest: Allure-Pytest is a plugin that generates interactive and informative test reports. It enhances test
      reporting with detailed information about test cases, test steps, and attachments (e.g., screenshots).
      ```bash 
      pip install allure-pytest
    - Pytest-xdist: Pytest-xdist is a plugin that enables parallel test execution. It allows you to run your tests
      concurrently, which can significantly reduce test execution time when you have a large suite of tests.
      ```bash
      pip install pytest-xdist

### Step 4: Run Tests:

1. To execute all your tests, use the following command in your terminal:
   ```bash
   pytest

2. To execute the specific test, use the following command in your terminal:
    - Copy the path of the test file you want to execute (the path from the root of your project directory).
    - Navigate to the root directory of your Pytest project.
    - Run the following command.
      ```bash
      pytest path/to/copied_test_file.py
    - Replace path/to/copied_test_file.py with the actual path you copied. Make sure to include the file name and
      extension in the path
    - For example:
      ```bash
      pytest tests/test_login.py

3. To run tests in parallel,
   Update your pytest command to specify the number of parallel processes you want to use.
   For example, to run tests in parallel with 4 processes:
   ```bash
   pytest tests/ -n 4

4. View Test Results: After running the tests, you can view the test results in your terminal.

5. Generate Allure Reports (Optional): If you want to generate Allure reports for your tests, you can use the following
   commands:
    ```bash 
   pytest --alluredir=./allure-results

- Open the allure report
  ```bash 
  allure serve