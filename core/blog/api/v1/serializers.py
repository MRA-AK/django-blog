from rest_framework.serializers import ModelSerializer

from blog.models import Post, Category, Comment


class PostSerializer(ModelSerializer):
    """
    A serializer for Post model
    """
    class Meta:
        model = Post
        fields = ['id', 'image', 'author', 'title', 'content', 'category', 'counted_views', 'status', 'created_date', 'updated_date']
        read_only_fields = ['author', 'counted_views', 'created_date', 'updated_date']

    def create(self, validated_data):
        validated_data["author"] = self.context.get("request").user
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        # if request.parser_context.get("kwargs").get("pk"):
        #     rep["created_at"] = instance.created_date
        #     rep["updated_at"] = instance.updated_date
        rep['author'] = instance.author.username
        if rep['status']:
            rep['status'] = 'Yes'
        else:
            rep['status'] = 'No'

        return rep


class CategorySerializer(ModelSerializer):
    """
    A serializer for Category model
    """
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(ModelSerializer):
    """
    A serializer for Comment model
    """
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message', 'approved', 'created_date', 'updated_date']
        read_only_fields = ['approved', 'created_date', 'updated_date']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        rep['post'] = instance.post.title
        if rep['approved']:
            rep['approved'] = 'Yes'
        else:
            rep['approved'] = 'No'

        return rep
