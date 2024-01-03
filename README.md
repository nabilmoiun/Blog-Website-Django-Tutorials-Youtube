# Django Blog Website

***This project is part of a series on YouTube that teaches how to build a blog  website with Django.***

[Watch on Youtube](https://www.youtube.com/watch?v=WpyXXBTcERc&list=PLoomN1iY7V9neojqrkqPVvE0GdmfOTcht)

Project Summary and Features
================

  + Crud operation on blogs
  + Custom user model
  + Registration
  + Authentication through username plus email
  + Personal profile management
  + Filter blogs by different criteria (title, category, tags)
  + Search blogs by different criteria
  + Like blogs
  + Comment and replies on blogs
  + Follow unfollow other users
  + Implementing generic relations
  + Notification system
  + Mute unmute notifications
  + Deployment on pythonanywhere

Usage
=================

First clone this repo and go to the project root.

    $ git clone https://github.com/Nabil-Moiun/Blog-Website-Django-Tutorials-Youtube.git
    $ cd Blog-Website-Django-Tutorials-Youtube

I would recommend to work on a virtual environment. I have used ***virtualenv*** package to create a virtual environment you may wanna use other package. So install this as well if you already haven't.

    $ pip install virtualenv
    
Now create you own virtual environment here and install the project required packages written in requirements.txt file by running the following commands.

    $ virtualenv venv_name

Activate the virtual environment by the following command:


***On Linux***

    $ source venv_name/bin/activate
    
***On Windows***

If you are using git bash

    $ source venv_name/Scripts/activate
    
If you are using CMD

    $ cd venv_name/Scripts
    $ activate
    $ cd ../../
    
    
Now install the package requirements by:

    $ pip install -r requirements.txt
    
Well your environment is ready now.

Finally, you have to make migrations to get the app started and create a new superuser to interact with the admin dashboard.
So run the following commands as follows:

    $ python manage.py migrate
    $ python manage.py createsuperuser

So after successful completion of these you are ready to run the application by the following command:

    $ python manage.py runserver
    
Now open the browser go to ***localhost/8000/*** and you will see the home page of the application.
But you will find no content. Now login to the the admin dashboard using the username and password you created as a super user.
So login to the admin panel using ***localhost:8000/admin/*** and you will find all of the models. Create some categories first that is needed to create blogs.
Now you are ready to go to use the app.

