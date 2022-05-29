import datetime
from django.db import models
from django.utils.translation import gettext as _
from userAuth.models import User
from common.base_model import BaseModel


class Post(BaseModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PostLikes(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
