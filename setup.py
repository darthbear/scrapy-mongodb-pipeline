from setuptools import setup

setup(
    name='scrapy-mongodb-pipeline',
    version='0.1.0',
    description='Scrapy pipeline to persist items to MongoDB',
    keywords='scrapy mongo mongodb pipeline',
    license='New BSD License',
    author="Francois Dang Ngoc",
    author_email='francois.dangngoc@gmail.com',
    url='http://github.com/darthbear/scrapy-mongodb-pipeline/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    packages=[
        'scrapy_mongodb_pipeline',
    ],
    install_requires=[
        'pymongo',
    ],
)
