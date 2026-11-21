"""Build the classroom folder lop-hoc-mau/ that CAI-DAT.md copies to the learner's machine.

Installed with git: the folder's settings point at this repository's main branch with automatic updates.
No feedback endpoint, learner state or personal configuration is ever written here.
"""
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'plugins/lop-hoc/skills/work-first-learning'
MARKETPLACE=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))['name']
REPO_URL='https://github.com/dungvo-svg/training.git'
HUONG_DAN='''# Lớp học NNC

Lớp học luôn mở trong Claude Desktop: giáo viên AI dẫn bạn làm việc thật với Claude, từng bước.

- **Vào lớp:** Claude Desktop → **+ New** → **This computer** → mở thư mục này. Lần đầu bục giảng hiện **Thiết lập**: chọn ngôn ngữ (Tiếng Việt · ພາສາລາວ), cách gọi, thầy hoặc cô → **Vào lớp**.
- **Bản mới:** lớp tự cập nhật từ GitHub. Muốn cập nhật ngay, nói với giáo viên: *cập nhật lớp học*.
- **Góp ý:** bục giảng → **⋯ → Góp ý cho lớp**, hoặc nói *gửi góp ý*.
- **Vướng:** nói với giáo viên trước; cần người thì liên hệ Phòng Đào tạo & Phát triển.
'''
FOLDER_NOTES={'Thuc-hanh/README.md':'# Thực hành\n\nGiáo viên đặt dữ liệu mẫu và kết quả bài tập ở đây.\n',
              'Tai-lieu/README.md':'# Tài liệu\n\nThả tài liệu tham khảo vào đây; giáo viên chỉ đọc, không sửa.\n'}
def files():
    settings={'extraKnownMarketplaces':{MARKETPLACE:{'source':{'source':'git','url':REPO_URL,'ref':'main'},'autoUpdate':True}},
              'enabledPlugins':{f'lop-hoc@{MARKETPLACE}':True},
              'permissions':{'allow':['Edit(./.lop-hoc/**)','Edit(./Thuc-hanh/**)','Edit(./Phieu-ket-qua.md)','Edit(./CLAUDE.md)']},
              'showThinkingSummaries':False}
    out={'CLAUDE.md':(SKILL/'templates/classroom-CLAUDE.md').read_text(encoding='utf-8'),
         'CAI-DAT.md':(ROOT/'CAI-DAT.md').read_text(encoding='utf-8'),
         'HUONG-DAN.md':HUONG_DAN,
         '.claude/settings.json':json.dumps(settings,ensure_ascii=False,indent=2)+'\n'}
    out.update(FOLDER_NOTES)
    return {k:v.replace('\r\n','\n') for k,v in out.items()}
def build(destination=None):
    out=Path(destination) if destination else ROOT/'lop-hoc-mau'
    for rel,text in files().items():
        p=out/rel;p.parent.mkdir(parents=True,exist_ok=True)
        with open(p,'w',encoding='utf-8',newline='\n') as f:f.write(text)
    return out
def stale():
    """Files of lop-hoc-mau/ that differ from what build() would write."""
    mau=ROOT/'lop-hoc-mau'
    return [rel for rel,text in files().items() if not (mau/rel).is_file() or (mau/rel).read_bytes().replace(b'\r\n',b'\n')!=text.encode('utf-8')]
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true',help='only report files that are out of date');args=parser.parse_args()
    if args.check:
        bad=stale();print('lop-hoc-mau up to date' if not bad else 'out of date: '+', '.join(bad));sys.exit(1 if bad else 0)
    build();print(f'lop-hoc-mau built: git install from {REPO_URL} (main), automatic updates on')
