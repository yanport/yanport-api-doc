import http.client
import json
import sys
import time

def color(status):
  if status.lower() == 'success':
    return 'good'
  elif status.lower() == 'failure':
    return 'danger'
  else:
    return 'warning'

def field (status):
  if status.lower() == 'success':
    return { "value": "Deploy with success"}
  else:
    return { "value": "Deploy failed"}

slack_token = sys.argv[1]
start_timestamp = sys.argv[2]
job_status = sys.argv[3]
job_id = sys.argv[4]
push_author = sys.argv[5]

gmtime = time.gmtime(int(time.time()) - int(start_timestamp))
duration = '{} min {} sec'.format(str(gmtime.tm_hour * 60 + gmtime.tm_min), str(gmtime.tm_sec))

data = {
  "channel": "#tech-code",
  "attachments": [
    {
      "pretext": 'Build and deploy API documentation <https://storage.googleapis.com/yanport-www.appspot.com/openapi.yaml>',
      "text": '{} after {} (<https://github.com/yanport/yanport-app/actions/runs/{}|Open>)'.format(job_status.capitalize(), duration, job_id),
      "color": color(job_status),
      "fields": [
        field(job_status)
      ],
      "footer": push_author
    }
  ]
}

body = json.dumps(data)

connection = http.client.HTTPSConnection('slack.com')
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + slack_token}

connection.request('POST', '/api/chat.postMessage', body, headers)

response = connection.getresponse()
print(response.read().decode())
