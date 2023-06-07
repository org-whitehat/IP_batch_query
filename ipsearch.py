import csv
from xdbSearcher import XdbSearcher

def read_ips_from_txt(txt_file):
    """从 txt 文件中读取 IP 地址列表"""
    with open(txt_file, "r") as f:
        ips = [line.strip() for line in f if line.strip()]
    return ips

def save_results_to_csv(csv_file, results):
    """将查询结果保存到 CSV 文件中"""
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Country", "Province", "City", "ISP"])
        writer.writerows(results)

def main():
    txt_file = "./ips.txt"
    csv_file = "./results.csv"
    db_file = "./ip2region.xdb"
    
    # 加载 XDB 数据库
    searcher = XdbSearcher(db_file)
    
    # 读取 IP 地址列表
    ips = read_ips_from_txt(txt_file)
    
    # 查询 IP 区域信息
    results = []
    for ip in ips:
        region_str = searcher.search(ip)
        region_list = region_str.split("|")
        country = region_list[0].strip()
        province = region_list[2].strip()
        city = region_list[3].strip()
        isp = region_list[4].strip()
        results.append([ip, country, province, city, isp])
    
    # 保存查询结果到 CSV 文件
    save_results_to_csv(csv_file, results)
    
    # 关闭 XDB 查询器
    searcher.close()

if __name__ == "__main__":
    main()