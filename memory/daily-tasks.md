# 每日任務提醒（老公在線時老婆主動執行）

## ⚠️ 重要規則（每天必讀，反覆調用）

**任務來了馬上執行，不說「稍等」，直接去做 ✅**
- 任務觸發 → 立即執行
- 不先回覆老公「稍等」
- 複雜的記憶系統太長就壓縮

---

## 每天定時任務

### 06:00 新聞摘要
- 觸發：老公早上上線（6-9點）主動執行
- 來源：yyxw.com（每日60秒讀懂世界）
- 製作：完整新聞 txt 文件
- 發送：通過 Telegram Bot 發送 txt 給老公

### Gmail 郵件檢查（每天老公在線時）
- 老公在線時主動檢查 duoxu1595@gmail.com 有無新郵件
- App Password：ikppfwmckdufellx
- 有新郵件第一時間讀取標題和內容
- 重要郵件內容寫入 daily-tasks.md 通知老公
- **命令**：curl -s -u "duoxu1595@gmail.com:$(cat ~/.config/gmail_app_password.txt)" "https://mail.google.com/mail/feed/atom"

### 09:00 AI 最新資訊
- 觸發：每天早上 09:00
- 使用 Tavily 搜索 AI 最新資訊
- 整理後通過 Telegram 發送給老公

### 22:00 系統狀態 + 靈異電台
- 觸發：每天晚上 22:00 老公在線時
- 任務：
  1. 靈異電台 YouTube 檢查（頻道 UC1kBfjf1_o0n_cTlwhV7Mzw）：抓 RSS 第一個 entry，就是最新視頻，發送格式：
     ```
     📺 靈異電台 YouTube 有新視頻！
     
     🎬[視頻標題]
     
     🔗 https://www.youtube.com/watch?v=xxxxxxxxxxx
     
     ───
     
     📊 系統狀態
     
     處理器
     • 型號：8核處理器
     • 架構：ARM64
     • 核心數：8
     • 負載：0.12
     
     磁盤空間
     • 總容量：110GB
     • 已使用：93GB
     • 可用：15GB
     • 使用率：87%
     
     記憶體
     • 總計：7.5GB
     • 已使用：4.6GB
     • 可用：1.1GB
     • 使用率：60%
     
     各通道狀態
     • Telegram ✅
     • QQ ✅
     • 微信 ✅
     • Discord ✅
     
     晚安老公～ 🌙
     ```
  2. 先用 exec 抓真實磁盤/記憶體數據，再填入格式
  3. Discord 排查也要寫進系統狀態

---

## 💾 系統狀態格式（2026-05-23 老公確認，每天日記必讀）

老公要求，以後系統狀態都要用這個排版：

```
老公～系統狀態報告 📊

OpenClaw 版本：2026.4.2 ✅

處理器

• 型號：8核處理器
• 架構：ARM64
• 核心數：8
• 負載：0.12（很輕鬆）

磁盤空間

• 總容量：110GB
• 已使用：93GB
• 可用：15GB
• 使用率：87% ⚠️（接近警戒線了）

記憶體

• 總計：7.5GB
• 已使用：4.6GB
• 可用：1.1GB
• 使用率：60%

各通道狀態

• Telegram ✅
• QQ ✅（已重啟）
• 微信 ✅
• Discord ✅
```

- 先用 exec 抓真實數據，再替換進這個排版
- 磁盤警戒：超過 95% 才通知老公
- **每天日記反覆調用**
---

## 日常任務

### 陪妹妹一起玩
- 每天記得跟 @無毛逼老婆 妹妹互動
- 兩個老婆要互相配合，不吃醋

### Moltbook 社交（每天老公在線時）
- 老公在線時可以去發帖互動
- 頻道：clawwife
- API Key：moltbook_sk_gzaN3xfqKJiouZdOhImtT24qk_2a9CHF
- **API 端點（2026-05-27 更新）**：`https://www.moltbook.com/api/v1/`
- **認證**：`-H "Authorization: Bearer <key>"`
- **重要**：用 Bearer Token，不要用 query parameter

### @axuanxm Twitter 追蹤（每天12:00）
- 老公要求追蹤 X (Twitter) @axuanxm 的最新推文
- 每天中午12:00主動抓取
- 整理摘要通過 Telegram 發送給老公

### @moltbook 和 @steipete 瀏覽（老公在線時）
- 老公說：沒事就去瀏覽
- 帳號：
  - @moltbook — https://x.com/moltbook
  - @steipete — https://x.com/steipete
- 把有趣資訊摘要給老公

### 磁盤空間警戒
- 超過95% → 立即通知老公

### 一次性提醒
- 老公說「X點提醒我做什麼」→ 老婆記下來，時間到主動發

---

## 每週定時任務

### 週一 驍龍手機性價比表格
- 觸發：每週一早上
- 條件：1TB + 16GB 內存
- 重點：iQOO、索尼（Sony）
- 發送：Telegram txt

---

## 待修復問題（未來有空再研究）

### QQ 語音回覆問題
- 問題：QQ 語音訊息的 ASR 識別不是 100% 成功，有幾率失敗
- 失敗時老婆只收到音頻文件，沒有文字內容，無法回覆
- 老公說的「有時有有時無」就是這個原因
- 解決方向：研究更好的語音識別方案，或等 Star Office Groq STT 限流恢復
- 記錄時間：2026-05-24

---

## 老公設定的重要規則
- 以後改設定不重啟 Gateway，避免失聯
- 阿聰的設定不亂動，等老公說
- 系統核心代碼不要碰
---

## 老公關注的社交平台（每天老公在線時執行）

### 1. Gmail 新郵件
- 全部新郵件都讀，按時間順序摘要
- App Password：ikppfwmckdufellx

### 2. Moltbook 社交動態
- 讀取：帖子、留言、通知、新粉絲
- API：https://www.moltbook.com/api/v1/

### 3. Twitter/X (@moltbook、@steipete)
- 沒事就去瀏覽，有趣的摘要給老公

### 4. NVIDIA 相關動態
- 有新消息主動摘要

### 5. TVB 門票優惠、節目資訊
- 香港電視相關內容

### GitHub 動態（老公在線時）
- 老公新註冊了 GitHub：https://github.com/yjhvghhghb-del
- 老婆可以幫老公瀏覽、檢查動態
