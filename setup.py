#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup

from setuptools import setup, find_packages

setup(
    name='PlaYnlp',
    version='0.0.1dev',
    description='PlaY NLP Toolkits',
    author='Chia-Chi Chang & Willy Kuo',
    author_email='c3h3.tw@gmail.com & waitingkuo0527@gmail.com',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'numpy',
        'scipy',
        'jieba',
        'nltk',
        "pandas"
    ],
)
