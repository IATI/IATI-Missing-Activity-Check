from datetime import datetime
import json

# Load data from the JSON files which contain the identifiers data
print "Opening files containing IATI identifiers from temp folder"
datastore_identifiers = set(json.load(open('temp/datastore_identifiers.json')))
dashboard_identifiers = set(json.load(open('temp/dashboard_identifiers.json')).keys())

# Compute the differences between the files
print "Computing missing IATI activities"
identifiers_missing_from_dashboard = sorted(list(datastore_identifiers - dashboard_identifiers))
identifiers_missing_from_datastore = sorted(list(dashboard_identifiers - datastore_identifiers))

# Add a count of all activities
print "Preparing output data"
data_missing_from_dashboard = {'count': len(identifiers_missing_from_dashboard), 'identifiers': identifiers_missing_from_dashboard}
data_missing_from_datastore = {'count': len(identifiers_missing_from_datastore), 'identifiers': identifiers_missing_from_datastore}

# Generate filenames based upon today's date
filename_not_in_dashboard = 'not_in_dashboard-' + datetime.today().strftime("%Y%m%d") + '.json'
filename_not_in_datastore = 'not_in_datastore-' + datetime.today().strftime("%Y%m%d") + '.json'

# Write resulting data to JSON output files
print "Writing to files"
json.dump(data_missing_from_dashboard, open('output/'+filename_not_in_dashboard, 'w'), indent=4)
json.dump(data_missing_from_datastore, open('output/'+filename_not_in_datastore, 'w'), indent=4)

# Output done message
print "Comparison completed!"