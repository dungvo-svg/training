# Validation scope

Lịch sử kiểm của lớp học từ khi tách khỏi repo nguồn. Các mục cũ nói về bản thử trước khi chuyển sang repo công khai này.

2026-10-30: three fresh standard-library packaging tests passed. They check that the ZIP is generated in a clean temporary folder, does not include feedback/learner data or auto-install settings, names the standalone skill, and has no OSER plugin or classic OSER shell hooks.

Claude Code 2.1.312 manifest validation returned success with no manifest/content errors or warnings. Initial directory advice requested a plugin README/license; a README and MIT manifest license were subsequently added. Public plugin-directory acceptance is not a goal and is not established.

The local CLI advertised `plugin test` in help, but invocation with `--safe-mode plugin test` returned `unknown command 'test'` before running any suite. The copied UI tests therefore remain unexecuted. Do not claim the historical upstream 208 UI tests or 311 Python tests passed on this extraction.

Not tested: Desktop UI rendering, actual teacher interaction, a Python-free learner machine, screen capture, feedback transport, production rollout, existing installer compatibility. The code still depends on the Claude host UI SDK; isolation from OSER is not proof of generic CLI UI compatibility.

## 2026-11-11 · cài bằng git (0.13.1-pilot.2)

Claude Code 2.1.321 trên Windows, máy có Git for Windows và đăng nhập GitHub đã lưu:

- Làm đúng `CAI-DAT.md` bước 1–6 từ GitHub (nhánh `feat/cai-bang-git` thay cho `main`) vào một thư mục lớp thử: đoạn tìm `claude.exe` thấy bản ở `%LOCALAPPDATA%\Claude-Data\…`; `git ls-remote` vào repo private đạt; chép thư mục lớp đủ 6 file; `plugin marketplace add … --scope project` và `plugin install … --scope project` đạt; bản cài `0.13.1-pilot.2`.
- `plugin marketplace add` ghi đè mục nguồn và **bỏ `autoUpdate`**; sau khi đặt lại (bước 5.4), `plugin update`, `plugin install` và `marketplace update` giữ nguyên.
- Cơ chế nhận bản mới (nguồn thư mục cục bộ): commit không tăng `version` → "already at the latest version", không nhận; tăng lên `pilot.3` → cập nhật lên `pilot.3`.
- `plugin validate .` và `plugin validate plugins/lop-hoc` đạt; `unittest` 9 bài đạt.

Chưa kiểm: việc tự cập nhật chạy nền trong một phiên thật (trễ tối đa 10 phút sau tin nhắn đầu); `autoUpdate` khai ở thiết lập dự án (tài liệu chỉ nêu ví dụ ở thiết lập quản trị); máy chưa đăng nhập GitHub (cửa sổ đăng nhập); máy đang có lớp cài từ ZIP (chuyển nguồn tại chỗ); giao diện trên Claude Desktop thật.

## 2026-11-21 · nhóm và góp ý bằng PR (0.13.1-pilot.3)

- `unittest` 12 bài đạt; `plugin validate .` đạt; `plugin test plugins/lop-hoc` 208 đạt (Claude Code 2.1.326).
- `plugin validate plugins/lop-hoc` trên 2.1.326 đạt kèm 7 cảnh báo kiểu TypeScript trong `register.tsx` và file test. Các file này không đổi từ 0.13.1; bản kiểm mới của Claude Code mới báo.
- `gh auth login --web --clipboard` khi không có bàn phím tương tác: không chờ Enter, chép mã vào clipboard, in `https://github.com/login/device` rồi chờ người dùng (thử với cấu hình `gh` tạm, không đăng nhập thật).
- Các lệnh đọc của thầy chạy đúng với `gh` 2.89: `api user`, `git/ref/heads/main`, `pr list` và `issue list` `--author "@me"` với các trường `number,title,state,comments`.

Chưa kiểm: tạo fork, nhánh, file và PR từ máy người học (lúc đó repo cũ không cho fork); `winget install GitHub.cli` trên máy chưa có; thầy gửi và đọc trả lời trong một buổi thật; thầy dạy theo `NHOM.md`.

## 2026-11-21 · repo công khai (0.13.1-pilot.4)

Bắt đầu repo `dungvo-svg/training` từ một commit sạch (không mang lịch sử cũ). Kết quả kiểm trên bản này ghi ở PR và tin phát hành.

## 2026-11-27 · sửa cảnh báo kiểu (0.13.1-pilot.5)

Claude Code 2.1.330 kiểm kiểu TypeScript khi `plugin validate`. Đã sửa 7 cảnh báo, không đổi hành vi:
- `register.tsx`: thu hẹp nấc im lặng trước khi tra bảng chờ; `Svg` chỉ dùng khi bề mặt có.
- File test: bỏ thuộc tính bị ghi đè, thêm `find` vào kiểu bục giả lập, khẳng định phần tử đầu.

README plugin thêm dòng lệnh cài.

Sau sửa: `plugin validate plugins/lop-hoc` và `plugin validate .` đạt, không còn cảnh báo kiểu; chỉ còn lưu ý thiếu biểu tượng, dành cho danh mục plugin công khai, lớp học không dùng. `plugin test` 208/208, `unittest` 14/14.

Chưa kiểm: máy đã cài `pilot.4` tự nhận `pilot.5` trong một phiên thật.
