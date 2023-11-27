from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    page_size_query_param = 'limit'


class UserCursorPagination(CustomCursorPagination):
    ordering = '-date_joined'
