class ReverseListIterator:
    '''Question 10'''
    def __init__(self,_list:list) -> None:
        self._list = _list
        self._index = len(self._list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            result = self._list[self._index]
            self._index -= 1
            return result

        raise StopIteration
        


def remove_dublicates_in_list(input_list:list) -> list:
    '''Question 3'''
    local_dict = {}
    for val in input_list:
        local_dict[val] = 1
    final_list = []
    for val in local_dict.keys():
        final_list.append(val)
    return final_list[::-1]

def generate_3d_array(l:int,b:int,h:int) -> list:
    '''Question 4'''
    final_list = []
    for i in range(l):
        local_j = []
        for j in range(b):
            local_k = []
            for k in range(h):
                local_k.append(0)
            local_j.append(local_k)
        final_list.append(local_j)

    return final_list

def binary_search(input_list:list,element:int) -> int:
    '''Question 5'''
    start = 0
    end = len(input_list) - 1
    while start <= end:
        mid = int((start + end)/2)
        if input_list[mid] == element:
            return mid
        elif input_list[mid] < element:
            start = mid + 1
        elif input_list[mid] > element:
            end = mid - 1

    return -1

def divisible_by_5_and_7(n:int):
    '''Question 6'''
    i = 1
    while i <= n:
        if i%5 == 0:
            yield i
        elif i%7 == 0:
            yield i
        i += 1



def find_company_name(email:str) -> str:
    '''Question 7'''
    return email.split('@')[1].split('.')[0]

def generate_square_of_number() -> list:
    '''Question 8'''
    square = lambda x: x*x
    return list(map(square,[x for x in range(1,21)]))
    

if __name__ == '__main__':
    print(remove_dublicates_in_list([12,24,35,24,88,120,155,88,120,155]))
    print(generate_3d_array(3,5,8))

    for num in divisible_by_5_and_7(int(input("Enter limit: "))):
        print(num,end=',')
    print()

    print(find_company_name("varnit.singh@datagrokr.com"))
    print(generate_square_of_number())

    for val in ReverseListIterator([1,2,3,4,5,6,7,8,9]):
        print(val,end=',')
    print()

    print(binary_search([1,2,3,4,5,6,7,8,9,10],5))

