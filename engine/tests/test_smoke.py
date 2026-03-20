from ontomiko.diviner_v2 import divine_text

def run():
    samples = [
        "未来是否存在依靠潜势和惯性计算的通用拟构处理器",
        "能不能造一台无源白嫖无限算力机",
        "Minecraft 红石永动装置",
    ]
    for s in samples:
        print(divine_text(s).to_dict())

if __name__ == "__main__":
    run()
