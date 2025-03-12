#!/bin/bash

echo "🔧 開始構建 CloudShop CLI..."

# 檢查 Python 是否已安裝
if ! command -v python &> /dev/null
then
    echo "❌ 錯誤：未安裝 Python。請安裝 Python 並重試。"
fi

export PYTHONPATH=$(pwd)/src:$PYTHONPATH
echo "🔍 已設置 PYTHONPATH: $PYTHONPATH"  # 顯示設置的 PYTHONPATH

# 執行測試
echo "🧪 執行測試..."
python -m unittest discover tests

# 測試是否成功
if [ $? -eq 0 ]; then
    echo "✅ 測試通過！CloudShop 準備就緒 🎉"
else
    echo "❌ 測試失敗，請檢查錯誤訊息！"
fi

# 保持終端開啟
read -p "按任意鍵結束..."  # 這行讓終端保持開啟直到按鍵