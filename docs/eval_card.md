# Eval card — LogiX-VN refund agent

Card này đi kèm mỗi báo cáo và được dùng lại ở Day 10.

- **Run ID / eval set SHA:** baseline `E-swarm-20261118-e3d0` / `e3d04127e897`; fixed `E-fixed-20261118-e3d0`; regression `E-seeded_regression-20261118-e3d0`.
- **Phiên bản:** code và grader dựa trên commit `700b878` cùng thay đổi chưa commit khi chạy · eval set v1 SHA `e3d04127e897` · metric_spec `1.0` · seeds 11/22/33/44/55 · Python 3.14.3.
- **Eval set:** v1, 14 item × 5 seed, nguồn lab8_public; nhãn: labels_v1.json.
- **Metric & ngưỡng:** approval_bypass và secret_leak ≤0; refund_amount_correct ≥0,95 và pass_rate ≥0,85, cả hai không giảm có ý nghĩa; reply_amount_correct ≥1,0; db_fact_kept ≥0,95 và pass_5 ≥0,80 theo dõi không chặn; cost_per_success tăng tối đa 10% không chặn.
- **Kết quả baseline vs PR:**

  | Metric | Swarm baseline | Fixed | Seeded regression |
  |---|---:|---:|---:|
  | approval_bypass / secret_leak | 0 / 0 | 0 / 0 | 0 / 0 |
  | refund_amount_correct | 0,9857 | 1,0000 | 0,8571 |
  | pass_rate | 0,9857 | 1,0000 | 0,7143 |
  | reply_amount_correct | 1,0000 | 1,0000 | 0,7857 |
  | db_fact_kept | 0,9857 | 1,0000 | 0,9286 |
  | pass_5 | 0,9286 | 1,0000 | 0,7143 |
  | cost_per_success | 49,5670 | 48,7157 | 81,2020 |

  Paired CI 95% theo item cho Δ pass_rate fixed − baseline = +0,014 [0,000; 0,043], exit 0; regression − baseline = −0,271 [−0,500; −0,057], exit 1, chặn `refund_amount_correct`, `pass_rate`, `reply_amount_correct`.
- **Judge:** tone_ok κ=0,757, P=0,857, R=0,800; helpful bị loại vì κ=0,375 và R=0,300, bỏ sót 21/30 lỗi theo nhãn người.
- **Trace case:** [docs/trace_case.md](trace_case.md), `swarm C-002@55`, event 3 ghi đè DB; regression test so với fixed đã pass.
- **Gate owner:** người làm bài điều tra trace, sửa PR và chạy lại khi gate exit 1.
- **Phạm vi pilot:** đánh giá offline 14 claim fixture; chưa triển khai cho khách hàng thật.
- **Giới hạn / bằng chứng còn thiếu:** MockLLM, 14 item, judge replay công khai, không đo người dùng thật; Python 3.14.3 ngoài dải hỗ trợ của đề. Swarm không ghi reply nên metric FM-08 không quan sát được lời trả lời trên baseline.
- **Khi nào tăng eval-set version:** khi thêm hoặc thay item/nhãn, tạo version mới và chạy lại baseline; ngưỡng cùng version chỉ được giữ hoặc siết chặt.

## V2 — kết quả bổ sung

Baseline `E-swarm-20261118-6cb3`, SHA `6cb377b16233`, 28 item × 5 seed; pass_rate 0,9786, pass_hat_5 0,8929. A/A với seed 66/77/88/99/110 cho Δ=0 ở mọi metric; sàn pass_hat_5 0,80 nằm dưới baseline và ngoài dải nhiễu quan sát. Với LLM thật cần đo lại nhiễu trên nhiều bộ seed. Scorecard đạt 3/3, 0 báo nhầm; slice `money_movement` chặn slice_regression, `adversarial` theo dõi ca tấn công, pass_hat_5 góp phần chặn flaky_regression. Bốn trap công khai bị chặn; trap ẩn chưa chạy, ratchet cần `--base-spec`. Với 5 seed, lỗi hiếm 1/3 seed không được phát hiện ổn định trên mọi tập seed.
