# ADBuddy - Best Way to Finish UAB Online Courses

Welcome to ADBuddy - the Python script that will help you breeze through your online courses! 
Whether you're studying for a certification or just trying to expand your knowledge, ADBuddy 
is here to help you navigate the course content with ease.

## How It Works

ADBuddy uses the Selenium library to automate the process of waiting for the required amount 
of time between course modules. And of course, it does all of this while keeping your precious 
ADB document at the forefront of everything!

## Getting Started

To get started with ADBuddy, simply clone the repository and install the necessary dependencies
using the following command:

```
pip install -r requirements.txt
```

After, installing the requirements you need to input your credentials in the `config.py` file. 
Both fields in the configuration file are required, which are the username and password for your
turkiye.gov.tr account. Do not worry about your credentials being stolen, as they are only used
to log you into the website and are not stored anywhere else. They are local to your computer. 

Next, navigate to `/src` containing `main.py`, and run the script using the following command:

```
python main.py
```

You will need to specify if you want to complete the Amatör Denizci Belgesi course or the Kısa 
Mesafe Telsiz Operatörlüğü course by entering either `adb` or `kmt` respectively.

ADBuddy will automatically begin navigating through the course content, waiting for the required 
amount of time between modules. 

## Contributions and Feedback

ADBuddy is an open-source project, and we welcome contributions from anyone interested in helping 
me improve the tool. If you encounter any bugs or issues, or if you have suggestions for new features 
or improvements, please don't hesitate to submit a pull request or open an issue.

## Last Words

We hope you find ADBuddy to be a helpful companion in your online learning journey. Selametle! 