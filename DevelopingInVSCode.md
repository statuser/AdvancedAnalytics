# Final Python Setup

You should now be nearly set up and ready to run the webapp.  There are a couple final steps that you need to complete before everything works correctly.

We will first install the Python Flask Package and then finishing setting up Visual Studio Code for program execution.

## Setup Visual Studio Code

1. Open Project Folder
    From now on we can do nearly all our work from within Visual Studio Code.  VSCode has a built in Git Client as well as a built in terminal.  This will make things signifiacntly easier to mange.  The first thing to do is to open up our project.
    > Go to the File Menu and Select Open Folder if you are on Mac and if you are on Windows select the Connection button in the lower left corner of the window. \
    > Browse to the folder that you have cloned from the Git repository and Select "Open Folder". \
    > Accept in the Security Prompt
2. Make sure you have the correct code
    > You will need to make sure that you have the current code.  We can do this by pulling down the code from the git repository.  We are going to pull a tagged version of the code so we can look at the application before certain changes have been made.  \
    > From the Git Menu in the lower left select the Chapter 1 Tag.  This will check out the code just after the initial files have been created.  \
    > <img width="238" alt="Git Extension" src="https://user-images.githubusercontent.com/2736768/142919576-a87beac1-39a5-4c98-8d93-1f6020cf58f1.png">
    
2. Install Python extensions
    > We will want to install some extensions to help with our Python Development.  There are a few ways to do this.  The easiest is to click on a file that has a .py extension from the file browser to open it up.  \
    > <img width="301" alt="Explorer Settings" src="https://user-images.githubusercontent.com/2736768/142920062-990e3d2e-9d93-4205-a97d-839f7ad7a9f5.png">  \
    > The first time you open a Python file Visual Studio will prompt you to install the extensions.  Otherwise you will have to install the extension manually.  You can do this from the extension menu.  \
    > <img width="338" alt="Python Extensions" src="https://user-images.githubusercontent.com/2736768/142926053-6ff6beea-a3f7-4d04-bb33-371462f2e143.png">  
    > You will want to install all four extensions shown in the screenshot.  \
    > There are many more extensions that can customize and enhance Visual Studio Code.  For know this set will work, but in the future you may want to search for other extensions for additional languages.  
4. Select Virtual Environment
    > We wil also need to set Visual Studio to use the proper Python Environment.  In the bottom status bar there is text to say which Python Environment you are using.  Clicking this will allow you to change it.  \
    > <img width="323" alt="Set Python Virtual Environment" src="https://user-images.githubusercontent.com/2736768/142926486-689ffcac-d776-47eb-bef6-667634593d1d.png">. \
    > Select the CSDashboard environment that we previously created.  It should be marked with a star as the Recommended environment.  \
    > You will need to restart Visual Studio Code for this to take effect.  
7. Install flask module
  > One final set up step.  We need to isntall the flask module upon which our project will be built.  This is done in the terminal via pip.  Visual Studio has a built in terminal that we can use.  From the **View** Menu select **Terminal** It will appear below your editor view.  \
  > Make sure our Virtual Environment is active by looking for _(CSDashboard)_ at the start of the terminal prompt line.  If it is not you can manually activate by typing: `workon CSDashboard`. \
  > In the terminal type: `pip install flask`. \
  > We are now ready to test the application.  \
  > Select the **Run** menu and choose **Start Debugging**. \
 to run the application.  You should e able to access the application at (http://127.0.0.1:5000) as specified in the terminal output.
 
## Requirements Files

We will be installing a lot of Pyton packages in order to get our program built.  It can be difficult to keep track of what needs to be installed and what has already been installed especially when working with others.  Python includes a way to manages this.  The applicaiton developers will keep a requirements.txt file that lists the required packages and versions in the root directory.  Everytime new packages are installed this file needs to be updated.  It is a good habit to install the packages from the requirements file everytime you do a "git pull".  You can do this by running:
```bash
  pip install -r requirements.txt
 ```
in the terminal after doing a git pull.

## Fixing a bug
There is a bug in the code.  The index page is not loading properly because there is no route defined for a student without a name.  We can easily fix this bug by updating the code:

```Python
@app.route("/student") \
@app.route('/student/<name>') \
def student(name=None): \
    return render_template("student.jinja", title="Student Page", name=name)
```

This will add a new blank student route and set the default student name to None which is Python for missing.
  
  
