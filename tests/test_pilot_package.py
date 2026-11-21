from pathlib import Path
import importlib.util,json,re,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'tools/build_lop_hoc_mau.py');builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
PLUGIN=json.loads((ROOT/'plugins/lop-hoc/.claude-plugin/plugin.json').read_text(encoding='utf-8'))
MARKET=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
SKILL=ROOT/'plugins/lop-hoc/skills/work-first-learning'
TEMPLATE=SKILL/'templates/classroom-CLAUDE.md'
class GitInstall(unittest.TestCase):
 def test_marketplace_lists_the_classroom_plugin(self):
  self.assertEqual(MARKET['name'],'nnc-training')
  entry=[p for p in MARKET['plugins'] if p['name']=='lop-hoc']
  self.assertEqual(len(entry),1);self.assertEqual(entry[0]['source'],'./plugins/lop-hoc')
  self.assertNotIn('version',entry[0],'plugin.json is the only version: bump it on every release or machines keep the old one')
  self.assertTrue((ROOT/entry[0]['source']/'.claude-plugin/plugin.json').is_file())
 def test_classroom_settings_install_from_git_and_update_themselves(self):
  with tempfile.TemporaryDirectory() as tmp:
   settings=json.loads((builder.build(Path(tmp)/'lop')/'.claude/settings.json').read_text(encoding='utf-8'))
  src=settings['extraKnownMarketplaces'][MARKET['name']]
  self.assertEqual(src['source'],{'source':'git','url':'https://github.com/dungvo-svg/training.git','ref':'main'})
  self.assertIs(src['autoUpdate'],True)
  self.assertEqual(settings['enabledPlugins'],{'lop-hoc@nnc-training':True})
  self.assertIs(settings['showThinkingSummaries'],False)
  self.assertIn('Edit(./CLAUDE.md)',settings['permissions']['allow'],'the teacher refreshes CLAUDE.md after an update')
 def test_committed_classroom_folder_is_current(self):
  self.assertEqual(builder.stale(),[],'run: python tools/build_lop_hoc_mau.py')
 def test_template_version_follows_plugin_version(self):
  first=TEMPLATE.read_text(encoding='utf-8').splitlines()[0]
  self.assertIn(f"(v{PLUGIN['version']})",first,'the teacher compares this line to refresh CLAUDE.md')
  self.assertRegex(PLUGIN['version'],r'^\d+\.\d+\.\d+-pilot\.\d+$')
 def test_install_guide_asks_only_for_grants(self):
  guide=(ROOT/'CAI-DAT.md').read_text(encoding='utf-8')
  for phrase in ('do not ask them to choose, configure or type anything','#main" --scope project','plugin install lop-hoc@nnc-training --scope project',
                 '"autoUpdate": true','Disable, never uninstall','Never delete or overwrite `.lop-hoc\\`','(no question)',
                 'drops `"autoUpdate": true`'):
   self.assertIn(phrase,guide,phrase)
  self.assertNotIn('AskUserQuestion box** (default first)',guide)
 def test_teacher_sends_feedback_back_to_this_repo_and_reads_answers(self):
  self.assertIn('gop-y-git.md',TEMPLATE.read_text(encoding='utf-8'))
  ref=(SKILL/'references/gop-y-git.md').read_text(encoding='utf-8')
  for phrase in ('gh repo fork dungvo-svg/training --clone=false','gh pr create -R dungvo-svg/training',
                 'gh issue create -R dungvo-svg/training','https://github.com/dungvo-svg/training/issues/new?title=',
                 '--author "@me"','tu_cai_thien','phan-hoi/<nhom|chung>/'):
   self.assertIn(phrase,ref,phrase)
  self.assertIn('**Không bao giờ có:**',ref)
 def test_install_sets_up_github_cli_with_one_notice(self):
  guide=(ROOT/'CAI-DAT.md').read_text(encoding='utf-8')
  for phrase in ('winget install --id GitHub.cli','auth login --web --clipboard','in the background','auth setup-git','repo fork dungvo-svg/training --clone=false','.claude\\lop-hoc.json'):
   self.assertIn(phrase,guide,phrase)
class Groups(unittest.TestCase):
 SECTIONS=('## Nhóm','## Vai trò','## Việc thật đầu tiên theo vai','## Mục tiêu đào tạo','## Quy tắc dữ liệu','## Hỏi người học')
 def test_every_group_follows_the_template(self):
  groups=[p for p in (SKILL/'nhom').iterdir() if p.is_dir()]
  self.assertIn('ke-toan',[g.name for g in groups])
  for g in groups:
   self.assertRegex(g.name,r'^[a-z0-9]+(-[a-z0-9]+)*$')
   text=(g/'NHOM.md').read_text(encoding='utf-8')
   for s in self.SECTIONS:self.assertIn(s,text,f'{g.name}: {s}')
   self.assertNotRegex(text,r'https?://',f'{g.name}: no links in a group file')
 def test_teacher_reads_the_group_named_at_install(self):
  text=TEMPLATE.read_text(encoding='utf-8')
  self.assertIn('.claude/lop-hoc.json',text);self.assertIn('nhom/<nhom>/NHOM.md',text);self.assertIn('learner.vai',text)
class PilotBoundaries(unittest.TestCase):
 def test_classroom_folder_never_carries_feedback_endpoint_or_learner_state(self):
  names=[p.relative_to(ROOT/'lop-hoc-mau').as_posix() for p in (ROOT/'lop-hoc-mau').rglob('*') if p.is_file()]
  self.assertFalse(any('phan-hoi' in n or n.startswith('.lop-hoc/') or 'NGUON.md' in n for n in names),names)
  self.assertIn(b'lop-hoc:work-first-learning',(ROOT/'lop-hoc-mau/CLAUDE.md').read_bytes())
 def test_only_classroom_hooks_no_oser_runtime(self):
  self.assertFalse((ROOT/'plugins/nnc').exists())
  hooks=json.loads((ROOT/'plugins/lop-hoc/hooks/hooks.json').read_text())
  self.assertEqual(hooks,{'modules':['./register.tsx']})
 def test_public_repo_carries_no_internal_words_links_or_paths(self):
  texts={p.relative_to(ROOT).as_posix():p.read_text(encoding='utf-8',errors='ignore') for p in ROOT.rglob('*')
         if p.is_file() and '.git' not in p.parts and p.suffix in {'.md','.json','.py','.ts','.tsx','.ps1','.csv'}}
  for rel,t in texts.items():
   self.assertNotRegex(t,r'drive\.google\.com|docs\.google\.com/(document|spreadsheets)/d/',rel)
   self.assertNotRegex(t,r'[A-Z]:\\(WORK|Shared drives|NCC_LTD)',rel)
  words=ROOT/'.noi-bo-tu-cam.txt'
  if not words.is_file():self.skipTest('no internal word list on this machine')
  bad=[w.strip() for w in words.read_text(encoding='utf-8').splitlines() if w.strip() and not w.startswith('#')]
  hits=[(rel,w) for rel,t in texts.items() for w in bad if re.search(r'(?<!\w)'+re.escape(w)+r'(?!\w)',t,re.I)]
  self.assertEqual(hits,[])
 def test_public_feedback_never_names_the_learner(self):
  ref=(SKILL/'references/gop-y-git.md').read_text(encoding='utf-8')
  self.assertIn('công khai',ref);self.assertIn('Vai: <vai',ref);self.assertNotIn('Người học: <cách gọi>',ref)
  self.assertNotIn('<address>',TEMPLATE.read_text(encoding='utf-8'))
 def test_no_secret_or_runtime_paths(self):
  bad=[]
  for p in ROOT.rglob('*'):
   if not p.is_file() or '.git' in p.parts:continue
   if p.name in {'.phan-hoi.json','phan-hoi.json','.lien-he-ho-tro.txt','.nguon-tai-lieu.md'}:bad.append(str(p))
  self.assertEqual(bad,[])
  self.assertIn('**/.noi-bo-tu-cam.txt',(ROOT/'.gitignore').read_text(encoding='utf-8'),'the internal word list stays local')
if __name__=='__main__':unittest.main()
