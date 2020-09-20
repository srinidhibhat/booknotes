# booknotes-myFirstDjangoProject
This repository contains source code for a Django based website to store and share your book notes.  
(You can visit the website <a href="http://srinidhikbhat.pythonanywhere.com/">here</a>)  
Huge thanks to <a href="https://github.com/CoreyMSchafer">Corey Schafer</a> as the code and design is inspired from his <a href="https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p">Django YouTube tutorial</a> series.

**In this website:**  
- You can Register and Login to the website.
- You can view the books and respective booknotes added by other users.
- You can add a book you read and the notes you made along with other info (like date read, rating, time taken to read etc.,) to share with every one.
- You can see a 'Quote of the Day' sidebar which will refresh with a new quote from a popular book every day.

**Instructions to use the code:**
- Clone the repository into your project folder.
- Install Python(3.6 or above).
- Create a virtual environment (optional but recommended) and activate it.
- Navigate to project folder and install all the prerequisites (using `pip install -r requirements.txt').
- Edit the *'settings.py'* file (path : booknotes-DjangoProject/myFirstDjangoProject/), to add your own 'SECRET_KEY'.
- Run these commands to migrate the django models:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Finally, run `python manage.py runserver` to run the project on localhost.

**Improvements planned:**  
- Support 'Forgot password' option.
- Make UI improvements to view the posts as thumbnails.
- A visualization page to display user statistics (like number of books read, books read on a certain year, average rating etc.)

