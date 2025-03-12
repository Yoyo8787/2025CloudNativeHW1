#!/bin/bash

echo "🚀 啟動 CloudShop CLI..."

# 確保 Python 版本正確
if ! command -v python &> /dev/null
then
    echo "❌ 錯誤：未安裝 Python。請安裝 Python 並重試。"
    read -p "按任意鍵結束..."
fi

# 設置 PYTHONPATH，將 src 資料夾添加到 Python 的模塊搜索路徑
export PYTHONPATH=$(pwd)/src:$PYTHONPATH

# 執行 Python 程式
python src/main.py

read -p "按任意鍵結束..."

