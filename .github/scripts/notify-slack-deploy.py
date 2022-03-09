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

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

slack_token = safe_list_get(sys.argv, 1, "unknown token")
start_timestamp = safe_list_get(sys.argv, 2, 0)
job_status = safe_list_get(sys.argv, 3, "unknown status")
job_id = safe_list_get(sys.argv, 4, "unknown workflow")
push_author = safe_list_get(sys.argv, 5, "unknown actor")

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
