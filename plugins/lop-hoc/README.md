# Lớp học NNC — plugin `lop-hoc`

Bục giảng (giao diện lớp học trên Claude Code Desktop) và giáo viên (Skill `lop-hoc:work-first-learning`) trong một plugin, không kèm OSER. Cách cài khuyên dùng là gửi Claude câu trong README gốc: Claude làm theo `CAI-DAT.md`, cài vào một thư mục lớp và bật tự cập nhật từ nhánh `main`.

Cài tay, chạy trong thư mục lớp:

```bash
claude plugin marketplace add dungvo-svg/training --scope project
claude plugin install lop-hoc@nnc-training --scope project
```

Plugin không mang địa chỉ hay mã nhận góp ý, không mang dữ liệu học viên. Giao diện trên Claude Desktop cần buổi thử thật (`docs/VALIDATION.md`).
