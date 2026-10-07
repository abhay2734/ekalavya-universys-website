from .models import (
    FooterSettings,
    DynamicInformationSettings,
    NoticeBoard,
    EventActivity,
)
from .navigation import NAVIGATION_ITEMS


def site_settings(request):
    footer_settings = FooterSettings.objects.first()
    dynamic_information_settings = DynamicInformationSettings.objects.first()

    items_to_show = 3

    if dynamic_information_settings:
        items_to_show = dynamic_information_settings.items_to_show

    notice_board_items = NoticeBoard.objects.filter(
        active=True
    ).order_by(
        "display_order",
        "-created_at",
        "id",
    )

    event_activity_items = EventActivity.objects.filter(
       active=True
    ).order_by(
        "display_order",
        "-created_at",
        "id",
)

    return {
        "footer_settings": footer_settings,
        "navigation_items": NAVIGATION_ITEMS,
        "dynamic_information_settings": dynamic_information_settings,
        "notice_board_items": notice_board_items,
        "event_activity_items": event_activity_items,
    }
