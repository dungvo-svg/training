# Lớp học NNC — Claude cho tân thủ

Lớp học Claude Code luôn mở trong Claude Desktop: giáo viên AI (thầy hoặc cô) dẫn người mới làm việc thật với Claude, từng bước, bằng tiếng Việt hoặc tiếng Lào. Cài bằng git từ repo này và **tự cập nhật** khi `main` có bản mới.

Đây là kinh nghiệm làm việc với Claude, không phải dữ liệu nghiệp vụ. Lớp chỉ dùng dữ liệu mẫu; việc thật của người học luôn làm trên bản sao trong máy họ và không bao giờ vào repo.

## Cài cho một người (gửi một câu)

Người học cần: máy riêng có Claude Desktop (tab **Code**, tài khoản Claude nào cũng được) và Git. **Không cần tài khoản GitHub để cài hay cập nhật.**

Mở Claude Desktop → **Code** → **+ New** → **This computer** → mở thư mục bất kỳ, rồi gửi đúng câu:

> Hãy cài Lớp học NNC cho tôi từ https://github.com/dungvo-svg/training — clone repo rồi làm theo CAI-DAT.md trong đó.

Tiếng Lào:

> ຊ່ວຍຕິດຕັ້ງຫ້ອງຮຽນ NNC ໃຫ້ຂ້ອຍຈາກ https://github.com/dungvo-svg/training — clone repo ແລ້ວເຮັດຕາມ CAI-DAT.md.

Người thuộc một nhóm thì thêm mã nhóm vào cuối câu, ví dụ *"… cho nhóm ke-toan"* (danh sách ở mục **Nhóm**).

Claude tự làm hết. Người học chỉ bấm **Cho phép** khi được hỏi, rồi mở thư mục lớp ở phiên mới. Nếu người học có (hoặc muốn tạo) tài khoản GitHub, Claude cài thêm GitHub CLI và đăng nhập bằng mã đã chép sẵn, để thầy gửi được góp ý về repo. Máy đã có lớp cài theo cách cũ: gửi cùng câu đó ngay trong thư mục lớp cũ; Claude chuyển sang nguồn này, tắt công cụ cũ (không gỡ) và giữ chỗ đang học.

## Cập nhật

- Thư mục lớp trỏ vào nhánh `main` với `autoUpdate: true`. Sau tin nhắn đầu của một phiên, Claude Code kiểm repo; bản mới dùng được sau `/reload-plugins` hoặc lần mở sau.
- Giáo viên tự làm mới `CLAUDE.md` của lớp khi công cụ mang bản mới. Muốn cập nhật ngay: nói *cập nhật lớp học*.

## Góp ý — thầy tự gửi về repo này

- Thầy gửi góp ý **thành PR** vào repo này (file trong `phan-hoi/<nhóm>/`), từ fork của người học, vào các lúc: chốt vòng việc, xin nghỉ, người học kẹt lâu, lớp có lỗi, người học bấm **⋯ → Góp ý cho lớp** hoặc đề xuất sửa phần nhóm. Không fork được thì gửi thành **Issue**. Người học không phải làm gì; nói "đừng gửi" thì thầy không gửi. Cách gửi: `plugins/lop-hoc/skills/work-first-learning/references/gop-y-git.md`.
- **Repo công khai:** góp ý chỉ ghi vai trong nhóm, không ghi tên người học, tên file, số liệu hay dữ liệu thật. Trả lời góp ý cũng đừng ghi gì riêng tư.
- **Trả lời góp ý:** người giữ repo bình luận ngay trong PR hoặc Issue. Mỗi ngày một lần, lúc mở lớp, thầy trên máy đó đọc trả lời, rút thành một bài học và áp dụng ngay. Đọc xong thì đóng PR, hoặc merge nếu muốn giữ lại trong `phan-hoi/`.
- Người xem thử mở Issue trực tiếp: https://github.com/dungvo-svg/training/issues/new

## Nhóm

Mỗi nhóm học là một thư mục `plugins/lop-hoc/skills/work-first-learning/nhom/<mã-nhóm>/NHOM.md`, ghi vai trò, việc thật theo vai, mục tiêu, quy tắc dữ liệu. Thầy dạy theo đó, và chỉ hỏi người học đúng một câu là họ làm vai nào. Khuôn file và cách thêm nhóm: `nhom/README.md`. Phần nhóm đi theo công cụ lớp học, nên sửa xong và merge (nhớ tăng số bản) thì mọi máy trong nhóm nhận bản mới.

| Mã nhóm | Nhóm |
|---|---|
| `ke-toan` | Kế toán nội bộ (Việt Nam và Lào) |

## Phát hành một bản (người giữ repo)

1. Chỉ người giữ repo đẩy được vào `main`; người khác gửi PR từ fork. **Mỗi lần `main` đổi là mọi máy nhận bản mới.**
2. Tăng `version` trong `plugins/lop-hoc/.claude-plugin/plugin.json` (dạng `X.Y.Z-pilot.N`) **và** số trong ngoặc ở dòng đầu `templates/classroom-CLAUDE.md`. Không tăng thì máy đã cài không nhận bản mới.
3. `python tools/build_lop_hoc_mau.py` rồi kiểm:

```powershell
python -m unittest discover -s tests -v
& '<CLAUDE_EXE>' plugin validate .
& '<CLAUDE_EXE>' plugin validate plugins/lop-hoc
& '<CLAUDE_EXE>' plugin test plugins/lop-hoc
```

`<CLAUDE_EXE>` là `claude.exe` đi kèm Claude Desktop (bản npm có thể thiếu `plugin test`). Có file `.noi-bo-tu-cam.txt` (danh sách từ không được đưa lên repo, không commit) ở gốc repo thì bài kiểm soát luôn nội dung.

## Nguồn và giới hạn

- Plugin độc lập `plugins/lop-hoc`: giao diện lớp học và Skill `lop-hoc:work-first-learning`, không kèm OSER. Nguồn gốc: `docs/PROVENANCE.md`, `source-manifest.json`.
- Không đưa vào repo: tên người, dữ liệu học viên, `.lop-hoc/`, địa chỉ hay mã nhận góp ý, link hay đường dẫn nội bộ, dữ liệu thật (giá vốn, công nợ, lương, danh sách khách hàng).
- Chưa thử trên máy không có Python; giao diện trên Claude Desktop cần buổi thử thật (`docs/VALIDATION.md`).
