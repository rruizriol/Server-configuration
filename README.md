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
13. Clone and configure the app

        sudo nano /etc/sudoers.d/grader
        # Add this line and save the file
        grader ALL=(ALL) NOPASSWD:ALL

