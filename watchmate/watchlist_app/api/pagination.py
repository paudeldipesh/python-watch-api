from rest_framework import pagination


class WatchListPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "size"
    max_page_size = 10


class WatchListLOPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    max_limit = 10
    limit_query_param = "limit"
    offset_query_param = "start"


class WatchListCPagination(pagination.CursorPagination):
    page_size = 4
    ordering = "created"
    cursor_query_param = "record"
