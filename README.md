# Log Analysis Project

## Project Description:
Create a reporting tool that prints out reports from the database. 
This project uses the psycopg2 module to connect to the database.
### Questions to Answer:
1. **What are the most popular three articles of all time?** 
1. **Who are the most popular article authors of all time?**
1. **On which days did more than 1% of requests lead to errors?**

## Project Setup:
This project uses Vagrant on a virtual machine, and requires a few extra steps to set up:

#### Installation and file setup:
1. Install the correct [VirtualBox](https://www.virtualbox.org/) for your system. 
1. Next, install [Vagrant](https://www.vagrantup.com/).
1. Download the vagrant setup [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
1. Unzip the file, and put newsdata.sql into your vagrant directory.
1. Download this project, unzip, and copy the project into your vagrant directory (shared with the VM).

#### Boot up the Virtual Machine (VM):
1. Via command line, navigate to your vagrant directory. 
1. Run ``` vagrant up ``` for the initial VM build. Allow several minutes for the shell prompt to return.
1. Run ``` vagrant ssh ``` to connect.
1. cd into the correct directory: ``` cd /vagrant/log_analysis ```
1. Load the database: ``` psql -d news -f newsdata.sql ```

## Start up the project
1. Connect to Vagrant with ``` vagrant up ``` and ``` vagrant ssh ```. 
1. cd into the project: ``` cd /vagrant/log_analysis ```
1. Execute ``` python log_analysis.py ```

## Expected Output:
Fetching results...

TOP THREE ARTICLES BY PAGE VIEWS:
"Candidate is jerk, alleges rival" | 338647 views
"Bears love berries, alleges bear" | 253801 views
"Bad things gone, say good people" | 170098 views

TOP THREE AUTHORS BY VIEWS:
Ursula La Multa | 507594 views
Rudolf von Treppenwitz | 423457 views
Anonymous Contributor | 170098 views

DAYS WITH MORE THAN 1% ERRORS:
July 17 2016 | 2.3% errors
