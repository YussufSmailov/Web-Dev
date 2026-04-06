# Меняй импорт чтобы переключаться между уровнями:

# Level 2 - FBV:
# from api.views.fbv import products_list, product_detail

# Level 3 - CBV:
# from api.views.cbv import ProductListAPIView, ProductDetailAPIView

# Level 4 - Mixins:
# from api.views.mixins import ProductListAPIView, ProductDetailAPIView

# Level 5 - Generics :
from api.views.generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)