from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from django.db.models import Prefetch
from .models import ClarityPage, SmartIdeaPage, HomePage, CapabilityPage, CareerPage, FAQPage, FAQItem, FreeTrainingPage, FreeTrainingVideo, FreeEBook, ContactPage, ContactCard, ContactInformation, ContactFAQ, ContactFormSettings, ELMSSettings, ContactSubmission, ExpertReviewsPage, ExpertReview, ExpertReviewImage, EkalavyaLandingPage, EkalavyaLandingSection
from .navigation import PLACEHOLDER_PAGES


import logging
import re
import hashlib
import time


logger = logging.getLogger(__name__)


def _extract_youtube_id(url):
    if not url:
        return None
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/shorts\/|m\.youtube\.com\/watch\?v=|youtube\.com\/v\/)([^&\s?#]+)',
        r'youtube\.com\/watch\?.*[?&]v=([^&\s?#]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def landing_page(request):
    landing_page_obj = EkalavyaLandingPage.objects.filter(active=True).first()

    sections = []
    for s in EkalavyaLandingSection.objects.filter(active=True).order_by("display_order", "id"):
        embed_url = None
        if s.video_type == "youtube" and s.youtube_url:
            vid_id = _extract_youtube_id(s.youtube_url)
            if vid_id:
                embed_url = f"https://www.youtube.com/embed/{vid_id}"
        sections.append({"section": s, "youtube_embed_url": embed_url})

    context = {
        "landing_page": landing_page_obj,
        "landing_sections": sections,
    }

    return render(request, "ekalavya_universys_home.html", context)


def home(request):
    page = HomePage.load()

    context = {
        "page": page,
        "seo_title": page.seo_title if page else "Welcome to Ekalavya Universys | Ekalavya Universys",
        "seo_description": page.seo_description if page else "",
        "seo_keywords": page.seo_keywords if page else "",
    }

    return render(request, "new_home.html", context)


def free_training(request):
    page = FreeTrainingPage.load()

    videos = FreeTrainingVideo.objects.filter(active=True).order_by("display_order", "id")

    ebooks = FreeEBook.objects.filter(active=True).order_by("display_order", "id")

    context = {
        "page": page,
        "videos": videos,
        "ebooks": ebooks,
    }

    return render(request, "free_training_page.html", context)


def clarity_page(request):
    page = ClarityPage.objects.filter(active=True).first()

    if not page:
        return render(request, "clarity_page.html", {"page": None})

    context = {
        "page": page,
        "seo_title": page.seo_title or "CLARITY | Ekalavya Universys",
        "seo_description": page.seo_description or "",
        "seo_keywords": page.seo_keywords or "",
    }

    return render(request, "clarity_page.html", context)


def placeholder_page(request, slug):
    page = PLACEHOLDER_PAGES.get(slug)

    if not page:
        raise Http404

    return render(request, "placeholder_page.html", {"page": page})


def smart_idea_page(request):
    page = SmartIdeaPage.objects.filter(active=True).first()

    context = {
        "page": page,
    }

    return render(request, "smart_idea_page.html", context)


def expert_reviews(request):
    page = ExpertReviewsPage.load()

    reviews = ExpertReview.objects.filter(active=True).prefetch_related(
        Prefetch(
            "additional_images",
            queryset=ExpertReviewImage.objects.filter(active=True).order_by("display_order", "id"),
        )
    ).order_by("display_order", "id")

    context = {
        "page": page,
        "reviews": reviews,
        "seo_title": page.seo_title or "Expert Reviews | Ekalavya Universys",
        "seo_description": page.seo_description or "",
        "seo_keywords": page.seo_keywords or "",
    }

    return render(request, "expert_reviews_page.html", context)


def capability_page(request):
    page = CapabilityPage.load()

    context = {
        "page": page,
        "seo_title": page.seo_title if page else "CAPABILITY | Ekalavya Universys",
        "seo_description": page.seo_description if page else "",
        "seo_keywords": page.seo_keywords if page else "",
    }

    return render(request, "capability_page.html", context)


def career_page(request):
    page = CareerPage.load()

    context = {
        "page": page,
        "seo_title": page.seo_title if page else "Choose the Right Branch | Ekalavya Universys",
        "seo_description": page.seo_description if page else "",
        "seo_keywords": page.seo_keywords if page else "",
    }

    return render(request, "career_page.html", context)


def faqs_page(request):
    page = FAQPage.load()

    if not page or not page.active:
        return render(request, "faqs_page.html", {"page": None})

    faq_items = page.faq_items.filter(active=True).order_by("display_order", "id")

    context = {
        "page": page,
        "faq_items": faq_items,
        "seo_title": page.seo_title or "FAQs | Ekalavya Universys",
        "seo_description": page.seo_description or "",
        "seo_keywords": page.seo_keywords or "",
    }

    return render(request, "faqs_page.html", context)


class ContactSubmissionForm:
    """Lightweight server-side validator for the Contact Us form.

    Kept scoped to the Contact page; mirrors client-side validation so that
    submitted data is always validated even if JS is disabled or bypassed.
    """

    MAX_MESSAGE = 2000

    FIELDS = ["full_name", "email", "phone", "subject", "message"]

    @classmethod
    def validate(cls, data):
        errors = {}

        full_name = (data.get("full_name") or "").strip()
        if not full_name:
            errors["full_name"] = "Please enter your full name."
        elif len(full_name) > 200:
            errors["full_name"] = "Name is too long."

        email = (data.get("email") or "").strip()
        if not email:
            errors["email"] = "Please enter your email address."
        elif "@" not in email or "." not in email or len(email) > 254:
            errors["email"] = "Please enter a valid email address."

        phone = (data.get("phone") or "").strip()
        if phone:
            cleaned = "".join(ch for ch in phone if ch.isdigit() or ch in "+-() ")
            if len(cleaned) > 50:
                errors["phone"] = "Phone number is too long."

        subject = (data.get("subject") or "").strip()
        if not subject:
            errors["subject"] = "Please enter a subject."
        elif len(subject) > 200:
            errors["subject"] = "Subject is too long."

        message = (data.get("message") or "").strip()
        if not message:
            errors["message"] = "Please enter your message."
        elif len(message) > cls.MAX_MESSAGE:
            errors["message"] = f"Message must be {cls.MAX_MESSAGE} characters or fewer."

        return errors


def contact_us(request):
    contact_page = ContactPage.load()
    contact_info = ContactInformation.load()
    form_settings = ContactFormSettings.load()
    elms_settings = ELMSSettings.load()

    help_cards = ContactCard.objects.filter(active=True).order_by("display_order", "id")
    contact_faqs = ContactFAQ.objects.filter(active=True).order_by("display_order", "id")[:5]

    context = {
        "contact_page": contact_page,
        "contact_info": contact_info,
        "form_settings": form_settings,
        "elms_settings": elms_settings,
        "help_cards": help_cards,
        "contact_faqs": contact_faqs,
    }

    if request.method == "POST":
        data = request.POST

        # Honeypot anti-spam field must stay empty
        if (data.get("company_website") or "").strip():
            return JsonResponse({"ok": True}, status=200)

        # --- Abuse protection ---
        client_ip = request.META.get("REMOTE_ADDR", "")
        now = time.time()

        # Flood protection: minimum 5 seconds between submissions
        flood_key = f"contact_flood_{client_ip}"
        last_post = cache.get(flood_key)
        if last_post is not None and (now - last_post) < 5:
            return JsonResponse({"ok": False, "errors": {"__all__": "Please wait before submitting again."}}, status=400)
        cache.set(flood_key, now, 60)

        # Rate limiting: max 10 requests per 60 seconds per IP
        rate_key = f"contact_rate_{client_ip}"
        request_count = cache.get(rate_key, 0)
        if request_count >= 10:
            return JsonResponse({"ok": False, "errors": {"__all__": "Too many requests. Please try again later."}}, status=400)
        cache.set(rate_key, request_count + 1, 60)

        # Duplicate submission protection: same form data within 60 seconds per IP
        form_data = "|".join([
            (data.get("full_name") or "").strip(),
            (data.get("email") or "").strip(),
            (data.get("phone") or "").strip(),
            (data.get("subject") or "").strip(),
            (data.get("message") or "").strip(),
        ])
        form_hash = hashlib.sha256(form_data.encode()).hexdigest()
        dup_key = f"contact_dup_{client_ip}_{form_hash}"
        if cache.get(dup_key):
            return JsonResponse({"ok": False, "errors": {"__all__": "This form was already submitted recently."}}, status=400)
        cache.set(dup_key, True, 60)
        # --- End abuse protection ---

        errors = ContactSubmissionForm.validate(data)

        if errors:
            return JsonResponse({"ok": False, "errors": errors}, status=400)

        ContactSubmission.objects.create(
            name=(data.get("full_name") or "").strip(),
            email=(data.get("email") or "").strip(),
            phone=(data.get("phone") or "").strip(),
            subject=(data.get("subject") or "").strip(),
            message=(data.get("message") or "").strip(),
        )

        if form_settings.enable_email_notification and form_settings.admin_email:
            try:
                send_mail(
                    subject=f"[Contact] {data.get('subject', '')}",
                    message=(
                        f"Name: {data.get('full_name', '')}\n"
                        f"Email: {data.get('email', '')}\n"
                        f"Phone: {data.get('phone', '')}\n\n"
                        f"{data.get('message', '')}"
                    ),
                    from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@ekalavyauniversys.com"),
                    recipient_list=[form_settings.admin_email],
                )
            except Exception as exc:
                logger.error("Failed to send contact email: %s", exc)

        return JsonResponse({"ok": True}, status=200)

    return render(request, "contact_us_page.html", context)

