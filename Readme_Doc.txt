################         Readme Doc       #############


********  SETUP   **********

1) Setup a Virtual Environment
2) Clone the github repository by using this link  --->  https://github.com/ankushrgv/otp 
3) Install the dependencies from REQUIREMENTS.txt file
4) Make migrations
	(though I have not included migrations in the .gitignore file, hence they'll be present in your APPS)
5) Go to the directory ->   otp/apps/otpmanager/
	a) Open the file ""json_data_upload.py""
	b) Add the path to your otp folder by specifying xxxxx in "/home/xxxxx/xxxxx/otp/static/json/contacts.json" 
	c) Run the script  ""json_data_upload.py""  to add contacts to the database
6) Start the server by using "python manage.py runserver" command
7) Open Mozilla/Chrome
8) In the address bar, type "localhost:8000/home"


**NOTE -> To access the Django-Admin to create Users manually, do this:
		a) make a superuser by typing the command -> python manage.py createsuperuser
		b) now open Mozilla/Chrome
		c) In the address bar, type "localhost:8000/admin"
		d) login with the username and password you set for the SUPERUSER
		

Your web app is working




********* FLOW ************

1) The user of OTP Manager sees the home page.

2) By default, the first tab i.e., CONTACTS is displayed
	a) List is sorted by NAME alphabetically
	b) Full Name is displayed
	c) A count of total OTPs sent to that user is also displayed
3) The page step-size has been set to 10 entries, i.e., will display on 10 entries on one page.

4) PAGINATION has also been taken care of
	a) Displays previous 5 and next 5 pages of the current page you are currently on
	   and at the same time displays only 4 or 3 or 2 or 1 or 0 accordingly when required.

5) Now, the user of this APP can click on the any off the contact displayed in the CONTACTS list

6) Clicking on the name of the any specific contact displays the contact details on the same PAGE in the right container
	a) If the user has clicked on a contact which is at the bottom of the page,
	   the page automatically scrolls up for user's convenience.
	b) First Name and Last Name displayed separately 
	c) The above is achieved by dynamically displaying content using JAVASCRIPT
	d) SEND MESSAGE button is given	

7) Clicking on the SEND MESSAGE button of the desired contact, redirects to another page SEND MESSAGE page.
8) A text field is present in which "Hi Your OTP is : XXXXXX" is displayed, which is editable.
	a) Form Validations have been applied.
	b) Message field can not be left EMPTY.
	c) Should have atleast 6 characters and less than 150 characters.
9) A unique 6-digit OTP is generated everytime this page is loaded.
10) On clicking the SEND button, the OTP and the phone is sent to the Nexmo SMS API.
	a) Multiple clicks on SEND button before receiving the RESPONSE from the API has been taken care of.
	   It wont accept multiple clicks.
	b) On receiving the response, the page automatically redirects to the home page in MESSAGES tab.
11) If the "status" value in response from NEXMO's API is a "0", it means it sent the SMS successfully, else it failed.
	a) Sent Messages are displayed under the MESSAGE tab and are sorted on the basis of time(latest)
	b) OTP value, Status value and the Date and Time of the sent message is displayed



******************** Technologies Used  ************************

1) Django 1.9 (python web framework)
2) MySQL Database
3) HTML, CSS, Javascript frontend



******************** Additional Tools Used *********************

1) Sublime Editor
2) Firefox Mozilla
3) Firebug
4) Django Debug Toolbar
5) iPython

******************** Templates and Libraries Used **************

1) Skeleton.css template used foe basic CSS layout (www.getskeleton.com)
2) jQuery library
3) some fonts have also been used


******************* Suggestions ********************************


1) We can also display the Message history along with the Contact Details\
	when any particular contact is clicked under CONTACTS tab.
2) Sending the message with the genearated OTP could have also been achieved by a
	modal window on the same screen, instead of redirecting the page to another URL,
	as it is bit inconvenient to go back to the home page if you have to send the message to some othe contact.
3) If the send message is on another page (another URL), then the NAME and PHONE NUMBER should also be displayed
	above the text field of SMS, so as to know whom we are seding the SMS to, and that have not mistakenly clicked
	on some other contact(I haven't given the functionality as it has not been specified in the requirements)
4) If the sole purpose of the APP is for sending the same message in the SMS, then the text field should NOT be EDITABLE
5) Finally we can give a search functionality as well, to search for a particular contact in the CONTACTS tab as
	well as in the MESSAGES tab as now, one needs to visit all the pages to find a SPECIFIC CONTACT.