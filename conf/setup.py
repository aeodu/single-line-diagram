from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("settings.py"), requires=['PyPubSub', 'openpyxl', 'Cython', 'flask', 'wmi', 'numpy',
                                                         'pypiwin32', 'FlaskApp','numpy','scipy','wx','wx.grid',
                                                          'easygui', 'cryptography', 'cryptography.fernet'])
