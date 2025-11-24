from command_handler import CommandHandler

def get_region():
    try:
        x1,y1,z1 = map(int,input("请输入起始点xyz坐标（间隔为空格）").split())
        #获取起始点坐标

        x2,y2,z2 = map(int,input("请输入终止点xyz坐标（间隔为空格）").split())
        #获取终止点坐标

        width = abs(x1-x2) + 1
        height = abs(y1-y2) + 1
        depth = abs(z1-z2) + 1
        block_count = width*height*depth
        #方块默认为1*1*1，体积大小即为方块数量
        return block_count
    
    except ValueError:
        #ValueError可以检测数据形式是否正确
        print("请输入有效坐标")
        return get_region()
    
def get_block_type(command):
    #获取方块类型
    if command in ["//set","//replace","//line"]:
        block_type = input("请输入方块类型：")
        return block_type
    return None

#以下为控制台输出内容,帮助用户使用指令
def main():
    handler = CommandHandler()
    print("欢迎使用WorldEdit（python版）:)")
    print("输入'help'查看命令")

    while True:
        command = input(">>")

        if command == "help":
            print("可用命令：")
            print("//set         放置方块")
            print("//cut         删除方块")
            print("//replace     替换方块")
            print("//line        生成直线")
            print("//undo        撤回操作")

        elif command in ["//set","//cut","//replace","//line"]:
            block_count = get_region()
            block_type = get_block_type(command)
            result = handler.handle(command,block_count)
            print(f"已执行指令{command}，改变方块数量{block_count}",end="")
            if block_type:
                print(f"方块类型{block_type}")
            else:
                print()

        elif command == "//undo":
            result = handler.handle(command)
            print(result)

        else:
            result = handler.handle(command)
            print(result)
        
if __name__ == "__main__":
    main()
            
