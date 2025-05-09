# 🤖 AI Code Auditor (GitHub Actions + OpenAI)

This starter repo integrates OpenAI with GitHub Actions to automatically audit Python code on every pull request.

## 🚀 Features
- Detects bugs, security flaws, and poor coding practices
- Uses GPT-4 to suggest improvements with explanations
- Fully automated using GitHub Actions

## 🛠️ Setup

1. Add your OpenAI API Key as a GitHub Secret:
   - Key: `OPENAI_API_KEY`

2. Push Python files to a branch and open a pull request.
3. See audit results in GitHub Actions logs.

## 📁 Files

- `code_audit.py`: Python script for OpenAI audit
- `.github/workflows/code_audit.yml`: Workflow file
- `README.md`: This file
