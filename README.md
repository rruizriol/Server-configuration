# Linux Server Configuration

---

## Introduction

In thi project we have to take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

## Server Info

**IP address**: 54.148.43.195

**SSH Connection**: *ssh -p 22 -i "./ssh/udacity_key.rsa" grader@54.148.43.195*

**Web URL**: http://54.148.43.195/

## Configuration Steps

These are the steps done in order to configure the server

1. Create a new user named ***grader***

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
2. Give the grader the permission to sudo

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
3. Copy authorized keys to new user and set privileges

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
4. Logout and loging as the grader user

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
5. Update all currently installed packages

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
6. Change the SSH port from 22 to 2200

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
8. Configure the local timezone to UTC

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
9. Install and configure Apache to serve a Python mod_wsgi application

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
10. Install PostgreSQL:

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
11. Create a catalog user and databse named catalog

        sudo apt-get install git
12. Install Git

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL
13. Install and configure the ***catalog*** application

        # Clone the app
        cd /var/www
        sudo git clone "https://github.com/rruizriol/item-catalog.git"
        sudo mv item-catalog/AppCode item-catalog/appcode
        sudo mv item-catalog catalog
        
        # Install python package
        sudo apt-get install python-psycopg2
        sudo apt-get install python-flask
        sudo apt-get install python-sqlalchemy
        sudo apt-get install python-pip
        sudo pip install oauth2client
        sudo pip install requests
        sudo pip install httplib2
        sudo pip install dicttoxml
        
        # Modify in the following python files the databse connection to use postgresql
        # engine = create_engine('postgresql://catalog:itemcatalogapp@localhost/catalog')
        cd /var/www/catalog/appcode
        sudo nano database_setup.py
        sudo nano db_helper.py
        sudo nano some_items.py
        
        #Configure the database and add some items
        sudo python /var/www/catalog/appcode/database_setup.py
        sudo python /var/www/catalog/appcode/some_items.py
        
        # Adding the server ip 54.148.43.195 to the to Authorized JavaScript Origins 
        # to the catalog application in Google Developer Console
        # Download the new Json file and add the new content to the  
        # client_secrets.json inside  /var/www/catalog/appcode
        sudo nano /var/www/catalog/appcode/client_secrets.json
        
        # Adding the ip http://54.148.43.195 to the "Valid OAuth redirect URIs" 
        # in the Advanced settins for the catalog application in Facebook
        
        # Create the wsgi file to handle the application
        sudo nano /var/www/catalog/appcode/catalog.wsgi
        
        # Create a catalog user
        sudo adduser catalog
        
        # Add to the site configuration to apache /etc/apache2/sites-available/000-default.conf
        sudo nano /etc/apache2/sites-available/000-default.conf
        
        # Restart the apache
        sudo apache2ctl restart

