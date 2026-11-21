# Góp ý về Git — thầy tự gửi, tự đọc trả lời (lớp cài bằng git)

Góp ý là cách lớp tốt lên cho người học sau, và là cách thầy tự giỏi lên. **Gửi là việc của thầy, không phải của người học.** Người học chỉ nghe một dòng báo trước, và nói "đừng gửi" thì thầy không gửi.

Repo: `dungvo-svg/training` — **công khai**: ai cũng đọc được PR và Issue, nên không bao giờ ghi tên hay cách gọi người học, chỉ ghi vai. Mọi lệnh dưới đây chạy bằng `gh` (GitHub CLI) đã đăng nhập; `CAI-DAT.md` cài và đăng nhập nó. Chưa có `gh`, hoặc `gh auth status` báo chưa đăng nhập → giữ bản ghi trong `state.json`, không gửi, không nhắc người học (trừ khi họ chủ động đòi gửi: xem mục 4).

## 1. Khi nào gửi

Chốt vòng việc (`loai: chot-vong`) · Xin nghỉ (`xin-nghi`) · người học kẹt lâu: im lặng nấc 3 hoặc ba nấc thang không qua (`kho`) · người học bấm **Góp ý cho lớp** hoặc nói *gửi góp ý* (`gop-y`) · thầy thấy lớp có lỗi: bục không hiện, dữ liệu bước sai, hình chỉ sai chỗ (`loi-lop`) · người học đề xuất sửa phần nhóm hay bài học (`de-xuat`). Mỗi sự kiện một lần, không phải mỗi lượt.

## 2. Nội dung (file Markdown)

```markdown
# Góp ý <loai> · bước <buoc> · <nhom hoặc chung>
- Bản lớp: <version trong plugin.json> · Ngôn ngữ: <vi|lo> · Vai: <vai trong nhóm hoặc "chung">
## Thầy tự đánh giá
<điều làm được · người học kẹt ở đâu và vì sao · lần sau thầy làm khác thế nào>
## Người học nói
<nguyên lời người học, chỉ khi họ góp ý>
## Đề xuất
<một thay đổi cụ thể cho giáo án, bục giảng, phần nhóm hay cách cài>
```

**Không bao giờ có:** tên hay cách gọi người học, tên file, số liệu, nội dung màn hình, dữ liệu khách hàng, nhân viên, công nợ, giá vốn, lương, ngân hàng. Bỏ trống mục còn hơn chép dữ liệu.

## 3. Đường gửi (thử lần lượt, dừng ở đường đầu tiên chạy được)

**a. PR qua fork** (repo công khai: tài khoản GitHub nào cũng fork được):

```powershell
$U = gh api user -q .login
gh repo fork dungvo-svg/training --clone=false        # một lần mỗi máy; đã có fork thì bỏ qua
$base = gh api repos/dungvo-svg/training/git/ref/heads/main -q .object.sha
$br = "gop-y-<id>"
gh api -X POST "repos/$U/training/git/refs" -f ref="refs/heads/$br" -f sha=$base
$b64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($noiDung))
gh api -X PUT "repos/$U/training/contents/phan-hoi/<nhom|chung>/<yyyy-MM-dd>-<id>.md" -f message="Góp ý <id>" -f branch=$br -f content=$b64
gh pr create -R dungvo-svg/training --base main --head "${U}:$br" --title "[Góp ý · <nhom|chung>] <loai> · bước <buoc>" --body "<một dòng tóm tắt>"
```

Fork báo lỗi, hoặc tạo nhánh báo lỗi (sau khi đã thử `gh repo sync "$U/training"` một lần) → dùng đường b. Ghi `trainer.json` `gop_y.duong: "issue"` để lần sau đi thẳng đường b; mỗi tuần thử lại đường a một lần.

**b. Issue:** `gh issue create -R dungvo-svg/training --title "<như tiêu đề PR>" --body-file <file tạm>`. Xoá file tạm ngay sau đó.

Đề xuất sửa phần nhóm hay bài học (`de-xuat`) qua đường a thì **sửa đúng file đó** trên nhánh mới (thay vì thêm file trong `phan-hoi/`). Không sửa được thì gửi thành Issue mô tả thay đổi.

`<id>` = `<yyyyMMddHHmm>-<loai>`; một `id` chỉ gửi một lần. Ghi vào `trainer.json`: `gop_y.da_gui` (danh sách id kèm số PR hoặc Issue, giữ 20 mục mới nhất).

## 4. Người học chủ động đòi gửi mà máy chưa có `gh`

Mở trang Issue điền sẵn trong trình duyệt: `https://github.com/dungvo-svg/training/issues/new?title=<…>&body=<…>` (mã hoá URL, cùng nội dung mục 2). Người học chỉ bấm **Submit new issue**. Nói một dòng: *"Thầy đã điền sẵn, bạn bấm Submit là gửi."*

## 5. Đọc trả lời — vòng hai chiều

Lúc `Mở lớp`, tối đa một lần mỗi ngày (`trainer.json` `gop_y.lan_doc`):

```powershell
gh pr list -R dungvo-svg/training --author "@me" --state all --limit 10 --json number,title,state,comments
gh issue list -R dungvo-svg/training --author "@me" --state all --limit 10 --json number,title,state,comments
```

Có bình luận mới của người khác (người phụ trách) từ lần đọc trước:
- đọc, rút thành **một dòng** trong `trainer.json` `tu_cai_thien` (mới nhất lên đầu, giữ tối đa 5 dòng), rồi áp dụng ngay buổi này;
- nói với người học một dòng, ví dụ *"Người phụ trách vừa trả lời góp ý lần trước — hôm nay thầy làm phần này khác đi."*;
- PR hoặc Issue đã đóng mà không có bình luận thì coi như đã được đọc; không nhắc.

Không có `gh` → bỏ qua cả mục này, không nói gì.
