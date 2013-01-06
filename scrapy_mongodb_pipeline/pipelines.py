import pymongo

class MongoDBPipeline(object):
    def __init__(self, mongodb_server, mongodb_port, mongodb_db, mongodb_collection, mongodb_full_overwrite, mongodb_concat_arrays):
	self.mongodb_server = mongodb_server
	self.mongodb_port = mongodb_port
	self.mongodb_db = mongodb_db
	self.mongodb_collection = mongodb_collection
	self.mongodb_full_overwrite = mongodb_full_overwrite
	self.mongodb_concat_arrays = mongodb_concat_arrays

    @classmethod
    def from_crawler(cls, crawler):
	settings = crawler.settings
	mongodb_server = settings.get('MONGODB_SERVER', 'localhost')
	mongodb_port = settings.get('MONGODB_PORT', 27017)
	mongodb_db = settings.get('MONGODB_DB', 'scrapy')
	mongodb_collection = settings.get('MONGODB_COLLECTION', None)
	mongodb_full_overwrite = settings.get('MONGODB_FULL_OVERWRITE', 'True') in ['true', 'True', 'TRUE', '1']
	mongodb_concat_arrays = settings.get('MONGODB_CONCAT_ARRAYS', 'False') in ['true', 'True', 'TRUE', '1']

	return cls(mongodb_server, mongodb_port, mongodb_db, mongodb_collection, mongodb_full_overwrite, mongodb_concat_arrays)

    def open_spider(self, spider):
	self.spider = spider	
	if self.mongodb_collection is None:
	    self.mongodb_collection = "%s_items"%spider.name

	connection = pymongo.Connection(self.mongodb_server, self.mongodb_port)
	self.db = connection[self.mongodb_db]

    def process_item(self, item, spider):
	# create a dict based on field different from None	

	if hasattr(item, 'MONGODB_COLLECTION'):
		name = item.MONGODB_COLLECTION
	else:
		name = self.mongodb_collection

	collection = self.db[name]
	if self.mongodb_full_overwrite:
	    item_values = {}
	    for key, value in item.iteritems():
	        if key != 'id' and value != None:
		    item_values[key] = value
	    item_values['_id'] = item['id']
	    collection.update({'_id': item['id']}, item_values, True)

	else:
	    item_set_values = {}
	    item_push_values = {}
	    for key, value in item.iteritems():
	        if key != 'id' and value != None:
		    if self.mongodb_concat_arrays and isinstance(value, (list, tuple)):
			if len(value) > 0:
		            item_push_values[key] = value
		    else:	
		        item_set_values[key] = value
	    updates = {}
	    if len(item_set_values) > 0:
		updates['$set'] = item_set_values

	    if len(item_push_values) > 0:
		updates['$pushAll'] = item_push_values

	    collection.update(
		{
	            '_id': item['id']
	        }, updates,
	        True)
	return item
		
	
