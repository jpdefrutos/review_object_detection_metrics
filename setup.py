from setuptools import find_packages, setup
import os

scripts = ['scripts/rodm']
entry_points = {'gui_scripts': ['rodm=rodm.main:main']}

if os.name == 'nt':
    scripts.append('scripts/rodm.bat')
    entry_points.update({'console_scripts': ['rodm=rodm.main:main']})

setup(
    name='rodm',
    packages=find_packages(include=['rodm', 'rodm.*']),
    version='0.1.0',
    description='Object Detection Metrics Open-source Toolkit',
    author='Rafael Padilla',
    license='MIT',
    install_requires=[
        'matplotlib',
        'numpy>=1.19',
        'opencv-python>=4.5',
        'pandas>=1.1',
        'PySide2',
        'pytest>=6.1',
        'awscli>=1.18.180',
        'chardet>=3.0.4',
        'click>=7.1.2',
        'flake8>=3.8.4',
        'python-dotenv>=0.15.0',
        'pyyaml>=5.3.1',
        'sphinx>=3.3.1'
        ],
    # scripts=['scripts/rodm'],
    entry_points=entry_points,
)
