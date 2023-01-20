from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yamager',
    version='1.0.2',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Yamager - Simple module for parsing images from Yandex and Google.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/yamager',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/yamager/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['requests', 'lxml'],
    python_requires='>=3.6'
)