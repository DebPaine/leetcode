/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


func rightSideView(root *TreeNode) []int {
    if root == nil {
        return nil
    }
    output := []int{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        var rightSideVal int 
        for _, _ = range queue {
            node := queue[0]
            queue = queue[1:]
            rightSideVal = node.Val

            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        output = append(output, rightSideVal)
    }
    return output
}