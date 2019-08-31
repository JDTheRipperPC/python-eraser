# -*- coding: utf-8 -*-

from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
    author='JD The Ripper PC',
    author_email='jdtheripperpc@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Erase files and directories',
    entry_points={
        'console_scripts': [
            'eraser = eraser.__main__:main',
        ]
    },
    license='MIT license',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='python-eraser',
    url='https://github.com/JDTheRipperPC/python-eraser',
    version='0.1.0',
    zip_safe=False,
)
