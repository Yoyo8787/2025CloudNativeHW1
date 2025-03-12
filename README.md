## **2025CloudNativeHW1 CloudShop Marketplace - CLI Application**

### **專案簡介**

CloudShop 是一個簡單的線上市場平台，允許用戶進行商品買賣。此專案實作了一個基於命令行介面 (CLI) 的市場平台，提供了用戶註冊、商品創建、查詢、刪除等功能。

### **功能**

-   用戶註冊 (`REGISTER <username>`)
-   創建商品列表 (`CREATE_LISTING <username> <title> <description> <price> <category>`)
-   查詢商品 (`GET_LISTING <username> <listing_id>`)
-   刪除商品 (`DELETE_LISTING <username> <listing_id>`)
-   查詢分類商品 (`GET_CATEGORY <username> <category>`)
-   查詢最熱門的分類 (`GET_TOP_CATEGORY <username>`)

### **專案架構**

本專案使用了分層架構，包含：

1. **`main.py`** - 程式進入點，處理命令行指令與用戶交互。
2. **`controllers/`** - 控制器層，負責處理用戶指令並呼叫服務層。
3. **`services/`** - 服務層，負責業務邏輯與數據處理。
4. **`repositories/`** - 資料存取層，模擬存儲與查詢功能（使用字典）。
5. **`tests/`** - 測試層，包含單元測試與整合測試。

### **安裝與運行**

1. **環境要求**

    - Python 3.6 或更高版本

2. **安裝指示**
   本專案不需要額外的依賴或套件，僅依賴 Python 內建標準庫。

3. **執行測試**
   執行以下命令來進行測試：

    ```bash
    ./build.sh
    ```

4. **啟動應用程式**
   測試成功後，可以運行以下命令來啟動 CloudShop CLI：

    ```bash
    ./run.sh
    ```

5. **命令行範例**

    - 註冊用戶：

        ```bash
        # REGISTER Alice
        Success
        ```

    - 創建商品：

        ```bash
        # CREATE_LISTING Alice "Phone" "Brand new" 800 "Electronics"
        100001
        ```

    - 查詢商品：

        ```bash
        # GET_LISTING Alice 100001
        Phone|Brand new|800|2025-03-12 14:00:00|Electronics|Alice
        ```

    - 刪除商品：

        ```bash
        # DELETE_LISTING Alice 100001
        Success
        ```

    - 查詢分類商品：

        ```bash
        # GET_CATEGORY Alice "Electronics"
        Phone|Brand new|800|2025-03-12 14:00:00|Electronics|Alice
        ```

    - 查詢最熱門分類：
        ```bash
        # GET_TOP_CATEGORY Alice
        Electronics
        ```

### **專案結構**

```
2024CloudNativeHW1/
│── src/
│   ├── main.py              # CLI 入口
│   ├── controllers/         # 控制器層
│   ├── services/            # 服務層
│   ├── repositories/        # 資料存取層
│── tests/                   # 測試
│── build.sh                 # 構建腳本
│── run.sh                   # 啟動腳本
│── README.md                # 專案文檔
│── .git/                    # Git 版本控制
```
