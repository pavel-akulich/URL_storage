from rest_framework.pagination import PageNumberPagination


class CollectionPaginator(PageNumberPagination):
    """
    Paginator for the Collection model.

    This class is a subclass of `PageNumberPagination` and is used to paginate the `Collection` model.
    It is used to control the pagination style for the list views.

    Attributes:
        page_size (int): The default number of items to include on a page.
        page_size_query_param (str): The name of the query parameter that allows the client to set the page size
        on a per-request basis.
        max_page_size (int): The maximum allowed page size.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
