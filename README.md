# OptiMate

Project in Medical Informatics bachelor's degree course at the University of Applied Sciences Upper Austria, Hagenberg.

## Description

Devices for perimetry measurements can be quite expensive, which poses a significant barrier to accessibility for many individuals. In this project, we aim to implement a perimetry measurement system that can be used on a mobile phone. By utilizing a VR box, users will be able to perform these tests in a more convenient and affordable manner.

We believe that by developing this mobile solution, we can significantly improve the accessibility of perimetry testing, enabling more people to monitor their visual fields regularly and detect potential issues early on.

VR Box used: TODO

## Getting Started

### Dependencies

#### Backend (Python/Django)
- **[Django](https://www.djangoproject.com/)** (v5.0.1): A high-level Python web framework.
- **[Django REST Framework](https://www.django-rest-framework.org/)** (v3.15.0): Toolkit for building Web APIs.
- **[django-cors-headers](https://pypi.org/project/django-cors-headers/)** (v4.3.1): Middleware for handling CORS requests.
- **[django-extensions](https://pypi.org/project/django-extensions/)** (v3.2.3): Extensions for Django development (e.g., shell_plus).
- **[psycopg2](https://www.psycopg.org/)** (v2.9.9): PostgreSQL adapter for Python.
- **[reportlab](https://www.reportlab.com/opensource/)** (v4.2.0): PDF generation library.
- **[requests](https://docs.python-requests.org/)** (v2.31.0): Simple HTTP library for making network requests.
- **[bcrypt](https://pypi.org/project/bcrypt/)** (v2.31.0): Modern password hashing for your software and your servers


#### Frontend (React/Node.js)
- **[Node.js](https://nodejs.org/)**: (v18.x.x) An open source server environment that runs on various platforms and uses JavaScript on the server.
- **[React](https://reactjs.org/)**: A JavaScript library for building user interfaces.
- **[axios](https://axios-http.com/)** (v1.6.8): Promise-based HTTP client for making API requests.
- **[bcryptjs](https://www.npmjs.com/package/bcryptjs)**: A JavaScrip library to automatically hash strings
- **[react-markdown](https://www.npmjs.com/package/react-markdown/v/8.0.6)**: Renders Markdown in HTML.

### Installing

* Clone the repository:
   ```bash
   git clone <repository-url>
   cd MPR4PTG2

### Executing program

1. Open a terminal in the `/backend` directory.

2. Start the server by executing:
   ```bash
   python manage.py runserver
   ```

3. Open another terminal in the `/frontend` directory.

4. Start the frontend application with:
   ```bash
   npm start
   ```

## How the Project Was Created

The project was created following the instructions from:

[How to Connect ReactJS & Django Framework](https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be)

**Note:**

In Step 2 in the instructions, make the following changes:

- Use:
  ```bash
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
  (to bypass execution policies)
  
- Then, run:
  ```bash
  npm install -g create-react-app
  ```

- Create the React app with:
  ```bash
  create-react-app myapp
  ```

Also, don't forget to run the following commands before starting the server:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Help

Ask Elisabeth

## Authors

* [@coldzeraa](https://github.com/coldzeraa)
* [@alexandradenk](https://github.com/alexandradenk)
* [@nicopointner](https://github.com/nicopointner)
* [@zintini](https://github.com/zintini)

