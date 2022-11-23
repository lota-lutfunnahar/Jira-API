import os

USERNAME = os.environ.get('JIRA_USERNAME')
HOST = os.environ.get('JIRA_HOST')
URL = f"https://{HOST}"
# API_URL = URL + '/rest/api/3'

API_URL = URL + '/rest/api/3'
AUTH = (USERNAME, os.environ.get('JIRA_PASSWORD'))
# AUTH = 'jYQUHX0lMo35TjbbOGtyC123'
PAGE_SIZE = 50
