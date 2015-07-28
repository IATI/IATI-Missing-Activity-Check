import json

datastore_identifiers = set(json.load(open('datastore_iati_identifiers.json')))
dashboard_identifiers = set(json.load(open('iati_identifiers.json')).keys())

json.dump(sorted(list(datastore_identifiers - dashboard_identifiers)), open('not_in_dashboard.json', 'w'), indent=4)
json.dump(sorted(list(dashboard_identifiers - datastore_identifiers)), open('not_in_datastore.json', 'w'), indent=4)
