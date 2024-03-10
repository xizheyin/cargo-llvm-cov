import re
import sys



# 检查是否有文件名作为命令行参数传入
if len(sys.argv) != 3:
    print("Usage: python coverage_calc.py <path_to_coverage_report>")
    exit(1)



# 读取覆盖率报告文件路径
coverage_report_path = sys.argv[1]

# 需要分析的库名称
library_name = sys.argv[2]  # 例如：url

# 初始化统计数据
total_lines = 0
covered_lines = 0

# 正则表达式模式用于提取行覆盖率数据
pattern = re.compile(rf"\.cargo/registry/src/index\.crates\.io-[^/]+/{library_name}-[\d\.]+/src/.+\.rs\s+[\d]+[\s]+[\d]+[\s]+([\d\.]+)%[\s]+[\d]+[\s]+[\d]+[\s]+([\d\.]+)%[\s]+([\d]+)[\s]+([\d]+)")

# 读取覆盖率报告文件
with open(coverage_report_path, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            line_coverage = float(match.group(1))
            lines_total = int(match.group(3))
            lines_missed = int(match.group(4))
            total_lines += lines_total
            covered_lines += lines_total - lines_missed

# 计算与打印结果
if total_lines == 0:
    print(f"No lines to cover in {library_name}.")
else:
    overall_coverage = (covered_lines / total_lines) * 100
    print(f"Total Lines: {total_lines}")
    print(f"Covered Lines: {covered_lines}")
    print(f"Overall coverage for library {library_name}: {overall_coverage:.2f}%")