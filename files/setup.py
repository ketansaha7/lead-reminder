from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="lead_reminder",
    version="0.0.1",
    description="App to add a Reminder field in Lead Doctype and send a notification when the reminder date matches the current date.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
