from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 10

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get(self.limit_query_param) is None:
            return None
        return super().paginate_queryset(queryset, request, view)
