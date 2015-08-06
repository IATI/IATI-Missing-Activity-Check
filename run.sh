# Shell script to run comparisons on missing IATI activities in both the IATI Datastore and IATI Dashboard

# Define a sub-routine to nest output
indent() { sed 's/^/  /'; }

# Download relevant data from the IATI Datastore and IATI Dashboard.
echo "Downloading required data from the IATI Datastore and IATI Dashboard.  This could take a while!"
./get_data.sh | indent || exit 1

# Process the data from the Datastore to obtain a JSON file of IATI identifiers from the raw XML data
echo "Extracing IATI identifiers from the raw XML downloaded from the IATI Datastore."
python extract_datastore_identifiers.py | indent || exit 1

# Compute the differences
echo "Computing differences between the IATI Datastore and the IATI Dashboard."
python compare.py | indent || exit 1

# Remove files in the temp folder
echo "Removing temporary files."
rm temp/* | indent

# Output complete message
echo "Completed!  Output files can be found in the 'output' directory."

