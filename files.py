from ctypes.wintypes import POINT
import os
import sys

COLOR = {"暂无评定": "BFBFBF", "入门": "FE4C61", "普及-": "F39C11", "普及/提高-": "FFC116", "普及+/提高": "52C41A", "提高+/省选-": "3498DB", "省选/NOI-": "9D3DCF",
         "NOI/NOI+/CTSC": "0E1D69", "Algorithem": "2949B4", "Source": "13C2C2", "Time": "3498DB", "District": "52C41A", "Special": "F39C11"}
ROOT = ["E:", "OI", "Luogu-Solution", "docs"]


def c(args):
    return os.sep.join(ROOT + args)


def new(path):
    if not os.path.exists(path):
        os.makedirs(path)


def new_file(path):
    if not os.path.exists(path):
        f = open(path, 'x')
        f.close()


prob = sys.argv[1:]
if prob[0].startswith('P'):
    bank = ["主题库"]
if prob[0].startswith('CF'):
    bank = ["CodeForces"]
if prob[0].startswith('SP'):
    bank = ["SPOJ"]
if prob[0].startswith('AT'):
    bank = ["AtCoder"]
if prob[0].startswith('UVA'):
    bank = ["UVA"]
if prob[0].startswith('T'):
    bank = ["团队题目"]
diff = list(map(lambda x: x.strip(), input("难度(用序号表示): ").split()))
if diff[0] == '0':
    diff = ["暂无评定"]
if diff[0] == '1':
    diff = ["入门"]
if diff[0] == '2':
    diff = ["普及-"]
if diff[0] == '3':
    diff = ["普及/提高-"]
if diff[0] == '4':
    diff = ["普及+/提高"]
if diff[0] == '5':
    diff = ["提高+/省选-"]
if diff[0] == '6':
    diff = ["省选/NOI-"]
if diff[0] == '7':
    diff = ["NOI/NOI+/CTSC"]
PROBLEM = ["题库", bank[0], diff[0].replace("/", "、"), prob[0]]
cmd = input(">>> ")
while cmd != 'q':
    if cmd == "p":
        algo = list(map(lambda x: x.strip(), input("算法: ").split()))
        src = list(map(lambda x: x.strip(), input("来源: ").split()))
        dist = list(map(lambda x: x.strip(), input("地区: ").split()))
        time = list(map(lambda x: x.strip(), input("时间: ").split()))
        spe = list(map(lambda x: x.strip(), input("特殊题目: ").split()))
        time_limit = input('时间限制(ms): ')
        memory_limit = input('内存限制(MB): ')

        new(c(["题库"] + bank + [diff[0].replace("/", "、")] + prob))
        new(c(["难度"] + [diff[0].replace("/", "、")]))
        for a in algo:
            new(c(["算法"] + [a]))

        if dist:
            for d in dist:
                new(c(["地区"] + [d]))
        if time:
            for t in time:
                new(c(["时间"] + [t]))
        if spe:
            for s in spe:
                new(c(["特殊题目"] + [s]))
        if src:
            for s in src:
                new(c(["来源"] + [s]))

        new_file(c(["题库"] + ["index.md"]))
        new_file(c(["题库"] + bank + ["index.md"]))
        new_file(c(["题库"] + bank + [diff[0].replace("/", "、")] + ["index.md"]))
        new_file(
            c(["题库"] + bank + [diff[0].replace("/", "、")] + prob + ["Problem.md"]))

        new_file(c(["难度"] + ["index.md"]))
        new_file(c(["难度"] + [diff[0].replace("/", "、")] + ["index.md"]))

        new_file(c(["算法"] + ["index.md"]))
        for a in algo:
            new_file(c(["算法"] + [a] + ["index.md"]))

        if dist:
            new_file(c(["地区"] + ["index.md"]))
            for d in dist:
                new_file(c(["地区"] + [d] + ["index.md"]))

        if time:
            new_file(c(["时间"] + ["index.md"]))
            for t in time:
                new_file(c(["时间"] + [t] + ["index.md"]))

        if spe:
            new_file(c(["特殊题目"] + ["index.md"]))
            for s in spe:
                new_file(c(["特殊题目"] + [s] + ["index.md"]))

        if src:
            new_file(c(["来源"] + ["index.md"]))
            for s in src:
                new_file(c(["来源"] + [s] + ["index.md"]))

        print("输入题面(Press 'EOF' to exit)")
        with open(c(["题库"] + bank + [diff[0].replace("/", "、")] + prob + ["Problem.md"]), 'w', encoding='utf-8') as f:
            t = input()[2:]

            # write title
            f.write("# [" + prob[0] + t +
                    "](https://www.luogu.com.cn/problem/" + prob[0] + ")\n\n")

            # add tags
            f.write(
                f"***Tags:*** **[<font color={COLOR[diff[0]]}>" + diff[0] + "</font>](../../../../难度/" + diff[0] + "/index.md)")
            for a in algo:
                f.write(
                    f"$\\quad$[<font color={COLOR['Algorithem']}>" + a + "</font>](../../../../算法/" + a + "/index.md)")
            for s in src:
                f.write(
                    f"$\\quad$[<font color={COLOR['Source']}>" + s + "</font>](../../../../来源/" + s + "/index.md)")
            for d in dist:
                f.write(
                    f"$\\quad$[<font color={COLOR['District']}>" + d + "</font>](../../../../地区/" + d + "/index.md)")
            for t in time:
                f.write(
                    f"$\\quad$[<font color={COLOR['Time']}>" + t + "</font>](../../../../时间/" + t + "/index.md)")
            for s in spe:
                f.write(
                    f"$\\quad$[<font color={COLOR['Special']}>" + s + "</font>](../../../../特殊题目/" + s + "/index.md)")
            f.write("**\n\n")

            # add limits
            f.write(
                f"***Time Limit: " + (time_limit + 'ms' if time_limit else 'Unknown') + "***\n***Memory Limit: " + (memory_limit + 'MB' if memory_limit else 'Unknown') + "***\n\n")

            # 正文
            txt = False
            while t != 'EOF':
                if txt and t == '```':
                    f.write(t + 'txt\n')
                    txt = False
                else:
                    f.write(t + '\n')
                    if t.startswith("### 样例输入 #") or t.startswith("### 样例输出 #"):
                        txt = True
                t = input()

        with open(c(["题库", "index.md"]), 'w', encoding='utf-8') as f:
            f.write("# 题库\n" + "\n" + "按题库分类题解\n")
        with open(c(["题库"] + bank + ["index.md"]), 'w', encoding='utf-8') as f:
            f.write("# " + (bank[0] if bank[0] != '主题库' else '洛谷主题库') +
                    "\n\n" + (bank[0] if bank[0] != '主题库' else '洛谷主题库') + "题目的题解\n")
        with open(c(["题库"] + bank + [diff[0].replace("/", "、")] + ["index.md"]), 'w', encoding='utf-8') as f:
            f.write("# " + (bank[0] if bank[0] != '主题库' else '洛谷主题库') + " <font color=" + COLOR[diff[0]] + ">" + diff[0] + "</font>\n\n" +
                    (bank[0] if bank[0] != '主题库' else '洛谷主题库') + "中<font color=" + COLOR[diff[0]] + ">" + diff[0] + "</font>题目的题解")

        with open(c(["算法", "index.md"]), 'w', encoding='utf-8') as f:
            f.write("# 算法\n\n按算法分类题解")
        for a in algo:
            with open(c(["算法", a, "index.md"]), 'w', encoding='utf-8') as f:
                f.write("# <font color=2949B4>" + a +
                        "</font>\n\n使用<font color=2949B4>" + a + "</font>算法的题目的题解")

        with open(c(["难度", "index.md"]), 'w', encoding='utf-8') as f:
            f.write("# 难度\n\n按难度分类题解")
        with open(c(["难度", diff[0], "index.md"]), 'w', encoding='utf-8') as f:
            f.write("# <font color=" + COLOR[diff[0]] + ">" + diff[0] +
                    "</font>\n\n<font color=" + COLOR[diff[0]] + ">" + diff[0] + "</font>题目的题解")

        if dist:
            with open(c(["地区"] + ["index.md"]), 'w', encoding='utf-8') as f:
                f.write("# 地区\n\n按地区分类题解")
            for d in dist:
                with open(c(["地区"] + [d] + ["index.md"]), 'w', encoding='utf-8') as f:
                    f.write("# <font color=" + COLOR['District'] + ">" + d +
                            "</font>\n\n来自<font color=" + COLOR['District'] + ">" + d + "</font>的题目的题解")

        if time:
            with open(c(["时间"] + ["index.md"]), 'w', encoding='utf-8') as f:
                f.write("# 时间\n\n按时间分类题解")
            for t in time:
                with open(c(["时间"] + [t] + ["index.md"]), 'w', encoding='utf-8') as f:
                    f.write("# <font color=3498DB>" + t +
                            "</font>\n\n<font color=3498DB>" + t + "</font>题目的题解")

        if spe:
            with open(c(["特殊题目"] + ["index.md"]), 'w', encoding='utf-8') as f:
                f.write("# 特殊题目\n\n归纳整理特殊题目（不含O2优化）")
            for s in spe:
                with open(c(["特殊题目"] + [s] + ["index.md"]), 'w', encoding='utf-8') as f:
                    f.write("# <font color=" + COLOR["Special"] +
                            ">" + s + "</font>\n\n使用" + s + "判题方法的题目的题解")

        if src:
            with open(c(["来源"] + ["index.md"]), 'w', encoding='utf-8') as f:
                f.write("# 来源\n\n按来源分类题解")
            for s in src:
                with open(c(["来源"] + [s] + ["index.md"]), 'w', encoding='utf-8') as f:
                    f.write("# <font color=13C2C2>" + s +
                            "</font>\n\n来自<font color=13C2C2>" + s + "</font>的题目的题解")

    elif cmd == 'cpp':
        num = int(input("输入C++题解数量: "))
        if num == 1:
            with open(c(PROBLEM + ["Code.cpp"]), 'x', encoding='utf-8') as f:
                t = input("输入AC程序(Press 'EOF' to exit)\n")
                while t != 'EOF':
                    f.write(t + '\n')
                    t = input()
            new_file(c(PROBLEM + ["C++.md"]))
        else:
            for i in range(1, num + 1):
                with open(c(PROBLEM + [f"Code{i}.cpp"]), 'x', encoding='utf-8') as f:
                    t = input(f"输入AC程序{i}(Press 'EOF' to exit)\n")
                    while t != 'EOF':
                        f.write(t + '\n')
                        t = input()
                new_file(c(PROBLEM + [f"C++{i}.md"]))

    elif cmd == 'py':
        num = int(input("输入Python题解数量: "))
        if num == 1:
            with open(c(PROBLEM + ["Code.py"]), 'x', encoding='utf-8') as f:
                t = input("输入AC程序(Press 'EOF' to exit)\n")
                while t != 'EOF':
                    f.write(t + '\n')
                    t = input()
            new_file(c(PROBLEM + ["Python.md"]))
        else:
            for i in range(1, num + 1):
                with open(c(PROBLEM + [f"Code{i}.py"]), 'x', encoding='utf-8') as f:
                    t = input(f"输入AC程序{i}(Press 'EOF' to exit)\n")
                    while t != 'EOF':
                        f.write(t + '\n')
                        t = input()
                new_file(c(PROBLEM + [f"Python{i}.md"]))

    elif cmd == 'h' or cmd == '':
        print("p: 添加题目")
        print("cpp: 添加C++题解")
        print("addcpp: 新增C++题解")
        print("py: 添加Python3题解")
        print("addpy: 新增Python3题解")
        print("q: 退出程序")

    elif cmd == 'addcpp':
        cnt = len([i for i in os.listdir(c(PROBLEM)) if i.endswith(".cpp")])
        if cnt == 1:
            os.rename(c(PROBLEM + ['Code.cpp']), c(PROBLEM + ['Code1.cpp']))
            os.rename(c(PROBLEM + ['C++.md']), c(PROBLEM + ['C++1.md']))
        num = int(input("输入C++题解数量: "))
        for i in range(cnt + 1, cnt + num + 1):
            with open(c(PROBLEM + [f"Code{i}.cpp"]), 'x', encoding='utf-8') as f:
                t = input(f"输入AC程序{i}(Press 'EOF' to exit)\n")
                while t != 'EOF':
                    f.write(t + '\n')
                    t = input()
            new_file(c(PROBLEM + [f"C++{i}.md"]))

    elif cmd == 'addpy':
        cnt = len([i for i in os.listdir(c(PROBLEM)) if i.endswith(".py")])
        if cnt == 1:
            os.rename(c(PROBLEM + ['Code.py']), c(PROBLEM + ['Code1.py']))
            os.rename(c(PROBLEM + ['Python.md']), c(PROBLEM + ['Python1.md']))
        num = int(input("输入Python题解数量: "))
        for i in range(cnt + 1, cnt + num + 1):
            with open(c(PROBLEM + [f"Code{i}.py"]), 'x', encoding='utf-8') as f:
                t = input(f"输入AC程序{i}(Press 'EOF' to exit)\n")
                while t != 'EOF':
                    f.write(t + '\n')
                    t = input()
            new_file(c(PROBLEM + [f"Python{i}.md"]))
    cmd = input(">>> ")
