# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.


# Example 1:
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".

# Example 2:

# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

# Example 3:

# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        # RECIPE USE INGREDIENT : SUPPLY
        # SUPPLY = RAW INGREDIENT

        # bread :   yeast flour
        # sandwich: bread meat
        # burger:   sandwich bread meat

        # supply > recipe
        cookable = {supply: True for supply in supplies}
        recipeList = {recipe: ingredient for ingredient,
                      recipe in enumerate(recipes)}
        result = []

        # dfs to find recipe ingredients and return
        def dfs():
            if recipe in cookable:
                return cookable[recipe]

            if recipe not in recipeList:
                return False

            cookable[recipe] = False

            for neighbour in ingredients[recipeList[recipe]]:
                if not dfs(neighbour):
                    return False

            cookable[recipe] = True
            return cookable[recipe]

        # add recipe that are cookable into result
        for recipe in recipes:
            if dfs(recipe):
                # can cook
                result.append(recipe)
        return result

    def __init__(self):
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["yeast", "flour", "corn"]
        result = self.findAllRecipes(recipes, ingredients, supplies)
        print(result)
