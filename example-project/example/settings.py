# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

ITEM_PIPELINES = [
    'scrapy_mongodb_pipeline.pipelines.MongoDBPipeline',
]

MONGODB_FULL_OVERWRITE=False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'example (+http://www.yourdomain.com)'
