scrapy-mongodb-pipeline
=======================

MongoDB pipeline for Scrapy. It allows to update existing entries (set new values or add elements to array) when item values are spread over multiple pages

Each item must have a field "id".
Items can optionally have a static class attribute MONGODB_COLLECTION that will be used as the name of the collection when the item is persisted to MongoDB

Settings:
* MONGODB_SERVER: host of the mongodb server (default: localhost)
* MONGODB_PORT: port of the mongodb server (default: 27017)
* MONGODB_DB: database to use in mongodb (default: scrapy)
* MONGODB_COLLECTION: collection to use in mongodb (default: name of the spider). It can also be overwritten in the item class with a static attribute (MONGODB_COLLECTION)
* MONGODB_OVERWRITE: overwrite the old value (default: False). If set to false, it will update the existing value with the new fields. 
* MONGODB_CONCAT_ARRAYS: if MONGODB_OVERWRITE is set to False, it will update array attributes by concatenating the original array with the new array
