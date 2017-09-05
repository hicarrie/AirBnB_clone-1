# AirBnb Clone - Web Framework
Web Framework for Airbnb Clone

## Project Requirements
### Python Scripts
- Formatted with PEP8 style standards
- Compiled with `python3`
- All files must be executable
- All modules should have a documentation `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should have documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`

### HTML / CSS
- Code is W3C compliant and validates with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator)
- Not allowed to use `!important` or `id`
- All tags must be in uppercase
- No cross browsers

## Files
**0-hello_route.py:** a script that starts a Flask web application listening on 0.0.0.0:5000
Routes:
- `/` displays "Hello HBNB!"

**1-hbnb_route.py:** a script that starts a Flask web application listening on 0.0.0.0:5000

**Routes:**
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"

**2-c_route.py:** a script that starts a Flask web application listening on 0.0.0.0:5000

Routes:
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"
- `/c/<text>` displays "C" followed by `text` variable

**3-python_route.py:** a script that starts a Flask web application listening on 0.0.0.0:5000

Routes:
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"
- `/c/<text>` displays "C " followed by `text` variable
- `/python/(<text>)` displays "Python " followed by `text` variable

**4-number_route.py:** a script that starts a Flask web application listening on 0.0.0.0:5000

Routes:
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"
- `/c/<text>` displays "C " followed by `text` variable
- `/python/(<text>)` displays "Python " followed by `text` variable
- `/number/<n>` displays "`n` is a number" only if `n` is an integer

**5-number_template.py, templates/5-number.html:** a script that starts a Flask web application listening on 0.0.0.0:5000

Routes:
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"
- `/c/<text>` displays "C " followed by `text` variable
- `/python/(<text>)` displays "Python " followed by `text` variable
- `/number/<n>` displays "`n` is a number" only if `n` is an integer
- `/number_template/<n>` displays an HTML page containing `n` only if `n` is an integer

**6-number_odd_or_even.py, templates/6-number_odd_or_even.html:** a script that starts a Flask web application listening on 0.0.0.0:5000

Routes:
- `/` displays "Hello HBNB!"
- `/hbnb` displays "HBNB"
- `/c/<text>` displays "C " followed by `text` variable
- `/python/(<text>)` displays "Python " followed by `text` variable
- `/number/<n>` displays "`n` is a number" only if `n` is an integer
- `/number_template/<n>` displays an HTML page containing `n` only if `n` is an integer
- `/number_odd_or_even/<n>` displays as HTML page containing number and whether it is even or odd only if `n` is an integer

**models/engine/file_storage.py, models/engine/db_storage.py, models/state.py:** Update `FileStorage`: (`models/engine/file_storage.py`)
- Add a public method `def close(self):` : call `reload()` method for deserializing the JSON file to objects
Update `DBStorage`: (`models/engine/db_storage.py`)
- Add a public method `def close(self):` : call `remove()` method on the private session attribute (`self.__session`) tips
Update `State`: (`models/state.py`)
- If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`

**web_flask/7-states_list.py, web_flask/templates/7-states_list.html:** a script that starts a Flask web application listening on 0.0.0.0:5000 and uses storage for fetching data from the storage engine

Routes:
- `/states_list` displays an HTML page listing all `State` objects

**web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html:** a script that starts a Flask web application listening on 0.0.0.0:5000 and uses storage for fetching data from the storage engine

Routes:
- `/cities_by_states` displays an HTML page listing all `State` and `City` objects

**web_flask/9-states.py, web_flask/templates/9-states.html:** a script that starts a Flask web application listening on 0.0.0.0:5000 and uses storage for fetching data from the storage engine

Routes:
- `/states` displays an HTML page listing all `State` objects
- `/states/<id>` displays an HTML page with `State` associated with that id and `City` objects associated with that state

**web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/:** a script that starts a Flask web application listening on 0.0.0.0:5000 and uses storage for fetching data from the storage engine

Routes:
- `/hbnb_filters` displays an HTML index page from web_static project

## Authors
Carrie Ybay, <a href='https://github.com/hicarrie'>Github</a>