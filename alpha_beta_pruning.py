import math

# Minimax with Alpha-Beta Pruning
def alphabeta(depth, node_index, is_maximizing, scores, alpha, beta, height):
    # Base case: If leaf node is reached
    if depth == height:
        return scores[node_index]

    if is_maximizing:
        best_score = -math.inf
        for i in range(2):  # Two children for each node
            val = alphabeta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height)
            best_score = max(best_score, val)
            alpha = max(alpha, best_score)
            if beta <= alpha:  # Beta cutoff
                break
        return best_score
    else:
        best_score = math.inf
        for i in range(2):  # Two children for each node
            val = alphabeta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height)
            best_score = min(best_score, val)
            beta = min(beta, best_score)
            if beta <= alpha:  # Alpha cutoff
                break
        return best_score

# Example: Binary tree representation of possible game outcomes
scores = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
tree_height = math.log2(len(scores))  # Height of the tree

# Start Alpha-Beta pruning from the root node
optimal_value = alphabeta(0, 0, True, scores, -math.inf, math.inf, tree_height)
print("Optimal value:", optimal_value)
