from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

    @models.permalink # or: get_absolute_url = models.permalink(get_absolute_url) below
    def get_absolute_url(self): # "view on site" link will be visible in admin interface
        """Construct the absolute URL for a Recipe."""
        return ('recipe_detail', (), {
                            'pk': self.pk})



class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    description = models.CharField(max_length=255)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description
        

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.recipe