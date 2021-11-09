My HTML, CSS, JS, Flask Project. Original: https://github.com/CITS3403MATH/Promath.
I just made a commit to transfer the entire project into this Respository, and hence it has only 1 commit: "Initial Commit"

> ProMath

A basic flask based math tutorial app designed to teach the basics of re-arranging equations, indicies, geometry and simultanous equations. The app features the ability for the user to create an account and have their answers saved for the tutorials, quizes and a final test. Feed back is given for the user to track their progress on a progress page.  

> Prerequisites

Requires python3, flask, venv, and sqlite

> Getting Started

Activate the python virtual environment: $source virtual-environment/bin/activate

Make sure to stay in your virtual environment state.

Change Directory to Promaths

(If this is your first time entering this flask app

Perform a download package step by: pip install -r requirements.txt
)

Set global variable by doing a set FLASK_APP=promaths.py

To run the app: $flask run

To stop the app: $^C

To exit the environment: $deactivate or Ctrl-C

> Running the tests

Make sure to be in your python virtual environment: 
(to activate Virtual environment: $source virtual-environment/bin/activate)

Change directory to Promaths

Set global variable by doing a set FLASK_APP=promaths.py

To run unit tests python -m tests.unittest

> Built With

HTML, CSS, Javascript, Flask, virtual Environment, sqlite3, sqlalchemy

> Authors
    
    * Leonard Burtenshaw  (21595359)
    * Nicholas Taylor (21506038)
    * Jessy Wang (22700247)
    * Ee Zher Kwoh (22641463)
    

> Acknowledgements

    Images for the website were extracted from the following sites
    
        - https://online-learning.harvard.edu/course/college-algebra?delta=0
        - https://www.istockphoto.com/vector/chalk-doodle-math-blackboard-gm1168040655-322361518
        - https://bookboon.com/blog/2013/10/learning-calculus-youtube-can-work-frederic-mynard/
        - https://en.ccunesco.ca/blog/2020/3/the-international-day-of-mathematics-because-the-world-needs-math
        - https://www.splashlearn.com/math-vocabulary/geometry/geometry
        - https://math.tools/equation/image

    Flask app was built following the Flask Mega-Tutorial by Miguel Grinberg.
    
       - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
       
    
    For HTML and CSS development for the app W3 schools was used as a reference.
        
        - https://www.w3schools.com/default.asp
