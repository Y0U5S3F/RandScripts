EmailStage
This Python script is used to send emails with an attachment. It uses the SMTP protocol to send emails. The script reads the email addresses, login credentials, message, and attachment from separate files.

Setup
Clone this repository to your local machine.
Install the required Python libraries by running pip install -r requirements.txt in your terminal.
Usage
Add a emails.txt file in the root directory. This file should contain the email addresses of the recipients. Each email address should be on a separate line.

Add a login.txt file in the root directory. This file should contain the email login credentials in the format login:pass.

Add a stage.txt file in the root directory. This file should contain the email subject and body. The first line should be the subject, and the rest of the file should be the body of the email.

Add a cv.pdf file in the root directory. This file will be attached to the email.

Run the script by typing python emailStage.py in your terminal.

Customization
You can customize the script by editing the variables and file names as per your requirements. For example, you can change the SMTP server and port, the file names, and the attachment type. Please read the code for more details.

Disclaimer
Please use this script responsibly. Do not use it for spamming or any illegal activities. The author is not responsible for any misuse of this script.