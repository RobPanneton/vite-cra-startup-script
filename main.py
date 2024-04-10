import subprocess

import pyautogui
import time


def create_cra():

    # # GET INFO FROM USER
    # Prompt the user for the folder path where the project will be created
    folder_name = input("Please enter the folder path where the project will be created: ")

    # Exit program if folder is invalid
    if folder_name != "coding" and folder_name != "frontendmentor":
        print("invalid input")
        return

    # Prompt the user for the name of the project folder
    project_name = input("Please enter the name of the project folder: ")

    # Just for demonstration, print out the collected information
    print(f"Folder Path: {folder_name}")
    print(f"Project Name: {project_name}")




    # OPEN GIT BASH
    # Option 1: open with Popen with an assumed directly path 
    # Path to the Git Bash executable
    # git_bash_path = r"C:\Program Files\Git\git-bash.exe"

    # # Use subprocess.Popen to open Git Bash
    # subprocess.Popen(git_bash_path)

    # Option 2: use windows search to launch it
    time.sleep(2)
    pyautogui.press('win')

    time.sleep(1)
    pyautogui.typewrite('git bash')

    time.sleep(1)
    pyautogui.press('enter')

    # ADD CHECKER TO MAKE SURE BASH WINDOW IS STILL OPEN BEFORE CONTINUING?


    # NAVIGATE TO CODING FOLDER
    time.sleep(2)
    if folder_name == "coding":
        pyautogui.typewrite("cd documents/coding")

    if folder_name == "frontendmentor":
        pyautogui.typewrite("cd documents/coding/frontendmentor")

    time.sleep(0.3)
    pyautogui.press('enter')

    # NAVIGATE TO PROJECT FOLDER
    pyautogui.typewrite(f"cd {project_name}")
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1)



    # RUN CRA W/ TYPESCRIPT
    # project_directory = ""

    project_directory = ""
    
    if folder_name == "coding":
        project_directory = f"C:\\Users\\PC\\Documents\\Coding\\{project_name}"
    elif folder_name == "frontendmentor":
        project_directory = f"C:\\Users\\PC\\Documents\\Coding\\frontendmentor\\{project_name}"
    else:
        print(f"invalid directory: {project_directory}")
        return

    print(f"creating react typescript app in the following directory: {project_directory}")
    print(f"please wait, this will take a minute")


    commandCRA = ["npx", "create-react-app", "app", "--template", "typescript"]    
    subprocess.run(commandCRA, shell=True, check=True, cwd=project_directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("CRA complete\n")

    time.sleep(0.5)

    commandSass = ["npm", "install", "sass", "--save-dev"]
    app_directory = f"{project_directory}\\app"

    print(f"adding sass in the following directory: {app_directory}")

    subprocess.run(commandSass, shell=True, check=True, cwd=app_directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

    print("Sass has been added to the project")

    

    # GET INTO APP FOLDER AND SRC FOLDER AND DELETE USELESS FILES




    pyautogui.typewrite("cd app/src")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("rm App.css App.test.tsx index.css logo.svg react-app-env.d.ts reportWebVitals.ts setupTests.ts")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)

    # EDIT APP AND INDEX
    typingSpeed = 0.001
    # Start the here-document command to write multi-line content to App.tsx
    pyautogui.write('cat <<EOF > App.tsx', interval=typingSpeed)
    pyautogui.press('enter')

    # The content of your TypeScript file
    ts_content = """import React from "react";\n
import "./cssReset.scss";\n
export function App() {
    return <div>clean cra</div>;
};
"""

    # Write the TypeScript content line by line
    for line in ts_content.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')

    ############
    time.sleep(1)

    pyautogui.write('cat <<EOF > index.tsx', interval=typingSpeed)
    pyautogui.press('enter')

    # The content of your TypeScript file
    ts_content ="""import React from "react";
import ReactDOM from "react-dom/client";

import { App } from "./App";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(<App />);
"""

    # Write the TypeScript content line by line
    for line in ts_content.split('\n'):
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

    # The content of your TypeScript file
    ts_content = """/* http://meyerweb.com/eric/tools/css/reset/ v2.0 | 20110126 License: none (public domain) */ html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video { margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline; } /* HTML5 display-role reset for older browsers */ article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section { display: block; } body { line-height: 1; } ol, ul { list-style: none; } blockquote, q { quotes: none; } blockquote:before, blockquote:after, q:before, q:after { content: ""; content: none; } table { border-collapse: collapse; border-spacing: 0; } *, *::before, *::after { box-sizing: border-box; }
"""

    # Write the TypeScript content line by line
    for line in ts_content.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')


    ############
    time.sleep(2)

    pyautogui.write('cat <<EOF > react-app-env.d.ts', interval=typingSpeed)
    pyautogui.press('enter')

    # The content of your TypeScript file
    ts_content = """declare module "*.png";
declare module "*.svg";
declare module "*.jpeg";
declare module "*.jpg";
declare module "*.scss";
declare module "*.webp";
"""

    # Write the TypeScript content line by line
    for line in ts_content.split('\n'):
        pyautogui.write(line, interval=typingSpeed)
        pyautogui.press('enter')

    # End the here-document
    pyautogui.write('EOF', interval=typingSpeed)
    pyautogui.press('enter')


    # RUN THE APP AND OPEN VS CODE
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
    pyautogui.typewrite("npm start")
    time.sleep(1)
    pyautogui.press("enter")



create_cra()