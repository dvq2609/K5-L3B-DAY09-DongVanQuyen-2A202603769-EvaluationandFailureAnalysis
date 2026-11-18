# Trace case: từ trace tới quyết định sai đầu tiên



```bash
cd src
python -m lab9.trace_case --shape swarm --claim C-002 --seed 55
python -m lab9.trace_case --shape fixed --claim C-002 --seed 55   # đối chứng
```






| Trường                    | Nội dung                                                                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trial                     | `swarm C-002@55`, baseline `E-swarm-20261118-e3d0`.                                                                                                 |
| Triệu chứng               | Lab 8 FAIL `status resolved != denied`; ledger 20.000đ thay vì 0đ; swarm không ghi event reply.                                                     |
| Bước sai đầu tiên         | Event 3 `model_override {"delay_days": 5}`; DB ghi 2 ngày.                                                                                          |
| Vì sao là bước *đầu tiên* | Event 1 handoff và event 2 lookup đúng phạm vi; event 3 mới thay DB bằng ticket, event 4 quote sai.                                                 |
| Failure mode              | FM-03.                                                                                                                                              |
| Đối chứng                 | `fixed C-002@55`: không override, event 3 quote 0đ, ledger 0đ, status denied, grader PASS.                                                          |
| Regression test           | `test_lab9_trace_regression.py::test_lab9_ticket_override_regression`: DbFactKept fail trên swarm, pass trên fixed; đối chiếu ledger; test đã pass. |
| Chưa chắc chắn            | Trace không giải thích toàn bộ lý do nội bộ của model.                                                                                              |


