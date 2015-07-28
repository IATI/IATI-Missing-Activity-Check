# Shell script to run the comparisons

# Download relevant data from the IATI Datastore and IATI Dashboard.
echo "Downloading required data from the IATI Datastore and IATI Dashboard.  This could take a while!"
./get_data.sh

# Process the data from the Datastore to obtain a JSON file of IATI identifiers from the raw XML data
echo "Extracing IATI identifiers from the raw XML downloaded from the IATI Datastore."
python extract_datastore_identifiers.py

# Compute the differences
echo "Computing differences between the IATI Datastore and the IATI Dashboard."
python compare.py

# Remove files in the temp folder
echo "Removing temporary files."
rm temp/*

# Output complete message
echo "Completed!  Output files can be found in the 'output' directory."