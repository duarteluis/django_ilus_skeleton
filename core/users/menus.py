from django.urls import reverse
from menu import Menu, MenuItem


def profile_title(request):
    """
    Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return f"Compte de {name}"


myaccount_children = (
    # this item will be shown to users who are not logged in
    MenuItem("Login", reverse('two_factor:login'), check=lambda request: not request.user.is_authenticated),

    # this will only be shown to logged in users and also demonstrates how to use
    MenuItem("Réglage MFA", reverse('two_factor:profile'), check=lambda request: request.user.is_authenticated),
    MenuItem("Changer le mot de passe", reverse('password_change'), check=lambda  request: request.user.is_authenticated),
    MenuItem("Logout", reverse('logout'), check=lambda request: request.user.is_authenticated),
    # this only shows to superusers
    MenuItem("Admin", reverse("admin:index"), separator=True, check=lambda request: request.user.is_superuser),
    # this only shows to superusers
    MenuItem("Sessions", reverse("user_sessions:session_list"), separator=False, check=lambda request: request.user.is_superuser),
)

# Add a My Account item to our user menu
Menu.add_item("user", MenuItem(profile_title, reverse("two_factor:login"), weight=10, children=myaccount_children))
