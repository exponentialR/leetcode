import json
import os
# m_dict = {'Name': 'Samuel Adebayo', 'Age': 'NULL', 'Location': 'Belfast', 'action_number' : 0}
# current_action = 0
with open('iams.iams', 'r') as f:
    data = json.load(f)
    current_action = data['action_number']
data['action_number'] = current_action + 1

with open('iams.iams', 'w') as f:
    json.dump(data, f, indent=2)