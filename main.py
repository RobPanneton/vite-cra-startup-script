import pyautogui
import time

from utils import run_subprocess
from strings import COMMAND_CREATE_APP, COMMAND_MODULES, COMMAND_SASS, TS_APP_CONTENT, TS_INDEX_CONTENT, CSS_RESET_CONTENT, TS_TYPE_DECLARATIONS


def create_cra():

    # # GET INFO FROM USER
    # prompt user for folder path where the project will be created
    folder_name = input("Please enter the folder path where the project will be created: ")

    # exit program if folder is invalid
    if folder_name != "coding" and folder_name != "frontendmentor":
        print("invalid input")
        return

    # prompt user for the name of the project folder
    project_name = input("Please enter the name of the project folder: ")

    # print out the collected information
    print(f"Folder Path: {folder_name}")
    print(f"Project Name: {project_name}")

    # RUN VITE CRA W/ TYPESCRIPT
    project_directory = ""
    path_to_dev_folder = "C:\\Users\\PC\\Documents\\Coding\\"
    
    if folder_name == "coding":
        project_directory = f"{path_to_dev_folder}{project_name}"
    elif folder_name == "frontendmentor":
        project_directory = f"{path_to_dev_folder}{project_name}\\{project_name}-frontendmentor"
    else:
        print(f"invalid directory: {project_directory}")
        return

    print(f"creating react typescript app with Vite in the following directory: {project_directory}")
    print(f"please wait, this will take a minute")

    # CREAT THE APP
    run_subprocess(COMMAND_CREATE_APP, project_directory)

    print("create vite react app complete\n")

    time.sleep(0.5)

    app_directory = f"{project_directory}\\app"

    print(f"installing node modules in the following directory: {app_directory}")
    run_subprocess(COMMAND_MODULES, app_directory)
    print("node_modules have been installed")

    time.sleep(0.3)

    print(f"adding sass in the following directory: {app_directory}")
    run_subprocess(COMMAND_SASS, app_directory)
    print("Sass has been added to the project")

    time.sleep(0.3)

    
    # OPEN GIT BASH
    
    time.sleep(2)
    pyautogui.press('win')

    time.sleep(1)
    pyautogui.typewrite('git bash')

    time.sleep(1)
    pyautogui.press('enter')

    # ADD CHECKER TO MAKE SURE BASH WINDOW IS STILL OPEN BEFORE CONTINUING?



    # NAVIGATE TO PROJECT FOLDER
    time.sleep(2)
    if folder_name == "coding":
        pyautogui.typewrite(f"cd documents/coding/{project_name}")

    if folder_name == "frontendmentor":
        pyautogui.typewrite(f"cd documents/coding/frontendmentor/{project_name}/{project_name}-frontendmentor")

    time.sleep(0.3)
    pyautogui.press('enter')


    # GET INTO APP FOLDER AND SRC FOLDER AND DELETE USELESS FILES

    pyautogui.typewrite("cd app/src")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("rm App.css index.css ./assets/react.svg")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)

    # EDIT APP AND INDEX
    typingSpeed = 0.001
    # Start the here-document command to write multi-line content to App.tsx
    pyautogui.write('cat <<EOF > App.tsx', interval=typingSpeed)
    pyautogui.press('enter')


    # Write the TypeScript content line by line
    for line in TS_APP_CONTENT.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')

    ############
    time.sleep(1)

    pyautogui.write('cat <<EOF > main.tsx', interval=typingSpeed)
    pyautogui.press('enter')

    # Write the index content line by line
    for line in TS_INDEX_CONTENT.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')

    ############
    time.sleep(1)

    pyautogui.write('cat <<EOF > variables.scss', interval=typingSpeed)
    pyautogui.press('enter')

    # The content of your TypeScript file
    ts_content = ""

    # Write the TypeScript content line by line
    for line in ts_content.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')


    ############
    time.sleep(1)

    pyautogui.write('cat <<EOF > cssReset.scss', interval=typingSpeed)
    pyautogui.press('enter')


    # Write the css reset content line by line
    for line in CSS_RESET_CONTENT.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')


    ############
    time.sleep(2)

    pyautogui.write('cat <<EOF > react-app-env.d.ts', interval=typingSpeed)
    pyautogui.press('enter')

    # Write the typescript type declarations line by line
    for line in TS_TYPE_DECLARATIONS.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')


    # OPEN VS CODE AND RUN THE APP
    time.sleep(1)
    pyautogui.typewrite("cd ..")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("cd ..")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("code .")
    time.sleep(0.5)
    pyautogui.press("enter")

    time.sleep(5)
    pyautogui.hotkey("ctrl", "`")
    time.sleep(1)
    pyautogui.typewrite("cd app")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.typewrite("npm run dev")
    time.sleep(1)
    pyautogui.press("enter")



create_cra()