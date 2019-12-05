A basic API using flask framework
====================================
1] Requires flask library installed
command - pip install flask
2] will run on port 5050
3] flask specific - @app.route is a decorator which defins that tthe following function should be executed once the parameter in the decorator is matched with the request url.


files:
=================
1] get_api - contains all get requests
        * get_api function  - has homepage decorator argument '/' so it will act as index page.
                            - It simply returns a string to be displayed on the browser
        * get_name(name)    - his function has decorator which accepts an string parameter which will act as a path parameter for the url which essentially be the dynamic value depending up on user accessing it.
                            - It returns the dynamic page assosiated with the path parameter however in this case we are just printing out the dynamic string value.
        * get_blog(blog_id) - This function has decorator which accepts an integer parameter which will act as a path parameter for the url which essentially be the dynamic value depending up on user's wish
                            - It returns the dynamic page assosiated with the path parameter however in this case we are just printing out the dynamic integer value.
        * get_revision_number(rev_no) - This get request is similar to the earlier one only the parameter type has changed and that is something we should take into consideration.
2] post_api - contains a post request
        * post_user()       - This fuction is special because it accepts both POST as well as GET requests on the same url.
                            - It will accept the payload to hypothetical registration and auto GET request call is intitiated on successful registration.