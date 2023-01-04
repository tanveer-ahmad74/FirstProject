from rest_framework.pagination import PageNumberPagination


class Page(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 15
