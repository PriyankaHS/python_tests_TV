import json
import os
import requests

from reporting.slack.slack_template import SlackTemplate


class SlackNotification:
    def __init__(self):
        self.WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

    def send_slack_notification(self):
        if not self.WEBHOOK_URL:
            print("SLACK_WEBHOOK_URL environment variable is not set. Unable to send Slack notification.")
            return

        response = requests.post(
            self.WEBHOOK_URL,
            data=json.dumps(SlackTemplate().constructed_message_format()),
            headers={'Content-Type': 'application/json'}
        )
        return response


if __name__ == '__main__':
    response = SlackNotification().send_slack_notification()

    if response.status_code == 200:
        print("Slack notification sent successfully.")
    else:
        print(f"Failed to send Slack notification. Status code: {response.status_code}")
