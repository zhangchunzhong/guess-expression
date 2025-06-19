import pandas as pd

def excel_to_js_objects(input_path, output_path, img_folder):
    """
    转换Excel前两列到JS对象格式
    参数：
    input_path: Excel文件路径
    output_path: 输出JS文件路径
    img_folder: 图片存储路径前缀
    """
    try:
        # 读取Excel前两列 (假设没有表头)
        df = pd.read_excel(input_path, usecols=[0, 1], header=None)
        df.columns = ['file_code', 'emotion_ch']
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                # 构造完整图片路径
                file_name = f"{row['file_code']}.JPG"  # 确保大写扩展名
                full_path = f"{img_folder}/{file_name}"
                
                # 生成格式化字符串
                line = f"{{ image: '{full_path}', answer: '{row['emotion_ch']}' }},"
                f.write(line + '\n')
        
        print(f"转换完成！共处理 {len(df)} 条记录")
        print(f"输出文件：{output_path}")

    except Exception as e:
        print(f"处理出错：{str(e)}")

# 使用示例（根据实际路径修改）
if __name__ == "__main__":
    excel_path = "/Users/zhangcz/Downloads/ASD/kdef/DATAMATRIXKDEF-zh.xls"  # 输入Excel路径
    js_output = "output_data.js"  # 输出JS文件路径
    img_prefix = "/Users/zhangcz/Downloads/ASD/kdef/pics"  # 图片存储目录
    
    excel_to_js_objects(excel_path, js_output, img_prefix)

