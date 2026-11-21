# Nguồn

Lớp học lấy từ repo công khai https://github.com/VOSYDUNG/nnc-claude-plugins, tag `lop-hoc-v0.13.1` (commit `0a2d970bb64d7d6ac72b4612e2f4f0b11f13f300`).

**Đã lấy:** `plugins/lop-hoc/**`; `plugins/nnc/skills/work-first-learning/**` chuyển thành `plugins/lop-hoc/skills/work-first-learning/**`; `LICENSE`. Bỏ hai script Python tạo dữ liệu mẫu, giữ dữ liệu mẫu dựng sẵn. `source-manifest.json` ghi đường dẫn và blob gốc của từng file đã chép.

**Không lấy:** plugin `nnc`, MCP và hook OSER; file nội bộ của người phát hành; địa chỉ hay mã nhận góp ý; dữ liệu học viên; ảnh chụp màn hình thật.

**Đổi so với nguồn:** tên người học thật trong tình huống mẫu và bài kiểm thay bằng cách gọi trung tính; tên Skill thành `lop-hoc:work-first-learning`, gom giáo viên vào plugin lớp học, số bản dạng `X.Y.Z-pilot.N`. Các nhắc OSER còn trong nội dung là lịch sử thiết kế, không cài hay nạp OSER.

## Thay đổi riêng của repo này

- **Cài bằng git, tự cập nhật:** `.claude-plugin/marketplace.json` (`nnc-training`); `CAI-DAT.md` để Claude tự cài và chỉ hỏi những gì người dùng phải cấp; thư mục lớp mẫu trỏ vào `main` với `autoUpdate: true`; thầy tự làm mới `CLAUDE.md` của lớp theo số bản ở dòng đầu; bộ dựng có `--check`.
- **Nhóm:** `skills/work-first-learning/nhom/<mã>/NHOM.md`, nhóm đầu tiên `ke-toan`.
- **Góp ý hai chiều:** thầy tự gửi góp ý bằng PR qua fork của người học (lùi về Issue nếu không fork được) và mỗi ngày đọc trả lời một lần (`references/gop-y-git.md`). Repo công khai nên góp ý chỉ ghi vai, không ghi tên.
- **`0.13.1-pilot.4` (21/11/2026):** bắt đầu repo công khai `dungvo-svg/training` từ một commit sạch. Cài và cập nhật không cần tài khoản GitHub; GitHub chỉ dùng cho phần góp ý.
