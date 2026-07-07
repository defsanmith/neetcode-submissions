class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # init the arrays A, B
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # check if len(B) < len(A)
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        # init loop
        while True:
            # init i, j
            i = (l + r) // 2
            j = half - i - 2

            # get left, right elements of the arrays
            ALeft = A[i] if i >= 0 else float('-inf')
            ARight = A[i + 1] if (i + 1) < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j + 1] if (j + 1) < len(B) else float('inf')

            # if al < br and bl < ar
            if ALeft <= BRight and BLeft <= ARight:
                # handle odd case
                if total % 2:
                    return min(ARight, BRight)

                # handle even case
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2

            # if al > br
            if ALeft > BRight: 
                r = i - 1
            # if bl > ar
            else:
                l = i + 1