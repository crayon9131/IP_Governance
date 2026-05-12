# IP 交易流程與合規分析 程式碼專案

這個專案收錄了用於比較傳統流程與 agentic architecture 的模擬與視覺化腳本，主題聚焦在 IP 交易流程與合規分析。

## 檔案說明

- `comparison.py`：使用 SimPy 建立端到端交易模擬。
- `gascost.py`：產生累積 gas cost 比較圖。
- `Latency.py`：產生協商延遲比較圖。
- `rag_compliance.py`：產生合規準確率比較圖。
- `run_all.py`：一次產生全部圖表。

## 環境需求

- Python 3.10 以上
- `requirements.txt` 中列出的相依套件

## 安裝方式

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 使用方式

一次產生所有圖表：

```bash
python run_all.py
```

個別產生圖表：

```bash
python gascost.py
python Latency.py
python rag_compliance.py
python comparison.py
```

所有輸出圖片都會寫入 `results/` 目錄。
