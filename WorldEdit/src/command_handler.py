from core import LinkedStack,BlockChange
from datetime import datetime
#导入core中所需代码
#datetime获取时间戳

class CommandHandler:
    def __init__(self):
        self.undo_stack = LinkedStack()
        self.operation_id = 0
        #存储操作记录，初始化属性，用以分配id

    def handle(self,command,block_count = 1,block_type = None):
        command = command.strip()
        #输入命令并忽略无效字符

        valid_commands = {"//set","//cut","//replace","//line","//undo"}
        #限定命令
        if command not in valid_commands:
            if command.startswith("//"):
                return "指令无效"
            #检测用户是否输入无效指令
        if command == "//undo":
            return self._undo()
        #undo做出栈操作，其他四个指令做压栈操作
        else:
            return self._push_operation(command,block_count)
        
    def _push_operation(self,command,block_count):
        #压栈
        operation = BlockChange(self.operation_id,command,block_count,datetime.now().timestamp())
        self.undo_stack.push(operation)
        self.operation_id +=1
        return operation

    def _undo(self):
        #出栈
        if self.undo_stack.is_empty():
            return"没有可撤回的操作"
        last_operation = self.undo_stack.pop()
        return f"已撤回{last_operation.operationtype}"
        




