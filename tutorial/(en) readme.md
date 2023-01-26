Welcome, today I will show you how to make a program to ask someone to be your girlfriend or boyfriend.

Note: The creator of the program is: @professorlucianoz
I am just creating the project with some changes made by me and teaching you step by step.

Attention: This program was made using the Python language, so make sure Python is installed on your computer before you start coding.

1st step: We must create a new folder for the project and open that folder in an IDE of your choice (I used VsCode).

2nd step: We must install two tools to create a virtual environment, the first is "Pipenv", this tool is necessary for us to access Pyside6, which is the second tool we will need. PySide is necessary for us to create the virtual environment I mentioned earlier.

3rd step: Open the VsCode terminal and type "pip3 install pipenv"; right after Pipenv is installed, type "pipenv install pyside6". Once the installation is finished, two files will appear in your folder "Pipfile" and "Pipfile.lock"; a virtual environment will also be created in your folder and the PySide6 library will be installed.

4th step: Before continuing with the next steps, you must look in the terminal for the location of your virtual environment. The location appears right below the line "Successfully created virtual enviroment!", I will provide a print for better guidance. After finding the location of the virtual environment, you must copy, paste, and save it somewhere, it can be save in a notepad.

5th step: Let's enter our virtual environment, to do this, type "pipenv shell".

Step 6: In the terminal, type "cd 'location of your virtual environment'", then type "dir". After that, the terminal will show you some folders, we need to enter the "Scripts" folder, so type "cd Scripts" and then type "dir" again. Now, there should be a lot of files in your terminal, but don't worry, we will only use one. Type "pyside6-designer", a new window will open on your computer, this is the "Qt Designer" program and we will use it to create the design of our program.

Step 7: To make our lives easier, we will create a directory to open the Qt Designer. To do this, copy the directory of your virtual environment, paste it in the terminal, and add the following: "\Scripts\pyside6-designer". Now, every time you want to open the Qt Designer, you can go to the terminal and write: "C:\Users\cdu_v.virtualenvs\Dating_request-uw2VL0Xs\Scripts\pyside6-designer"

Step 8: Open the Qt Designer, select the "Main Window" option and click "Create". Now you can start creating the layout of your program as you wish, but if this is your first time using this tool, you can continue following the tutorial step by step.

Step 9: Let's select the dimensions of the window of our program, in the right corner, you can see some lines with a yellow background, there you can find the options "Width: 800" and "Height: 600", let's change the dimensions to "Width: 462" and "Height: 450".

Step 10: On the left side, we see several tool options, we will need to use the "label" tool.
