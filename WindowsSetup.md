# Setup Windows for Python Development

There are five main steps that we will take to set up our windows environment for working with Python and program our web applications.  We will need to:

1. Set up a Linux Command line
2. Set up Git for version control
3. Setup a database for our development work
4. Install Python
5. Set up a Visual Studio Code to use as a text editor

Each of these steps will ahve multiple substeps that you should follow along with exactly.  As you go through this process you will not only learn how to use the command line better, but we can ensure that everybody is working with the same environment so errors and problemns are easier to find.

## Set up the command line

_We will be loosely following the instructions found at: [Best Practices for Setting up WSL](https://docs.microsoft.com/en-us/windows/wsl/setup/environment) from Microsoft.

Before we can get started with the rest of the setup we need to set up our commadn line environment.  For this class we will be using a UNIX based command line environment.  This is for a couple of reasons.  The first is that it will ensure a consistent environment for both Windows and Mac users so we can use the same commands and instructions.  (Mac is a UNIX based operating system.)  For Windows we can use the "Windows Subsystem for Linux" to provide a Linux based environment on top our our Windows OS.  Microsoft developed and supports this environment to all Windows customers mainly because of web developers.  The second reason is that nearly all webservers run Linux and so all the tools and technologies that are used on those servers work best in that environment.  It is best practice to have your local development environment match the server environment as close as possible to minimize the chance of hard to diagnose bugs, errors, and misconfigurations.

To setup the commadn line environment you will need to:

> Open a PowerShell prompt as an administrator
	
![Steps to open Power Shell as administrator](http://Link to file)

> Type `wsl --install` in to the newly opened PowerShell
> Wait for the install to complete then reboot
> The Linux terminal windows called 'Ubuntu' should automatically open when your computer reboots
>> Choose a unix username
>> Choose a unix password

You now have a Linux operating system installed as a Windows app called "Ubuntu". Ubuntu (oo·boon·too) is the most common flavor of Linux and is widely used to host web applications.  You do not have a full version of Ununtu, but the smallest set available that will allow you to run commands on a command line.

By default it is completely isolated from your Windows environment.  It cannot control any programs on Windows or access any of your Windows apps or files.

You can now issue your first command by typing `touch /home/<userusername>/.hushlogin`
	
This will create a file in your home directory that prevents Ubuntu from displaying the full information for the system when you first login for the day.

A few important points:

1. `touch` is a "command." It will create the file given by the argument if it doesn't already exist.  If it does exist it will just update the last modified date to the current date and time.
2. /home/<username>/.hushlogin is the argument.  In this case it is the location of the file you want to create.  (As a convention, whenever you need to "fill in the blank" with information specific to your computer we will use `< >` to denote the information that you need to provide.)
	
	Alternatively we could ahve used `~/.hushlogin` as a shortcut.  `~` is a built in alias for "my home directory."
3. Notice that the file _.hushlogin_ starts with a ".".  This signifies that the file is a hidden file.  By default it won't be displayed when we ask for a list of files.

We can list files with the `ls` command. Type the command into the terminal.

```
	ls
~$
````

We should be getting no ouput since we do not have any visible files in our home folder yet.

Let's create a file:
```
~$ touch mynewfile
~$ ls
mynewfile
```

Now try typing `ls -la` into the terminal
```
~$ ls -la
total 40
drwxr-xr-x 3 jrhowell jrhowell 4096 Nov 11 09:36 ./
drwxr-xr-x 3 root     root     4096 Nov 11 08:04 ../
-rw-r--r-- 1 jrhowell jrhowell   33 Nov 11 09:35 .bash_aliases
-rw------- 1 jrhowell jrhowell  100 Nov 11 09:35 .bash_history
-rw-r--r-- 1 jrhowell jrhowell  220 Nov 11 08:04 .bash_logout
-rw-r--r-- 1 jrhowell jrhowell 3771 Nov 11 08:04 .bashrc
-rw-r--r-- 1 jrhowell jrhowell    0 Nov 11 09:36 .hushlogin
drwxr-xr-x 2 jrhowell jrhowell 4096 Nov 11 08:05 .landscape/
-rw-r--r-- 1 jrhowell jrhowell    0 Nov 11 08:05 .motd_shown
-rw-r--r-- 1 jrhowell jrhowell  807 Nov 11 08:04 .profile
-rw------- 1 jrhowell jrhowell 6105 Nov 11 09:35 .viminfo
```
	
Your output might look slightly different from mine based since we have different usernames and we might have slightly different files.
