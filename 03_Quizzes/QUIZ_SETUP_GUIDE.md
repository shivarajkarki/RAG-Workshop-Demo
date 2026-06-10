# Quiz Setup Guide for Instructors
## How to Create Interactive Online Quizzes

This guide shows you how to set up the quizzes for your 150 students using popular platforms.

---

## 🎯 Platform Recommendations

| Platform | Best For | Pros | Cons | Cost |
|----------|----------|------|------|------|
| **Google Forms** | General use, easy setup | Free, integrated with Sheets, timestamps | No real-time leaderboard | Free ✅ |
| **Kahoot** | High energy, competitive | Fun, real-time leaderboard, music | 5-min setup per quiz | Free tier available |
| **Mentimeter** | Professional, clean | Beautiful UI, analytics | Limited free tier | Freemium |
| **Quizizz** | Self-paced option | Memes, avatars, fun | Can be distracting | Free tier available |
| **Slido** | Q&A + polls | Good for hybrid events | Less game-like | Freemium |

**RECOMMENDED FOR YOUR SESSION**: Google Forms (primary) + Kahoot (bonus/final quiz)

---

## 📋 Option 1: Google Forms (RECOMMENDED)

### Why Google Forms?
- ✅ 100% free, no limits
- ✅ Automatic timestamp (know who answered first)
- ✅ Responses go to Google Sheets (easy analysis)
- ✅ Can include images/code snippets
- ✅ Works on any device
- ✅ No account needed for students

### Setup Steps (15 minutes per quiz):

#### 1. Create the Form
1. Go to [forms.google.com](https://forms.google.com)
2. Click "+ Blank" to create new form
3. Title: "RAG Demo - Quiz 1: Basics"

#### 2. Configure Settings
Click "Settings" ⚙️:
- **General**:
  - ✅ Limit to 1 response (prevent spam)
  - ✅ Don't collect email addresses (faster for students)
- **Presentation**:
  - ✅ Show progress bar
  - ✅ Shuffle question order (optional - prevents cheating)
  - Confirmation message: "Submitted! Check the projector for answers."
- **Quizzes**:
  - ✅ Make this a quiz
  - ✅ Release grades: Immediately after each submission
  - ✅ Respondents can see: Missed questions, Correct answers

#### 3. Add Questions

**Example for Quiz 1, Question 1:**
```
Question: What does RAG stand for?

Type: Multiple choice
Options:
  ○ Rapid AI Generation
  ○ Retrieval Augmented Generation (correct - 1 point)
  ○ Random Access Generation
  ○ Recursive Algorithm Generator

Points: 1
Answer key: Select "Retrieval Augmented Generation"
Add explanation: "RAG = Retrieval Augmented Generation. It combines search with LLM generation!"
```

Repeat for all questions in the quiz.

#### 4. Create QR Code
1. Click "Send" button (top right)
2. Click link icon 🔗
3. Click "Shorten URL" ✅
4. Copy the short URL (e.g., forms.gle/abcd1234)
5. Go to [qr-code-generator.com](https://www.qr-code-generator.com/)
6. Paste URL, generate QR code
7. Download PNG
8. Insert in your slide: "Scan to take Quiz 1!"

#### 5. View Responses Live
1. Click "Responses" tab in form
2. Click green Sheets icon to create spreadsheet
3. Share this sheet on projector (optional - for live leaderboard)
4. Columns will show: Timestamp, Score, Each answer

### During the Session:

**Display slide with:**
```
┌─────────────────────────────────────┐
│         QUIZ 1: RAG BASICS          │
│                                     │
│     [QR CODE]                       │
│                                     │
│  Scan to answer!                    │
│  Time limit: 3 minutes              │
│                                     │
│  Link: forms.gle/RAGQuiz1           │
└─────────────────────────────────────┘
```

**Announce:**
> "Quiz time! Scan the QR code or type the link. You have 3 minutes. Top 3 teams with highest scores AND fastest times win prizes! GO!"

**Start timer visibly (phone/projector)**

**After 3 minutes:**
> "Time's up! Let's see the results..."

**Show leaderboard:**
1. Open Google Sheets with responses
2. Sort by Score (descending), then by Timestamp (ascending)
3. Announce top 3 teams
4. Review answers together (Form shows % correct per question)

---

## 🎮 Option 2: Kahoot (For Quiz 4 - The Final Challenge)

### Why Kahoot for the final quiz?
- 🎵 High energy with music
- 🏆 Real-time leaderboard
- 🎉 Celebration animations
- 💪 Builds to exciting conclusion

### Setup Steps:

#### 1. Create Account
1. Go to [kahoot.com](https://kahoot.com)
2. Sign up (free teacher account)

#### 2. Create Kahoot
1. Click "Create" → "New Kahoot"
2. Title: "RAG Mastery Challenge - Quiz 4"
3. Description: "Advanced RAG & Evaluation Metrics"
4. Visibility: Private (or Public to share later)

#### 3. Add Questions

**For each question:**
- Click "+ Add question"
- Select "Quiz" (not Poll or True/False, unless applicable)
- **Question text**: (e.g., "What does MRR measure?")
- **Time limit**: 60 seconds (adjust based on difficulty)
- **Points**: 1000 (Kahoot awards points based on speed + correctness)
- **Answer options**: Add 2-4 options
- **Mark correct answer**: Click the checkmark ✓
- **Add image** (optional): Upload diagram/meme for engagement

**Example:**
```
Question: MRR (Mean Reciprocal Rank) measures:

Time: 60 sec
Options:
  ✓ The position of the first relevant document [CORRECT]
  ✗ How many docs were retrieved
  ✗ The database size
  ✗ The embedding quality

Image: [Upload diagram of ranked results]
```

#### 4. Launch During Session

**Display slide:**
```
┌─────────────────────────────────────┐
│    🎮 FINAL CHALLENGE - QUIZ 4!     │
│                                     │
│      Kahoot Game PIN:               │
│         ► 123456 ◄                  │
│                                     │
│   Go to: kahoot.it                  │
│   Enter the PIN                     │
│   Enter your TEAM NAME              │
└─────────────────────────────────────┘
```

**Announce:**
> "This is it - the final challenge! It's a Kahoot, so you'll see the leaderboard live. Go to kahoot.it, enter PIN 123456, use your team name. Let's see who's the RAG champion!"

**Kahoot Gameplay:**
1. Students join with PIN
2. You control pace from your screen
3. Read question aloud (displayed on projector)
4. Students answer on their devices
5. **Leaderboard shows after each question** (builds suspense!)
6. Music and animations keep energy high
7. Top 5 teams shown on podium at end

**After game:**
> "Let's give a HUGE round of applause to our top 3 teams! Come collect your prizes!"

---

## 🏆 Prize Management System

### Tracking Winners

**Create a simple spreadsheet:**

| Quiz | Team Name | Score | Time | Prize | Notes |
|------|-----------|-------|------|-------|-------|
| Quiz 1 | Team Alpha | 8/8 | 2:15 | ✅ Stickers | First to finish! |
| Quiz 1 | Team Beta | 8/8 | 2:30 | ✅ Notebook | - |
| Quiz 1 | Team Gamma | 7/8 | 2:00 | ✅ Pen Set | Fast but 1 wrong |
| Quiz 2 | Team Delta | 10/10 | 3:45 | ✅ USB Drive | - |
| ... | ... | ... | ... | ... | ... |

### Prize Ideas (Budget-Friendly)

**Low Cost (₹50-100 each):**
- Branded stickers
- Notebooks
- Pens/markers
- Keychains
- Badges

**Medium Cost (₹200-500 each):**
- Tech-themed mugs
- USB drives
- Laptop stickers pack
- Books (Python/AI)

**Grand Prize (₹500-1000) - For Quiz 4 Winners:**
- Course vouchers (Udemy/Coursera)
- Tech books
- Power banks
- Wireless mouse

**Non-Monetary Rewards:**
- Certificate of RAG Mastery (email PDF)
- LinkedIn recommendation
- Internship referral (if you have connections)

---

## 📊 Quick Reference: Quiz Flow

```
TIME    | ACTIVITY               | PLATFORM      | DURATION
--------|------------------------|---------------|----------
0-10    | Paper Exercise         | Physical      | 10 min
10-15   | RAG Intro             | Slides        | 5 min
15-18   | QUIZ 1                 | Google Forms  | 3 min
18-20   | Quiz 1 Review + Prizes | Slides        | 2 min
20-40   | Chunking + Demo 1-2    | Code + Slides | 20 min
40-45   | QUIZ 2                 | Google Forms  | 4 min (10 Q)
45-47   | Quiz 2 Review + Prizes | Slides        | 2 min
47-62   | Vector DB + Demo 3     | Code + Slides | 15 min
62-67   | QUIZ 3                 | Google Forms  | 5 min (12 Q)
67-69   | Quiz 3 Review + Prizes | Slides        | 2 min
69-83   | Advanced + Demo 4-5    | Code + Slides | 14 min
83-89   | QUIZ 4 (FINAL)         | Kahoot        | 6 min (15 Q)
89-90   | Winners + Wrap-up      | Celebration!  | 1 min
```

---

## 🔧 Troubleshooting

### Problem: Students can't scan QR code
**Solution:** Display the short URL as text too (forms.gle/xyz)

### Problem: Google Forms slow with 150 simultaneous responses
**Solution:** Unlikely to be an issue, but if it happens:
- Have backup Kahoot ready
- Or split into 2 batches (first 75, then next 75)

### Problem: Students submit multiple times
**Solution:** In Form settings, enable "Limit to 1 response"

### Problem: Cheating (sharing answers)
**Solution:**
- Emphasize it's team-based (2-3 people collaborating is OK!)
- Shuffle question order in Google Forms
- Time pressure helps (3-5 min limits)
- Focus on learning, not just winning

### Problem: Students finish quiz too fast
**Solution:**
- Have bonus questions ready
- While waiting, show interesting RAG memes/tweets on projector
- Start reviewing answers immediately

### Problem: Internet goes down
**Solution:**
- Have printed quiz as backup
- Collect answers on paper
- Grade manually (yes/no) - 2 min per quiz

---

## 📱 Student Instructions (Share Before Session)

**Email to students 1 day before:**

```
Subject: Tomorrow's RAG Demo - Bring Your Devices! 📱💻

Hi everyone,

Excited for tomorrow's RAG demo! Here's what you need:

✅ MUST BRING:
   • Laptop OR smartphone with internet
   • Python 3.8+ installed (for hands-on demos)
   • Gemini API key (get free at: https://makersuite.google.com/app/apikey)

✅ FORM TEAMS:
   • Groups of 2-3 people
   • Pick your teammates before class
   • You'll compete for prizes! 🏆

✅ WHAT TO EXPECT:
   • Interactive paper exercise
   • Live coding demos
   • 4 quizzes with prizes
   • Hands-on RAG building
   • Lots of fun! 🎉

✅ PRIZE GOODIES:
   • Top teams in each quiz win prizes
   • Challenge project for post-session

See you tomorrow! Let's build some RAG systems! 🚀

[Your Name]
```

---

## 📈 Post-Session Analytics

### What to Track:

1. **Quiz Performance:**
   - Average score per quiz
   - Question-level difficulty (% correct)
   - Time taken

2. **Engagement:**
   - Completion rate (how many submitted?)
   - Drop-off points (if any)

3. **Learning Outcomes:**
   - Questions with <50% correct → needs more emphasis next time
   - Questions with >90% correct → can speed up

4. **Student Feedback:**
   - Add final question to Quiz 4: "Rate this session 1-5 stars"
   - Add: "What was most confusing?"
   - Add: "What did you love most?"

### Use Data to Improve:

- Adjust difficulty for next session
- Add more examples for confusing topics
- Reduce time on easy concepts

---

## ✅ Pre-Session Checklist

**1 Day Before:**
- [ ] Create all 4 Google Forms
- [ ] Create Kahoot for Quiz 4 (optional)
- [ ] Generate QR codes
- [ ] Test on phone and laptop
- [ ] Prepare spreadsheet for tracking winners
- [ ] Buy/prepare prizes

**2 Hours Before:**
- [ ] Test internet connection
- [ ] Load all quiz links in browser tabs
- [ ] Have QR codes ready in slides
- [ ] Start timer app on phone
- [ ] Print backup quizzes (just in case)

**Start of Session:**
- [ ] Show QR code test slide - ensure students can scan
- [ ] Announce prize structure
- [ ] Remind time limits
- [ ] Encourage friendly competition

**During Session:**
- [ ] Monitor response count (Google Sheets)
- [ ] Call out time milestones ("2 min left!")
- [ ] Have backup plan if tech fails

---

## 🎓 You're Ready!

Follow this guide and your quiz setup will be smooth and engaging! Students will have fun competing, and you'll have data to measure learning outcomes.

**Remember:** Quizzes are not just for assessment - they're for:
- ✅ Breaking up lecture monotony
- ✅ Reinforcing key concepts
- ✅ Creating excitement and energy
- ✅ Identifying gaps in real-time
- ✅ Rewarding participation

**Make it fun, not stressful!** 🎉

Good luck! 🚀
