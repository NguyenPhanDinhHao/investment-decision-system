# investment-decision-system
# 🚀 Hệ Thống Hỗ Trợ Ra Quyết Định Đầu Tư (NPV – IRR – ML – Bayesian)

---

## 📌 Giới thiệu

Dự án này xây dựng một **hệ thống hỗ trợ ra quyết định đầu tư** dựa trên phân tích dòng tiền.

Hệ thống kết hợp:

* Phương pháp tài chính (NPV, IRR)
* Giải thuật số (Chia đôi, Newton, Secant)
* Mô phỏng rủi ro (Monte Carlo)
* Machine Learning (dự báo dòng tiền)
* Bayesian (cập nhật theo dữ liệu mới)
* Yếu tố hành vi nhà đầu tư

👉 Mục tiêu:

> Giúp nhà đầu tư đánh giá, so sánh và ra quyết định trong điều kiện không chắc chắn.

---

## 🎯 Bài toán

Nhà đầu tư thường gặp:

* Dòng tiền tương lai không chắc chắn
* Nhiều dự án để lựa chọn
* Khẩu vị rủi ro khác nhau

👉 Cần:

* Đánh giá hiệu quả đầu tư
* So sánh nhiều dự án
* Hỗ trợ ra quyết định

---

## ⚙️ Chức năng chính

### 1. Phân tích tài chính

* NPV (Giá trị hiện tại ròng)
* IRR (Tỷ suất hoàn vốn nội bộ)

Giải phương trình:

```
NPV(r) = 0
```

---

### 2. Giải thuật tìm nghiệm

* Chia đôi (ổn định)
* Newton (nhanh)
* Secant (không cần đạo hàm)

---

### 3. Trực quan hóa

* Đồ thị NPV – r
* Xác định IRR
* So sánh nhiều dự án

---

### 4. Mô phỏng rủi ro

* Dòng tiền có nhiễu
* Chạy nhiều lần (Monte Carlo)

👉 Output:

* Phân phối NPV
* Xác suất lỗ

---

### 5. Machine Learning (giai đoạn sau)

* Dự báo dòng tiền
* Mô hình:

  * Linear Regression
  * Random Forest
  * ARIMA / LSTM

---

### 6. Bayesian

* Cập nhật dự báo theo dữ liệu mới
* Giảm sai lệch theo thời gian

---

### 7. Yếu tố hành vi

* Mức chấp nhận rủi ro
* Ưu tiên lợi nhuận / ổn định

👉 Hệ thống đưa ra gợi ý phù hợp

---

## 📊 Ví dụ dòng tiền

```
Năm 0: -2000
Năm 1: +400
Năm 2: +600
Năm 3: +800
Năm 4: +800
Năm 5: +1200
```

👉 Kết quả:

* IRR ≈ 21.5%
* Quyết định: đầu tư nếu IRR > chi phí vốn

---

## 🗂️ Cấu trúc dự án

```
project/
│
├── data/
├── notebooks/
├── src/
│   ├── npv.py
│   ├── irr.py
│   ├── simulation.py
│   ├── ml_model.py
│   └── bayesian.py
│
├── dashboard/
├── reports/
├── README.md
```

---

## 🛠️ Công nghệ

* Python (NumPy, Pandas, Matplotlib)
* Scikit-learn
* SQL
* Power BI / Streamlit

---

## 🗺️ Lộ trình

### Giai đoạn 1

* NPV, IRR
* Vẽ đồ thị

### Giai đoạn 2

* Nhiều dự án
* Monte Carlo
* Dashboard

### Giai đoạn 3 (NCKH)

* So sánh IRR vs NPV

### Giai đoạn 4 (Năm 3)

* Machine Learning
* Bayesian
* Behavior

---

## 📈 Kết quả mong đợi

* Hệ thống đánh giá đầu tư
* Phân tích rủi ro
* Dự báo dòng tiền
* Dashboard trực quan

---

## 🔥 Insight quan trọng

* IRR là mức hòa vốn
* NPV là giá trị thực
* Nhiều IRR → không đáng tin
* Rủi ro phải mô phỏng

---

## 👤 Tác giả

* Sinh viên năm 2
* Ngành: Marketing / Data
* Định hướng: Data + Finance

---

## ⭐ Kết luận

> “Đây không chỉ là bài toán tính IRR, mà là xây dựng hệ thống ra quyết định giống như một nhà đầu tư thực thụ.”

---
