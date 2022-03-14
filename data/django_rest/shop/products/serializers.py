#ls1
from rest_framework import serializers
from products.models import Product

#ls2
from products.models import Brand, Review

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

