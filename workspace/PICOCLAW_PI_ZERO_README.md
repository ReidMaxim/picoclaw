# 🦞 Picoclaw on Raspberry Pi Zero 2 W

**Your friendly AI assistant - no tech skills needed!**

---

## 🎯 What is Picoclaw?

Picoclaw is a tiny AI assistant that runs on your Raspberry Pi. Think of it like a personal chatbot that can help you with:

- Answering questions
- Searching the web
- Writing code
- Learning new things

Perfect for beginners who want to explore AI without complicated setup!

---

## 📋 What You'll Need

1. **Raspberry Pi Zero 2 W**
2. **MicroSD card** with Raspberry Pi OS Lite (32-bit recommended)
3. **Internet connection**
4. **About 5 minutes** of your time

---

## 🚀 Step-by-Step Installation

### Step 1: Update Your Pi

Open the terminal and run:

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Build Tools

```bash
sudo apt install -y git gcc go libffi-dev
```

### Step 3: Download Picoclaw

```bash
cd ~/
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw
```

### Step 4: Install Picoclaw

```bash
make install
```

### Step 5: Set Up OpenRouter Account

1. Go to [openrouter.ai](https://openrouter.ai)
2. Click **"Sign Up"** (use email or Google)
3. Go to your **Account Dashboard**
4. Copy your **API Key** (looks like `sk-or-...`)

### Step 6: Choose Your AI Model

Different models have different personalities and abilities:

| Model | Speed | Price | Best For |
|-------|-------|-------|----------|
| `stepfun/step-3.5-flash:free` | ⚡ Fast | 💰 Free | Quick questions, learning |
| `mistralai/mistral-7b-instruct` | 🐌 Moderate | 💰 Cheap | Code help, detailed answers |
| `google/gemma-2-2b-it` | ⚡ Fast | 💰 Free | Simple tasks, chat |

**For beginners, we recommend: `stepfun/step-3.5-flash:free`**

---

## ⚙️ Configure Picoclaw

### Step 7: Create Your Config File

Create a configuration file:

```bash
mkdir -p ~/.picoclaw
nano ~/.picoclaw/config.yaml
```

**Paste this into the file (replace YOUR_API_KEY):**

```yaml
llm:
  provider: openrouter
  model: stepfun/step-3.5-flash:free
  api_key: YOUR_API_KEY_HERE  # Paste your key here!
```

**Save and exit:**
- Press `Ctrl+O` then `Enter` to save
- Press `Ctrl+X` to exit

### Step 8: Test It Works!

```bash
picoclaw -m "Hello, can you help me with something?"
```

---

## 🎉 That's It!

You now have a working AI assistant on your Pi!

### Common Commands

```bash
# Chat with picoclaw
picoclaw -m "Your question here"

# Search the web
picoclaw -s "weather in London"

# Learn more
picoclaw -h
```

---

## 💡 Tips for Beginners

1. **Start simple** - Ask basic questions first
2. **Keep your API key secret** - Don't share it publicly
3. **Check usage** - Free tiers have limits, check OpenRouter
4. **Have fun!** - This is your playground to learn AI

---

## 🆘 Troubleshooting

**"Command not found"** → Make sure you ran `make install`

**Connection errors** → Check your internet connection

**Still stuck?** → Run `picoclaw -h` for help

---

## 🌟 Next Steps

Once you're comfortable, try:

- [Checking settings](https://github.com/sipeed/picoclaw)
- [Adding custom skills](https://github.com/sipeed/picoclaw)
- [Joining the community](https://github.com/sipeed/picoclaw/discussions)

---

Made with ❤️ for beginners exploring AI on Raspberry Pi
