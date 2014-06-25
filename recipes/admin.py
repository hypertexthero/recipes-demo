from django.contrib import admin
from recipes.models import *
        
class InstructionInline(admin.StackedInline):
    model = Instruction
    extra = 3

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 3
    
class RecipeAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [IngredientInline, InstructionInline]

admin.site.register(Recipe, RecipeAdmin)
