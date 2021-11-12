# Setup Your Mac for Python Development

When we are doing Python development we will be primarily using two tools.  The first is a text editor called Visual Studio and the second is a built in Mac program called "Terminal".  Terminal is the command line for the Mac and is where we can type in a execute commands.  This may feel a little strange at first, but you will find that it is much faster and more precise for many of the development tasks that we will be doing.

There are two ways to open the Terminal.  The first is to open it by going to Applications>Utilities>Terminal.  The second, my preferred way, is to use spotlight.  Press the ⌘+Space shortcut to invoke spotlight search and then typing "Terminal" and pressing Enter.  This will launch the Terminal application.

**Insert GIF Demo Here**

## Set up the command line

Before we can get started with the rest of the setup we need to set up our command line environment.  For this class we will be using a UNIX based command line environment.  This is for a couple of reasons.  The first is that it will ensure a consistent environment for both Windows and Mac users so we can use the same commands and instructions.  (Mac is a UNIX based operating system.)  For Windows we can use the "Windows Subsystem for Linux" to provide a Linux based environment on top our our Windows OS.  Microsoft developed and supports this environment to all Windows customers mainly because of web developers.  The second reason is that nearly all webservers run Linux and so all the tools and technologies that are used on those servers work best in that environment.  It is best practice to have your local development environment match the server environment as close as possible to minimize the chance of hard to diagnose bugs, errors, and misconfigurations.

 You can now issue your first command by typing `touch ~/.hidden_file`
	
This will create a file in your home directory.

A few important points:

1. `touch` is a "command." It will create the file given by the argument if it doesn't already exist.  If it does exist it will just update the last modified date to the current date and time.
2. ~/.hidden_file is an argument.  In this case it is the name and location of the file you want to create. `~` is a built in alias for "my home directory."
3. Notice that the file _.hidden\_file_ starts with a ".".  This signifies that the file is a hidden file.  By default it won't be displayed when we ask for a list of files.

We can list files with the `ls` command. Type the command into the terminal.

```
ls
````

This will list the files in your home directory.  The output will vary depending on what you currently have installed.


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

	
Your output might look slightly different from mine based since we have different usernames and we will have different files.  This command users the _-la_ options for the ls command.  Options are different from arguments.  Options control how the command run and are also prefereced by either a single or a double dash.  (In general use a single dash for single letter options and a double dash for long form word length options.). The _l_ options tells `ls` to display the results in long format and the _a_ option says to display all the files rather than just the visible ones.  I could also have written `ls -l -a` or `ls -l --all` to get the same output.

If I wanted help on a specific command you can use the option `--help` to a list of arguments and options available for the command or `man ls` to get the manual page for the command.  (Usually it is easier to use Google for specific help rather than reading the man page.)

Let's clean up the stray file we created.
```bash
rm ~./mynewfile
```

The command `rm `./mynewfile` removes the file named "mynewfile" from the home directory.


## Installing and setting up Git and GitHub

The next step in the process is to install the command line tools for development.  This is a combination of the git command as well as additional tools for building Python and other software products.  We can do that with the following command:

```bash
sudo xcode-select --install
```

There are a couple of intersting things going on with this command.  The first is _sudo_.  This command takes as an argument an additional command and runs it as an administrator.  In Unix based systems it is generally considered best practices to run programs and issue commands using the most restricted user possible.  This makes sure that your environment remains secure.  However if you are going to update the operating system you need access to all files and programs.  For that reason there is a special way to elevate your user privileges  to preform specific commands; _sudo_ is the command that allows that. The second thing is that this command runs an actually Mac program rather than just a command for the command.  

Alternatively we could simple download and install the XCode program from the Mac App Store.  This is a much larger program and is only really useful if you are planning on developing Mac or iOS apps.

We now need to configure git.

```bash
git config --global user.name "<Your Name>"
git config --global user.email "<Your Email>"
```

This will set up git so that your name and email are attached to to each commit you make automatically.  This way we can tell who made each change to the code.  You can override this on a commit by commit basis, but if we are going to change somebody else's code it is nice to be able to easily identify and contact the person originally responsible for the code so we can make sure we don't introduce a bug or break a feature that they have added.

### Set up an account on GitHub

You will need an account on GitHub to download and check in the source code for our project.  You can create an account at: [Sign up for Github](https://github.com/signup?ref_cta=Sign+up).

You should also go through the [Quickstart on Github Guides](https://docs.github.com/en/get-started/quickstart) to get an understanding of git and GitHub.

We will checkout the Advanced Analytics Project later in the tutorial.

When you use git for the first time, you will need to authenticate.  The git command will automatically launch a web browser that will connect to GitHub and allow you to login.

## Set up a development database

For the final program we will use a full database program like Postgres or MySQL.  Those are a little heavy for development work so for now we will use a lightweight database called SQLite.  This uses regular files to store the databases and can easily be accessed.  SQLite as a fully featured database for single user access, but it is not appropriate when multiple people may be accessing the database at the same time. 

SQLite does not need to be installed since it is already present on your system.  It is used heavily in MacOS for storing data and files.  

## Set up a Text Editor

For this class, we will use Visual Studio Code (**Not Visual Studio**) as our text editor.  It have excellent Python support and is well integrated with the Mac command line.

To install, visit the [VS Code install page](https://code.visualstudio.com/download) and select the appropriate installer.  (If you have a relatively recent computer the 64-bit installer is the correct one.). You should install this by dragging the program from your Downloads folder to you Applications folder.

When you open Visual Studion for the first time , it opens a nice interactive getting started program.  If you are not familiar with Text Editors or IDEs and want to investigate the different features that are available I would recommend that you go through the "Getting Started" carefully.

We want to make one final configuration to Visual Studio Code for now.  It would be really nice do be able to start up Visual Studion Code from the command line.  In order to do this we need to let the command line know that it exists.  We can do that by:

> In Visual Studio Code press ⌘+⇧+P
> Type in `Shell Command` to search for the command to "Install 'code' command in PATH"
> Select the appropriate command and press Enter

We can now open Visual Studio Code by issuing the `code` command from anywhere in the command line.  It takes a single argument which is a folder or a file.  If that is provided it will open that file or folder.


## Install Python

There are many ways to install Python and get it working in your Mac program. (In fact there is already a version of Python installed on MacOS.) The different methods all have their pros and cons.  One of the problems when working with a lot of different projects is that each project could depend on different external bits of code called modules or on different versions of Python.  If you update Python for one project, it could break another project without you knowing it.  In addition you could have conflicts in the external packages, called dependencies, that you are going to use.  One additional thing to consider is that when you upload your code to a server you need to upload all the dependencies as well. When install all your dependencies in a single place you could end up uploading unnecessary dependencies with your project.  To get around these problems we are going to use someting called virtual environments.  This will give us a separate Python version and set of dependencies for each program that you write.  This is a good practice even though this may be the only program that you work on.

### Install Pyenv for virtual Python Environments

We are going to install the Pyenv package from GitHub to manage our Python versions.  This makes installing and updating multiple versions of Python simple and seamless.  

We are going to install this program into ~/.pyenv a hidden folder in our home directory.  The command to do this is:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

We now need to add a bit of configuration to make sure that pyenv works correctly.  **Tip: You can copy and paste into the command line by copying the text you want to paste and then right-clicking in the command prompt window.  This will paste and execute the copied text.**

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile

echo 'eval "$(pyenv init -)"' >> ~/.zshrc
````

You will need to restart your command prompt for this to take effect.  This is as simple as quitting and restarting Terminal.

### Install Python 3.10.0

_This will take a while so you might want study up on HTML and CSS while you wait.  A good written resource is [Getting Started with the Web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web) from Mozilla the makers of Firefox.  If you prefer video the [Web Demystified](https://www.youtube.com/playlist?list=PLo3w8EB99pqLEopnunz-dOOBJ8t-Wgt2g) created by Jérémie Patonnier is a quick introduction._

We will be using Python 3.10.0 for this class.  Installing this is as simple as issuing the following command and then waiting.

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

If you see something else, first try restarting terminal.

Python is now set up and ready to go.  We just need to set up our project directory and set up a project specific virtual environment.  

To set up the virtual environment I like to use a program called virtualenv-wrapper. We use a command called "pip" to install the virtualenv-wrapper program.  This is a python program and comes from the python "App Store"

```bash
pip install virtualenvwrapper
mkdir -p ~/.virtualenvs
cat <<EOT >> ~/.zshrc
#Virtualenvwrapper settings:
export WORKON_HOME=$HOME/.virtualenvs
. $(pyenv prefix)/bin/virtualenvwrapper.sh
EOT
```

Restart Terminal.

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
cd ~/src/CSDashBoard
mkvirtualenv CSDashboard
```

This will create the virtual environment and activate it.  As a general rule I like to have the virtual environment named the same things as the folder holding my project.  That is why the `mkvirtuelenv` command uses the argument CSDashboard.

if you ever want to deactivate the virtual environment so you can work update the global python modules you can use `deactivate`. you can then reactivate the command by going to your project directory and typing `workon .` for work on the current directory.  You can tell tell a virtual environment is active by checking your prompt on the command line. The currently active virtual environment is displayed in parenthesis at the beginning of your command prompt. Like this:

> (CSDashboard) ~/src/CSDashboard$ 

# Opening the project in Visual Studio Code

 In Visual Studio select File> Open Folder or type  `⌘+⇧+P File: Open Folder`.  Navigate to the CSDahboard Folder and click Open.