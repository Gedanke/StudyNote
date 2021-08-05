di = list(range(1, 12))

# def f():
#     for i in range(1, len(di) + 1):
#         path = "module_" + str(i) + "/lecture_"
#         for j in di[i - 1]:
#             open(path + str(j) + ".md", "w")



from pyquery import PyQuery

t='''
<div data-v-daa3f53a="" class="menu-content calc"><div data-v-68b0779c="" data-v-daa3f53a="" class="class-menu-contaniner"><div data-v-68b0779c="" class="class-menu-title"><div data-v-68b0779c="" class="active-block"></div>
        课程目录
    </div> <div data-v-68b0779c="" class="class-menu-box" style="max-height: 1251px;"><!----> <!----> <div data-v-68b0779c="" class="class-menu-block"><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        开篇寄语：算法功底决定Offer质量
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第01讲：常用数据结构
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第02讲：高级数据结构
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第03讲：排序
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第04讲：递归与回溯
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis   isclick  class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第05讲：深度与广度优先搜索
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第06讲：动态规划
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第07讲：二分搜索与贪婪
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第08讲：高频真题解析 I
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第09讲：高频真题解析 II
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第10讲：高频真题解析 III（上)
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第10讲：高频真题解析 III（下)
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        第11讲：高频真题解析 IV
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div><div data-v-68b0779c="" class="class-level-one over-ellipsis    class-level-one-detail"><div data-v-68b0779c="" class="text-wrap"><div data-v-68b0779c="" class="content">
                        彩蛋：算法面试冲刺
                    </div> <div data-v-68b0779c="" class="item-status-wrap"><!----></div></div></div></div></div></div></div>
'''

def ff():
    c = PyQuery(t)
    l = c.text().split("\n")
    for _ in l:
        if _.find("：") != -1 or _.find("|") != -1:
            print(_)
            if _.find("模块") != -1:
                print("* ")
ff()