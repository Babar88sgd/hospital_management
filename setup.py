from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name="hospital_management",
    version=version,
    description="My custom Frappe app",
    author="Babar Mehmood",
    author_email="babar88sgd@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)

