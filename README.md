# Airveda Assignment

To run this project:
1. Download the repository
2. `cd` into the directory
3. Run `source env/bin/activate` to use the environment
4. Install the required packages using `pip install -r requirements.txt`
5. Run `python manage.py migrate` to do the migrations
6. Finally run `python manage.py runserver`

*Admin ID and Pass*
id: admin
password: admin

*Sample urls to test the code*
http://127.0.0.1:8000/api/devices/c3f09b22-b77b-11ea-b3de-0242ac130004/readings/temperature?start_on=2020-06-26T07:10:05.16&end_on=2020-06-27T07:10:33.98

http://127.0.0.1:8000/api/devices/c3f09b22-b77b-11ea-b3de-0242ac130004/readings/temperature?start_on=2020-06-25T10:12:09.90&end_on=2020-06-26T10:11:51.87