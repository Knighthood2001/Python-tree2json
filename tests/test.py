from tree2json import Tree2Json

tree_str = """
aaa/
├── data
│   ├── data.zip
│   ├── examples
│   ├── PUNet
│   └── results
├── datasets
│   ├── __pycache__
│   └── toy.py
└── utils
    ├── denoise.py
    ├── __pycache__
    └── transforms.py
"""

if __name__ == "__main__":
    converter = Tree2Json(mode="auto")
    converter.from_string(tree_str)
    converter.to_json("result1.json")
    print(converter.to_json())