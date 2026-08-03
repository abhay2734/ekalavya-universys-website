from .models import FooterSettings
from .navigation import NAVIGATION_ITEMS


def site_settings(request):
    footer_settings = FooterSettings.objects.first()

    return {
        "footer_settings": footer_settings,
        "navigation_items": NAVIGATION_ITEMS,
    }
