#ls1
from rest_framework import serializers
from products.models import Product

#ls2
from products.models import Brand, Review

#ls4
from rest_framework.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'id name'.split()

#ls1
class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    # reviews = ReviewSerializer(many=True) #автоматический вывод всех данных
    reviews = serializers.SerializerMethodField()
    # reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields = '__all__'
        fields = 'id title price brand reviews reviews_count rating'.split()

    def get_reviews(self, product):
        # filtered_reviews = Review.objects.filter(product=product, stars__gte=4) #кастомная фильтрация - способ 1
        # filtered_reviews = product.reviews.filter(stars__gte=4) #кастомная фильтрация - способ 2
        # return ReviewSerializer(filtered_reviews, many=True).data
        return ReviewSerializer(product.filtered_reviews, many=True).data

    # def get_reviews_count(self, product):
    #     return product.reviews.filter(stars__gte=4).count()

#ls4
class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    weight = serializers.FloatField(required=True)
    price = serializers.IntegerField()
    is_stock = serializers.BooleanField(required=False, default=True)
    valid_until = serializers.DateField()
    brand_id = serializers.IntegerField()
    # list_ = serializers.ListField(child=serializers.CharField())
    # dict_ = serializers.DictField(child=None)
    # dict_ = ReviewSerializer()
    reviews = serializers.ListField(child=ReviewSerializer())

    # def validate_brand_id(self, brand_id): #10
    #     try:
    #         Brand.objects.get(id=brand_id)
    #     except Brand.DoesNotExist:
    #         raise ValidationError('Brand does not exists')

    def validate(self, attrs):
        try:
            Brand.objects.get(id=attrs['brand_id'])
        except Brand.DoesNotExist:
            raise ValidationError(f'Brand with id {attrs["brand id"]}does not exists')
        return attrs