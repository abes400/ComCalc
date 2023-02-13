# ComCalc
A simple GUI calculator application written in Python using the PyQt5 library

# Getting Started
- Click ***Code***, then click ***Download ZIP***
- Unzip the files to a directory, keep an eye out on where the ***requirements.txt*** is
  - Let's suppose that you moved the unzipped files to a folder called ***MyDirectory***, the folder shold look like this:
  - MyDirectory:
    - ***README.md***
    - ***requirements.txt***
    - ***Source/***
- If you are using Windows, run ***CMD***; if you are using macOS or unix, run ***Terminal***
- Locate to the ***MyDirectory***
  - CMD: > ***cd C:\Users\admin\desktop\MyDirectory***
  - Terminal: $ ***cd /Users/admin/desktop/MyDirectory***
  - You should see the name MyDirectory in the prompt
- Create a virtual environment next to the Source folder in ***MyDirectory***
  - CMD: > ***python -m venv MyVenv***
  - Terminal: $ ***python3 -m venv MyVenv***
- Now, the folder shold look like this:
  - MyDirectory:
    - ***README.md***
    - ***requirements.txt***
    - ***Source/***
    - ***MyVenv/***
- Activate the virtual environment you have created
  - CMD: > ***MyVenv\Scripts\activate***
  - Terminal: $ ***source MyVenv/bin/activate***
- Now, your prompt should look like this:
  - CMD: > ***(MyVenv) C:\Users\admin\desktop\MyDirectory > ***
  - Terminal: $ ***(MyVenv) ....... $ ***
- Type the following command:
  - CMD: > ***pip install -r requirements.txt***
  - Terminal: $ ***pip install -r requirements.txt***

You can check whether the required packages are installed on your virtual environment:
  - type ***pip freeze***
  
The PyQt5 should be included in the list printed.

- Finally, locate to the ***Source/*** folder and open the ***ComCalc.py*** with your favorite Python IDE, and you are ready to go.

