# 0x02. i18n (Internationalization)

![i-dont-always-tests-i-18-n](../memes/i-dont-always-test-i18n.jpeg)

---

### Overview

This project focuses on implementing internationalization (i18n) in a Flask application. Internationalization is the process of designing and developing software in such a way that it can be adapted to various languages and regions without engineering changes. In this tutorial, you will learn how to parametrize Flask templates to display different languages, infer the correct locale based on URL parameters, user settings, or request headers, and localize timestamps.

### Prerequisites

- Basic understanding of Python and Flask framework.
- Familiarity with HTML/CSS for template rendering.
- Basic understanding of localization and internationalization concepts.

### Installation

1. Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install Flask using pip:
   ```bash
   pip install Flask
   ```

### Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/lorens247/alx-backend/0x02-i18n.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-project
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000` to see the application in action.

### Implementation Details

#### 1. Parametrizing Flask Templates

- Templates are HTML files containing placeholders for dynamic content.
- Use Flask's templating engine to parametrize templates.
- Example:
   ```html
   <p>{{ gettext('Hello, World!') }}</p>
   ```
   
#### 2. Inferring Locale

- Determine the user's preferred language from URL parameters, user settings, or request headers.
- Set the locale accordingly using Flask-Babel or similar libraries.
- Example:
   ```python
   @app.route('/')
   def index():
       # Infer locale from URL parameter, user settings, or request headers
       locale = request.accept_languages.best_match(app.config['LANGUAGES'])
       # Set the locale
       babel.locale_selector_func = lambda: locale
       # Render template
       return render_template('index.html')
   ```

#### 3. Localizing Timestamps

- Localize timestamps to display dates and times according to the user's preferred locale.
- Use Flask-Babel to format timestamps.
- Example:
   ```python
   from flask_babel import format_datetime

   @app.route('/')
   def index():
       # Get current timestamp
       timestamp = datetime.now()
       # Localize timestamp
       localized_timestamp = format_datetime(timestamp)
       # Pass localized timestamp to template
       return render_template('index.html', timestamp=localized_timestamp)
   ```

### Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-Babel Documentation](https://pythonhosted.org/Flask-Babel/)
