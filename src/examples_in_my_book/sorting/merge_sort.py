#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


   
def merge_sort(seq):
    if len(seq) <= 1: return seq
    mid = len(seq)//2 
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft)>1: lft = merge_sort(lft)
    if len(rgt)>1: rgt = merge_sort(rgt)
    
    res = []
    while lft and rgt: 
        if lft [-1]>= rgt[-1]:
            res.append(lft.pop())
        else: 
            res.append(rgt.pop())
    res.reverse()
    return(lft or rgt) + res   
    



def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(merge_sort(seq) == sorted(seq))
    print('Tests passed!')


if __name__ == '__main__':
    test_merge_sort()
