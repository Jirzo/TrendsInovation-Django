
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

To set up WSL, ensure your system is running Windows 10 version 2004 or later, or Windows 11. If you're using an older version, please refer to the [manual ](https://learn.microsoft.com/en-us/windows/wsl/install-manual) for upgrading your system to a compatible version.

Now, you can install all the necessary components for Windows Subsystem for Linux (WSL) with a single command.

To get started, open PowerShell or the Windows Command Prompt as an administrator (right-click and select "Run as administrator"). Then, run the command `wsl --install`. Once the installation is complete, restart your computer.

After the restart, launch WSL with administrator privileges. You'll be prompted to create a username and password for your Linux distribution.

This account will be your Linux administrator, allowing you to run administrative commands using `sudo` (Super User Do).


### MariaDB

Before installing MariaDB, run the following command: `sudo apt update && sudo apt upgrade`.

If you encounter a _Temporary failure resolving error_, you'll need to update the DNS settings.
Enter `sudo nano /etc/resolv.conf`, change the IP address to `8.8.8.8`, save the file, and rerun the update and upgrade commands.

Next, install MariaDB with this command: `sudo apt install mariadb-server`.

This will install MariaDB without requiring a password or additional configurations. Since the default setup may leave your MariaDB instance vulnerable, use the script provided by the `mariadb-server` package to secure it by limiting access and removing inactive accounts.

Run the command: `sudo mysql_secure_installation`, and press ENTER when prompted to leave the password as 'none'.

> **Output:** <br>
> **NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB SERVERS IN PRODUCTION USE! PLEASE READ EACH STEP CAREFULLY!**
>
> To log into MariaDB for securing it, you'll need the current password for the root user. If you’ve just installed MariaDB and haven’t set a root password yet, leave the field blank and simply press ENTER.
>
> **Enter current password for root (enter for none):**


You will be prompted with a question about transitioning to Unix socket authentication. Since you already have a secured root account, you can skip this step. Simply type 'n' and press ENTER to continue.

> **Output:**
> <br>
> Setting the root password or using Unix socket authentication ensures that no one can access the MariaDB root user without proper authorization.
>
> Since your root account is already secured, you can confidently respond with 'n'.
>
> **Switch to Unix socket authentication [Y/n]:** n
>
> After the installation, you will mainly use these three commands to interact with MariaDB:

Now, type 'n' and then press ENTER to proceed.

> **Output:**
> <br>
> OK, successfully used password, moving on...
>
> Setting the root password ensures that no one can access the MariaDB root user without proper authorization.
>
> **Set root password? [Y/n]:** n

After that, you can press 'Y' and then ENTER to accept the default settings for all subsequent prompts. This will remove anonymous users and the test database, disable remote root logins, and apply the new configurations, ensuring that MariaDB enforces the changes you've made.

If desired, you can also create an administrative user. Please follow the next steps:

> Type `sudo mariadb` to access the MariaDB shell.
>
> Next, create a new user with root privileges and password-based access. Be sure to replace the username and password with your desired values:
>
> ```sql
> GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
> ```
>
> Then, flush the privileges to ensure that the changes are saved and accessible in the current session:
>
> ```sql
> FLUSH PRIVILEGES;
> ```
>
> Finally, exit the MariaDB shell by typing: 
>
> ```sql
> exit
> ```


Now it's time to start the process and verify if the installation was successful.

- Use `sudo systemctl start mariadb` to launch the database; you may be prompted for the WSL root password.
- Run `sudo systemctl status mariadb` to check the current status of the database.
- If needed, use `sudo systemctl stop mariadb` to halt the database service.


### To establish a connection from Windows HeidiSQL to MariaDB running on WSL2.

Ensure that you have HeidiSQL installed on your Windows machine. <br> You can download it from the [HeidiSQL](https://www.heidisql.com/download.php?download=installer) website. 

Make sure the MariaDB service is up before proceeding.

- Launch HeidiSQL. Once inside, start the process of creating a new server by right-clicking on **New**. Ensure that the **Network Type** is set to **MariaDB** or **MySQL (TCP/IP)**. 
![Register server image](https://imgur.com/aPhI7wt.png)


### Create and populate the database

- Once you've established a new session and accessed it, right-click on the session name and select the option to <br> **Create new database**. This will allow you to set up a new database within your MariaDB instance..  
![Database name image](https://imgur.com/6l7DLnL.png)

- Set the next name 'mariadbScaffold'.  
![Database name image](https://imgur.com/bLGB56H.png)

- After the previous steps you will see this.
![Database name image](https://imgur.com/6rzIjnM.png)

Once you've created the database, go to the **Query** tab, copy the code from the `_DRFDB.sql` file, and paste it into the script area. Execute the script to run the SQL commands.

Ensure you have already followed the steps to run the Django server as outlined in the [DJANGO - GETTING STARTED](https://github.com/Jirzo/DJANGOM) guide, as this process creates the necessary tables. The SQL file will then only be used to populate those tables.

If a modal appears, simply press the yes option.

- [MariaDB script](https://github.com/Jirzo/DJANGOM/blob/main/DB/DJANGOM.sql) - file path


IIf the process was successful, you will see a message similar to this: `Affected rows: 25  Found rows: 0  Warnings: 0  Duration for 32 queries: 0.125 sec.` Finally, you will observe the database being populated. After running the file, you will have visibility into the tables and will be able to execute queries against them. </br>
![Create database image](https://imgur.com/5qpYsUk.png)
<hr/>
