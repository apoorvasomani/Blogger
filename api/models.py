import uuid

from django.db import models


class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(blank=True, default='', editable=False)
	hash_value = models.UUIDField(default=uuid.uuid4, editable=False) 
	commented_body = models.JSONField(default=dict, blank=True, null=True)

	class Meta:
		ordering = ['created']

	def save(self, *args, **kwargs):
		self.body = ''.join(self.commented_body.keys())
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	body = models.TextField(blank=True, default='')
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	hash_value = models.UUIDField(default=uuid.uuid4, editable=False)

	class Meta:
		ordering = ['created']