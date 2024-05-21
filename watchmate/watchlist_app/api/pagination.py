from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = "p"
    page_size_query_param = "size"
    max_page_size = 10
    # last_page_strings = "end"


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10
    limit_query_param = "limit"
    offset_query_param = "start"
