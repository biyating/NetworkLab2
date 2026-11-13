# GitHub 仓库地址: https://github.com/biyating/NetworkLab2
import socket
import sys

def main():
    # T3 参数化：检查参数是否充足
    if len(sys.argv) < 3:
        print("用法: python webget.py host path [port]")
        print("示例: python webget.py www.bjfu.edu.cn /")
        sys.exit(1)

    host = sys.argv[1]
    path = sys.argv[2]
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 80

    # 构造 HTTP 请求报文 (必须带 Connection: close)
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10) # T1: 设置超时时间
    
    try:
        print(f"正在连接 {host}:{port} ...")
        s.connect((host, port))
        s.sendall(request.encode('utf-8'))
        
        response_data = b""
        recv_count = 0
        
        # T1：把 recv 放进循环
        while True:
            try:
                data = s.recv(4096)
                if not data:
                    break # 收到空数据，代表对端关闭了连接
                recv_count += 1
                response_data += data
                print(f"recv() 第 {recv_count} 次调用，收到 {len(data)} 字节")
            except socket.timeout:
                print("超时了！")
                break
                
    except Exception as e:
        print(f"连接出错: {e}")
        return
    finally:
        s.close()

    # T2：解析 HTTP 响应
    header_data, _, body_data = response_data.partition(b"\r\n\r\n")
    header_text = header_data.decode('utf-8', errors='ignore')
    
    print("\n--- 响应头 ---")
    print(header_text)
    
    # 提取状态码
    if header_text:
        status_line = header_text.split('\r\n')[0]
        print(f"\n[状态码]: {status_line.split(' ')[1]}")
    
    # T2：用二进制模式保存文件
    with open("output.html", "wb") as f:
        f.write(body_data)
    print(f"\n--- Body 已保存到 output.html 文件 ---")

if __name__ == "__main__":
    main()