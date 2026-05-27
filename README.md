# Interfacing ChatGPT on a TI 84 Plus CE Calculator
This code allows ChatGPT to be interfaced on a TI 84 Plus CE calculator. Using the CE C/C++ Toolchain, a program was written that allows users to enter a prompt on the calculator and send the prompt to a computer connected over USB (via serial). The computer then takes the prompt, makes the API call, and passes the response back to the calculator over serial.
## Installation
To use this program, you will need to install the following:

 - TI Connect™ CE software to transfer the program onto the calculator (available from the TI website), or alternatively you can go to "ticalc.link" website to transfer the .8xp file
 - The DEMO.8xp program (included in this repository)
 - calcgpt.py (included in this repository)
 - Python (available from the Python website)
 - The PySerial library (can be installed by running `pip install pySerial`)
 - A GroqCloud API Key
 - The OpenAI Python library (can be installed by running `pip install openai`)

**IMPORTANT READ**
I could not get the program to work when just double clicking on the .py file so yes it is necessary to open it as I do from the terminal using instructions below.

## Usage

 1. Connect the calculator to your computer via USB.
 2. Transfer the DEMO.8xp program to your TI 84 Plus CE calculator using TI Connect™ CE software.
 3. Launch the program on your calculator by going to the catalog and selecting `Asm(`. Then, open the programs menu, select DEMO, and press enter twice to run it. The calculator will display "ready" when the program is ready to use.
 4. Open terminal and cd into the directory containing "calcgpt.py" on your computer.
 5. Run "python calcgpt.py" in your terminal
 6. Select the COM port the calculator is connected to when prompted by the program.
 7. The calculator should display that it has connected. From here, press the "2nd" key to enter a prompt.
 8. The response from the AI will be displayed on the calculator screen.

## Notes

 - This program has only been tested on a TI 84 Plus CE calculator and may not work on other calculator models.
 - Newer TIOS versions may require modification to run the program. I am running it on OS 5.2.2.0043
 - The OpenAI API requires an API key, which will be obtained from the GroqCloud website. You will need to replace the placeholder text in the .py file with your api key that you obtained from "https://console.groq.com/"
 - There may some issues getting input from the user that you may run into, but I didnt expereince any.
 - I am using Python 3.14
 - I am on Windows 11 25H2
