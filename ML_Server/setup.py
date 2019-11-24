from setuptools import setup

setup(
   name='elios',
   packages=['elios'],
   include_package_data=True,
   install_requires=[
      'flask',
      'flask-bcrypt',
      'firebase_admin',
      'apscheduler',
      'pandas',
      'numpy'
   ],
)
