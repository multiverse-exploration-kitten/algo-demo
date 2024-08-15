from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indices_stack = []
        max_area = 0

        # 按顺序一个一个走。 右侧加一个0当最小值
        for idx, height in enumerate(heights + [0]):
            # 当monotonic stack里有东西，且栈顶的高度大于当前即将入栈的高度时
            # i.e.碰到比栈顶小的了，不再继续递增了。 递减
            while indices_stack and heights[indices_stack[-1]] >= height:
                # 拿出栈顶的index
                top_idx = indices_stack.pop()
                # 栈顶左侧的index，如果是最后一个元素，取-1
                left_idx = indices_stack[-1] if indices_stack else -1
                # 长度 = 即将入栈的index - 左侧的index 再 -1
                width = idx - left_idx - 1
                # 计算最大面积。因为进行操作时是不再递增了，所以与木桶原理相似，heights[top_idx]即为
                # 整个面积的高度
                max_area = max(max_area, width * heights[top_idx])
                # 循环这个过程直到左侧第一个比当前小的，恢复了递增性质时性质

            # 把当前这个放入，当前还是一个monotonic increasing stack
            indices_stack.append(idx)

        return max_area
