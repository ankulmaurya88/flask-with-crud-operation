from setuptools import setup, find_packages

setup(
    name="flask-with-crud-operation",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A Flask MVC CRUD application with integrated frontend",
    packages=find_packages(),
    include_package_data=True,  # Includes templates and static folders
    install_requires=[
        "Flask==2.3.3",
        "pytest==7.4.2"
    ],
    entry_points={
        "console_scripts": [
            "run-app=main:app.run",  # Calls app.run() from main.py
        ],
    },
)
