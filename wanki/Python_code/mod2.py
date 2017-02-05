PI = 3.141592

class Math:
    def solv(self, r):
        return PI*(r**2)

def sum(a, b):
    return a+b

## python mod2 했을 때 실행됨.
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))