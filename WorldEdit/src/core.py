class BlockChange:
    #模拟方块变更操作
    def __init__(self,blockid,operationtype,changed_count,timestamp):
        self.blockid = blockid
        self.operationtype = operationtype
        self.changed_count = changed_count
        self.timestamp = timestamp
        #定义方块类型，改变类型，改变数量，时间戳
    
    def __str__(self):
        return f"Op{self.blockid}({self.operationtype},blocks:{self.changed_count})"
    
    def __repr__(self):
        return self.__str__()
    #人类可读

class ListNode:
    #self代表节点

    def __init__(self,operation):
        #operation用于储存整个操作的所有信息，相比于val(只能储存一个方块的改变)更加高效
        self.operation = operation
        self.next = None

    def __str__(self):
        return f"ListNode({self.operation})"
        #打印对象人类可读,f表示format，可以在字符串中直接嵌入变量和表达式

class LinkedStack:
    #self代表栈

    def __init__(self):
        #初始化链栈
        self.top = None
        self._size = 0

    def is_empty(self):
        #判断栈是否为空
        return self.top is None
    
    def push(self,operation):
        #压栈操作
        newnode = ListNode(operation)
        newnode.next = self.top
        self.top = newnode
        self._size += 1
        return True
    
    def pop(self):
        #出栈操作
        if self.is_empty():
            return None
        pop_operation = self.top.operation
        self.top = self.top.next
        self._size -=1
        return pop_operation
    
    def peek(self):
        #查看栈顶元素
        if self.is_empty():
            return None
        return self.top.operation
    
    def get_size(self):
        #获取栈大小
        return self._size
    
    def clear(self):
        #清除栈
        self.top = None
        self.size = 0
    
    def check(self):
        try:
            with open("./logs/lastest","r") as f:
                lines = f.readlines()[-10:]
            for line in lines:
                if "Worldedit" in line and "error" in line:
                    return True
        except:
            return False
        # 检测是否出现网络故障以便对用户进行提醒
        # 由于在该模组操作过程中，用户可能会刻意进行重复操作
        # 并且即使因为网络问题发生重复操作，用户也可以进行撤回
        # 因此选择用在疑似发生网络故障导致重复操作时对用户进行提醒来代替去重(查看游戏根目录中的日志)

  
        
 #简单小测试  
if __name__ == "__main__":
    stack = LinkedStack()

    stack.push("1:放置方块")
    stack.push("2:删除方块")
    stack.push("3:填充区域")

    print(f"弹出: {stack.pop()}")
    print(f"当前栈顶: {stack.peek()}")
    print(f"栈大小: {stack.get_size()}")


    

    
