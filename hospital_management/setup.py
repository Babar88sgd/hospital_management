from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# Read version from your_app/__init__.py or version.py
version = "0.0.1"
from hospital_management import __version__ as version

setup(
    name="hospital_management",  # اپنی ایپ کا درست نام دیں
    version=version,
    description="My custom Frappe app",
    author="Babar Mehmood",
    author_email="babar88sgd@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
