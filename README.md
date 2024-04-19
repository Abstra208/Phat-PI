# Phat-PI

**This project is a web application designed to control a Scroll Phat HD screen on a Raspberry Pi. It is built using Flask and uses a simple user authentication system.**

## Getting Started

**Before you begin, make sure you have Python installed on your Raspberry Pi. If not, you can install it by running the following command in the terminal:**

```sh
sudo apt-get update
sudo apt-get install python3
```

**Next, navigate to where you want your file to be located, for exemple documents:**
```sh
cd /home/pi/documents
```

**Clone this repository:**
```sh
git clone https://github.com/abstra208/phat-pi.git
```

**Navigate to the project directory:**
```sh
cd phat-pi
```

**Install the required dependencies:**
```sh
pip install -r requirements.txt
```

**You will also need to install the Scroll Phat HD screen api:**
```sh
curl https://get.pimoroni.com/scrollphathd | bash
```
You do not need to do a full install, but you still can if you want

**The Scroll Phat HD screen api must only be run on a Raspberry Pi using the official OS (with or without the graphic interface)**

## IMPORTANT

**Before using, change the string `app.secret_key` in [`app.py`](https://github.com/abstra208/phat-pi/blob/main/app.py#L5) to something else.**<br>
**This is to keep the saved session saved securely**<br>
**If you don't have a long string in your head, you can always run `python -c 'import secrets; print(secrets.token_hex())'` to get a random string using python**

## Usage
**Run in a development server:**
```sh
./dev.sh
```
Running the app in a development server can be useful to try the app, but not to have it always running<br>
This will always run the app on `http://localhost:5000`<br><br>
**Run using gunicorn:**
```sh
./run.sh
```
Using the gunicorn app, on the other hand is made to always run on a server or on our case, on a Raspberry Pi<br>
This will always run the app on `http://localhost:8000`.<br>

**To stop the app, press `ctrl + c` when the terminal is focused**

## Features

- Users login and logout
- Users management (Coming soon)
- Control your Scroll Phat HD screen from anywhere on your network
- Using a gunicorn server for an always running server, or a development server for testing purpose

## Project Structure

```
.
├── __pycache__/        / Include the crash and logs
├── .github/            / Include the license and funding files
├── app.py              / The app
├── README.md           / Read this file before using
├── requirements.txt    / The requirements for this project to work
├── run.sh              / To run the project using gunicorn
├── dev.sh              / To run the project on a development server
├── screen.json         / The saved screen information to show
├── users.json          / The users infomation to login
├── screen.py           / The code to show the text on the screen
├── static/
│   ├── img/            / Contain image used in this project
│   ├── users/          / Contain the users images
│   ├── style.css       / The style sheet for the two html page
│   └── script.js       / The java script for the two html page
└── templates/
    ├── index.html      / The main page
    └── login.html      / The page to login
```

## Information

**Contributing:**<br>
Contributions are always welcome! Create a pull request or donate. See [FUNDING](/.github/FUNDING.yml) for more information.

**License:**<br>
Distributed under the MIT License. See [LICENSE](/.github/LICENSE) for more information.

**Contact:**<br>
Ludovic Morin (Owner) - ludovicmorin357@hotmail.com

**Project Link:**<br>
- [Phat Pi](https://github.com/abstra208/phat-pi) (Owner: Ludovic Morin)
- [Scroll Phat HD](https://github.com/pimoroni/scroll-phat-hd) (Owner: Pimoroni Ltd)