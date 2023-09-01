from .models import CartItem


def get_or_create_cart_item(user, item, request):
    if user.is_authenticated:
        # Authenticated user
        session_key = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(
            user=user, session_key=session_key, item=item)
    else:
        # Non-authenticated user
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(
            session_key=session_key, item=item)
    return cart_item, created
