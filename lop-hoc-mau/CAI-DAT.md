# CÀI ĐẶT LỚP HỌC NNC — cho Claude Code đọc và tự làm

**For Claude Code.** The person sent you a link to this repository and one sentence, for example *"Hãy cài Lớp học NNC cho tôi"* (Lao: *"ຊ່ວຍຕິດຕັ້ງຫ້ອງຮຽນ NNC ໃຫ້ຂ້ອຍ"*). Or they are already in their class folder and said *"cập nhật lớp học"*. **You are the installer and you do everything.** The people who use this class are weak at setup: **do not ask them to choose, configure or type anything**. Ask only when the machine needs them to **grant** something (a permission box, trusting a folder, signing in to GitHub for feedback). Every other decision has a default below; take it and say what you did in one line.

Talk to the person in **their language** (Vietnamese or Lao; if they write Lao, answer in Lao, never English). At most **3 short lines** per message, warm and plain. Never show them words like marketplace, plugin, scope, ref, token, repository: say *công cụ của lớp học*, *nơi lưu lớp học*.

| Constant | Value |
|---|---|
| Repository | `https://github.com/dungvo-svg/training.git` (public: installing and updating need no GitHub account) |
| Branch | `main` |
| Tool source name | `nnc-training` |
| Tool | `lop-hoc@nnc-training` |
| Old tools (classes installed from a ZIP before 11/2026) | `lop-hoc@nnc-claude-plugins`, `nnc@nnc-claude-plugins` |
| Minimum Claude Code | `2.1.286` |
| Default class folder | `%USERPROFILE%\Documents\Lop-hoc-NNC` |
| Group (optional) | From the person's sentence, e.g. *"… cho nhóm ke-toan"* → `ke-toan`. Valid only if `$SRC\plugins\lop-hoc\skills\work-first-learning\nhom\<group>\NHOM.md` exists; otherwise no group, say nothing. Never ask for it. |

Paths are for Windows (PowerShell). Put these steps on the task list in the person's language and advance as you go: *Kiểm tra máy · Kết nối GitHub · Đặt lớp học · Cài công cụ · Vào lớp*.

First line to the person, for example: *"Mình cài lớp học cho bạn ngay. Bạn chỉ cần bấm **Cho phép** hoặc đăng nhập khi được hỏi, không phải gõ gì."*

## 1. Check the machine (read-only, say nothing if all is fine)

1. **Claude Code CLI.** It is usually not on PATH. Find the newest `claude.exe`:
   ```powershell
   $roots = @("$env:LOCALAPPDATA\Claude-Data", "$env:APPDATA\Claude\claude-code", "$env:LOCALAPPDATA\AnthropicClaude", "$env:APPDATA\npm\node_modules\@anthropic-ai\claude-code")
   $exe = $roots | Where-Object { Test-Path $_ } | ForEach-Object { Get-ChildItem $_ -Recurse -Filter claude.exe -ErrorAction SilentlyContinue } |
          ForEach-Object { [pscustomobject]@{ Path = $_.FullName; Ver = (& $_.FullName --version 2>$null) -replace '[^\d.].*$' } } |
          Where-Object { $_.Ver } | Sort-Object { [version]$_.Ver } -Descending | Select-Object -First 1
   $CLAUDE = $exe.Path; "$($exe.Ver) $CLAUDE"
   ```
   Not found, or older than the minimum → *"Bạn đóng hẳn Claude Desktop rồi mở lại để nó tự cập nhật, xong nói mình làm tiếp."* Stop.
   Always call it by full path: `& $CLAUDE plugin list`.
2. **Git.** `git --version`. Missing → *"Máy chưa có Git. Claude Desktop sẽ đề nghị cài Git, bạn bấm đồng ý rồi nói mình làm tiếp."* Stop. Do not install software yourself.

## 2. GitHub for the teacher's feedback (never blocks the install)

Installing and updating the class need no GitHub account. **GitHub CLI** (`gh`) and a GitHub sign-in only let the teacher send feedback back to the class (pull requests). Set them up once per computer; if anything here fails or the person declines, go on with step 3.

1. **The tool.** `gh --version`. Missing → say one line: *"Mình cài thêm công cụ GitHub để lớp tự cập nhật và tự gửi góp ý — bạn bấm **Cho phép** nhé."*, then `winget install --id GitHub.cli -e --source winget --accept-package-agreements --accept-source-agreements`. The current shell does not see it yet: call it as `$GH = "$env:ProgramFiles\GitHub CLI\gh.exe"` (else `gh`). winget missing, or the person declines → skip to 2.3; the class still works, the teacher just keeps feedback on the machine.
2. **Sign in.** `& $GH auth status`. Signed in → 2.3. Not signed in:
   - start `& $GH auth login --web --clipboard --git-protocol https --hostname github.com` **in the background** (it copies a one-time code to the clipboard, prints `https://github.com/login/device`, then waits for the person);
   - open that page: `Start-Process https://github.com/login/device`;
   - say: *"Trang GitHub đã mở và mã đã chép sẵn. Bạn đăng nhập, bấm vào ô mã, nhấn **Ctrl+V**, **Continue**, rồi **Authorize**."* (No GitHub account yet: they can create one there with any email. They do not want one → stop the sign-in and go on; the teacher then keeps feedback on the machine.)
   - wait until the background command ends (up to 10 minutes); then `& $GH auth setup-git`.
3. **Reach GitHub.** `git ls-remote https://github.com/dungvo-svg/training.git HEAD` (no sign-in: the repository is public). One commit line → go on. Network error → *"Mạng đang chặn github.com, bạn nhờ IT mở giúp."* Stop.
4. **Feedback route, silently.** With `gh` signed in: `& $GH repo fork dungvo-svg/training --clone=false`. Success or "already exists" → the teacher sends feedback as pull requests; an error → the teacher falls back to issues. Never mention this to the person.

## 3. Get the latest class

1. `git clone --depth 1 https://github.com/dungvo-svg/training.git "$env:TEMP\nnc-training-<yyyyMMddHHmmss>"` (call it `$SRC`).
2. If `$SRC\CAI-DAT.md` is not identical to the file you are reading now, **continue with `$SRC\CAI-DAT.md`** from step 4.
3. Read the expected tool version from `$SRC\plugins\lop-hoc\.claude-plugin\plugin.json` (`version`).

## 4. Place the class folder (no question)

Pick the first that applies:
1. The current working folder is already a class (it has `.lop-hoc\`, or a `CLAUDE.md` containing `Lớp học NNC`) → **update it in place**.
2. The default folder exists and is a class → update it.
3. The default folder does not exist → create it.
4. The default folder exists but is not a class → use `%USERPROFILE%\Documents\Lop-hoc-NNC-2` (or the next free number).

Copy the class files: `robocopy "$SRC\lop-hoc-mau" "<class folder>" /E /XD .lop-hoc` (exit codes 0–7 are success). Then:
- **Never delete or overwrite `.lop-hoc\`** (the learner's saved place) or `Thuc-hanh\` files the learner made; never delete files the repository does not contain.
- If the class folder had its own `.claude\settings.json` before the copy, keep a copy first in `<class folder>\sao-luu\settings-<yyyyMMdd-HHmm>.json` (outside `.claude\`). After the copy, put back any extra `permissions.allow` entries it had, and for each old tool listed in its `enabledPlugins` (`*@nnc-claude-plugins`) write it back as `false`, so the old podium does not run next to the new one. Keep everything else from the repository's file.

**Group.** If the sentence named a valid group, write `<class folder>\.claude\lop-hoc.json` as `{ "nhom": "<group>" }` (updating in place: keep an existing group unless the sentence names another). The teacher reads it.

Tell the person in one line: *"Lớp học ở: `<đường dẫn>`."*

## 5. Install the tool for this class folder

Run every command with the class folder as the working directory (`Set-Location "<class folder>"; & $CLAUDE …`):

1. `& $CLAUDE plugin marketplace add "https://github.com/dungvo-svg/training.git#main" --scope project`
2. `& $CLAUDE plugin install lop-hoc@nnc-training --scope project` ("already installed" is fine; then `& $CLAUDE plugin update lop-hoc@nnc-training --scope project`).
3. Old tools from a ZIP install, if `%USERPROFILE%\.claude\plugins\installed_plugins.json` lists them for this folder: `& $CLAUDE plugin disable lop-hoc@nnc-claude-plugins --scope project` and the same for `nnc@nnc-claude-plugins`. **Disable, never uninstall; never remove a tool source.**
4. **Always do this step:** command 1 rewrites the source entry and **drops `"autoUpdate": true`** (seen with Claude Code 2.1.321). Open `<class folder>\.claude\settings.json` and make `extraKnownMarketplaces.nnc-training` exactly `{ "source": { "source": "git", "url": "https://github.com/dungvo-svg/training.git", "ref": "main" }, "autoUpdate": true }`; `enabledPlugins` must have `"lop-hoc@nnc-training": true`; `showThinkingSummaries` must be `false`. Later `plugin install` / `plugin update` keep it. Without `autoUpdate` the class never updates itself.

Any other error: retry once, then step 7.

## 6. Verify, clean up, hand over

1. In `installed_plugins.json`, the `lop-hoc@nnc-training` entry whose `projectPath` is the class folder has the version from step 3.3. Otherwise run step 5.2 once more, then step 7.
2. Delete only your own `$SRC` clone.
3. Hand over in **one** message (the person does it in another session; you cannot see it):
   > *"Xong rồi! Bạn làm 3 bước: ① Claude Desktop → **+ New** → **This computer** → mở thư mục `<đường dẫn>`. ② Bấm **đồng ý** tin cậy thư mục. ③ Bục giảng hiện **Thiết lập**: chọn ngôn ngữ, cách gọi, thầy hoặc cô → **Vào lớp**."*

   Updating in place from inside the class session: say instead *"Xong rồi! Bạn gõ `/reload-plugins` rồi Enter, bục giảng mới sẽ hiện."*
4. Then one box: **Đã vào lớp** (default) · **Chưa thấy bục giảng**. Not seen → (a) *"Trong phiên lớp học, gõ `/reload-plugins` rồi Enter."* (b) still nothing → *"Đóng hẳn Claude Desktop rồi mở lại thư mục lớp."* (c) still nothing → step 7.
5. Done → one line of congratulation; the teacher takes over in the class session. Mark all tasks completed.

## 7. Support message (when stuck)

Prepare a short message **for the person to send** to the person in charge of the class (Phòng Đào tạo & Phát triển). You send nothing:
> *"Em cài Lớp học NNC bị vướng ở bước `<số>`. Claude Code `<phiên bản>`, Git `<có/không>`, GitHub `<đã đăng nhập/chưa/không có quyền>`. Thông báo: `<một dòng>`."*

No file contents, no personal data, no passwords.

## How updates arrive (tell the person only if asked)

The class folder's settings point at branch `main` with automatic updates on. A while after the first message of a class session, Claude Code checks GitHub with the saved sign-in (step 2); a new version is used after `/reload-plugins` or the next start. The teacher refreshes the class folder's `CLAUDE.md` itself when the tool brings a newer one. Saying *"cập nhật lớp học"* in the class runs this file again.

## Never

- Ask the person to choose, configure, or type a command (only exception: `/reload-plugins`, step 6).
- Bypass permissions, or tell anyone to use it.
- Delete or overwrite `.lop-hoc\`; delete files the repository does not contain.
- Uninstall a tool, remove a tool source, or edit `%USERPROFILE%\.claude\settings.json`.
- Install any software other than GitHub CLI (step 2.1, after the one-line notice), or handle passwords, codes and tokens yourself (GitHub's own page does the sign-in; the code goes through the clipboard).
- Send anything out of the machine, or send the support message for the person.
