class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        insertable_left = list(warehouse)
        insertable_right = list(warehouse)
        W = len(warehouse)
        for i in range(1, W):
            insertable_left[i] = min(insertable_left[i], insertable_left[i - 1])
        for i in range(W - 2, 0, -1):
            insertable_right[i] = min(insertable_right[i], insertable_right[i + 1])
        
        insertable = [max(insertable_left[i], insertable_right[i]) for i in range(W)]
        insertable.sort()
        boxes.sort()
        
        inserted = 0
        ptr = 0
        for b in boxes:
            while ptr < W and b > insertable[ptr]:
                ptr += 1
            if ptr >= W:
                break
            inserted += 1
            ptr += 1
        
        return inserted
                
        