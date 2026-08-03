from django import template

register = template.Library()

STAGE_ORDER = ["roots", "clarity", "smart", "python", "career", "success"]


@register.filter
def stage_state(key, active):
    """Return the status of a learning journey stage relative to the active stage.

    Returns one of: 'active', 'completed', or 'upcoming'.
    """
    try:
        key_index = STAGE_ORDER.index(key)
        active_index = STAGE_ORDER.index(active)
    except (ValueError, TypeError):
        return "upcoming"

    if key_index == active_index:
        return "active"
    if key_index < active_index:
        return "completed"
    return "upcoming"
