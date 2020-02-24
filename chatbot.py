#!/usr/bin/python

class Category:
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.parentCategory = None
        self.subCategories = []
