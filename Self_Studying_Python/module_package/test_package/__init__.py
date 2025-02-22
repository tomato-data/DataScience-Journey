# 패키지를 읽어들일 때 __init__.py 가 가장 먼저 실행 됨.
# 따라서 패키지와 관련된 초기화 처리 등을 할 수 있음.

__all__ = ['module_a', 'module_b']

print('test_package를 읽어 들였습니다')