from tastypie.resources import ModelResource
from djangoblog.models import Article
class ArticleResource(ModelResource):
	class Meta:
		queryset = Article.objects.all()
		resource_name= 'Article'
