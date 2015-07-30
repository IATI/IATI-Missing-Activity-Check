# Shell script to download files from the IATI Datastore and IATI Dashboard

# Download all activities from the Datastore. Save in the temp folder
echo "Getting data from the IATI Datastore"
wget --progress=bar "http://datastore.iatistandard.org/api/1/access/activity.xml?stream=True" -O temp/datastore_all_data.xml

# Download all activities from the Datastore. Save in the temp folder
echo "Getting data from the IATI Dashboard"
wget --progress=bar "http://dashboard.iatistandard.org/stats/current/aggregated/iati_identifiers.json" -O temp/dashboard_identifiers.json
