from distutils.core import setup
import py2exe

setup(
    console=["manage.py"],
    options={
        'py2exe': {
            'bundled_files': 1,
            'compressed': True,
        }
    },
    zipfile=None
)