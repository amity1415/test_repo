import os
import sys
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def audit_code(code: str):
    prompt = f"""
You are a senior software auditor. Review the code below for:
- Bugs
- Security issues
- Style violations
- Performance problems
- Missing tests or comments

Then provide a corrected version with explanation.

Code:
{code}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath, "r") as file:
        code = file.read()
    report = audit_code(code)
    print(report)
