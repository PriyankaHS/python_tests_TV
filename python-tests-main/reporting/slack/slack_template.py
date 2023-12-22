import os

from reporting.slack.slack_helper_methods import SlackHelperMethods


class SlackTemplate:
    def __init__(self):
        self.slack_helper = SlackHelperMethods()
        self.allure_data = self.slack_helper.get_allure_report_data()
        self.artifact_url = (os.getenv('GITHUB_SERVER_URL') + '/' + os.getenv('GITHUB_REPOSITORY') + '/actions/runs/'
                             + os.getenv('GITHUB_RUN_ID'))

    def _slack_header(self):
        return [
            {
                'type': 'header',
                'text': {
                    'type': 'plain_text',
                    'text': f"Test Execution Summary    [{self.slack_helper.get_current_datetime()}]    :bar_chart:"
                }
            }
        ]

    def _slack_body(self):
        return [
            {
                'text': f"ENV: *{self.allure_data['env']}*",
                'mrkdwn_in': ['text'],
                'color': 'info'
            },
            {
                'text': f"Platform: *{self.allure_data['platform']}*",
                'mrkdwn_in': ['text'],
                'color': 'info'
            },
            {
                'text': f"Total Tests: *{self.allure_data['total_tests']}*    :test_tube:",
                'mrkdwn_in': ['text'],
                'color': 'good'
            },
            {
                'text': f"Passed Tests: *{self.allure_data['passed_tests']}*    :white_check_mark:",
                'mrkdwn_in': ['text'],
                'color': 'good'
            },
            {
                'text': f"Broken Tests: *{self.allure_data['broken_tests']}*    :warning:",
                'mrkdwn_in': ['text'],
                'color': 'warning'
            },
            {
                'text': f"Failed Tests: *{self.allure_data['failed_tests']}*    :x:",
                'mrkdwn_in': ['text'],
                'color': 'danger'
            },
            {
                'text': f"*<{self.artifact_url}|Allure Results>*    :link:",
                'mrkdwn_in': ['text'],
                'color': '#0000FF'
            }
        ]

    def constructed_message_format(self):
        return {
            'blocks': SlackTemplate._slack_header(self),
            'attachments': SlackTemplate._slack_body(self)
        }
