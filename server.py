#!/usr/bin/env python3
"""
简易HTTP服务器 - 用于测试PWA应用
运行后访问: http://localhost:8000
"""
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # 添加PWA所需的HTTP头
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"="*50)
        print(f"PWA测试服务器已启动！")
        print(f"="*50)
        print(f"")
        print(f"在手机浏览器中访问：")
        print(f"  http://<你的IP地址>:{PORT}")
        print(f"")
        print(f"例如：")
        print(f"  http://192.168.1.100:{PORT}")
        print(f"")
        print(f"然后在浏览器菜单中选择「添加到主屏幕」")
        print(f"")
        print(f"按 Ctrl+C 停止服务器")
        print(f"="*50)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
