import sys

def name(x):
    a = "hwanseung"
    print(sys.getrefcount("hwanseung"))    

print(sys.getrefcount("hwanseung"))
a = "hwanseung"
print(sys.getrefcount("hwanseung"), sys.getrefcount(a))

name(1)
print(sys.getrefcount("hwanseung"))

# import gc
# import sys

# # Garbage collector를 강제로 실행하여 불필요한 객체를 정리합니다.
# gc.collect()

# # 추적 가능한 모든 객체를 가져옵니다.
# objects = gc.get_objects()

# # 각 객체의 참조 카운트를 출력합니다.
# for obj in objects:
#     ref_count = sys.getrefcount(obj) - 1  # 현재 함수 호출로 인한 추가 참조를 제외합니다.
#     print(f"Object: {repr(obj)}, Reference count: {ref_count}")
