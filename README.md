# tree2json

将树形目录结构转换为结构化的 JSON 格式。

`tree2json` 是一个轻量级 Python 工具，用于解析目录树格式的文本（例如 `tree` 命令的输出或自定义目录结构字符串），并将其转换为层次化的 JSON 结构，适用于可视化、自动化或结构分析任务。

---

## 📦 安装

从 PyPI 安装：

```bash
pip install tree2json

```
或克隆本地进行开发使用：

```bash
git clone https://github.com/Knighthood2001/tree2json.git
cd tree2json
pip install -e .
```

---

## 🧩 功能特色

* 支持解析纯文本目录树结构
* 支持多级嵌套的文件和文件夹
* 输出结构化 JSON，包含完整目录层级信息

---

## 🚀 快速使用

### Python 示例
**(PS:也可以查看tests/test.py)**

```python
from tree2json import Tree2Json

tree_str = """
.
├── data
│   ├── data.zip
│   └── results
├── README.md
└── utils
    ├── denoise.py
    └── transforms.py
"""

converter = Tree2Json()
converter.from_string(tree_str)
json_str = converter.to_json_file("output.json")  # 保存文件并返回字符串
```

### 输出示例

```json
{
    "level": 0,
    "type": "dir",
    "name": ".",
    "description": "",
    "child": [
        {
            "level": 1,
            "type": "dir",
            "name": "data",
            "description": "",
            "child": [
                {
                    "level": 2,
                    "type": "file",
                    "name": "data.zip",
                    "description": "",
                    "child": []
                },
                {
                    "level": 2,
                    "type": "dir",
                    "name": "results",
                    "description": "",
                    "child": []
                }
            ]
        },
        {
            "level": 1,
            "type": "file",
            "name": "README.md",
            "description": "",
            "child": []
        },
        {
            "level": 1,
            "type": "dir",
            "name": "utils",
            "description": "",
            "child": [
                {
                    "level": 2,
                    "type": "file",
                    "name": "denoise.py",
                    "description": "",
                    "child": []
                },
                {
                    "level": 2,
                    "type": "file",
                    "name": "transforms.py",
                    "description": "",
                    "child": []
                }
            ]
        }
    ]
}
```

---

## 🔧 API 接口说明

### `Tree2Json(mode="auto")`

* `mode`：缩进识别模式（`auto` | `step3` | `step4`）

### `.from_string(tree_str)`

从树状字符串中解析目录结构。

### `.to_dict()`

以 Python 字典形式返回目录结构。

### `.to_json_file(path=None)`

将结构保存为 JSON 文件（可选）。始终返回 JSON 字符串。

---

## 📄 许可证

本项目使用 MIT 开源许可证。

---

## 💬 问题反馈 & 贡献

欢迎在 [issue 页面](https://github.com/Knighthood2001/tree2json/issues) 提出问题或提交 PR！
## TODO
- [√] 项目根目录的完善
- [ ] 适配更多类型的目录树
- [√] 将目录树注释提取出来，支持 ← # // -- 作为注释分隔符

## 版本

### v0.1.0
- 初始版本
### v0.1.1
- 调整了README.md
### v0.1.2
-  [√] 项目根目录的完善
### v0.1.3
- 支持 ← # // -- 作为注释分隔符
### v0.1.4
- 解决根目录结尾为/或者\\的问题

