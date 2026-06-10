# 🔑 How to Get Your Free Google Gemini API Key

**Quick Guide for RAG Workshop Students**

---

## Step-by-Step Instructions

### ➡️ Step 1: Visit Google AI Studio

Open your browser and go to:

**Option 1:** https://aistudio.google.com/app/apikey

**Option 2:** https://makersuite.google.com/app/apikey

> 💡 Both URLs work! Use whichever loads faster for you.

---

### ➡️ Step 2: Sign In with Google

- Click **"Sign in"** button (top right corner)
- Use your **Google account** (Gmail, Google Workspace, etc.)
- Don't have a Google account? Create one free at: https://accounts.google.com/

---

### ➡️ Step 3: Create Your API Key

Once signed in:

1. Click the blue **"Get API key"** or **"Create API key"** button

2. You'll see two options:
   - ✅ **"Create API key in new project"** ← Choose this if first time
   - **"Create API key in existing project"** ← Only if you have Google Cloud projects

3. Click **"Create API key in new project"**

4. Wait 2-3 seconds while Google creates your key...

5. Your API key appears! It looks like:
   ```
   AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

---

### ➡️ Step 4: Copy Your API Key

- Click the **"Copy"** icon (📋) next to your key
- Or select the entire key and press `Ctrl+C` (Windows) or `Cmd+C` (Mac)
- **Save it somewhere safe!** (Notepad, Notes app, etc.)

> ⚠️ **Important:** Keep your API key private! Don't share it publicly or commit to GitHub.

---

### ➡️ Step 5: Set Up Your Project

#### 5A. Navigate to the Code Folder

Open terminal/command prompt and run:

```bash
cd RAG-Workshop-Demo/04_Hands_On_Code
```

#### 5B. Create .env File

**Option 1: Quick Command (Mac/Linux/Git Bash on Windows)**
```bash
cp .env.example .env
```

**Option 2: Manual (Any System)**
1. Open `04_Hands_On_Code` folder
2. Create new file
3. Name it `.env` (with dot at the beginning!)
4. Open in text editor

#### 5C. Add Your API Key

Open the `.env` file and add this line:

```
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Replace** `AIzaSyXXX...` with your **actual API key**

**Important:**
- ✅ No spaces around the `=` sign
- ✅ No quotes around the key
- ✅ Save the file!

#### 5D. Verify Setup

Run this command to test:

```bash
python demo_1_basic_rag.py
```

If you see `✅ API Key loaded successfully!` → You're good to go! 🎉

---

## 🆓 Free Tier Limits

Google gives you generous free usage:

| Limit | Amount |
|-------|--------|
| **Requests per minute** | 60 |
| **Requests per day** | 1,500 |
| **Cost** | FREE! |

Perfect for:
- ✅ Learning RAG
- ✅ Building prototypes
- ✅ Small projects
- ✅ This workshop!

Need more? Upgrade to paid tier: https://ai.google.dev/pricing

---

## ❓ Troubleshooting

### Problem: "API key not found"

**Check 1:** Does `.env` file exist?
```bash
ls -la  # Mac/Linux
dir     # Windows
```
You should see `.env` in the list.

**Check 2:** Open `.env` file and verify:
```
GOOGLE_API_KEY=AIzaSy...  ✅ Correct
GOOGLE_API_KEY = AIzaSy... ❌ Extra spaces
GOOGLE_API_KEY="AIzaSy..." ❌ Don't use quotes
```

**Check 3:** Make sure you're in the right folder
```bash
pwd  # Should show: .../RAG-Workshop-Demo/04_Hands_On_Code
```

---

### Problem: "Invalid API key"

**Solution 1:** Copy key again
1. Go back to https://aistudio.google.com/app/apikey
2. Your key should still be there
3. Click copy icon again
4. Replace in `.env` file

**Solution 2:** Create new key
1. Visit https://aistudio.google.com/app/apikey
2. Click "Create API key" again
3. Copy the new key
4. Update `.env` file

**Solution 3:** Check for typos
- Key must start with `AIza`
- No spaces before or after
- Copy entire key (usually 39 characters)

---

### Problem: "Quota exceeded" (429 error)

**What happened:**
- You used all 1,500 requests for today (impressive!)
- Or 60 requests in last minute

**Solution:**
- Wait 24 hours for daily quota reset
- Or slow down (max 60 requests/minute)
- Or upgrade to paid tier

**Check your usage:**
https://aistudio.google.com/app/apikey → Click on your key → View usage

---

### Problem: "API not enabled for Gemini"

**Solution:**
- Wait 1-2 minutes after creating key (activation time)
- Make sure you created key at https://aistudio.google.com/app/apikey
- NOT Google Cloud Console (different API!)
- Try refreshing the page

---

## 🔒 Security Best Practices

### ✅ DO:
- Keep API key in `.env` file
- Add `.env` to `.gitignore` (already done!)
- Create different keys for different projects
- Delete keys you're not using

### ❌ DON'T:
- Commit `.env` to GitHub
- Share API key publicly
- Hardcode key in source code
- Post key in chat/forum

### If Key is Compromised:
1. Go to https://aistudio.google.com/app/apikey
2. Click trash icon next to compromised key
3. Create new key
4. Update `.env` file

---

## 💡 Pro Tips

1. **Backup your key:** Save it in password manager or secure note
2. **Test immediately:** Run `demo_1_basic_rag.py` right after setup
3. **Monitor usage:** Check https://aistudio.google.com/app/apikey periodically
4. **Multiple projects?** Create separate API keys for organization
5. **Workshop day:** Get key 1-2 days before (in case of issues)

---

## 📞 Need Help?

**During Workshop:**
- Raise your hand 🙋
- Ask instructor or TA
- Check with neighbor (they might have same issue!)

**After Workshop:**
- GitHub Issues: https://github.com/shivarajkarki/RAG-Workshop-Demo/issues
- Check troubleshooting section above
- Google "Gemini API" + your error message

---

## ✅ Final Checklist

Before workshop, make sure:

- [ ] Created Google account
- [ ] Visited https://aistudio.google.com/app/apikey
- [ ] Created API key
- [ ] Copied key to safe place
- [ ] Created `.env` file in `04_Hands_On_Code` folder
- [ ] Added `GOOGLE_API_KEY=your-key` to `.env`
- [ ] Ran `python demo_1_basic_rag.py` successfully
- [ ] Saw "✅ API Key loaded successfully!"

**All checked?** You're ready for the workshop! 🚀

---

## 📚 Additional Resources

**Official Docs:**
- Gemini API: https://ai.google.dev/docs
- Pricing: https://ai.google.dev/pricing
- Rate Limits: https://ai.google.dev/gemini-api/docs/rate-limits

**Video Tutorials:**
- Search YouTube: "How to get Gemini API key"
- Watch: "Google AI Studio tutorial"

---

**Questions?** Ask during the workshop or open a GitHub issue!

**Happy Learning!** 🎓✨
