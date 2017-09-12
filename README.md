# python-fca-reference-scraper

This is a python 3 app.

The purpose of this app is to get company data from https://register.fca.org.uk/.

So the app needs to accept a reference number and return any firm data.
The data should include:
    Address (if you can get the postcode separately that gets cookies).
    Phone
    Email
    Website
    Companies House Number
    Effective Date
    Current Status.

While the app isnt ended the user can enter as many entries as they like, the results
will be displayed in a human readable format.

At the end the user should be able to export the data to a file, the format will be
defaulted to csv but other formats should be available.

Installation instructions.
	Create a virtual environment.
	pip install requirements.txt

Running the app.
	python manage.py runserver
	go to http://localhost:8000/. 

Next Steps:
	Install coverage.
	Write unit tests, aiming for 90+ test coverage.
	Optimise the code.
		Use bulk create instead of create, which will minimise the db hits.
		Read more docs on beautifulsoup see if i cant optimise the scraping.
		Remove the Ajax call as its not necessary.
	Finish getting the rest of the required fields.
	Make the frontend look pretty.
	