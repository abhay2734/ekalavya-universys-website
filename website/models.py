from django.core.exceptions import ValidationError
from django.db import models


class ClarityPage(models.Model):
    """Single record for the CLARITY page content - like site settings"""

    title = models.CharField(
        max_length=200,
        default="CLARITY",
        help_text="Page title"
    )

    subtitle = models.CharField(
        max_length=200,
        default="Understand Before You Speak",
        help_text="Page subtitle"
    )

    tree_architecture_image = models.ImageField(
        upload_to="clarity/",
        blank=True,
        null=True,
        help_text="Tree Architecture image displayed below the title and subtitle"
    )

    # Section 1 - Every Great Career Begins with Understanding
    section1_heading = models.CharField(
        max_length=200,
        default="Every Great Career Begins with Understanding",
        help_text="Heading for the first content section"
    )
    section1_intro = models.TextField(
        blank=True,
        default="Many students begin learning technology by memorizing programming syntax, commands, or definitions. However, true learning begins much earlier. It begins with understanding.",
        help_text="Introductory paragraph for the first section"
    )
    section1_prompt = models.TextField(
        blank=True,
        default="Before writing your first program, you should understand:",
        help_text="Prompt sentence shown before the understanding checklist"
    )
    section1_checklist = models.TextField(
        blank=True,
        default="What is AI?\nWhat is Data Science?\nWhat is Programming?\nWhat is Software Development?\nWhat is Cloud Computing?\nWhy are databases required?\nHow do modern technologies work together?",
        help_text="Understanding checklist - one item per line"
    )
    section1_outro = models.TextField(
        blank=True,
        default="When concepts are clear, learning becomes faster, communication becomes easier, and confidence grows naturally.",
        help_text="Closing paragraph for the first section"
    )

    # Section 2 - Why CLARITY-50?
    section2_heading = models.CharField(
        max_length=200,
        default="Why CLARITY-50?",
        help_text="Heading for the second content section"
    )
    section2_para1 = models.TextField(
        blank=True,
        default="The CLARITY-50 Series is the foundation of the Ekalavya Learning System. It develops the conceptual understanding required before learning any technology.",
        help_text="First paragraph for the Why CLARITY-50 section"
    )
    section2_para2 = models.TextField(
        blank=True,
        default="Instead of memorizing technical words, you learn to understand, connect, and explain them confidently.",
        help_text="Second paragraph for the Why CLARITY-50 section"
    )
    section2_para3 = models.TextField(
        blank=True,
        default="Our objective is simple:",
        help_text="Lead-in sentence before the emphasis line"
    )
    section2_emphasis = models.TextField(
        blank=True,
        default="Understand first. Implement next.",
        help_text="Emphasised statement for the Why CLARITY-50 section"
    )

    # Section 3 - What You Build
    section3_heading = models.CharField(
        max_length=200,
        default="What You Build",
        help_text="Heading for the What You Build section"
    )
    section3_checklist = models.TextField(
        blank=True,
        default="Conceptual Understanding\nTechnical Communication Skills\nAbility to Explain Concepts\nAI Ecosystem Awareness\nIndustry Terminology\nConfidence & Clarity\nThink Real. Code Clear.",
        help_text="What You Build checklist - one item per line"
    )

    # Section 4 - Why It Matters
    section4_heading = models.CharField(
        max_length=200,
        default="Why It Matters",
        help_text="Heading for the Why It Matters section"
    )
    section4_para1 = models.TextField(
        blank=True,
        default="Imagine constructing a building. No engineer begins with the first floor. The foundation is built first.",
        help_text="First paragraph for the Why It Matters section"
    )
    section4_para2 = models.TextField(
        blank=True,
        default="Similarly, every successful software professional begins with a strong conceptual foundation. The stronger the understanding, the easier it becomes to learn programming, solve problems, and master advanced technologies.",
        help_text="Second paragraph for the Why It Matters section"
    )

    # Section 5 - The Outcome
    section5_heading = models.CharField(
        max_length=200,
        default="The Outcome",
        help_text="Heading for the The Outcome section"
    )
    section5_intro = models.TextField(
        blank=True,
        default="After completing CLARITY-50, you will be able to:",
        help_text="Introductory sentence before the outcome checklist"
    )
    section5_checklist = models.TextField(
        blank=True,
        default="Understand modern technology concepts\nExplain them confidently\nCommunicate effectively during interviews\nLearn new technologies faster\nBuild a strong foundation for lifelong learning",
        help_text="Outcome checklist - one item per line"
    )

    # Section 6 - The Next Step
    section6_heading = models.CharField(
        max_length=200,
        default="The Next Step",
        help_text="Heading for the The Next Step section"
    )
    section6_para1 = models.TextField(
        blank=True,
        default="Understanding alone is not enough. Once concepts become clear, the next stage is developing the right learning habits, professional discipline, and growth mindset.",
        help_text="First paragraph for the The Next Step section"
    )
    section6_para2 = models.TextField(
        blank=True,
        default="That is the purpose of our next learning system: SMART-50",
        help_text="Second paragraph for the The Next Step section"
    )
    section6_emphasis = models.TextField(
        blank=True,
        default="Build the Right Mindset Before Building Technology Capability.",
        help_text="Emphasised statement for the The Next Step section"
    )

    background_image = models.ImageField(
        upload_to="clarity/",
        blank=True,
        null=True,
        help_text="Background image for the page"
    )

    section1_image = models.ImageField(
        upload_to="clarity/",
        blank=True,
        null=True,
        help_text="Image displayed in Section 1"
    )

    section2_image = models.ImageField(
        upload_to="clarity/",
        blank=True,
        null=True,
        help_text="Image displayed in Section 2"
    )

    cta_title = models.CharField(
        max_length=200,
        blank=True,
        default="🟢 Test Before You Trust",
        help_text="CTA section title"
    )

    cta_subtitle = models.CharField(
        max_length=200,
        blank=True,
        default="🎯 Experience CLARITY Before You Enroll",
        help_text="CTA section subtitle"
    )

    cta_description = models.TextField(
        blank=True,
        default="The best way to evaluate any learning system is to experience it yourself.\n\nTake our FREE 3-Concept Challenge and discover how Ekalavya transforms understanding into confident explanation.",
        help_text="CTA section description"
    )

    cta_button_text = models.CharField(
        max_length=200,
        blank=True,
        default="Launch the FREE 3-Concept Challenge →",
        help_text="CTA button text"
    )

    cta_button_link = models.CharField(
        max_length=500,
        blank=True,
        help_text="CTA button link URL (defaults to the FREE TRAINING page)"
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CLARITY"
        verbose_name_plural = "CLARITY"

    def __str__(self):
        return self.title

    def get_section1_checklist(self):
        return [line.strip() for line in (self.section1_checklist or "").split("\n") if line.strip()]

    def get_section3_checklist(self):
        return [line.strip() for line in (self.section3_checklist or "").split("\n") if line.strip()]

    def get_section5_checklist(self):
        return [line.strip() for line in (self.section5_checklist or "").split("\n") if line.strip()]


SMART_INTRODUCTION = """Knowledge Alone Is Not Enough.

Every year, thousands of students complete courses, watch hundreds of videos and collect certificates.

Yet many struggle to build lasting skills.

Why?

Because success depends not only on what you learn, but also on how you learn.

That is why we created SMART-50."""

SMART_WHY = """The SMART-50 Series develops the habits, attitudes, and learning strategies that transform knowledge into real capability.

Instead of simply telling students to "work hard", SMART-50 teaches them how to work smart.

It helps learners become more disciplined, more consistent, and more effective throughout their learning journey."""

SMART_WHAT_YOU_BUILD = """Smart Learning Habits
Self-Motivation
Review & Reflection
Consistency
Problem-Solving Mindset
Learning by Teaching
Project Thinking
Domain Understanding
Continuous Improvement
Career-Oriented Thinking"""

SMART_WHY_IT_MATTERS = """Imagine two students.

Both study the same technology.

Both use the same books.

Both watch the same videos.

One steadily improves every week.

The other gives up after a few months.

The difference is rarely intelligence.

The difference is mindset, discipline, and learning habits.

SMART-50 helps you build those habits."""

SMART_HIDDEN_SECRET = """Knowledge answers "What should I know?"

SMART-50 answers "How should I learn?"

When these two work together, learning becomes faster, deeper, and more enjoyable."""

SMART_OUTCOME = """Better Learning Discipline
Greater Confidence
Professional Thinking
Continuous Growth
Lifelong Learning Skills"""

SMART_NEXT_STEP = """A strong mindset prepares you to build strong technical capability.

The next stage of your journey is PYTHON-50 - Build Your Technology Capability."""

SMART_FINAL_QUOTE = """Knowledge tells you what to do.

Mindset determines whether you will actually do it."""


class SmartIdeaPage(models.Model):
    """Single record for the SMART-50 page content - singleton model"""

    title = models.CharField(
        max_length=200,
        default="SMART-50",
        help_text="Main page title"
    )

    subtitle_1 = models.CharField(
        max_length=200,
        default="Build the Right Mindset",
        help_text="First subtitle displayed below the title"
    )

    subtitle_2 = models.CharField(
        max_length=200,
        default="Transform Knowledge into Capability",
        help_text="Second subtitle displayed below the title"
    )

    tree_image = models.ImageField(
        upload_to="smart_idea/tree/",
        blank=True,
        null=True,
        help_text="Tree Architecture image displayed below the title. Editable from the admin; a placeholder is shown if none is uploaded."
    )

    poster_image = models.ImageField(
        upload_to="smart_idea/poster/",
        blank=True,
        null=True,
        help_text="SMART-50 Poster image displayed in Section 2."
    )

    background_image = models.ImageField(
        upload_to="smart_idea/",
        blank=True,
        null=True,
        help_text="Background image for the SMART-50 page."
    )

    journey_title = models.CharField(
        max_length=200,
        default="Continue Your Journey",
        help_text="Title for the journey card in Section 3"
    )

    journey_button_text = models.CharField(
        max_length=200,
        default="Explore SMART-50 – Build the Right Mindset for IT Success",
        help_text="Button text for the journey card CTA"
    )

    journey_button_url = models.CharField(
        max_length=500,
        blank=True,
        default="",
        help_text="Button URL for the journey card CTA. Defaults to the FREE TRAINING page if left empty."
    )

    introduction_heading = models.CharField(
        max_length=200,
        default="Introduction",
        help_text="Heading for the Introduction section"
    )
    introduction = models.TextField(
        blank=True,
        default=SMART_INTRODUCTION,
        help_text="Introduction section content"
    )

    why_smart_50_heading = models.CharField(
        max_length=200,
        default="Why SMART-50",
        help_text="Heading for the Why SMART-50 section"
    )
    why_smart_50 = models.TextField(
        blank=True,
        default=SMART_WHY,
        help_text="WHY SMART-50 section content"
    )

    what_you_build_heading = models.CharField(
        max_length=200,
        default="What You Build",
        help_text="Heading for the What You Build section"
    )
    what_you_build = models.TextField(
        blank=True,
        default=SMART_WHAT_YOU_BUILD,
        help_text="WHAT YOU BUILD checklist - one item per line, rendered as premium checklist cards"
    )

    why_it_matters_heading = models.CharField(
        max_length=200,
        default="Why It Matters",
        help_text="Heading for the Why It Matters section"
    )
    why_it_matters = models.TextField(
        blank=True,
        default=SMART_WHY_IT_MATTERS,
        help_text="WHY IT MATTERS section content"
    )

    hidden_secret_heading = models.CharField(
        max_length=200,
        default="The Hidden Secret",
        help_text="Heading for the Hidden Secret section"
    )
    hidden_secret = models.TextField(
        blank=True,
        default=SMART_HIDDEN_SECRET,
        help_text="THE HIDDEN SECRET section content"
    )

    the_outcome_heading = models.CharField(
        max_length=200,
        default="The Outcome",
        help_text="Heading for the The Outcome section"
    )
    the_outcome = models.TextField(
        blank=True,
        default=SMART_OUTCOME,
        help_text="THE OUTCOME checklist - one item per line, rendered as premium checklist cards"
    )
    the_outcome_note = models.TextField(
        blank=True,
        default="These qualities support every technology you learn in the future.",
        help_text="Supporting note displayed below the Outcome checklist"
    )

    next_step_heading = models.CharField(
        max_length=200,
        default="The Next Step",
        help_text="Heading for the The Next Step section"
    )
    next_step = models.TextField(
        blank=True,
        default=SMART_NEXT_STEP,
        help_text="THE NEXT STEP section content"
    )
    next_step_label = models.CharField(
        max_length=50,
        default="NEXT STAGE",
        help_text="Label shown on the next-step badge"
    )
    next_step_name = models.CharField(
        max_length=50,
        default="PYTHON-50",
        help_text="Name shown on the next-step badge"
    )
    next_step_sub = models.CharField(
        max_length=100,
        default="Build Your Technology Capability",
        help_text="Supporting text shown on the next-step badge"
    )

    final_quote_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional heading above the final quote"
    )
    final_quote = models.TextField(
        blank=True,
        default=SMART_FINAL_QUOTE,
        help_text="FINAL QUOTE section content"
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "SMART-50"
        verbose_name_plural = "SMART-50"

    def __str__(self):
        return self.title

    def get_what_you_build_items(self):
        return [line.strip() for line in (self.what_you_build or "").split("\n") if line.strip()]

    def get_outcome_items(self):
        return [line.strip() for line in (self.the_outcome or "").split("\n") if line.strip()]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def get_specialization_list_items(self):
        if not self.specialization_list:
            return []
        return [item.strip() for item in self.specialization_list.splitlines() if item.strip()]


class HomePage(models.Model):
    """Singleton model for the new HOME page content"""

    # Section 1 - Tree Diagram
    tree_diagram_image = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        help_text="Tree diagram image for the new Section 1 of the HOME page."
    )

    # Section 2 - Feature Banner
    feature_banner_image = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        help_text="Feature banner image for the new Section 2 of the HOME page."
    )

    background_image = models.ImageField(
        upload_to="home/",
        blank=True,
        null=True,
        help_text="Background image for the HOME page."
    )

    # Section 3 - AI Expert Reviews
    ai_expert_reviews_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Heading for the AI Expert Reviews section."
    )
    ai_expert_reviews_sub_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Sub heading for the AI Expert Reviews section."
    )
    ai_expert_reviews_button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Button text for the AI Expert Reviews section."
    )
    ai_expert_reviews_button_link = models.CharField(
        max_length=500,
        blank=True,
        help_text="Button link for the AI Expert Reviews section."
    )

    # Section 4 - Test Before You Trust
    test_before_trust_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Heading for the Test Before You Trust section."
    )
    test_before_trust_subtitle = models.TextField(
        blank=True,
        help_text="Subtitle for the Test Before You Trust section."
    )
    test_before_trust_feature1 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Feature 1 for the Test Before You Trust section."
    )
    test_before_trust_feature2 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Feature 2 for the Test Before You Trust section."
    )
    test_before_trust_feature3 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Feature 3 for the Test Before You Trust section."
    )
    test_before_trust_feature4 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Feature 4 for the Test Before You Trust section."
    )
    test_before_trust_feature5 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Feature 5 for the Test Before You Trust section."
    )
    test_before_trust_button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Button text for the Test Before You Trust section."
    )
    test_before_trust_button_link = models.CharField(
        max_length=500,
        blank=True,
        help_text="Button link for the Test Before You Trust section."
    )

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "HOME Page"
        verbose_name_plural = "HOME Page"

    def __str__(self):
        return "Home Page"

    def get_specialization_list_items(self):
        return [line.strip() for line in (self.specialization_list or "").split("\n") if line.strip()]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CareerPage(models.Model):
    """Singleton model for the CAREER page content"""

    title = models.CharField(
        max_length=200,
        default="Choose the Right Branch. Grow Toward the Right Future.",
        help_text="Page title"
    )

    subtitle = models.CharField(
        max_length=200,
        default="The Final Phase of the Ekalavya Industry-Ready Roadmap",
        help_text="Page subtitle"
    )

    introduction_heading = models.CharField(
        max_length=200,
        default="Introduction",
        help_text="Heading for the Introduction section"
    )
    introduction = models.TextField(
        blank=True,
        help_text="Introduction content. Preserves paragraphs, arrows, line breaks, and spacing."
    )

    career_tree_image = models.ImageField(
        upload_to="career/",
        blank=True,
        null=True,
        help_text="Career Tree image displayed immediately after the introduction. This is the only image on the page."
    )

    career_tree_heading = models.CharField(
        max_length=200,
        default="Career Tree Analogy",
        help_text="Heading for the Career Tree Analogy section"
    )
    career_tree_section = models.TextField(
        blank=True,
        help_text="Career Tree Analogy section content"
    )

    choose_career_path_heading = models.CharField(
        max_length=200,
        default="Choose Your Career Path",
        help_text="Heading for the Choose Your Career Path section"
    )
    choose_career_path = models.TextField(
        blank=True,
        help_text="Choose Your Career Path content. Each line becomes a styled specialization item."
    )

    learn_organically_heading = models.CharField(
        max_length=200,
        default="Learn Organically. Learn by Doing.",
        help_text="Heading for the Learn Organically section"
    )
    learn_organically = models.TextField(
        blank=True,
        help_text="Learn Organically section content"
    )

    ekalavya_advantage_heading = models.CharField(
        max_length=200,
        default="The Ekalavya Advantage",
        help_text="Heading for the Ekalavya Advantage section"
    )
    ekalavya_advantage = models.TextField(
        blank=True,
        help_text="Ekalavya Advantage section content. Each line becomes a styled checklist item."
    )

    remember_formula_heading = models.CharField(
        max_length=200,
        default="Remember the Formula",
        help_text="Heading for the Remember the Formula section"
    )
    remember_formula = models.TextField(
        blank=True,
        help_text="Remember the Formula content. Separate each step with a blank line. First line is the step title, following lines are the description."
    )

    career_50_ecosystem_heading = models.CharField(
        max_length=200,
        default="CAREER-50 Ecosystem",
        help_text="Heading for the CAREER-50 Ecosystem section"
    )
    career_50_ecosystem = models.TextField(
        blank=True,
        help_text="CAREER-50 Ecosystem content. Separate each step with a blank line. First line is the step title, following lines are the description."
    )

    final_message_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional heading for the Final Message section"
    )
    final_message = models.TextField(
        blank=True,
        help_text="Final message content"
    )

    page_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Large title displayed in Section 1 of the CAREER page"
    )

    description = models.TextField(
        blank=True,
        help_text="Description content displayed in the Description Card section"
    )

    career_path_image = models.ImageField(
        upload_to="career/",
        blank=True,
        null=True,
        help_text="Career Path image displayed in Section 4"
    )

    background_image = models.ImageField(
        upload_to="career/",
        blank=True,
        null=True,
        help_text="Background image for the CAREER page."
    )

    specializations_section_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Section title for the Career Specializations section"
    )

    specializations_section_subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Section subtitle for the Career Specializations section"
    )

    specialization_list = models.TextField(
        blank=True,
        help_text="Career specializations - one per line"
    )

    closing_statement = models.TextField(
        blank=True,
        help_text="Closing statement displayed below the specialization list"
    )

    expert_reviews_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Title for the Expert Reviews CTA section"
    )

    expert_reviews_subtitle = models.TextField(
        blank=True,
        help_text="Subtitle for the Expert Reviews CTA section"
    )

    expert_reviews_button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Button text for the Expert Reviews CTA"
    )

    expert_reviews_button_link = models.CharField(
        max_length=500,
        blank=True,
        help_text="Button link URL for the Expert Reviews CTA. Defaults to the Expert Reviews page if left empty."
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CAREER"
        verbose_name_plural = "CAREER"

    def __str__(self):
        return self.title

    def get_specialization_list_items(self):
        if not self.specialization_list:
            return []
        return [item.strip() for item in self.specialization_list.splitlines() if item.strip()]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FooterSettings(models.Model):
    address = models.TextField(
        default="Ekalavya Universys\nAddress Line 1\nAddress Line 2\nCity\nState\nPIN Code",
        help_text="Footer address, displayed below the map."
    )

    google_map_embed_url = models.URLField(
        max_length=1000,
        blank=True,
        help_text="Google Maps embed URL, for example https://www.google.com/maps/embed?..."
    )

    google_map_share_url = models.URLField(
        max_length=1000,
        blank=True,
        help_text="Google Maps share URL opened by the Share Location button."
    )

    share_button_text = models.CharField(
        max_length=100,
        default="Share Location"
    )

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    elms_url = models.URLField(
        default="https://elms.ekalavyauniversys.com",
        help_text="Default target: https://elms.ekalavyauniversys.com"
    )

    copyright_text = models.CharField(
        max_length=255,
        default="© 2026 Ekalavya Universys. All Rights Reserved."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer Settings"
        verbose_name_plural = "Footer Settings"

    def __str__(self):
        return "Footer Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CapabilityPage(models.Model):
    """Singleton model for the CAPABILITY page content"""

    title = models.CharField(
        max_length=200,
        default="CAPABILITY",
        help_text="Main page heading"
    )

    subtitle_1 = models.CharField(
        max_length=200,
        default="Build Your Technology Capability",
        help_text="First subtitle displayed below the heading"
    )

    subtitle_2 = models.CharField(
        max_length=200,
        default="",
        blank=True,
        help_text="Second subtitle displayed below the heading"
    )

    tree_architecture_image = models.ImageField(
        upload_to="capability/",
        blank=True,
        null=True,
        help_text="Tree Architecture image displayed below the title and subtitle. If left empty, a clean placeholder is shown."
    )

    introduction_heading = models.CharField(
        max_length=200,
        default="Introduction",
        help_text="Heading for the Introduction section"
    )
    introduction = models.TextField(
        blank=True,
        default="Understanding technology is only the beginning.\n\nSuccess in the software industry depends on your ability to apply knowledge, solve problems, and build real-world solutions.\n\nThat is the purpose of the Capability Stage in the Ekalavya Learning System.",
        help_text="Introduction content. Preserves paragraphs, arrows, line breaks, and spacing."
    )

    show_what_is_capability = models.BooleanField(
        default=True,
        help_text="Show the 'What is Capability' section on the page. When unchecked, the entire section is hidden."
    )
    what_is_capability_heading = models.CharField(
        max_length=200,
        default="What is Capability?",
        blank=True,
        help_text="Heading for the What is Capability section"
    )
    what_is_capability = models.TextField(
        blank=True,
        default="Capability is much more than knowing programming syntax.\n\nTrue capability means the ability to\n• Understand problems\n• Design logical solutions\n• Develop reliable software\n• Build practical projects\n• Demonstrate your skills confidently\n\nKnowledge tells you what to do.\nCapability enables you to do it successfully.",
        help_text="What is Capability section content. Preserves paragraphs and line breaks."
    )

    what_you_build_heading = models.CharField(
        max_length=200,
        default="What You Build",
        help_text="Heading for the What You Build section"
    )
    what_you_build = models.TextField(
        blank=True,
        default="Programming Skills\nProblem-Solving Ability\nLogical & Analytical Thinking\nProject Development Skills\nSoftware Design Thinking\nDebugging & Testing Skills\nPractical Coding Confidence\nInterview Readiness\nSkill Demonstration through Portfolio",
        help_text="WHAT YOU BUILD checklist - one item per line, rendered as premium checklist cards"
    )

    learning_philosophy_heading = models.CharField(
        max_length=200,
        default="Our Learning Philosophy",
        help_text="Heading for the Learning Philosophy section"
    )
    learning_philosophy_steps = models.TextField(
        blank=True,
        default="Think\nDesign\nCode\nTest\nImprove",
        help_text="Learning Philosophy steps - one step per line, rendered as a vertical flow with arrows"
    )

    learning_philosophy_text = models.TextField(
        blank=True,
        default="Every concept is transformed into practice.\nEvery practice develops capability.\nEvery capability prepares you for professional success.",
        help_text="Learning Philosophy description text"
    )

    the_outcome_heading = models.CharField(
        max_length=200,
        default="The Outcome",
        help_text="Heading for the The Outcome section"
    )
    the_outcome = models.TextField(
        blank=True,
        default="Build real-world software solutions\nSolve practical programming problems\nDevelop professional-quality projects\nShowcase capabilities through a strong portfolio\nPrepare confidently for Career Specialization",
        help_text="THE OUTCOME checklist - one item per line, rendered as premium checklist cards"
    )

    your_next_step_heading = models.CharField(
        max_length=200,
        default="Your Next Step",
        help_text="Heading for the Your Next Step section"
    )

    your_next_step_introduction = models.TextField(
        blank=True,
        default="",
        help_text="Introduction paragraph displayed before the specialization list in the Your Next Step section"
    )

    your_next_step = models.TextField(
        blank=True,
        default="AI\nData Science\nPower BI\nSQL\nAutomation\nPython Finance\n…and many more.",
        help_text="YOUR NEXT STEP content. Each line becomes a styled specialization item."
    )

    next_step_label = models.CharField(
        max_length=50,
        default="NEXT STAGE",
        help_text="Label shown on the next-step badge"
    )
    next_step_name = models.CharField(
        max_length=50,
        default="PYTHON-50",
        help_text="Name shown on the next-step badge"
    )
    next_step_sub = models.CharField(
        max_length=100,
        default="Build Your Technology Capability",
        help_text="Supporting text shown on the next-step badge"
    )

    golden_principle_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional heading above the Golden Principle final message"
    )
    golden_principle = models.TextField(
        blank=True,
        default="Knowledge becomes valuable only when it is transformed into capability.",
        help_text="Golden Principle final message"
    )

    page_title = models.CharField(
        max_length=200,
        default="CAPABILITY",
        help_text="Page title displayed as a large heading in Section 1."
    )

    page_subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Subtitle displayed below the page title in Section 1. Leave empty to hide."
    )

    career_tree_image = models.ImageField(
        upload_to="capability/",
        blank=True,
        null=True,
        help_text="Career Tree image displayed in Section 2."
    )

    background_image = models.ImageField(
        upload_to="capability/",
        blank=True,
        null=True,
        help_text="Background image for the CAPABILITY page."
    )

    description = models.TextField(
        blank=True,
        default="",
        help_text="Description content displayed in Section 3. Preserves paragraphs and line breaks."
    )

    python_ecosystem_tree_image = models.ImageField(
        upload_to="capability/",
        blank=True,
        null=True,
        help_text="Python Ecosystem tree image displayed in Section 4."
    )

    python_ecosystem_section_title = models.CharField(
        max_length=200,
        default="Python Ecosystem",
        help_text="Section title for the Python Ecosystem section."
    )

    python_ecosystem_section_subtitle = models.CharField(
        max_length=200,
        default="",
        blank=True,
        help_text="Section subtitle for the Python Ecosystem section."
    )

    python_ecosystem_highlight_line = models.CharField(
        max_length=200,
        default="",
        blank=True,
        help_text="Highlight line for the Python Ecosystem section (visually emphasized)."
    )

    python_ecosystem_point_1 = models.TextField(
        blank=True,
        default="",
        help_text="Point 1 for the Python Ecosystem section."
    )

    python_ecosystem_point_2 = models.TextField(
        blank=True,
        default="",
        help_text="Point 2 for the Python Ecosystem section."
    )

    python_ecosystem_point_3 = models.TextField(
        blank=True,
        default="",
        help_text="Point 3 for the Python Ecosystem section."
    )

    python_warmup_title = models.CharField(
        max_length=200,
        default="Python WarmUp",
        help_text="Title for the Python WarmUp CTA section."
    )

    python_warmup_subtitle = models.CharField(
        max_length=200,
        default="",
        blank=True,
        help_text="Subtitle for the Python WarmUp CTA section."
    )

    python_warmup_intro_paragraph = models.TextField(
        blank=True,
        default="",
        help_text="Intro paragraph for the Python WarmUp CTA section. Preserves paragraphs and line breaks."
    )

    python_warmup_checklist_items = models.TextField(
        blank=True,
        default="",
        help_text="Checklist items for the Python WarmUp CTA section - one item per line."
    )

    python_warmup_button_text = models.CharField(
        max_length=100,
        default="Start Free Training",
        help_text="Button text for the Python WarmUp CTA button. Links to the existing Free Training page."
    )

    python_warmup_button_link = models.CharField(
        max_length=500,
        blank=True,
        help_text="Button link URL for the Python WarmUp CTA button. Defaults to the FREE TRAINING page if left empty."
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CAPABILITY"
        verbose_name_plural = "CAPABILITY"

    def __str__(self):
        return self.title

    def get_what_you_build_items(self):
        return [line.strip() for line in (self.what_you_build or "").split("\n") if line.strip()]

    def get_outcome_items(self):
        return [line.strip() for line in (self.the_outcome or "").split("\n") if line.strip()]

    def get_philosophy_steps(self):
        return [line.strip() for line in (self.learning_philosophy_steps or "").split("\n") if line.strip()]

    def get_next_step_items(self):
        return [line.strip() for line in (self.your_next_step or "").split("\n") if line.strip()]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FAQPage(models.Model):
    """Singleton model for the FAQs page content"""

    title = models.CharField(
        max_length=200,
        default="FAQs",
        help_text="Main page title"
    )

    subtitle = models.CharField(
        max_length=200,
        default="Know Before You Commit",
        help_text="Page subtitle displayed below the title"
    )

    background_image = models.ImageField(
        upload_to="faq/",
        blank=True,
        null=True,
        help_text="Background image for the FAQs page."
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQs Page"
        verbose_name_plural = "FAQs Page"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FAQItem(models.Model):
    """Individual FAQ item linked to the FAQPage singleton"""

    faq_page = models.ForeignKey(
        FAQPage,
        on_delete=models.CASCADE,
        related_name="faq_items",
        help_text="The FAQs page this item belongs to"
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which this FAQ appears (lower numbers first)"
    )

    question = models.CharField(
        max_length=500,
        help_text="The FAQ question"
    )

    answer = models.TextField(
        help_text="The FAQ answer. Supports paragraphs and line breaks."
    )

    active = models.BooleanField(
        default=True,
        help_text="Only active items appear on the frontend"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ Item"
        verbose_name_plural = "FAQ Items"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.question


class FreeTrainingPage(models.Model):
    """Singleton model for the new FREE TRAINING page content"""

    title = models.CharField(
        max_length=200,
        default="Free Training",
        help_text="Main page title"
    )

    subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Page subtitle displayed below the title"
    )
    intro_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional title displayed below the gallery images."
    )

    intro_description = models.TextField(
        blank=True,
        help_text="Optional description displayed below the introduction title."
    )

    show_serial_numbers = models.BooleanField(
        default=True,
        help_text="Display an automatically generated serial-number column at the beginning of the table."
    )

    # Free Training Section
    free_training_section_title = models.CharField(
        max_length=200,
        default="Free Training",
        help_text="Heading for the Free Training (videos) section"
    )
    free_training_section_subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional subtitle for the Free Training (videos) section"
    )

    # Free eBooks Section
    free_ebooks_section_title = models.CharField(
        max_length=200,
        default="Free eBooks",
        help_text="Heading for the Free eBooks section"
    )
    free_ebooks_section_subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional subtitle for the Free eBooks section"
    )

    background_image = models.ImageField(
        upload_to="free_training/",
        blank=True,
        null=True,
        help_text="Background image for the Free Training page."
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )
    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )
    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Free Training Page"
        verbose_name_plural = "Free Training Page"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FreeTrainingImage(models.Model):
    """An optional, ordered image displayed on the Free Training page."""

    page = models.ForeignKey(
        FreeTrainingPage,
        on_delete=models.CASCADE,
        related_name="gallery_images",
    )
    image = models.ImageField(
        upload_to="free_training/gallery/",
    )
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Free Training Image"
        verbose_name_plural = "Free Training Images"

    def __str__(self):
        return self.caption or f"Free Training Image {self.pk or ''}"


class FreeTrainingAfterTableImage(models.Model):
    """Optional images displayed after the Free Training table."""

    page = models.ForeignKey(
        FreeTrainingPage,
        on_delete=models.CASCADE,
        related_name="after_table_images",
    )
    image = models.ImageField(
        upload_to="free_training/after_table/",
    )
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Free Training Image After Table"
        verbose_name_plural = "Free Training Images After Table"

    def __str__(self):
        return self.caption or f"After-table image {self.pk or ''}"

class FreeTrainingTableColumn(models.Model):
    """A configurable column in the Free Training table."""

    page = models.ForeignKey(
        FreeTrainingPage,
        on_delete=models.CASCADE,
        related_name="table_columns",
    )
    heading = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Free Training Table Column"
        verbose_name_plural = "Free Training Table Columns"

    def __str__(self):
        return self.heading or f"Column {self.pk or ''}"


class FreeTrainingTableRow(models.Model):
    """A configurable row in the Free Training table."""

    page = models.ForeignKey(
        FreeTrainingPage,
        on_delete=models.CASCADE,
        related_name="table_rows",
    )
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Free Training Table Row"
        verbose_name_plural = "Free Training Table Rows"

    def __str__(self):
        return f"Table Row {self.display_order or self.pk or ''}"


class FreeTrainingTableCell(models.Model):
    """A cell that displays either text or a clickable button."""

    CELL_TYPE_CHOICES = [
        ("text", "Plain Text"),
        ("button", "Clickable Button"),
    ]

    row = models.ForeignKey(
        FreeTrainingTableRow,
        on_delete=models.CASCADE,
        related_name="cells",
    )
    column = models.ForeignKey(
        FreeTrainingTableColumn,
        on_delete=models.CASCADE,
        related_name="cells",
    )
    cell_type = models.CharField(
        max_length=10,
        choices=CELL_TYPE_CHOICES,
        default="text",
    )
    text = models.TextField(
        blank=True,
        help_text="Text to display, or button label when the cell type is Clickable Button.",
    )
    button_url = models.URLField(
        max_length=1000,
        blank=True,
        help_text="Required for a Clickable Button cell.",
    )

    class Meta:
        ordering = ["column__display_order", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["row", "column"],
                name="unique_free_training_cell_per_column",
            ),
        ]
        verbose_name = "Free Training Table Cell"
        verbose_name_plural = "Free Training Table Cells"

    def __str__(self):
        return f"{self.row} - {self.column}"

    def clean(self):
        from django.core.exceptions import ValidationError

        errors = {}

        if self.row_id and self.column_id:
            if self.row.page_id != self.column.page_id:
                errors["column"] = (
                    "The selected column must belong to the same page as the row."
                )

        if self.cell_type == "button":
            if not self.text.strip():
                errors["text"] = "Button text is required for a button cell."
            if not self.button_url.strip():
                errors["button_url"] = "A URL is required for a button cell."
        elif self.cell_type == "text" and self.button_url:
            errors["button_url"] = (
                "Leave the button URL empty when the cell type is Plain Text."
            )

        if errors:
            raise ValidationError(errors)


class ContactPage(models.Model):
    """Singleton model for the CONTACT US page hero and final CTA content."""

    hero_title = models.CharField(
        max_length=200,
        default="Begin Your Transformation",
        help_text="Main hero title for the Contact Us page"
    )

    hero_subtitle = models.TextField(
        blank=True,
        default="Every successful technology career begins with a single conversation. Whether you're exploring IT for the first time or planning your next career move, we're here to guide you.",
        help_text="Hero subtitle / supporting paragraph"
    )

    hero_background_image = models.ImageField(
        upload_to="contact/hero/",
        blank=True,
        null=True,
        help_text="Hero background image. A premium gradient is shown if none is uploaded."
    )

    cta_title = models.CharField(
        max_length=200,
        default="Ready to Build Your Future?",
        help_text="Title for the final CTA banner"
    )

    cta_description = models.TextField(
        blank=True,
        default="Every expert was once a beginner. Start your transformation with Ekalavya today.",
        help_text="Description for the final CTA banner"
    )

    cta_button_text = models.CharField(
        max_length=100,
        default="Go to ELMS",
        help_text="Text for the primary CTA button (links to ELMS)"
    )

    cta_button_url = models.URLField(
        max_length=1000,
        blank=True,
        default="https://elms.ekalavyauniversys.com/",
        help_text="URL the primary CTA button opens"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

    def __str__(self):
        return "Contact Page"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactCard(models.Model):
    """Animated 'How Can We Help You?' / decision card."""

    ICON_CHOICES = [
        ("career", "Career Guidance"),
        ("program", "Program Information"),
        ("support", "Technical Support"),
        ("partnership", "Partnership Opportunities"),
        ("book", "Book / New Learner"),
        ("code", "Specialization Guidance"),
        ("college", "College / Institution"),
        ("chat", "General Enquiry"),
    ]

    icon = models.CharField(
        max_length=20,
        choices=ICON_CHOICES,
        default="career",
        help_text="Icon shown on the card"
    )

    title = models.CharField(max_length=200, help_text="Card title")

    description = models.TextField(blank=True, help_text="Card description")

    subject_text = models.CharField(
        max_length=200,
        blank=True,
        help_text="Text auto-filled into the contact form Subject when this card is clicked (defaults to the title)."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which this card appears (lower numbers first)"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Card"
        verbose_name_plural = "Contact Cards"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title

    def get_subject(self):
        return self.subject_text or self.title


class ContactInformation(models.Model):
    """Singleton model with the contact details shown in the info cards."""

    address = models.TextField(
        blank=True,
        help_text="Address displayed on the Address card. Recommended to reuse FooterSettings address."
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
        help_text="Phone number. Used for click-to-call."
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True,
        help_text="WhatsApp number in international format, e.g. 919999999999 (no + or spaces)."
    )

    email = models.EmailField(
        blank=True,
        help_text="Email address. Used to open the email client."
    )

    working_hours = models.TextField(
        blank=True,
        default="Monday - Saturday\n9:00 AM - 7:00 PM",
        help_text="Working hours (display only). One line per entry."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactFAQ(models.Model):
    """Quick FAQ shown in the accordion on the Contact Us page."""

    question = models.CharField(max_length=500, help_text="The FAQ question")

    answer = models.TextField(help_text="The FAQ answer. Supports paragraphs and line breaks.")

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which this FAQ appears (lower numbers first)"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact FAQ"
        verbose_name_plural = "Contact FAQs"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.question


class ContactFormSettings(models.Model):
    """Singleton model for the contact form behaviour and messaging."""

    form_heading = models.CharField(
        max_length=200,
        default="Send Us a Message",
        help_text="Heading displayed above the contact form"
    )

    success_message = models.TextField(
        blank=True,
        default="Your message has been received successfully. We'll contact you shortly.",
        help_text="Message shown after a successful submission"
    )

    admin_email = models.EmailField(
        blank=True,
        help_text="Email address notified when a new inquiry is submitted (optional)."
    )

    button_text = models.CharField(
        max_length=100,
        default="Send Message",
        help_text="Text shown on the submit button"
    )

    enable_email_notification = models.BooleanField(
        default=False,
        help_text="Send an email notification to the admin email on new submissions (requires email backend configured)."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Form Settings"
        verbose_name_plural = "Contact Form Settings"

    def __str__(self):
        return "Contact Form Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ELMSSettings(models.Model):
    """Singleton model for the 'Connect to ELMS' section."""

    button_text = models.CharField(
        max_length=100,
        default="Go to ELMS",
        help_text="Text shown on the ELMS button"
    )

    elms_url = models.URLField(
        max_length=1000,
        default="https://elms.ekalavyauniversys.com/",
        help_text="URL opened by the ELMS button"
    )

    description = models.TextField(
        blank=True,
        default="Continue your learning journey on ELMS.",
        help_text="Description shown above the ELMS button"
    )

    open_in_new_tab = models.BooleanField(
        default=True,
        help_text="Open the ELMS URL in a new browser tab"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ELMS Settings"
        verbose_name_plural = "ELMS Settings"

    def __str__(self):
        return "ELMS Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactSubmission(models.Model):
    """Stores every inquiry submitted through the Contact Us form."""

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("replied", "Replied"),
        ("closed", "Closed"),
    ]

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=50, blank=True)

    subject = models.CharField(max_length=200, blank=True)

    message = models.TextField()

    submission_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    admin_notes = models.TextField(
        blank=True,
        help_text="Internal notes visible only in the admin"
    )

    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ["-submission_date"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"


class ExpertReviewsPage(models.Model):
    """Singleton model for the Expert Reviews page content"""

    title = models.CharField(
        max_length=200,
        default="Expert Reviews",
        help_text="Page title"
    )

    # Retained for existing database data.
    # This field will no longer be displayed in Admin or on the frontend.
    subtitle = models.CharField(
        max_length=200,
        blank=True,
        help_text="Legacy subtitle field retained for existing data."
    )

    introduction_heading = models.CharField(
        max_length=200,
        blank=True,
        default="Introduction",
        help_text="Optional editable heading displayed above the introduction."
    )

    introduction = models.TextField(
        blank=True,
        help_text="Optional introductory content displayed below the introduction heading."
    )

    hero_description = models.TextField(
        blank=True,
        help_text="Hero section description"
    )

    background_image = models.ImageField(
        upload_to="expert_reviews/",
        blank=True,
        null=True,
        help_text="Background image for the Expert Reviews page."
    )

    active = models.BooleanField(default=True)

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO Keywords (comma separated)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Expert Reviews Page"
        verbose_name_plural = "Expert Reviews Page"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ExpertReview(models.Model):
    """Individual expert review linked to the ExpertReviewsPage singleton"""

    expert_reviews_page = models.ForeignKey(
        ExpertReviewsPage,
        on_delete=models.CASCADE,
        related_name="expert_reviews",
        help_text="The Expert Reviews page this review belongs to"
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which this review appears (lower numbers first)"
    )

    active = models.BooleanField(
        default=True,
        help_text="Only active reviews appear on the frontend"
    )

    module_name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional module/category label displayed in the left column, for example CLARITY-50."
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        default="View Testimonial",
        help_text="Optional button text that expands or collapses this review's testimonial images."
    )

    cover_image = models.ImageField(
        upload_to="expert_reviews/",
        blank=True,
        null=True,
        help_text="Cover image for the review"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Expert Review"
        verbose_name_plural = "Expert Reviews"
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"Independent Educational Review of {self.module_name}" if self.module_name else "Expert Review"


class ExpertReviewImage(models.Model):
    """Additional image attached to an Expert Review"""

    expert_review = models.ForeignKey(
        ExpertReview,
        on_delete=models.CASCADE,
        related_name="additional_images",
        help_text="The expert review this image belongs to"
    )

    image = models.ImageField(
        upload_to="expert_reviews/",
        help_text="Additional image for the review"
    )

    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional caption for the image"
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which this image appears (lower numbers first)"
    )

    active = models.BooleanField(
        default=True,
        help_text="Only active images appear on the frontend"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Expert Review Image"
        verbose_name_plural = "Expert Review Images"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.caption or f"Image for {self.expert_review.module_name or 'Expert Review'}"


class EkalavyaLandingPage(models.Model):
    """Singleton model for the Ekalavya Landing Page content"""

    hero_image = models.ImageField(
        upload_to="ekalavya/",
        help_text="Hero image displayed on the Ekalavya landing page"
    )

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO Title tag"
    )

    seo_description = models.TextField(
        blank=True,
        help_text="SEO Meta Description"
    )

    seo_keywords = models.TextField(
        blank=True,
        help_text="SEO Keywords"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ekalavya Landing Page"
        verbose_name_plural = "Ekalavya Landing Page"

    def __str__(self):
        return "Ekalavya Landing Page"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

class EkalavyaLandingSection(models.Model):
    """Repeatable landing page section for the Ekalavya Universys landing page."""

    image = models.ImageField(
        upload_to="ekalavya/landing/",
        blank=True,
        null=True,
        help_text="Optional section image",
    )

    display_order = models.PositiveIntegerField(
        default=1,
        help_text="Order in which this section appears (lower numbers first)",
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ekalavya Landing Section"
        verbose_name_plural = "Ekalavya Landing Sections"
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"Landing Section {self.pk or ''}"

class EkalavyaLandingSectionVideo(models.Model):
    """
    Individual video + thumbnail pair for an Ekalavya landing page section.

    A section can contain multiple video items.
    Each video item must have a thumbnail and exactly one video source.
    """

    VIDEO_TYPE_CHOICES = [
        ("youtube", "YouTube"),
        ("upload", "Uploaded Video"),
        ("other", "Other (External Link)"),
    ]

    section = models.ForeignKey(
        EkalavyaLandingSection,
        on_delete=models.CASCADE,
        related_name="videos",
        help_text="Landing page section this video belongs to",
    )

    thumbnail = models.ImageField(
        upload_to="ekalavya/landing/thumbnails/",
        help_text="Thumbnail image for this video",
    )

    video_type = models.CharField(
        max_length=20,
        choices=VIDEO_TYPE_CHOICES,
        default="youtube",
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube video URL",
    )

    other_url = models.URLField(
        blank=True,
        help_text="Optional external URL opened when the thumbnail is clicked if Video Type is Other.",
    )

    uploaded_video = models.FileField(
        upload_to="ekalavya/landing/videos/",
        blank=True,
        null=True,
        help_text="Uploaded video file",
    )

    display_order = models.PositiveIntegerField(
        default=1,
        help_text="Order in which this video appears within the section",
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Landing Section Video"
        verbose_name_plural = "Landing Section Videos"
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.section} - Video {self.pk or ''}"


    def clean(self):
        if self.video_type == "youtube":
            if not self.youtube_url:
                raise ValidationError({
                    "youtube_url": (
                        "YouTube URL is required when Video Type is YouTube."
                    )
                })

            if self.uploaded_video:
                raise ValidationError({
                    "uploaded_video": (
                        "Uploaded Video must be empty when Video Type is YouTube."
                    )
                })

            if self.other_url:
                raise ValidationError({
                    "other_url": (
                        "External URL must be empty when Video Type is YouTube."
                    )
                })

        elif self.video_type == "upload":
            if not self.uploaded_video:
                raise ValidationError({
                    "uploaded_video": (
                        "Uploaded Video is required when Video Type is Uploaded Video."
                    )
                })

            if self.youtube_url:
                raise ValidationError({
                    "youtube_url": (
                        "YouTube URL must be empty when Video Type is Uploaded Video."
                    )
                })

            if self.other_url:
                raise ValidationError({
                    "other_url": (
                        "External URL must be empty when Video Type is Uploaded Video."
                    )
                })

        elif self.video_type == "other":
            if self.youtube_url:
                raise ValidationError({
                    "youtube_url": (
                        "YouTube URL must be empty when Video Type is Other."
                    )
                })

            if self.uploaded_video:
                raise ValidationError({
                    "uploaded_video": (
                        "Uploaded Video must be empty when Video Type is Other."
                    )
                })


# ---------------------------------------------------------------------------
# Dynamic Information Zone
# ---------------------------------------------------------------------------

class DynamicInformationSettings(models.Model):
    """Singleton settings for the dynamic information zone above the footer."""

    main_heading = models.CharField(
        max_length=200,
        default="WHAT'S HAPPENING AT EKALAVYA",
        help_text="Main heading displayed above the Notice Board and Events & Activities sections.",
    )
    main_image = models.ImageField(
        upload_to="footer/dynamic_information/",
        blank=True,
        null=True,
        help_text="Main image displayed directly below the Dynamic Information Zone heading.",
    )

    notice_section_heading = models.CharField(
        max_length=200,
        default="NOTICE BOARD",
        help_text="Heading displayed above the Notice Board items.",
    )

    notice_section_subtitle = models.CharField(
        max_length=300,
        blank=True,
        help_text="Optional subtitle displayed below the Notice Board heading.",
    )

    notice_view_all_text = models.CharField(
        max_length=100,
        default="VIEW ALL →",
        help_text="Text displayed on the Notice Board View All button.",
    )

    notice_view_all_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="URL opened by the Notice Board View All button.",
    )

    event_section_heading = models.CharField(
        max_length=200,
        default="EVENTS & ACTIVITIES",
        help_text="Heading displayed above the Events & Activities items.",
    )

    event_section_subtitle = models.CharField(
        max_length=300,
        blank=True,
        help_text="Optional subtitle displayed below the Events & Activities heading.",
    )

    event_view_all_text = models.CharField(
        max_length=100,
        default="VIEW ALL →",
        help_text="Text displayed on the Events & Activities View All button.",
    )

    event_view_all_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="URL opened by the Events & Activities View All button.",
    )

    items_to_show = models.PositiveIntegerField(
        default=3,
        help_text="Maximum number of active Notice Board and Events & Activities items shown in the compact footer zone.",
    )

    active = models.BooleanField(
        default=True,
        help_text="When disabled, the entire Dynamic Information Zone is hidden.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Dynamic Information Settings"
        verbose_name_plural = "Dynamic Information Settings"

    def __str__(self):
        return "Dynamic Information Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class NoticeBoard(models.Model):
    """Individual notice displayed in the dynamic Notice Board section."""

    admin_label = models.CharField(
        max_length=200,
        blank=True,
        help_text="Internal admin label used to identify this notice. Not displayed on the website.",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional notice title.",
    )

    description = models.TextField(
        blank=True,
        help_text="Notice description or supporting information.",
    )

    image = models.ImageField(
        upload_to="footer/notices/",
        blank=True,
        null=True,
        help_text="Optional image displayed with this notice.",
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional button text. Leave empty if the notice should not have a button.",
    )

    button_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Optional button URL. Supports internal or external URLs.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which notices appear. Lower numbers appear first.",
    )

    active = models.BooleanField(
        default=True,
        help_text="Only active notices are displayed on the frontend.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notice Board Item"
        verbose_name_plural = "Notice Board Items"
        ordering = ["display_order", "-created_at", "id"]

    def __str__(self):
        return self.title


class EventActivity(models.Model):
    """Individual event or activity displayed in the dynamic events section."""

    admin_label = models.CharField(
        max_length=200,
        blank=True,
        help_text="Internal admin label used to identify this event or activity. Not displayed on the website.",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional event or activity title.",
    )

    event_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional event type, for example Workshop, Seminar, Training, or Student Activity.",
    )

    event_date = models.DateField(
        blank=True,
        null=True,
        help_text="Optional event or activity date.",
    )

    image = models.ImageField(
        upload_to="footer/events/",
        blank=True,
        null=True,
        help_text="Optional event or activity image.",
    )

    description = models.TextField(
        blank=True,
        help_text="Event or activity description.",
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional button text. Leave empty if the event should not have a button.",
    )

    button_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Optional button URL. Supports internal or external URLs.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Manual display priority. Lower numbers appear first when dates are equal.",
    )

    active = models.BooleanField(
        default=True,
        help_text="Only active events and activities are displayed on the frontend.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event & Activity"
        verbose_name_plural = "Events & Activities"
        ordering = ["-event_date", "display_order", "-created_at", "id"]

    def __str__(self):
        return self.title