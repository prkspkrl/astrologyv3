from django.contrib import admin
from .models import Contact, Review, Slider, OurService, AboutUs, WhyChooseUs

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'photo')
    actions = ['duplicate_review_content']

    def duplicate_review_content(self, request, queryset):
        for review in queryset:
            new_review = Review.objects.create(
                photo=review.photo,
                name=review.name,
                review=review.review,
                designation=review.designation
            )

    duplicate_review_content.short_description = "Duplicate selected reviews"

admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(WhyChooseUs)
admin.site.register(OurService)
admin.site.register(AboutUs)
admin.site.register(Review, ReviewAdmin)