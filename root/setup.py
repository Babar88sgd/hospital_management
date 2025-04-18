from setuptools import setup, find_packages

setup(
    name='hospital_management',
    version='0.0.1',
    description='Hospital Management System for ERPNext',
    author='Babar Mehmood',
    author_email='babar88sgd@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
