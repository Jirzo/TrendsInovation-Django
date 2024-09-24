
<h1 align="center">Maria DB</h1>

## 🧐 About <a name = "about"></a>

A vary basic and simple SQL script that will populate our Maria DB.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will give you the ability to have the database mounted

## Prerequisites

You will need to have install postgres SQL 14

- [Linux on windows ](https://learn.microsoft.com/en-us/windows/wsl/install) - WSL 2
- [Maria DB ](https://www.pgadmin.org/download/) - Data base
- [HeidiSQL ](https://www.heidisql.com/download.php?download=installer) - DBMS 



## Manual installation

### WSL

To set it up, your system must be running Windows 10 version 2004 or a newer version, or it should be running Windows 11.If you have an older version, please refer this [manual ](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

Now, you have the option to install all the necessary components for running Windows Subsystem for Linux (WSL) using a single command. 
To do this, open PowerShell or the Windows Command Prompt with administrator privileges (right-click and choose "Run as administrator"). Input the command `wsl --install`, and after that, restart your computer.

After restarting your computer, launch the Windows Subsystem for Linux (WSL) with administrator privileges. You will then be prompted to set up a username and password for your Linux distribution.

This account will be designated as the Linux administrator, granting the capability to execute sudo (Super User Do) administrative commands.


### MariaDB

Prior to installing MariaDB, you need to execute the following command `sudo apt update && sudo apt upgrade`.
If you get the _Temporary failure resolving error_ you have to change the DNS.

Type `sudo nano /etc/resolv.conf` in that file, modify the IP address to 8.8.8.8, save the changes, and then execute the update and upgrade commands again.

Type this command: `sudo apt install mariadb-server </br> 
Executing these commands will install MariaDB without requiring you to set a password or make any additional configuration changes. As the default setup may leave your MariaDB installation vulnerable, you'll utilize a script provided by the mariadb-server package to limit server access and remove any inactive accounts.

So, type this command: `sudo mysql_secure_installation`
Then, simply press ENTER to indicate 'none'.

> Output
> NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
>      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!
>
> In order to log into MariaDB to secure it, you'll need the current
> password for the root user.  If you've just installed MariaDB, and
> you haven't set the root password yet, the password will be blank,
> so you should just press enter here.
>
>Enter current password for root (enter for none):

You'll encounter a query asking whether you wish to transition to Unix socket authentication. Given that you already possess a secured root account, you can bypass this stage. Type 'n' and then press ENTER to proceed.

> Output
> . . .
> Setting the root password or using the unix_socket ensures that nobody
> can log into the MariaDB root user without the proper authorisation.
>
> You already have your root account protected, so you can safely answer 'n'.
>
> Switch to unix_socket authentication [Y/n] n
>
> Once installed, you'll primarily utilize these three commands for working with MariaDB:

Now, type 'n' and then press ENTER to proceed.

> Output
> . . .
> OK, successfully used password, moving on...
>
> Setting the root password ensures that nobody can log into the MariaDB <br>
> root user without the proper authorisation.
>
> Set root password? [Y/n] n

Afterward, you can proceed by pressing 'Y' and then ENTER to accept the defaults for all subsequent prompts. This action will remove certain anonymous users and the test database, disable remote root logins, and immediately implement these new configurations so that MariaDB enforces the changes you've made.

Optional, you can create an administrative user.
Please follow the next steps

>    Type `sudo mariadb` <br>
> Then create a new user with root privileges and password-based access. Be sure to change the username and password to match your preferences: <br>
> Then `GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;` <br>
> Flush the privileges to ensure that they are saved and available in the current session: <br>
> `FLUSH PRIVILEGES;` <br>
> Following this, exit the MariaDB shell: `exit`

Now it's time to initiate the process and confirm whether the installation was successful.

- `sudo systemctl start mariadb` to initiate the database, it will prompt you for the WSL root key.
- `sudo systemctl status mariadb` to know the status of the database.
- `sudo systemctl stop mariadb` to stop the database


### Establishing a connection from Windows HeidiSQL to WSL2 MariaSB.


After finishing the MariaDB installation, download and install [HeidiSQL](https://www.heidisql.com/download.php?download=installer). Make sure the MariaDB service is up before proceeding.

- Launch HeidiSQL. Once inside, initiate the process of creating a server by right-clicking on **New**. Make sure that Network type is MAriaDB or MySQL (TCP/IP) 
![Register server image](https://imgur.com/aPhI7wt.png)


### Create and populate the database

- Once you've established a new session and accessed it, you'll need to right-click on the session name and select the option to create a new database.  
![Database name image](https://imgur.com/6l7DLnL.png)

- Set the next name 'mariadbScaffold'.  
![Database name image](https://imgur.com/bLGB56H.png)

- After the previous steps you will see this.
![Database name image](https://imgur.com/6rzIjnM.png)


Once you have created the database, on the query tab copy the code from the _DRFDB.sql_ file and paste it into the script file and execute it.
Make sure that you already follow the steps to run the django server [DJANGO - GETTING STARTED](https://github.com/Jirzo/DJANGOM) , because on that process Django create ours tables so the sql file will only populate the tables.
If a modal appears, simply press the yes option.

- [MariaDB script](https://github.com/Jirzo/DJANGOM/blob/main/DB/DJANGOM.sql) - file path


If the process was successful you will see a message like this: `Affected rows: 25  Found rows: 0  Warnings: 0  Duration for 32 queries: 0.125 sec.` Lastly, you'll witness the database populating, and upon running the file, you'll have visibility into the tables and be capable of executing queries. </br>
![Create database image](https://imgur.com/5qpYsUk.png)

<hr/>
