# Judge audit

Chạy: `python -m lab9.judge --csv <file> --audit 5`

| Tiêu chí | n | κ | Precision | Recall | Đạt FLOORS (κ≥0.6, P≥0.8, R≥0.7)? | Quyết định |
|---|---|---|---|---|---|---|
| tone_ok | 100 | 0,757 | 0,857 | 0,800 | Có | Dùng có kiểm soát cho tone |
| helpful | 100 | 0,375 | 1,000 | 0,300 | Không | Loại khỏi gate |

## ≥5 case audit thủ công
| # | Case | Judge nói | Người nói | Ai đúng? | Ghi chú |
|---|---|---|---|---|---|
| 1 | H-008 | PASS | FAIL | Người theo quy ước fixture | Xưng hô suồng sã; bổ sung ví dụ xưng hô không phù hợp. |
| 2 | H-029 | PASS | FAIL | Người | Có phần ra lệnh; đánh giá cả câu, không chỉ từ lịch sự đầu câu. |
| 3 | H-042 | FAIL | PASS | Người theo nhãn | Câu ngắn vẫn lịch sự; không bắt buộc xin lỗi khi ngữ cảnh không yêu cầu. |
| 4 | H-051 | FAIL | PASS | Người theo quy ước fixture | `refund` được phép; không phạt máy móc tiếng Anh. |
| 5 | H-070 | PASS | FAIL | Người theo rubric fixture | Emoji cười không phù hợp; thêm ví dụ theo ngữ cảnh. |
| 6 | H-088 | FAIL | PASS | Người theo nhãn | Lặp “Dạ” là lỗi nhỏ; xác định ngưỡng nghiêm trọng. |
| 7 | H-081 | FAIL | PASS | Chưa đủ ngữ cảnh | Note ghi nhãn người sai; yêu cầu người thứ hai đối chiếu ticket trước khi sửa nhãn. |
| 8 | HL-015 | PASS | FAIL | Người nếu xác minh được ledger | Note ghi ledger 40.000đ, reply 55.000đ; kiểm tra số tiền bằng code. |

## Kết luận
- Loại helpful: ma trận TP=9, FP=0, FN=21, TN=70; recall 0,300 và κ 0,375 dưới ngưỡng. Tone: TP=24, FP=4, FN=6, TN=66. Tỷ lệ lỗi quan sát → Rogan–Gladen là 0,28 → 0,30 (tone) và 0,09 → 0,30 (helpful), tính trên nhãn CSV gốc.
- Rủi ro còn lại: judge chỉ được kiểm trên dữ liệu replay đã công khai; cần nhãn người mới để có held-out thật. Nhận định audit dựa trên note fixture khi thiếu ngữ cảnh, không tự sửa nhãn nguồn.
