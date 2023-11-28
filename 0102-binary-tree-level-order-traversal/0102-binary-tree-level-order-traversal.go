/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type Queue struct {
    list []TreeNode
}

func (q *Queue) dequeue () TreeNode {
    poppedValue := q.list[0]
    q.list = q.list[1:]
    return poppedValue
}

func (q *Queue) enqueue (node *TreeNode) {
    q.list = append(q.list, *node)
}

func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    } 
    
    var output [][]int
    q := &Queue{}
    q.enqueue(root)

    for len(q.list) > 0 {
        level := []int{}
        for range q.list {
            node := q.dequeue()
            level = append(level, node.Val)
            if node.Left != nil {
                q.enqueue(node.Left)
            }
            if node.Right != nil {
                q.enqueue(node.Right)
            }
        }
        output = append(output, level)
    }
    return output
}

