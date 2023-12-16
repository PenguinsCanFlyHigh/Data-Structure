# 코드 3.12

#멤버 함수
class ArrayList:
    def __init__(self, elements):
        self.elements = elements

    def findMinMax(self):
        # 리스트가 비어 있으면 (-1, -1) 반환
        if not self.elements:
            return (-1, -1)

    # 최초의 요소를 최소값과 최대값의 인덱스로 가정한다.
        min_index = 0
        max_index = 0
        
        # 리스트를 순회하며 최소값과 최대값의 인덱스를 찾는다
        for i in range(1, len(self.elements)):
            if self.elements[i] < self.elements[min_index]:
                min_index = i
            elif self.elements[i] > self.elements[max_index]:
                max_index = i

        return (min_index, max_index)
#----------------------------------------------------------------------------------------

# 출력
my_list = ArrayList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
min_index, max_index = my_list.findMinMax()
print(f"최소값 인덱스: {min_index}, 최대값 인덱스: {max_index}")


# 빈 리스트의 경우
empty_list = ArrayList([])
min_index, max_index = empty_list.findMinMax()
print(f"빈 리스트: {min_index}, {max_index}")
