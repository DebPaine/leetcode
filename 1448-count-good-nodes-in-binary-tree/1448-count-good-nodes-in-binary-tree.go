/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int { 
    count := 0
    dfs(root, math.Inf(-1), &count)
    return count
}

func dfs(node *TreeNode, maxVal float64, count *int) {
    if node == nil {
        return 
    }
    if float64(node.Val) >= maxVal {
        *count++
    }
    dfs(node.Left, math.Max(maxVal, float64(node.Val)), count)
    dfs(node.Right, math.Max(maxVal, float64(node.Val)), count)
}