# Nhóm kế toán nội bộ (`ke-toan`)

## Nhóm

Bộ phận kế toán nội bộ, làm việc ở Việt Nam và Lào. Nhóm dùng Claude để rà soát chéo mọi khâu kế toán.

## Vai trò

| Vai | Việc chính | Số liệu vào → ra |
|---|---|---|
| Phụ trách kế toán | Kiểm soát, khoá sổ, báo cáo, đào tạo người trong nhóm | Số liệu các khâu → báo cáo, sổ đã khoá |
| Hàng hoá và kho | Theo dõi nhập, xuất, tồn | Phiếu nhập/xuất từ cung ứng và thủ kho → bảng tồn kho |
| Thanh toán và công nợ | Theo dõi thanh toán, công nợ phải trả và phải thu | Hoá đơn, chứng từ thanh toán → bảng công nợ |
| Kiểm soát doanh thu và ngân hàng | Đối chiếu doanh thu với tiền về ngân hàng | Báo cáo thu ngân các cửa hàng, sao kê ngân hàng → bảng đối chiếu |
| Cung ứng (cấp số liệu) | Đưa số liệu mua hàng vào thư mục chung | Đơn mua, phiếu nhập → thư mục số liệu |

Trợ lý AI (Claude) rà soát chéo mọi khâu: tìm chỗ lệch giữa các bảng, không tự sửa sổ.

## Việc thật đầu tiên theo vai

Gợi ý cho bước 6 (*Việc của tôi*). Luôn làm trên **bản sao** do người học tự chọn; kết quả là file mới.

| Vai | Gợi ý |
|---|---|
| Phụ trách kế toán | Lập danh sách kiểm trước khoá sổ tháng từ các bảng của nhóm; Claude chỉ ra mục còn thiếu |
| Hàng hoá và kho | Đối chiếu tổng nhập − xuất với tồn cuối kỳ; Claude liệt kê mã hàng lệch |
| Thanh toán và công nợ | Đối chiếu bảng công nợ với chứng từ thanh toán; Claude liệt kê khoản chưa khớp |
| Kiểm soát doanh thu và ngân hàng | Đối chiếu doanh thu từng ngày với tiền về trên sao kê; Claude đánh dấu ngày lệch |
| Cung ứng | Gom phiếu nhập trong tuần thành một bảng đúng mẫu nhóm cần |

## Mục tiêu đào tạo

- Sau vòng việc đầu: người học tự giao cho Claude một việc đối chiếu của vai mình (đủ 4 ý giao việc) và tự kiểm được kết quả với bảng nguồn.
- Sau ba vòng việc: người học dùng Claude hằng tuần cho ít nhất một việc lặp lại của vai mình, và biết khi nào kết quả cần người phụ trách xem lại.

## Quy tắc dữ liệu

- Công nợ, giá vốn, lương, doanh thu, số tài khoản và sao kê ngân hàng, tên khách hàng và nhà cung cấp là **dữ liệu nhạy cảm**.
- Chỉ làm trên bản sao trong máy người học. Không chép vào `Thuc-hanh/`, không ghi vào sổ lớp, không đưa vào góp ý, PR hay Issue.
- Khi dạy và làm mẫu: dùng dữ liệu mẫu của lớp, hoặc số giả do thầy tạo.
- Claude chỉ ra chỗ lệch; người học quyết định sửa sổ.

## Hỏi người học

Một lần, ở bước 0, bằng nút trên bục: *"Bạn làm vai nào trong nhóm?"*, với các lựa chọn là cột **Vai** ở trên, cộng thêm **Khác**. Ghi vào `trainer.json` `learner.vai`. Không hỏi gì khác về công việc trước khi cần.
