
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}

colors = ["Red", "Green", "Blue"]

def is_valid(assignment, region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False 
    return True

def backtrack(assignment):
    if len(assignment) == len(neighbors): 
        return assignment

    
    unassigned = [r for r in neighbors if r not in assignment][0]

    for color in colors:
        if is_valid(assignment, unassigned, color):
            assignment[unassigned] = color  
            
            
            result = backtrack(assignment)
            if result:
                return result  

            del assignment[unassigned]

    return None  
solution = backtrack({})
if solution:
    print("Solution:", solution)
else:
    print("No solution found")

