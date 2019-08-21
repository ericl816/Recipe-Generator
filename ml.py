"""
TO DO: Create
"""
#place holder function for assigning recepies ml_rank
def assignMLranking(recipes_data):
    score = 10
    for recipe in recipes_data:
        recipe.append(score)
        score+=1
    return recipes_data