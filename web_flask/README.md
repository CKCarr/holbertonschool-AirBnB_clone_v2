# AirBnB clone - Web framework

## Learning Objectives
### General

<details>
<summary>What is a Web Framework?</summary>
A web framework is a software framework that provides a structure and set of tools for developing web applications. It helps streamline the development process by offering predefined patterns, libraries, and utilities for handling common web development tasks such as routing, handling requests and responses, accessing databases, and managing sessions.
</details>
<details>
<summary>How to build a web framework with Flask</summary>
To build a web framework with Flask, you need to follow these steps:
Install Flask: Use pip (Python package manager) to install Flask on your machine.
Create a Flask application: Create a Python file and import the Flask module. Create an instance of the Flask class and define your application's routes and functionality.
Define routes: Use the @app.route() decorator to define routes in Flask. Routes are URL patterns that map to specific functions in your application.
Run the application: Use the app.run() method to start the Flask development server and run your web application.
</details>
<details>
<summary>How to define routes in Flask</summary>
In Flask, routes are defined using the `@app.route()` decorator. This decorator binds a URL pattern to a specific function in your application. For example:
    python
    
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return 'Hello, World!'
    
    @app.route('/about')
    def about():
        return 'About page'
    
    if __name__ == '__main__':
        app.run()
In this example, the home page is bound to the root URL '/', and the home() function is called when a user visits that URL. The about page is bound to the URL '/about', and the about() function is called for that route.

</details>
<details>
<summary>What is a route?</summary>
In web development, a route is a URL pattern that corresponds to a specific functionality or resource in a web application. It defines how the server should respond to a client's request for a particular URL. Routes typically map to specific functions or handlers that generate the appropriate response for that URL.
</details>
<details>
<summary>How to handle variables in a route</summary>
In Flask, you can handle variables in a route by specifying them within the route's URL pattern. For example:
      
    python
    
    @app.route('/user/<username>')
    def user_profile(username):
        return f'Profile page of {username}'
In this example, the route /user/<username> captures any value in the URL after /user/ and passes it as a variable (username) to the user_profile() function. You can then use this variable within the function to customize the response based on the captured value.

</details>
<details>
<summary>What is a template?</summary>
In web development, a template is a file that contains the structure and layout of a web page. It separates the presentation logic (HTML, CSS) from the application logic. Templates often include placeholders or variables that can be dynamically filled with data from the application before rendering.
</details>
<details>
<summary>How to create an HTML response in Flask by using a template</summary>
To create an HTML response in Flask using a template, you can use a template engine such as Jinja2, which is built into Flask. Here's an example:
  
    python
    
    from flask import Flask, render_template
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        name = 'John'
        return render_template('index.html', name=name)
    
    if __name__ == '__main__':
        app.run()
In this example, the render_template() function is used to render an HTML template named index.html. The template file can include HTML, CSS, and placeholders ({{ }}) for dynamic content. The name variable is passed to the template and can be accessed within the template using the placeholder {{ name }}.

</details>
<details>
<summary>How to create a dynamic template (loops, conditions…)</summary>
To create a dynamic template with loops, conditions, and other control structures, you can use the template engine's syntax. In Flask's template engine (Jinja2), you can use constructs like loops and conditions. For example:
  
    html
    
    <ul>
      {% for item in items %}
        <li>{{ item }}</li>
      {% endfor %}
    </ul>
    
    {% if condition %}
      <p>This is true</p>
    {% else %}
      <p>This is false</p>
    {% endif %}
You can combine loops and conditions to create more complex templates.

</details>
<details>
<summary>How to display data from a MySQL database</summary>
To display data from a MySQL database in HTML with Flask, you need to follow these steps:
Connect to the MySQL database using a suitable library like mysql-connector-python.
Execute SQL queries to fetch the desired data from the database.
Pass the fetched data to the template for rendering.
Here's an example:

    python
    
    from flask import Flask, render_template
    import mysql.connector
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='username',
            password='password',
            database='database_name'
        )

    # Execute SQL query to fetch data
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # Close database connection
    cursor.close()
    connection.close()

    return render_template('index.html', users=users)

    if __name__ == '__main__':
        app.run()
In this example, we connect to a MySQL database, execute a query to fetch user data from the users table, and pass the fetched data (users) to the template for rendering.

</details>
