from django.contrib import admin
from .models import (
    ClarityPage,
    FooterSettings,
    SmartIdeaPage,
    HomePage,
    CapabilityPage,
    CareerPage,
    FAQPage,
    FAQItem,
    FreeTrainingPage,
    FreeTrainingImage,
    FreeTrainingAfterTableImage,
    FreeTrainingTableColumn,
    FreeTrainingTableRow,
    FreeTrainingTableCell,
    ContactPage,
    ContactCard,
    ContactInformation,
    ContactFAQ,
    ContactFormSettings,
    ELMSSettings,
    ContactSubmission,
    ExpertReviewsPage,
    ExpertReview,
    ExpertReviewImage,
    EkalavyaLandingPage,
    EkalavyaLandingSection,
    EkalavyaLandingSectionVideo,
    DynamicInformationSettings,
    NoticeBoard,
    EventActivity,
)

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ["active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section 1 - Tree Diagram", {
            "fields": ("tree_diagram_image",),
            "description": "Tree diagram image for the new Section 1 of the HOME page."
        }),
        ("Section 2 - Feature Banner", {
            "fields": ("feature_banner_image",),
            "description": "Feature banner image for the new Section 2 of the HOME page."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Section 3 - AI Expert Reviews", {
            "fields": ("ai_expert_reviews_heading", "ai_expert_reviews_sub_heading", "ai_expert_reviews_button_text", "ai_expert_reviews_button_link"),
            "description": "Heading, sub heading, button text, and button link for the AI Expert Reviews section."
        }),
        ("Section 4 - Test Before You Trust", {
            "fields": ("test_before_trust_heading", "test_before_trust_subtitle", "test_before_trust_feature1", "test_before_trust_feature2", "test_before_trust_feature3", "test_before_trust_feature4", "test_before_trust_feature5", "test_before_trust_button_text", "test_before_trust_button_link"),
            "description": "Heading, subtitle, five features, button text, and button link for the Test Before You Trust section."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CapabilityPage)
class CapabilityPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section 1 - Large Title", {
            "fields": ("page_title", "page_subtitle"),
            "description": "The main large title displayed as a heading in Section 1, with an optional subtitle below it."
        }),
        ("Section 2 - Career Tree Image", {
            "fields": ("career_tree_image",),
            "description": "Career Tree image displayed in Section 2."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Section 3 - Description", {
            "fields": ("description",),
            "description": "Description content displayed in Section 3."
        }),
        ("Section 4 - Python Ecosystem Tree Image", {
            "fields": ("python_ecosystem_tree_image",),
            "description": "Python Ecosystem tree image displayed in Section 4."
        }),
        ("Section 5 - Python Ecosystem", {
            "fields": ("python_ecosystem_section_title", "python_ecosystem_section_subtitle", "python_ecosystem_highlight_line", "python_ecosystem_point_1", "python_ecosystem_point_2", "python_ecosystem_point_3"),
            "description": "Section title, subtitle, highlight line, and three points for the Python Ecosystem section."
        }),
        ("Section 6 - Python WarmUp CTA", {
            "fields": ("python_warmup_title", "python_warmup_subtitle", "python_warmup_intro_paragraph", "python_warmup_checklist_items", "python_warmup_button_text", "python_warmup_button_link"),
            "description": "Title, subtitle, intro paragraph, checklist items (one per line), button text, and button link for the Python WarmUp CTA. The button navigates to the existing Free Training page."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CareerPage)
class CareerPageAdmin(admin.ModelAdmin):
    list_display = ["active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section 1 - Title", {
            "fields": ("page_title",),
            "description": "Large title displayed in Section 1 of the CAREER page."
        }),
        ("Section 2 - Career Tree Image", {
            "fields": ("career_tree_image",),
            "description": "Career Tree image displayed immediately after the title."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Section 3 - Description", {
            "fields": ("description",),
            "description": "Premium animated interactive description card content."
        }),
        ("Section 4 - Career Path Image", {
            "fields": ("career_path_image",),
            "description": "Career Path image displayed in Section 4."
        }),
        ("Section 5 - Career Specializations", {
            "fields": ("specializations_section_title", "specializations_section_subtitle", "specialization_list", "closing_statement"),
            "description": "Section title, subtitle, specialization list (one per line), and closing statement."
        }),
        ("Section 6 - Expert Reviews CTA", {
            "fields": ("expert_reviews_title", "expert_reviews_subtitle", "expert_reviews_button_text", "expert_reviews_button_link"),
            "description": "Title, subtitle, button text, and button link for the Expert Reviews CTA. The button navigates to the existing Expert Reviews page."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ["updated_at"]
    fieldsets = (
        ("Location", {
            "fields": ("address", "google_map_embed_url", "google_map_share_url", "share_button_text")
        }),
        ("Social Media", {
            "fields": ("facebook_url", "instagram_url", "youtube_url")
        }),
        ("Student Portal", {
            "fields": ("elms_url",)
        }),
        ("Copyright", {
            "fields": ("copyright_text",)
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False





@admin.register(ClarityPage)
class ClarityPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Page Identity", {
            "fields": ("title", "subtitle", "tree_architecture_image")
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Section 1 - Image", {
            "fields": ("section1_image",),
            "description": "Image displayed in Section 1."
        }),
        ("Section 2 - Image", {
            "fields": ("section2_image",),
            "description": "Image displayed in Section 2."
        }),
        ("CTA Section", {
            "fields": ("cta_title", "cta_subtitle", "cta_description", "cta_button_text", "cta_button_link"),
            "description": "Call-to-action section content."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords")
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SmartIdeaPage)
class SmartIdeaPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Section 1 - Tree Image", {
            "fields": ("tree_image",),
            "description": "Tree Architecture image displayed below the title. If left empty, a placeholder is shown."
        }),
        ("Section 2 - SMART-50 Poster Image", {
            "fields": ("poster_image",),
            "description": "SMART-50 Poster image displayed in Section 2."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Section 3", {
            "fields": ("journey_title", "journey_button_text", "journey_button_url"),
            "description": "Journey card title, button text, and button URL for the Section 3 CTA."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


class FAQItemInline(admin.TabularInline):
    model = FAQItem
    extra = 1
    fields = ["display_order", "question", "answer", "active"]
    ordering = ["display_order", "id"]


@admin.register(FAQPage)
class FAQPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    inlines = [FAQItemInline]
    fieldsets = (
        ("Page Identity", {
            "fields": ("title", "subtitle"),
            "description": "The main heading and subtitle of the FAQs page."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ["display_order", "question", "active", "updated_at"]
    list_display_links = ["question"]
    list_filter = ["active"]
    search_fields = ["question", "answer"]
    list_editable = ["display_order", "active"]
    ordering = ["display_order", "id"]




class FreeTrainingImageInline(admin.TabularInline):
    model = FreeTrainingImage
    extra = 1
    fields = ["display_order", "image", "caption", "active"]
    ordering = ["display_order", "id"]

class FreeTrainingAfterTableImageInline(admin.TabularInline):
    model = FreeTrainingAfterTableImage
    extra = 1
    fields = ["display_order", "image", "caption", "active"]
    ordering = ["display_order", "id"]
    verbose_name = "Image After Table"
    verbose_name_plural = "Images After Table"

class FreeTrainingTableColumnInline(admin.TabularInline):
    model = FreeTrainingTableColumn
    extra = 1
    fields = ["display_order", "heading", "active"]
    ordering = ["display_order", "id"]

class FreeTrainingTableCellInline(admin.TabularInline):
    model = FreeTrainingTableCell
    extra = 1
    fields = ["column", "cell_type", "text", "button_url"]
    ordering = ["column__display_order", "id"]

@admin.register(FreeTrainingPage)
class FreeTrainingPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    inlines = [
    FreeTrainingImageInline,
    FreeTrainingTableColumnInline,
    FreeTrainingAfterTableImageInline,
    ]
    fieldsets = (
        ("Page Identity", {
            "fields": ("title", "subtitle"),
            "description": "The main heading and subtitle of the Free Training page."
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
                ("Optional Introduction", {
            "fields": ("intro_title", "intro_description"),
            "description": "Both fields are optional. Leave either field empty if it should not appear on the page.",
        }),
        ("Table Settings", {
            "fields": ("show_serial_numbers",),
            "description": "Enable or disable the automatically generated serial-number column.",
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )
    readonly_fields = ["created_at", "updated_at"]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FreeTrainingTableRow)
class FreeTrainingTableRowAdmin(admin.ModelAdmin):
    list_display = ["page", "display_order", "active"]
    list_filter = ["page", "active"]
    ordering = ["page", "display_order", "id"]
    fieldsets = (
        ("Table Row", {
            "fields": ("page", "display_order", "active"),
            "description": (
                "Create the table columns in the Free Training Page record first. "
                "Then select the same page here and add this row's cells below. "
                "For each cell, choose a column and select Text or Button."
            ),
        }),
    )
    inlines = [FreeTrainingTableCellInline]


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ["active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_title", "hero_subtitle", "hero_background_image"),
            "description": "Title, subtitle, and background image for the Contact Us hero."
        }),
        ("Final CTA Banner", {
            "fields": ("cta_title", "cta_description", "cta_button_text", "cta_button_url"),
            "description": "Large premium banner shown at the bottom of the page."
        }),
        ("Status", {
            "fields": ("active",)
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    list_display = ["display_order", "title", "icon", "active"]
    list_display_links = ["title"]
    list_filter = ["active", "icon"]
    search_fields = ["title", "description"]
    list_editable = ["display_order", "active"]
    ordering = ["display_order", "id"]


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ["updated_at"]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactFAQ)
class ContactFAQAdmin(admin.ModelAdmin):
    list_display = ["display_order", "question", "active"]
    list_display_links = ["question"]
    list_filter = ["active"]
    search_fields = ["question", "answer"]
    list_editable = ["display_order", "active"]
    ordering = ["display_order", "id"]


@admin.register(ContactFormSettings)
class ContactFormSettingsAdmin(admin.ModelAdmin):
    list_display = ["updated_at"]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ELMSSettings)
class ELMSSettingsAdmin(admin.ModelAdmin):
    list_display = ["updated_at"]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "status", "submission_date"]
    list_filter = ["status"]
    search_fields = ["name", "email", "subject", "message"]
    list_editable = ["status"]
    readonly_fields = ["name", "email", "phone", "subject", "message", "submission_date"]
    ordering = ["-submission_date"]

    def has_add_permission(self, request):
        return False



class ExpertReviewImageInline(admin.TabularInline):
    model = ExpertReviewImage
    extra = 1
    fields = ["display_order", "image", "caption", "active"]
    ordering = ["display_order", "id"]


class ExpertReviewInline(admin.TabularInline):
    model = ExpertReview
    extra = 1
    fields = [
        "display_order",
        "active",
        "module_name",
        "button_text",
    ]
    ordering = ["display_order", "id"]
    show_change_link = True


@admin.register(ExpertReviewsPage)
class ExpertReviewsPageAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "updated_at"]
    list_filter = ["active"]
    inlines = [ExpertReviewInline]

    fieldsets = (
        ("Page Identity", {
            "fields": ("title",),
        }),
        ("Background Image", {
            "fields": ("background_image",),
            "classes": ("collapse",),
        }),
        ("Introduction", {
            "fields": ("introduction_heading", "introduction"),
            "description": (
                "Optional introduction heading and content. "
                "Leave either field empty if it should not appear."
            ),
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ExpertReview)
class ExpertReviewAdmin(admin.ModelAdmin):
    list_display = [
        "display_order",
        "module_name",
        "button_text",
        "active",
        "updated_at",
    ]
    list_display_links = ["module_name"]
    list_filter = ["active"]
    search_fields = ["module_name", "button_text"]
    list_editable = ["display_order", "active"]
    ordering = ["display_order", "id"]
    inlines = [ExpertReviewImageInline]

    fieldsets = (
        ("Review Row", {
            "fields": (
                "expert_reviews_page",
                "display_order",
                "active",
                "module_name",
                "button_text",
                "cover_image",
            ),
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EkalavyaLandingPage)
class EkalavyaLandingPageAdmin(admin.ModelAdmin):
    list_display = ["active", "updated_at"]
    list_filter = ["active"]
    fieldsets = (
        ("Page Identity", {
            "fields": ("hero_image",),
            "description": "Hero image displayed on the Ekalavya landing page."
        }),
        ("SEO", {
            "fields": ("seo_title", "seo_description", "seo_keywords"),
            "classes": ("collapse",),
        }),
        ("Status", {
            "fields": ("active",),
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


class EkalavyaLandingSectionVideoInline(admin.TabularInline):
    model = EkalavyaLandingSectionVideo
    extra = 1
    fields = [
        "display_order",
        "thumbnail",
        "video_type",
        "youtube_url",
        "other_url",
        "uploaded_video",
        "active",
    ]
    ordering = ["display_order", "id"]

    class Media:
        js = ("js/admin_video_toggle.js",)


@admin.register(EkalavyaLandingSection)
class EkalavyaLandingSectionAdmin(admin.ModelAdmin):
    inlines = [EkalavyaLandingSectionVideoInline]
    list_display = ["display_order", "active", "updated_at"]
    ordering = ["display_order", "id"]
    fieldsets = (
        ("Section Content", {
            "fields": ("image",),
        }),
        ("Display", {
            "fields": ("display_order", "active"),
        }),
    )

@admin.register(DynamicInformationSettings)
class DynamicInformationSettingsAdmin(admin.ModelAdmin):
    list_display = ["main_heading", "active", "items_to_show", "updated_at"]

    fieldsets = (
        ("Main Information Zone", {
            "fields": ("main_heading", "main_image", "active", "items_to_show"),
            "description": "Controls the main Dynamic Information Zone displayed above the conventional footer."
        }),

        ("Notice Board", {
            "fields": (
                "notice_section_heading",
                "notice_section_subtitle",
                "notice_view_all_text",
                "notice_view_all_url",
            ),
            "description": "Controls the Notice Board section."
        }),

        ("Events & Activities", {
            "fields": (
                "event_section_heading",
                "event_section_subtitle",
                "event_view_all_text",
                "event_view_all_url",
            ),
            "description": "Controls the Events & Activities section."
        }),
    )

    readonly_fields = ["created_at", "updated_at"]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = [
        "display_order",
        "admin_label",
        "title",
        "active",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["admin_label"]
    list_filter = ["active"]
    search_fields = ["admin_label", "title", "description"]
    list_editable = ["display_order", "active"]
    ordering = ["display_order", "-created_at", "id"]


@admin.register(EventActivity)
class EventActivityAdmin(admin.ModelAdmin):
    list_display = [
        "display_order",
        "admin_label",
        "title",
        "event_type",
        "event_date",
        "active",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["admin_label"]
    list_filter = ["active", "event_type"]
    search_fields = ["admin_label", "title", "description", "event_type"]
    list_editable = ["display_order", "active"]
    ordering = ["-event_date", "display_order", "-created_at", "id"]