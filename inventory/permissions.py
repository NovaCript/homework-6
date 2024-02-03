from rest_framework.permissions import IsAuthenticatedOrReadOnly

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class IsProviderOrAuthenticatedOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or getattr(request.user, "type", None) == "pr"
        )


class IsConsumerOrAuthenticatedOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or getattr(request.user, "type", None) == "co"
        )
