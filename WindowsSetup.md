# Setup Windows for Python Development

There are five main steps that we will take to set up our windows environment for working with Python and program our web applications.  We will need to:

1. Set up a Linux Command line
2. Set up Git for version control
3. Setup a database for our development work
4. Install Python
5. Set up a Visual Studio Code to use as a text editor

Each of these steps will have multiple sub-steps that you should follow along with exactly.  As you go through this process you will not only learn how to use the command line better, but we can ensure that everybody is working with the same environment so errors and problems are easier to find.

## Set up the command line

_We will be loosely following the instructions found at: [Best Practices for Setting up WSL](https://docs.microsoft.com/en-us/windows/wsl/setup/environment) from Microsoft._

Before we can get started with the rest of the setup we need to set up our command line environment.  For this class we will be using a UNIX based command line environment.  This is for a couple of reasons.  The first is that it will ensure a consistent environment for both Windows and Mac users so we can use the same commands and instructions.  (Mac is a UNIX based operating system.)  For Windows we can use the "Windows Subsystem for Linux" to provide a Linux based environment on top our our Windows OS.  Microsoft developed and supports this environment to all Windows customers mainly because of web developers.  The second reason is that nearly all web servers run Linux and so all the tools and technologies that are used on those servers work best in that environment.  It is best practice to have your local development environment match the server environment as close as possible to minimize the chance of hard to diagnose bugs, errors, and misconfigurations.

To setup the command line environment you will need to:

> Open a PowerShell prompt as an administrator
	
![Steps to open Power Shell as administrator](https://github.com/statuser/MBA656AdvancedAnalytics/blob/a6e1f64e78ae4442ccc5e23dbbee65f486127856/Open%20Power%20Shell.gif?raw=true)

Type or copy and paste the command below on the command line then follow the instructions.
```bash
wsl --install
```
The Linux terminal windows called 'Ubuntu' should automatically open when your computer reboots.  If you need to open it later there is a Ubuntu application that you can run from the start menu.  

> Choose a unix username  
> Choose a unix password  
Your password will not show anything when you type it in.  Not even **.

You now have a Linux operating system installed as a Windows app called "Ubuntu". Ubuntu (oo·boon·too) is the most common flavor of Linux and is widely used to host web applications.  You do not have a full version of Ubuntu, but the smallest set available that will allow you to run commands on a command line.

One advantage is that you can share files between the Windows and Linux environment so you can use both Windows and Linux programs with the files.

You can now issue your first command by typing `touch /home/<userusername>/.hushlogin`

This will create a file in your home directory that prevents Ubuntu from displaying the full information for the system when you first login for the day.

A few important points:

1. `touch` is a "command." It will create the file given by the argument if it doesn't already exist.  If it does exist it will just update the last modified date to the current date and time.

2. /home/<username>/.hushlogin is the argument.  In this case it is the location of the file you want to create.  (As a convention, whenever you need to "fill in the blank" with information specific to your computer we will use `< >` to denote the information that you need to provide.)

Alternatively we could have used `~/.hushlogin` as a shortcut.  `~` is a built in alias for "my home directory."

3. Notice that the file _.hushlogin_ starts with a ".".  This signifies that the file is a hidden file.  By default it won't be displayed when we ask for a list of files.

We can list files with the `ls` command. Type the command into the terminal.

```bash
ls
```

We should be getting no output since we do not have any visible files in our home folder yet.

Let's create a file:
```bash
touch mynewfile
ls
```
> mynewfile


Now try typing `ls -la` into the terminal

```bash
ls -la
```
> total 40
> drwxr-xr-x 3 jrhowell jrhowell 4096 Nov 11 09:36 ./  
> drwxr-xr-x 3 root     root     4096 Nov 11 08:04 ../  
> -rw-r--r-- 1 jrhowell jrhowell   33 Nov 11 09:35 .bash_aliases  
> -rw------- 1 jrhowell jrhowell  100 Nov 11 09:35 .bash_history  
> -rw-r--r-- 1 jrhowell jrhowell  220 Nov 11 08:04 .bash_logout  
> -rw-r--r-- 1 jrhowell jrhowell 3771 Nov 11 08:04 .bashrc  
> -rw-r--r-- 1 jrhowell jrhowell    0 Nov 11 09:36 .hushlogin  
> drwxr-xr-x 2 jrhowell jrhowell 4096 Nov 11 08:05 .landscape/  
> -rw-r--r-- 1 jrhowell jrhowell    0 Nov 11 08:05 .motd_shown  
> -rw-r--r-- 1 jrhowell jrhowell  807 Nov 11 08:04 .profile  
> -rw------- 1 jrhowell jrhowell 6105 Nov 11 09:35 .viminfo  

Your output might look slightly different from mine based since we have different usernames and we might have slightly different files.  This command users the _-la_ options for the ls command.  Options are different from arguments.  Options control how the command run and are invoked by either a single or a double dash.  (In general use a single dash for single letter options and a double dash for long form word length options.). The _l_ options tells `ls` to display the results in long format and the _a_ option says to display all the files rather than just the visible ones.  I could also have written `ls -l -a` or `ls -l --all` to get the same output.

If I wanted help on a specific command you can use the option `--help` to a list of arguments and options available for the command or `man ls` to get the manual page for the command.  (Usually it is easier to use Google for specific help rather than reading the man page.)

Let's clean up the stray file we created.
```bash
rm mynewfile
```

The command `rm mynewfile` removes the file named "mynewfile" from the current directory.

We can now finish setting up our Linux environment by insuring that we are up-to-date and have all the latest patches.  You will want to run this command on a regular basis to make sure you have any security and other updates installed.

```bash
sudo apt update && sudo apt upgrade
...
```

There are a couple of interesting things going on with this command.  The first is _sudo_.  This command takes as an argument an additional command and runs it as an administrator.  In Unix based systems it is generally considered best practices to run programs and issue commands using the most restricted user possible.  This makes sure that your environment remains secure.  However if you are going to update the operating system you need access to all files and programs.  For that reason there is a special way to elevate your user privileges  to preform specific commands; _sudo_ is the command that allows that.

The command _apt_ is the Ubuntu package manager.  You can think of it as the command to access the Ubuntu app store.  The argument _update_ tells the program to update the list of available packages and programs.  The argument _upgrade_ tells the app store to upgrade all the installed programs to their latest version.

One interesting thing is going on.  The _&&_ allows you to combine two commands into a single line.  They will run one after another and is exactly the same as running as two separate commands like so:

```bash
sudo apt update
sudo apt upgrade
```

We are going to use one final command.  In the command prompt type:

```bash
explorer.exe .
```

This will open your windows file explorer to the current directory which should be your Linux home directory.  A couple of small things worth noting.  First notice the .exe on the end of explorer.  We have to add this because explorer is a Windows not a Linux program.  Windows programs all have the .exe file extension and anytime we want to open a Windows program from Linux we will need to specify the full command including the .exe extension.  The second thing is that the argument is "."   This is a shortcut for the current directory.  This will open Windows File Explorer to the current directory where the Linux command line is open too.

## Installing and setting up Git and GitHub

The good news is that git is already installed when we set up WSL and updated the packages.  We can makes sure that we have the latest version and that it is still installed by issuing the command:

```bash
sudo apt-get install git
```

You should receive  message that git is already installed at at the lastest version.  We still need to set some configuration options for git however.  This will set some default options and configurations.

```bash
git config --global user.name "<Your Name>"
git config --global user.email "<Your Email>"
```

This will set up git so that your name and email are attached to to each commit you make automatically.  This way we can tell who made each change to the code.  You can override this on a commit by commit basis, but if we are going to change somebody else's code it is nice to be able to easily identify and contact the person originally responsible for the code so we can make sure we don't introduce a bug or break a feature that they have added.

### Set up an account on GitHub

You will need an account on GitHub to download and check in the source code for our project.  You can create an account at: [Sign up for Github](https://github.com/signup?ref_cta=Sign+up).

You should also go through the [Quickstart on Github Guides](https://docs.github.com/en/get-started/quickstart) to get an understanding of git and GitHub.

We will checkout the Advanced Analytics Project later in the tutorial.

In order to use GitHub from your command line you will need to authenticate by running the following command.  This will have you authenticate using a web browser the first time you connect and then store a computer specific password so you don't have to authenticate again in the future.  To do this run the following command:

```bash
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager-core.exe"
```

[Logging in to GitHub from the commandline](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Set up a development database

For the final program we will use a full database program like Postgres or MySQL.  Those are a little heavy for development work so for now we will use a lightweight database called SQLite.  This uses regular files to store the databases and can easily be accessed.  SQLite as a fully featured database for single user access, but it is not appropriate when multiple people may be accessing the database at the same time. 

To install SQLite we simply need to type the following on the command line.

```bash
sudo apt-get install sqlite
```

The structure of this command should be familiar to you at this point.


## Set up a Text Editor

For this class, we will use Visual Studio Code (**Not Visual Studio**) as our text editor.  It have excellent Python support and is well integrated with the Windows Subsystem for Linux.

To install, visit the [VS Code install page](https://code.visualstudio.com/download) and select the appropriate installer.  (If you have a relatively recent computer the 64-bit installer is the correct one.).You should install this like a regular Windows program on your Windows file system.

As you are going through the install pay attention to the following options:

* Install Visual Studio Code to your C drive.  This is a regular Windows program and should run in Windows not your Linux Subsystem.

* On the page to **Select Additional Tasks** during the installation check the **Add to PATH** option so you can easily open files and folders from your Linux Command prompt using the `code` command.

* Install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).  This extension pack includes the Remote - WSL extension allowing you to open any folder on your machine or over a network include those folders in your Linux File System.

![Install WSL Steps](https://github.com/statuser/MBA656AdvancedAnalytics/blob/a6e1f64e78ae4442ccc5e23dbbee65f486127856/Install%20Remote%20Cote%20-WSL.gif?raw=true)

Visual Studio Code has a nice interactive getting started program.  If you are not familiar with Text Editors or IDEs and want to investigate the different features that are available I would recommend that you go through the "Getting Started" carefully.

With the Remote - WSL extension installed, you will see a new Status bar item at the far left.

![Remote Status bar item](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/remote-status-bar.png)

The Remote Status bar item can quickly show you in which context VS Code is running (local or remote) and clicking on the item will bring up the Remote - WSL commands.

![Remote - WSL commands](https://code.visualstudio.com/assets/docs/remote/wsl-tutorial/remote-wsl-commands.png)
 
## Install Python

There are many ways to install Python and get it working in your Linux program.  The different methods all have their pros and cons.  One of the problems when working with a lot of different projects is that each project could depend on different external bits of code called modules or on different versions of Python.  If you update Python for one project, it could break another project without you knowing it.  In addition you could have conflicts in the external packages, called dependencies, that you are going to use.  One additional thing to consider is that when you upload your code to a server you need to upload all the dependencies as well. When install all your dependencies in a single place you could end up uploading unnecessary dependencies with your project.  To get around these problems we are going to use someting called virtual environments.  This will give us a separate Python version and set of dependencies for each program that you write.  This is a good practice even though this may be the only program that you work on.

### Install Pyenv for virtual Python Environments

We are going to install the Pyenv package from GitHub to manage our Python versions.  This makes installing and updating multiple versions of Python simple and seamless.  

We are going to install this program into ~/.pyenv a hidden folder in our home directory.  The command to do this is:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

We now need to add a bit of configuration to make sure that pyenv works correctly.  **Tip: You can copy and paste into the Linux command line by copying the text you want to paste and then right-clicking in the Linux command prompt window.  This will paste and execute the copied text.**

```bash
# the sed invocation inserts the lines at the start of the file
# after any initial comment lines
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.profile
echo 'eval "$(pyenv init --path)"' >>~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
````

You will need to restart your command prompt for this to take effect.  This is as simple as closing the window and reopening Ubuntu from the start menu.

### Install Python 3.10.0

_This will take a while so you might want study up on HTML and CSS while you wait.  A good written resource is [Getting Started with the Web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web) from Mozilla the makers of Firefox.  If you prefer video the [Web Demystified](https://www.youtube.com/playlist?list=PLo3w8EB99pqLEopnunz-dOOBJ8t-Wgt2g) created by Jérémie Patonnier is a quick introduction._

We will be using Python 3.10.0 for this class.  Before we can install it, we need to install some additional packages to make sure that Python build correctly.  You can do this by executing the following commands:

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

We are now ready to install Python.  This is a simple as issuing the following command and then waiting.

```bash
pyenv install 3.10.0
```

We now need to tell pyenv which version of Python to use.  The easiest way to do this is to set the global flag which will default to the specified version.

```bash
pyenv global 3.10.0
```

To test to make sure everything works try:

```bash
python --version
```

You should see the output:
> Python 3.10.0

Python is now set up and ready to go.  We just need to set up our project directory and set up a project specific virtual environment.  

To set up the virtual environment I like to use a program called virtualenv-wrapper. We use a command called "pip" to install the virtualenv-wrapper program.  This is a python program and comes from the python "App Store"

```bash
pip install virtualenvwrapper
mkdir -p ~/.virtualenvs
cat <<EOT >> ~/.bashrc
#Virtualenvwrapper settings:
export WORKON_HOME=$HOME/.virtualenvs
. $(pyenv prefix)/bin/virtualenvwrapper.sh
EOT
```

You will need to reboot the Ubuntu shell again.

Before we activate our virtual environment we should clone the project repository.  There is a directory structure that I like to use that will be demonstrated in the code below.  Feel free to modify the directories below to match your preferences.  I like to have a "src" directory in my home directory that contains all my programming projects.  With in the source directory I have a folder for each individual project that is managed as a git repository.  

You can set this up as:

```bash
cd ~
mkdir -p src
cd src
git clone https://github.com/statuser/BYUMBACSDashboard.git CSDashboard
```
This creates a src folder, changes the current directory to that source folder and then clones the repository from GitHub into a folder called CSDashboard.
 
Let's change to to this directory and activate our virtual environment.

```bash
cd ~/src/CSDashboard
mkvirtualenv CSDashboard
```

This will create the virtual environment and activate it.  As a general rule I like to have the virtual environment named the same things as the folder holding my project.  That is why the `mkvirtuelenv` command uses the argument CSDashboard.

if you ever want to deactivate the virtual environment so you can work update the global python modules you can use `deactivate`. you can then reactivate the command by going to your project directory and typing `workon .` to activate the virtual environment for the current directory.  You can tell tell a virtual environment is active by checking your prompt on the command line. The currently active virtual environment is displayed in parenthesis at the beginning of your command prompt. Like this:

> (CSDashboard) ~/src/CSDashboard$ 

# Opening the project in Visual Studio Code

 Open Visual Studio Code and click the green "connect" icon in the lower left corner of the window.  Select "Open Folder in WSL..."  Navigate to your Home > _Username_ > src folder and select the CSDashboard folder.  Click Open.  You will receive a security warning.  Because Visual Studio can execute code to change your computer automatically, you should only open programs you trust with execution privileges. Select "Yes I trust the authors" and you are ready to go with a properly set up environment.
 
