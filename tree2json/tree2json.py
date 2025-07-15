import re
import json
import os   

class Tree2Json:
    def __init__(self, mode="auto"):
        self.mode = mode
        self.nodes = []
        self.root = None

    def find_branch_pos(self, line):
        match = re.search(r'[├└]──', line)
        return match.start() if match else -1

    def compute_level(self, pos):
        if pos < 0:
            return None
        if self.mode == "auto":
            if pos % 4 == 0:
                return pos // 4
            elif pos % 3 == 0:
                return pos // 3
            else:
                return round(pos / 4 if pos % 4 < pos % 3 else pos / 3)
        elif self.mode == "step3":
            return pos // 3
        elif self.mode == "step4":
            return pos // 4
        else:
            raise ValueError("mode must be 'auto', 'step3', or 'step4'")

    def parse_lines(self, tree_lines):
        self.nodes = []

        for line in tree_lines:
            pos = self.find_branch_pos(line)
            if pos == -1:
                continue
            level = self.compute_level(pos) + 1  # +1: 根目录为 level 0

            content = line[pos + 3:].strip()
            # 支持 ← # // -- 作为注释分隔符
            match = re.match(r'^(.*?)(?:\s*(?:←|#|//|--)\s*)(.+)$', content)
            if match:
                name_part = match.group(1).strip()
                desc_part = match.group(2).strip()
            else:
                name_part = content
                desc_part = ""

            node = {
                "level": level,
                "type": "file" if '.' in name_part else "dir",
                "name": name_part,
                "description": desc_part,
                "child": []
            }

            self.nodes.append(node)

    def build_tree(self):
        stack = [self.root]
        for node in self.nodes:
            # 回退到正确的目录层级，跳过 file
            while len(stack) > 1 and (stack[-1]["level"] >= node["level"] or stack[-1]["type"] != "dir"):
                stack.pop()

            parent = stack[-1]
            parent["child"].append(node)

            # 只有是目录才入栈（file 不能作为父节点）
            if node["type"] == "dir":
                stack.append(node)


    def from_string(self, tree_str):
        lines = tree_str.strip().splitlines()
        if not lines:
            raise ValueError("tree string is empty")

        # 解析第一行作为根节点名称
        first_line = lines[0].strip()
        if first_line == ".":
            root_name = "."
        else:
            # root_name = os.path.basename(first_line.replace("\\", "/"))  # 防止 Windows 路径
            # 修复：移除末尾的路径分隔符
            root_name = first_line.rstrip("/\\")
            # 如果还有路径分隔符，取最后一部分
            if "/" in root_name or "\\" in root_name:
                root_name = os.path.basename(root_name.replace("\\", "/"))
        
        # 确保根目录名称不为空
        if not root_name:
            root_name = "root"
            
        self.root = {
            "level": 0,
            "type": "dir",
            "name": root_name,
            "description": "",
            "child": []
        }

        self.parse_lines(lines[1:])  # 跳过第一行
        self.build_tree()

    def to_dict(self):
        return self.root

    def to_json(self, path=None):
        json_str = json.dumps(self.root, indent=4, ensure_ascii=False)

        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(json_str)

        return json_str

