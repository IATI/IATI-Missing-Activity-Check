# IATI-Missing-Activity-Checker

This is a standalone tool to compare IATI activities in the IATI Datastore and IATI Dashboard. The IATI Tech team will endevout to incorporate this into the Dashboard in due course.
These scripts are based on those written by Ben Webb @Bjwebb


## Requirements
* Unix environment
* wget
* Python 2.7+



## Set-up

Once you have cloned this repositary, open a terminal window and navigate to the correct folder and set the file permissions of the shell scripts so that they can be executed: 
```
chmod +x run.sh
chmod +x get_data.sh
```


## Running

To run, open a terminal window and navigate to the folder where your files are stored.  Then run:

```
./run.sh
```

The process involves downloading all IATI data - this totals 2GB+ (July 2015). Therefore, depending on the speed of your computer/network, the process will take some time - perhaps 2+ hours on a home broadband connection.

Files are outputted in JSON format and can be found in the 'output' directory.



## Deployment

You can set a job in cron to execute `run.sh` at an interval of your choice.  Note that the output files will append a date, and thus repeat running in the same day will overwrite output files generated earlier that day.



## License

::
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
