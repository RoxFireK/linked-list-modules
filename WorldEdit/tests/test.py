import time
import random
from datetime import datetime

from core import BlockChange,LinkedStack

def generate_test_data(num_operation=100000):
    #生成测试数据,次数可改变
    print(f"正在生成{num_operation}条测试数据...")
    start_time = time.time()

    operation_types = ["set","cut","stack","replace","line"]
    #定义操作类型：放置，删除，堆叠，替换，生成列
    test_data = []

    for i in range(num_operation):
        op_type = random.choice(operation_types)
        block_count = random.randint(1,1000)
        timestamp = datetime.now().timestamp()+i
        #设置随机数据
        op_id = i

        operation = BlockChange(op_id,op_type,block_count,timestamp)
        test_data.append(operation)
        #记录测试数据

    end_time = time.time()
    print(f"数据生成完成，耗时：{end_time-start_time}秒")
    return test_data

def performance_test():
    #性能测试函数
    print("性能测试:撤销系统")

    test_data = generate_test_data(100000)

    stack = LinkedStack()

     #压栈操作
    print("开始压栈操作")
    start_time = time.time()
    for operation in test_data:
        stack.push(operation)
    push_time = time.time()-start_time
    print(f"压栈完成，耗时：{push_time}秒")
    print(f"当前栈大小为:{stack.get_size()}")

    #检测是否发生错误并进行警告操作(代替去重)
    error = stack.check()
    if error:
        print("检测到模组错误，如重复操作请输入//undo进行撤回")
    elif error == False :
        print("未找到日志文件")

    #出栈操作
    print("开始测试出栈操作")
    start_time = time.time()
    pop_count = 0
    while not stack.is_empty():
        stack.pop()
        pop_count +=1
    pop_time = time.time()-start_time
    print(f"出栈完成，耗时{pop_time}秒")

    #总结
    print("性能测试总结报告")
    print(f"总操作数量: {len(test_data)}")
    print(f"压栈耗时: {push_time:.4f}秒")
    print(f"出栈耗时: {pop_time:.4f}秒")
    print(f"平均每个操作处理时间: {(push_time + pop_time) / len(test_data) * 1000:.4f}毫秒")
    print(f"栈最大大小: {stack.get_size()}")

#运行性能测试
if __name__ == "__main__":
    performance_test()
