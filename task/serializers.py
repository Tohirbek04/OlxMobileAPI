from rest_framework import serializers

from task.models import Category, Product, Valyuta, User, Status


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'location',


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'phone', 'location'


class CategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = 'name',


class ValyutaModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Valyuta
        fields = 'id', 'name'


class ProductListSerializers(serializers.ModelSerializer):
    status = StatusSerializers(read_only=True)
    valyuta = ValyutaModelSerializers(read_only=True)
    user_location = UserSerializers(read_only=True)

    class Meta:
        model = Product
        fields = 'name', 'price', 'created_at', 'image', 'valyuta', 'user_location', 'status'


class ProductRetrieveSerializers(serializers.ModelSerializer):
    category = CategoryModelSerializers(read_only=True)
    valyuta = ValyutaModelSerializers(read_only=True)
    user = UserModelSerializers(read_only=True)

    class Meta:
        model = Product
        fields = 'id', 'name', 'description', 'price', 'created_at', 'image', 'see_count', 'user', 'valyuta', 'category'


class ProductPostPutPatchSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = 'name', 'description', 'image', 'price', 'category', 'user', 'valyuta'
