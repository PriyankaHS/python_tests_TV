import json
import os
from datetime import datetime
import pytz

from resources.test_data import TestData


class SlackHelperMethods:
    def get_current_datetime(self):
        current_datetime = datetime.now(pytz.timezone('Asia/Kolkata'))
        return current_datetime.strftime("%d-%m-%Y  %H:%M:%S")

    def get_allure_report_data(self, directory_path=None):
        if directory_path is None:
            current_directory = os.getcwd()
            directory_path = os.path.join(current_directory, 'allure-results')

        if not os.path.exists(directory_path):
            print(f'Directory not found {directory_path}')
            return None

        passed_count = 0
        failed_count = 0
        broken_count = 0
        covered_tests = set()

        json_files = [file for file in os.listdir(directory_path) if file.endswith('-result.json')]

        for json_file in json_files:
            file_path = os.path.join(directory_path, json_file)
            with open(file_path, 'r') as json_data:
                data = json.load(json_data)
                status = data.get('status')
                test_name = data.get('name')

                if test_name in covered_tests:
                    continue

                if status == 'passed':
                    passed_count += 1
                elif status == 'failed':
                    failed_count += 1
                elif status == 'broken':
                    broken_count += 1

                covered_tests.add(test_name)

        return {
            "env": TestData.env,
            "platform": TestData.browser,
            "total_tests": len(covered_tests),
            "passed_tests": passed_count,
            "failed_tests": failed_count,
            "broken_tests": broken_count
        }
